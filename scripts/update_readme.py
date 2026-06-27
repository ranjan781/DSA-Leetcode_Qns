#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path


ROOT         = Path(__file__).resolve().parents[1]
README_PATH  = ROOT / "README.md"
STATS_PATH   = ROOT / "stats.json"
PROBLEMS_PATH = ROOT / "problems.json"   # <-- new file you maintain


LANGUAGE_MAP = {
    ".cpp": "C++", ".cc": "C++", ".cxx": "C++", ".c": "C",
    ".java": "Java", ".py": "Python", ".js": "JavaScript",
    ".ts": "TypeScript", ".go": "Go", ".rs": "Rust",
    ".cs": "C#", ".kt": "Kotlin", ".swift": "Swift",
    ".rb": "Ruby", ".php": "PHP",
}

DIFFICULTY_EMOJI = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}


@dataclass
class Problem:
    folder:     str
    number:     int
    title:      str
    difficulty: str
    language:   str
    mtime:      datetime
    topics:     list[str] = field(default_factory=list)


def title_from_folder(folder: str) -> tuple[int, str]:
    number_raw, slug = folder.split("-", 1)
    return int(number_raw), " ".join(w.capitalize() for w in slug.split("-"))


def load_stats() -> dict:
    return json.loads(STATS_PATH.read_text(encoding="utf-8"))


def load_problem_topics() -> dict[str, list[str]]:
    """Load per-problem topic lists from problems.json (you maintain this file)."""
    if not PROBLEMS_PATH.exists():
        return {}
    data = json.loads(PROBLEMS_PATH.read_text(encoding="utf-8"))
    return {k: v.get("topics", []) for k, v in data.items()}


def collect_problems(stats: dict, problem_topics: dict[str, list[str]]) -> list[Problem]:
    problems: list[Problem] = []
    for item in sorted(ROOT.iterdir()):
        if not item.is_dir() or not re.match(r"^\d{4}-", item.name):
            continue
        number, title = title_from_folder(item.name)
        source_files  = [f for f in item.iterdir() if f.is_file() and f.name != "README.md"]
        language = "Unknown"
        if source_files:
            src      = sorted(source_files)[0]
            language = LANGUAGE_MAP.get(src.suffix.lower(), src.suffix.lstrip(".").upper())
        difficulty = (
            stats.get("leetcode", {})
                 .get("shas", {})
                 .get(item.name, {})
                 .get("difficulty", "unknown")
                 .capitalize()
        )
        topics = problem_topics.get(item.name, [])
        mtime  = datetime.fromtimestamp(item.stat().st_mtime, tz=timezone.utc)
        problems.append(Problem(item.name, number, title, difficulty, language, mtime, topics))
    return problems


def make_bar(pct: int, width: int = 20) -> str:
    n = round(pct / 100 * width)
    return "█" * n + "░" * (width - n)


def replace_section(content: str, pattern: str, body: str) -> str:
    m = re.compile(pattern, re.DOTALL).search(content)
    if not m:
        return content
    return content[: m.start(2)] + body + content[m.end(2):]


# ── DSA Topics section ────────────────────────────────────────────────────────

def build_dsa_topics(problems: list[Problem]) -> str:
    # topic → difficulty counts
    stats: dict[str, dict[str, int]] = defaultdict(lambda: {"Easy": 0, "Medium": 0, "Hard": 0})
    for p in problems:
        for t in (p.topics or ["Uncategorised"]):
            d = p.difficulty if p.difficulty in stats[t] else "Easy"
            stats[t][d] += 1

    max_solved = max((sum(v.values()) for v in stats.values()), default=1)

    rows = []
    for topic, counts in sorted(stats.items(), key=lambda kv: -sum(kv[1].values())):
        e, m, h  = counts["Easy"], counts["Medium"], counts["Hard"]
        solved   = e + m + h
        pct      = round(solved / max_solved * 100)
        rows.append(f"| {topic} | {solved} | 🟢 {e} | 🟡 {m} | 🔴 {h} | `{make_bar(pct,10)}` {pct}% |")

    header = "| Topic | Solved | Easy | Medium | Hard | Progress |\n|---|---:|---:|---:|---:|---|"
    return header + "\n" + "\n".join(rows) if rows else header + "\n| — | 0 | 0 | 0 | 0 | — |"


# ── LeetCode Topics section (the improved grouped one) ────────────────────────

def build_leetcode_topics(problems: list[Problem]) -> str:
    BASE = "BASE_URL = "https://github.com/ranjan781/DSA-Leetcode_Qns/tree/main""

    # Build topic → problems mapping
    topic_map: dict[str, list[Problem]] = defaultdict(list)
    for p in problems:
        for t in (p.topics or ["Uncategorised"]):
            topic_map[t].append(p)

    lines = ["<!---LeetCode Topics Start-->", "# LeetCode Topics", ""]

    for topic in sorted(topic_map):
        probs = sorted(topic_map[topic], key=lambda p: p.number)
        emoji = {"Array": "📦", "String": "🔤", "Dynamic Programming": "🧮",
                 "Tree": "🌳", "Graph": "🕸️", "Linked List": "🔗",
                 "Hash Table": "🗂️", "Math": "➗", "Sorting": "🔃",
                 "Binary Search": "🔍", "Stack": "📚", "Queue": "🚶",
                 "Heap (Priority Queue)": "⛰️", "Two Pointers": "👆",
                 "Sliding Window": "🪟", "Backtracking": "↩️",
                 "Bit Manipulation": "⚙️", "Greedy": "💰",
                 "Recursion": "🔁", "Uncategorised": "📂"}.get(topic, "🏷️")

        lines.append(f"## {emoji} {topic}")
        lines.append("")
        lines.append("| # | Problem | Difficulty | Language |")
        lines.append("|---|---------|-----------|----------|")
        for p in probs:
            diff_emoji = DIFFICULTY_EMOJI.get(p.difficulty, "⚪")
            link = f"[{p.title}]({BASE}/{p.folder})"
            lines.append(f"| {p.number} | {link} | {diff_emoji} {p.difficulty} | {p.language} |")
        lines.append("")

    lines.append("<!---LeetCode Topics End-->")
    return "\n".join(lines)


