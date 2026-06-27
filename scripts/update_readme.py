#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
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

DIFFICULTY_EMOJI = {
    "Easy": "🟢",
    "Medium": "🟡",
    "Hard": "🔴",
    "Unknown": "⚪",
}


@dataclass
class Problem:
    folder: str
    number: int
    title: str
    difficulty: str
    language: str
    mtime: datetime
    topics: list[str] = field(default_factory=list)


def title_from_folder(folder: str) -> tuple[int, str]:
    number_raw, slug = folder.split("-", 1)
    number = int(number_raw)
    title = " ".join(word.capitalize() for word in slug.split("-"))
    return number, title


def load_stats() -> dict:
    return json.loads(STATS_PATH.read_text(encoding="utf-8"))


def extract_topics_from_readme(readme_path: Path) -> list[str]:
    """
    Parse topics from the problem's README.md written by LeetHub.
    LeetHub writes a 'Topics' section like:
        ## Topics
        - Array
        - Hash Table
    or sometimes inline as `Array`, `Hash Table`
    """
    if not readme_path.exists():
        return []
    text = readme_path.read_text(encoding="utf-8", errors="ignore")

    # Try markdown list format under a Topics/Tags/Companies heading
    section_match = re.search(
        r"##\s*(?:Topics?|Tags?|LeetCode Topics?)\s*\n((?:\s*[-*]\s*.+\n?)+)",
        text,
        re.IGNORECASE,
    )
    if section_match:
        raw = section_match.group(1)
        return [re.sub(r"[-*\s]", "", line).strip() for line in raw.splitlines() if line.strip()]

    # Try backtick-inline format: `Array` `Hash Table`
    inline = re.findall(r"`([A-Za-z][A-Za-z\s]+)`", text)
    # Filter out obvious non-topic words
    skip = {"README", "cpp", "java", "python", "py", "js", "ts", "go", "rs", "Solution", "sol"}
    topics = [t.strip() for t in inline if t.strip() and t.strip() not in skip and len(t.strip()) < 40]
    if topics:
        return topics

    return []


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

        # Extract topics from the problem's own README.md (written by LeetHub)
        problem_readme = item / "README.md"
        topics = extract_topics_from_readme(problem_readme)

        mtime = datetime.fromtimestamp(item.stat().st_mtime, tz=timezone.utc)
        problems.append(
            Problem(
                folder=item.name,
                number=number,
                title=title,
                difficulty=difficulty,
                language=language,
                mtime=mtime,
                topics=topics,
            )
        )
    return problems


def make_progress_bar(percent: int, total_blocks: int = 20) -> str:
    filled = round((percent / 100) * total_blocks)
    return "█" * filled + "░" * (total_blocks - filled)


def replace_section(content: str, pattern: str, replacement_body: str) -> str:
    regex = re.compile(pattern, re.DOTALL)
    match = regex.search(content)
    if not match:
        return content
    return content[: match.start(2)] + replacement_body + content[match.end(2) :]


# ── NEW: DSA Topics section ────────────────────────────────────────────────────

def build_dsa_topics_section(problems: list[Problem]) -> str:
    """
    Builds an improved DSA Topics table with per-topic Easy/Medium/Hard counts
    and a mini progress bar.  Falls back gracefully if topics aren't parsed yet.
    """
    # topic → {Easy: n, Medium: n, Hard: n}
    topic_stats: dict[str, dict[str, int]] = defaultdict(lambda: {"Easy": 0, "Medium": 0, "Hard": 0})

    for p in problems:
        for topic in (p.topics or ["Uncategorised"]):
            diff = p.difficulty if p.difficulty in ("Easy", "Medium", "Hard") else "Easy"
            topic_stats[topic][diff] += 1

    if not topic_stats:
        return "| Topic | Solved | Easy | Medium | Hard | Progress |\n|---|---:|---:|---:|---:|---|\n| — | — | — | — | — | — |"

    max_solved = max(sum(v.values()) for v in topic_stats.values()) or 1

    rows = []
    for topic, counts in sorted(topic_stats.items(), key=lambda kv: -sum(kv[1].values())):
        easy   = counts["Easy"]
        medium = counts["Medium"]
        hard   = counts["Hard"]
        solved = easy + medium + hard
        pct    = round((solved / max_solved) * 100)
        bar    = make_progress_bar(pct, total_blocks=10)
        rows.append(
            f"| {topic} | {solved} | "
            f"🟢 {easy} | 🟡 {medium} | 🔴 {hard} | "
            f"`{bar}` {pct}% |"
        )

    header = "| Topic | Solved | Easy | Medium | Hard | Progress |\n|---|---:|---:|---:|---:|---|"
    return header + "\n" + "\n".join(rows)


