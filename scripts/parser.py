
import os
import re
from pathlib import Path

LANGUAGE_MAP = {
    ".cpp": "C++",
    ".cc": "C++",
    ".c": "C",
    ".java": "Java",
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".cs": "C#",
    ".go": "Go",
    ".kt": "Kotlin",
    ".rs": "Rust"
}


def get_language(folder):
    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            if ext in LANGUAGE_MAP:
                return LANGUAGE_MAP[ext]
    return "Unknown"


def parse_problem(folder: Path):
    readme = folder / "README.md"

    if not readme.exists():
        return None

    text = readme.read_text(encoding="utf-8", errors="ignore")

    title = "Unknown"
    difficulty = "Unknown"
    url = ""

    title_match = re.search(r'<h2><a href="([^"]+)">(.+?)</a></h2>', text)

    if title_match:
        url = title_match.group(1)
        title = re.sub("<.*?>", "", title_match.group(2))

    diff_match = re.search(r'<h3>(Easy|Medium|Hard)</h3>', text)

    if diff_match:
        difficulty = diff_match.group(1)

    return {
        "folder": folder.name,
        "title": title,
        "difficulty": difficulty,
        "url": url,
        "language": get_language(folder),
        "modified": folder.stat().st_mtime
    }


def scan_repository():
    root = Path(".")

    problems = []

    for item in root.iterdir():

        if not item.is_dir():
            continue

        if item.name.startswith("."):
            continue

        if item.name == "scripts":
            continue

        data = parse_problem(item)

        if data:
            problems.append(data)

    problems.sort(key=lambda x: x["modified"], reverse=True)

    return problems
