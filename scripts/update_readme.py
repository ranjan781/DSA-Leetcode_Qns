#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
STATS_PATH = ROOT / "stats.json"


LANGUAGE_MAP = {
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
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
    ".rb": "Ruby",
    ".php": "PHP",
}


@dataclass
class Problem:
    folder: str
    number: int
    title: str
    difficulty: str
    language: str
    mtime: datetime


def title_from_folder(folder: str) -> tuple[int, str]:
    number_raw, slug = folder.split("-", 1)
    number = int(number_raw)
    title = " ".join(word.capitalize() for word in slug.split("-"))
    return number, title


def load_stats() -> dict:
    return json.loads(STATS_PATH.read_text(encoding="utf-8"))


def collect_problems(stats: dict) -> list[Problem]:
    problems: list[Problem] = []
    for item in sorted(ROOT.iterdir()):
        if not item.is_dir() or not re.match(r"^\d{4}-", item.name):
            continue

        number, title = title_from_folder(item.name)
        source_files = [f for f in item.iterdir() if f.is_file() and f.name != "README.md"]
        language = "Unknown"
        if source_files:
            source = sorted(source_files)[0]
            language = LANGUAGE_MAP.get(source.suffix.lower(), source.suffix.lstrip(".").upper())

        difficulty = (
            stats.get("leetcode", {})
            .get("shas", {})
            .get(item.name, {})
            .get("difficulty", "unknown")
            .capitalize()
        )
        mtime = datetime.fromtimestamp(item.stat().st_mtime, tz=timezone.utc)
        problems.append(
            Problem(
                folder=item.name,
                number=number,
                title=title,
                difficulty=difficulty,
                language=language,
                mtime=mtime,
            )
        )
    return problems


def make_progress_bar(percent: int) -> str:
    total_blocks = 20
    filled = round((percent / 100) * total_blocks)
    return "█" * filled + "░" * (total_blocks - filled)


def replace_section(content: str, pattern: str, replacement_body: str) -> str:
    regex = re.compile(pattern, re.DOTALL)
    match = regex.search(content)
    if not match:
        return content
    return content[: match.start(2)] + replacement_body + content[match.end(2) :]


def render_readme(stats: dict, problems: list[Problem]) -> str:
    content = README_PATH.read_text(encoding="utf-8")
    leetcode = stats.get("leetcode", {})
    easy = int(leetcode.get("easy", 0))
    medium = int(leetcode.get("medium", 0))
    hard = int(leetcode.get("hard", 0))
    total = int(leetcode.get("solved", len(problems)))
    folder_count = len(problems)
    source_count = sum(
        1
        for p in problems
        for f in (ROOT / p.folder).iterdir()
        if f.is_file() and f.name != "README.md"
    )
    language_counter = Counter(p.language for p in problems if p.language != "Unknown")
    language_count = len(language_counter)

    total_nonzero = total if total else 1
    easy_pct = round((easy / total_nonzero) * 100)
    medium_pct = round((medium / total_nonzero) * 100)
    hard_pct = round((hard / total_nonzero) * 100)

    badges = "\n".join(
        [
            f"![Total Problems](https://img.shields.io/badge/Total%20Problems-{total}-blue)",
            f"![Easy](https://img.shields.io/badge/Easy-{easy}-brightgreen)",
            f"![Medium](https://img.shields.io/badge/Medium-{medium}-orange)",
            f"![Hard](https://img.shields.io/badge/Hard-{hard}-red)",
            "![GitHub Stars](https://img.shields.io/github/stars/ranjan781/DSA-Leetcode_Qns)",
            "![Last Commit](https://img.shields.io/github/last-commit/ranjan781/DSA-Leetcode_Qns)",
            "![Repository Size](https://img.shields.io/github/repo-size/ranjan781/DSA-Leetcode_Qns)",
            f"![Language Count](https://img.shields.io/badge/Languages-{language_count}-informational)",
        ]
    )

    stats_table = "\n".join(
        [
            "| Metric | Value |",
            "|---|---:|",
            f"| Total solved questions | {total} |",
            f"| Easy solved | {easy} |",
            f"| Medium solved | {medium} |",
            f"| Hard solved | {hard} |",
            f"| Number of folders | {folder_count} |",
            f"| Number of source files | {source_count} |",
            f"| Number of programming languages | {language_count} |",
        ]
    )

    difficulty_table = "\n".join(
        [
            "| Difficulty | Count | Percentage |",
            "|---|---:|---:|",
            f"| Easy | {easy} | {easy_pct}% |",
            f"| Medium | {medium} | {medium_pct}% |",
            f"| Hard | {hard} | {hard_pct}% |",
        ]
    )

    progress = "\n".join(
        [
            "**Easy**  ",
            f"{make_progress_bar(easy_pct)} {easy_pct}%",
            "",
            "**Medium**  ",
            f"{make_progress_bar(medium_pct)} {medium_pct}%",
            "",
            "**Hard**  ",
            f"{make_progress_bar(hard_pct)} {hard_pct}%",
        ]
    )

    if language_counter:
        language_rows = "\n".join(
            f"| {language} | {count} |"
            for language, count in sorted(language_counter.items(), key=lambda pair: (-pair[1], pair[0]))
        )
    else:
        language_rows = "| N/A | 0 |"
    languages_table = "| Language | Solutions |\n|---|---:|\n" + language_rows

    recent_rows = "\n".join(
        f"| {problem.mtime.date().isoformat()} | {problem.number}. {problem.title} | {problem.difficulty} | {problem.language} |"
        for problem in sorted(problems, key=lambda p: p.mtime, reverse=True)[:10]
    )
    if not recent_rows:
        recent_rows = "| - | - | - | - |"
    recently_added = "| Date | Problem | Difficulty | Language |\n|---|---|---|---|\n" + recent_rows

    topics_rows = "\n".join(
        f"| [{problem.folder}](https://github.com/ranjan781/DSA-Leetcode_Qns/tree/master/{problem.folder}) |"
        for problem in sorted(problems, key=lambda p: p.number)
    )
    if not topics_rows:
        topics_rows = "| - |"
    topics_block = "\n".join(
        [
            "<!---LeetCode Topics Start-->",
            "# LeetCode Topics",
            "## Solved Problems",
            "|  |",
            "| ------- |",
            topics_rows,
            "<!---LeetCode Topics End-->",
        ]
    )

    content = replace_section(content, r"(## 🏷️ Badges\n\n)(.*?)(\n---\n)", badges)
    content = replace_section(content, r"(## 📊 Repository Statistics\n\n)(.*?)(\n---\n)", stats_table)
    content = replace_section(content, r"(## 📈 Difficulty Distribution\n\n)(.*?)(\n---\n)", difficulty_table)
    content = replace_section(content, r"(## 📉 Progress Bar\n\n)(.*?)(\n---\n)", progress)
    content = replace_section(content, r"(## 💻 Languages Used\n\n)(.*?)(\n---\n)", languages_table)
    content = replace_section(content, r"(## 🆕 Recently Added Problems\n\n)(.*?)(\n---\n)", recently_added)
    content = re.sub(
        r"<!---LeetCode Topics Start-->.*?<!---LeetCode Topics End-->",
        topics_block,
        content,
        flags=re.DOTALL,
    )
    return content


def main() -> None:
    stats = load_stats()
    problems = collect_problems(stats)
    updated = render_readme(stats, problems)
    README_PATH.write_text(updated + ("\n" if not updated.endswith("\n") else ""), encoding="utf-8")


if __name__ == "__main__":
    main()