# ── NEW: LeetCode Topics section ───────────────────────────────────────────────

def build_leetcode_topics_section(problems: list[Problem]) -> str:
    """
    Groups problems by topic.  Each topic gets its own sub-heading with a table
    that shows number, title (linked), difficulty emoji, and language.
    """
    BASE_URL = "https://github.com/ranjan781/DSA-Leetcode_Qns/tree/main"

    # topic → list of problems
    topic_map: dict[str, list[Problem]] = defaultdict(list)
    for p in problems:
        for topic in (p.topics or ["Uncategorised"]):
            topic_map[topic].append(p)

    sections = [
        "<!---LeetCode Topics Start-->",
        "# LeetCode Topics",
    ]

    for topic in sorted(topic_map):
        probs = sorted(topic_map[topic], key=lambda p: p.number)
        sections.append(f"\n## {topic}\n")
        sections.append("| # | Problem | Difficulty | Language |")
        sections.append("|---|---------|-----------|----------|")
        for p in probs:
            emoji = DIFFICULTY_EMOJI.get(p.difficulty, "⚪")
            link  = f"[{p.number}. {p.title}]({BASE_URL}/{p.folder})"
            sections.append(f"| {p.number} | {link} | {emoji} {p.difficulty} | {p.language} |")

    sections.append("\n<!---LeetCode Topics End-->")
    return "\n".join(sections)


# ── README renderer ────────────────────────────────────────────────────────────

