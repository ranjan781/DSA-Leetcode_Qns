#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
README_PATH = REPO_ROOT / "README.md"
STATS_PATH = REPO_ROOT / "stats.json"

SOURCE_EXTENSIONS = {
    ".cpp": "C++",
    ".cxx": "C++",
    ".cc": "C++",
    ".c": "C",
    ".java": "Java",
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".go": "Go",
    ".rs": "Rust",
    ".cs": "C#",
    ".kt": "Kotlin",
    ".swift": "Swift",
}

TOPIC_KEYWORDS = {
    "Array": {"array", "arrays"},
    "String": {"string", "strings"},
    "Math": {"math", "number", "numbers"},
    "Two Pointers": {"two", "pointer", "pointers"},
    "Linked List": {"linked", "list", "lists"},
    "Stack": {"stack"},
    "Queue": {"queue", "deque"},
    "Binary Search": {"binary", "search"},
    "Tree": {"tree", "bst"},
    "Graph": {"graph"},
    "Dynamic Programming": {"dynamic", "dp"},
    "Greedy": {"greedy"},
    "Backtracking": {"backtracking"},
    "Heap": {"heap", "priority"},
    "Hash Table": {"hash", "map", "set"},
}


def load_stats() -> dict:
    if not STATS_PATH.exists():
        return {"leetcode": {"solved": 0, "easy": 0, "medium": 0, "hard": 0}}
    return json.loads(STATS_PATH.read_text(encoding="utf-8"))


def problem_dirs() -> list[Path]:
    return sorted(
        [
            p
            for p in REPO_ROOT.iterdir()
            if p.is_dir() and re.match(r"^\d{4}-", p.name)
        ]
    )


def parse_problem_metadata(problem_dir: Path) -> tuple[str, str]:
    readme = problem_dir / "README.md"
    title = problem_dir.name
    difficulty = "Unknown"

    if not readme.exists():
        return title, difficulty

    content = readme.read_text(encoding="utf-8", errors="ignore")
    title_match = re.search(r'>(\d+\.\s*[^<]+)<', content)
    if title_match:
        title = title_match.group(1).strip()

    difficulty_match = re.search(r"<h3>([^<]+)</h3>", content, flags=re.IGNORECASE)
    if difficulty_match:
        difficulty = difficulty_match.group(1).strip().title()

    return title, difficulty


def infer_topics(problem_dir: Path) -> set[str]:
    words = set(problem_dir.name.replace("-", " ").lower().split())
    matched: set[str] = set()
    for topic, keywords in TOPIC_KEYWORDS.items():
        if words.intersection(keywords):
            matched.add(topic)
    if not matched:
        matched.add("General")
    return matched


def get_problem_date(problem_dir: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(problem_dir.name)],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        date = result.stdout.strip()
        if date:
            return date
    except OSError:
        pass

    timestamp = datetime.fromtimestamp(problem_dir.stat().st_mtime, timezone.utc)
    return timestamp.strftime("%Y-%m-%d")


def format_percentage(count: int, total: int) -> int:
    if total <= 0:
        return 0
    return round((count / total) * 100)


def render_progress_bar(percentage: int, length: int = 20) -> str:
    filled = round(length * (percentage / 100))
    return ("█" * filled) + ("░" * (length - filled)) + f" {percentage}%"