# ── Main README renderer ──────────────────────────────────────────────────────

def render_readme(stats: dict, problems: list[Problem]) -> str:
    content  = README_PATH.read_text(encoding="utf-8")
    lc       = stats.get("leetcode", {})
    easy     = int(lc.get("easy",   0))
    medium   = int(lc.get("medium", 0))
    hard     = int(lc.get("hard",   0))
    total    = int(lc.get("solved", len(problems)))
    nz       = total or 1

    lang_ctr = Counter(p.language for p in problems if p.language != "Unknown")

    badges = "\n".join([
        f"![Total Problems](https://img.shields.io/badge/Total%20Problems-{total}-blue)",
        f"![Easy](https://img.shields.io/badge/Easy-{easy}-brightgreen)",
        f"![Medium](https://img.shields.io/badge/Medium-{medium}-orange)",
        f"![Hard](https://img.shields.io/badge/Hard-{hard}-red)",
        "![GitHub Stars](https://img.shields.io/github/stars/ranjan781/DSA-Leetcode_Qns)",
        "![Last Commit](https://img.shields.io/github/last-commit/ranjan781/DSA-Leetcode_Qns)",
        "![Repository Size](https://img.shields.io/github/repo-size/ranjan781/DSA-Leetcode_Qns)",
        f"![Language Count](https://img.shields.io/badge/Languages-{len(lang_ctr)}-informational)",
    ])

    stats_table = "\n".join([
        "| Metric | Value |", "|---|---:|",
        f"| Total solved questions | {total} |",
        f"| Easy solved | {easy} |", f"| Medium solved | {medium} |",
        f"| Hard solved | {hard} |", f"| Number of folders | {len(problems)} |",
        f"| Number of source files | {sum(1 for p in problems for f in (ROOT/p.folder).iterdir() if f.is_file() and f.name!='README.md')} |",
        f"| Number of programming languages | {len(lang_ctr)} |",
    ])

    diff_table = "\n".join([
        "| Difficulty | Count | Percentage |", "|---|---:|---:|",
        f"| Easy | {easy} | {round(easy/nz*100)}% |",
        f"| Medium | {medium} | {round(medium/nz*100)}% |",
        f"| Hard | {hard} | {round(hard/nz*100)}% |",
    ])

    progress = "\n".join([
        "**Easy**  ",   f"{make_bar(round(easy/nz*100))} {round(easy/nz*100)}%", "",
        "**Medium**  ", f"{make_bar(round(medium/nz*100))} {round(medium/nz*100)}%", "",
        "**Hard**  ",   f"{make_bar(round(hard/nz*100))} {round(hard/nz*100)}%",
    ])

    lang_rows = "\n".join(f"| {l} | {c} |" for l, c in sorted(lang_ctr.items(), key=lambda x: -x[1])) or "| N/A | 0 |"
    languages = "| Language | Solutions |\n|---|---:|\n" + lang_rows

    recent_rows = "\n".join(
        f"| {p.mtime.date()} | [{p.number}. {p.title}](https://github.com/ranjan781/DSA-Leetcode_Qns/tree/main/{p.folder}) | {DIFFICULTY_EMOJI.get(p.difficulty,'⚪')} {p.difficulty} | {p.language} |"
        for p in sorted(problems, key=lambda p: p.mtime, reverse=True)[:10]
    ) or "| - | - | - | - |"
    recently_added = "| Date | Problem | Difficulty | Language |\n|---|---|---|---|\n" + recent_rows

    content = replace_section(content, r"(## 🏷️ Badges\n\n)(.*?)(\n---\n)",                 badges)
    content = replace_section(content, r"(## 📊 Repository Statistics\n\n)(.*?)(\n---\n)",   stats_table)
    content = replace_section(content, r"(## 📈 Difficulty Distribution\n\n)(.*?)(\n---\n)", diff_table)
    content = replace_section(content, r"(## 📉 Progress Bar\n\n)(.*?)(\n---\n)",            progress)
    content = replace_section(content, r"(## 💻 Languages Used\n\n)(.*?)(\n---\n)",          languages)
    content = replace_section(content, r"(## 🆕 Recently Added Problems\n\n)(.*?)(\n---\n)", recently_added)
    content = replace_section(content, r"(## 🧠 DSA Topics\n\n)(.*?)(\n---\n)",             build_dsa_topics(problems))
    content = re.sub(
        r"<!---LeetCode Topics Start-->.*?<!---LeetCode Topics End-->",
        build_leetcode_topics(problems),
        content, flags=re.DOTALL,
    )
    return content


def main() -> None:
    stats          = load_stats()
    problem_topics = load_problem_topics()
    problems       = collect_problems(stats, problem_topics)
    updated        = render_readme(stats, problems)
    README_PATH.write_text(updated + ("" if updated.endswith("\n") else "\n"), encoding="utf-8")
    print(f"✅ README updated — {len(problems)} problems, topics loaded from problems.json")


if __name__ == "__main__":
    main()