def render_readme(stats: dict, problems: list[Problem]) -> str:
    content = README_PATH.read_text(encoding="utf-8")
    leetcode = stats.get("leetcode", {})
    easy   = int(leetcode.get("easy",   0))
    medium = int(leetcode.get("medium", 0))
    hard   = int(leetcode.get("hard",   0))
    total  = int(leetcode.get("solved", len(problems)))
    folder_count = len(problems)
    source_count = sum(
        1
        for p in problems
        for f in (ROOT / p.folder).iterdir()
        if f.is_file() and f.name != "README.md"
    )
    language_counter = Counter(p.language for p in problems if p.language != "Unknown")
    language_count   = len(language_counter)

    total_nonzero = total if total else 1
    easy_pct   = round((easy   / total_nonzero) * 100)
    medium_pct = round((medium / total_nonzero) * 100)
    hard_pct   = round((hard   / total_nonzero) * 100)

    # ── Badges ────────────────────────────────────────────────────────────────
    badges = "\n".join([
        f"![Total Problems](https://img.shields.io/badge/Total%20Problems-{total}-blue)",
        f"![Easy](https://img.shields.io/badge/Easy-{easy}-brightgreen)",
        f"![Medium](https://img.shields.io/badge/Medium-{medium}-orange)",
        f"![Hard](https://img.shields.io/badge/Hard-{hard}-red)",
        "![GitHub Stars](https://img.shields.io/github/stars/ranjan781/DSA-Leetcode_Qns)",
        "![Last Commit](https://img.shields.io/github/last-commit/ranjan781/DSA-Leetcode_Qns)",
        "![Repository Size](https://img.shields.io/github/repo-size/ranjan781/DSA-Leetcode_Qns)",
        f"![Language Count](https://img.shields.io/badge/Languages-{language_count}-informational)",
    ])

    # ── Stats table ───────────────────────────────────────────────────────────
    stats_table = "\n".join([
        "| Metric | Value |",
        "|---|---:|",
        f"| Total solved questions | {total} |",
        f"| Easy solved | {easy} |",
        f"| Medium solved | {medium} |",
        f"| Hard solved | {hard} |",
        f"| Number of folders | {folder_count} |",
        f"| Number of source files | {source_count} |",
        f"| Number of programming languages | {language_count} |",
    ])

    # ── Difficulty distribution ───────────────────────────────────────────────
    difficulty_table = "\n".join([
        "| Difficulty | Count | Percentage |",
        "|---|---:|---:|",
        f"| Easy | {easy} | {easy_pct}% |",
        f"| Medium | {medium} | {medium_pct}% |",
        f"| Hard | {hard} | {hard_pct}% |",
    ])

    # ── Progress bars ─────────────────────────────────────────────────────────
    progress = "\n".join([
        "**Easy**  ",
        f"{make_progress_bar(easy_pct)} {easy_pct}%",
        "",
        "**Medium**  ",
        f"{make_progress_bar(medium_pct)} {medium_pct}%",
        "",
        "**Hard**  ",
        f"{make_progress_bar(hard_pct)} {hard_pct}%",
    ])

    # ── Languages ─────────────────────────────────────────────────────────────
    if language_counter:
        language_rows = "\n".join(
            f"| {lang} | {cnt} |"
            for lang, cnt in sorted(language_counter.items(), key=lambda kv: (-kv[1], kv[0]))
        )
    else:
        language_rows = "| N/A | 0 |"
    languages_table = "| Language | Solutions |\n|---|---:|\n" + language_rows

    # ── Recently added ────────────────────────────────────────────────────────
    recent_rows = "\n".join(
        f"| {p.mtime.date().isoformat()} | {p.number}. {p.title} | {DIFFICULTY_EMOJI.get(p.difficulty,'⚪')} {p.difficulty} | {p.language} |"
        for p in sorted(problems, key=lambda p: p.mtime, reverse=True)[:10]
    )
    if not recent_rows:
        recent_rows = "| - | - | - | - |"
    recently_added = "| Date | Problem | Difficulty | Language |\n|---|---|---|---|\n" + recent_rows

    # ── IMPROVED DSA Topics section ───────────────────────────────────────────
    dsa_topics_table = build_dsa_topics_section(problems)

    # ── IMPROVED LeetCode Topics section ─────────────────────────────────────
    leetcode_topics_block = build_leetcode_topics_section(problems)

    # ── Inject into README ────────────────────────────────────────────────────
    content = replace_section(content, r"(## 🏷️ Badges\n\n)(.*?)(\n---\n)",                   badges)
    content = replace_section(content, r"(## 📊 Repository Statistics\n\n)(.*?)(\n---\n)",     stats_table)
    content = replace_section(content, r"(## 📈 Difficulty Distribution\n\n)(.*?)(\n---\n)",   difficulty_table)
    content = replace_section(content, r"(## 📉 Progress Bar\n\n)(.*?)(\n---\n)",              progress)
    content = replace_section(content, r"(## 💻 Languages Used\n\n)(.*?)(\n---\n)",            languages_table)
    content = replace_section(content, r"(## 🆕 Recently Added Problems\n\n)(.*?)(\n---\n)",   recently_added)
    content = replace_section(content, r"(## 🧠 DSA Topics\n\n)(.*?)(\n---\n)",               dsa_topics_table)

    # Replace the full LeetCode Topics block (marker-based)
    content = re.sub(
        r"<!---LeetCode Topics Start-->.*?<!---LeetCode Topics End-->",
        leetcode_topics_block,
        content,
        flags=re.DOTALL,
    )

    return content


def main() -> None:
    stats    = load_stats()
    problems = collect_problems(stats)
    updated  = render_readme(stats, problems)
    README_PATH.write_text(
        updated + ("" if updated.endswith("\n") else "\n"),
        encoding="utf-8",
    )
    print(f"✅ README updated — {len(problems)} problems processed.")


if __name__ == "__main__":
    main()