def generate_readme() -> str:
    stats = load_stats().get("leetcode", {})
    easy = int(stats.get("easy", 0))
    medium = int(stats.get("medium", 0))
    hard = int(stats.get("hard", 0))
    solved = int(stats.get("solved", easy + medium + hard))

    folders = problem_dirs()

    language_counter: Counter[str] = Counter()
    topic_counter: Counter[str] = Counter()
    recent_rows = []
    source_file_count = 0

    for folder in folders:
        source_files = [
            f
            for f in folder.iterdir()
            if f.is_file() and f.suffix.lower() in SOURCE_EXTENSIONS
        ]
        source_file_count += len(source_files)

        for file in source_files:
            language_counter[SOURCE_EXTENSIONS[file.suffix.lower()]] += 1

        title, difficulty = parse_problem_metadata(folder)
        language = (
            SOURCE_EXTENSIONS[source_files[0].suffix.lower()]
            if source_files
            else "Unknown"
        )
        date = get_problem_date(folder)
        recent_rows.append((date, title, difficulty, language))

        for topic in infer_topics(folder):
            topic_counter[topic] += 1

    recent_rows.sort(key=lambda row: row[0], reverse=True)
    recent_rows = recent_rows[:10]

    easy_pct = format_percentage(easy, solved)
    medium_pct = format_percentage(medium, solved)
    hard_pct = format_percentage(hard, solved)

    language_lines = (
        "\n".join(
            f"| {language} | {count} |"
            for language, count in sorted(
                language_counter.items(), key=lambda x: (-x[1], x[0])
            )
        )
        if language_counter
        else "| N/A | 0 |"
    )

    topic_lines = (
        "\n".join(
            f"| {topic} | {count} |"
            for topic, count in sorted(topic_counter.items(), key=lambda x: (-x[1], x[0]))
        )
        if topic_counter
        else "| General | 0 |"
    )

    recent_lines = (
        "\n".join(
            f"| {date} | {title} | {difficulty} | {language} |"
            for date, title, difficulty, language in recent_rows
        )
        if recent_rows
        else "| N/A | N/A | N/A | N/A |"
    )

    language_count = len(language_counter)

    return f"""# 🚀 LeetCode Solutions Portfolio

> This README is automatically generated by `.github/workflows/update-readme.yml`.

A curated collection of my LeetCode solutions, automatically synced with **LeetHub**.

This repository reflects my ongoing Data Structures & Algorithms journey for software engineering interview preparation.

![LeetCode](https://upload.wikimedia.org/wikipedia/commons/1/19/LeetCode_logo_black.png)

---

## 🏷️ Badges

![Total Problems](https://img.shields.io/badge/Total%20Problems-{solved}-blue)
![Easy](https://img.shields.io/badge/Easy-{easy}-brightgreen)
![Medium](https://img.shields.io/badge/Medium-{medium}-orange)
![Hard](https://img.shields.io/badge/Hard-{hard}-red)
![GitHub Stars](https://img.shields.io/github/stars/ranjan781/DSA-Leetcode_Qns)
![Last Commit](https://img.shields.io/github/last-commit/ranjan781/DSA-Leetcode_Qns)
![Repository Size](https://img.shields.io/github/repo-size/ranjan781/DSA-Leetcode_Qns)
![Language Count](https://img.shields.io/badge/Languages-{language_count}-informational)

---

## 📊 Repository Statistics

| Metric | Value |
|---|---:|
| Total solved questions | {solved} |
| Easy solved | {easy} |
| Medium solved | {medium} |
| Hard solved | {hard} |
| Number of folders | {len(folders)} |
| Number of source files | {source_file_count} |
| Number of programming languages | {language_count} |

---

## 📈 Difficulty Distribution

| Difficulty | Count | Percentage |
|---|---:|---:|
| Easy | {easy} | {easy_pct}% |
| Medium | {medium} | {medium_pct}% |
| Hard | {hard} | {hard_pct}% |

---

## 📉 Progress Bar

**Easy**  
{render_progress_bar(easy_pct)}

**Medium**  
{render_progress_bar(medium_pct)}

**Hard**  
{render_progress_bar(hard_pct)}

---

## 💻 Languages Used

| Language | Solutions |
|---|---:|
{language_lines}

---

## 🧠 DSA Topics

| Topic | Solved |
|---|---:|
{topic_lines}

---

## 🗂️ Repository Structure

- Each LeetCode problem is stored in its own folder named as `<problem-number>-<problem-slug>`.
- Each problem folder contains:
  - a solution source file (`.cpp`, `.java`, `.py`, etc.)
  - a problem statement `README.md` synced by LeetHub
- Root-level `stats.json` stores difficulty and solved counts used for tracking progress.

```text
DSA-Leetcode_Qns/
├── <problem-folder>/
│   ├── <solution-file>
│   └── README.md
├── README.md
└── stats.json
```

---

## 🆕 Recently Added Problems

| Date | Problem | Difficulty | Language |
|---|---|---|---|
{recent_lines}

---

## 🏁 Milestones

⬜ First 50 Problems  
⬜ First 100 Problems  
⬜ First 250 Problems  
⬜ First 500 Problems  
⬜ First 1000 Problems

---

## 🌱 Learning Journey

I’m continuously improving my problem-solving skills by practicing algorithmic thinking, strengthening core data structures knowledge, and building interview-ready coding consistency through regular LeetCode practice.

---

## 🎯 Goals

- Solve LeetCode Daily
- Master DSA
- Improve Code Quality
- Prepare for Product-Based Companies
- Crack Coding Interviews

---

## 🤝 Connect

- GitHub: https://github.com/ranjan781
- LinkedIn: _Add your LinkedIn profile URL_
- LeetCode: _Add your LeetCode profile URL_
- Portfolio: _Add your portfolio URL_

---

> Every problem solved is another step toward becoming a better Software Engineer.
"""


def main() -> None:
    content = generate_readme()
    README_PATH.write_text(content.rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
