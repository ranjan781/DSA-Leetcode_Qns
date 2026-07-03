from pathlib import Path
import re

LANGUAGE_MAP = {
    ".cpp": "C++",
    ".cc": "C++",
    ".c": "C",
    ".java": "Java",
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".go": "Go",
    ".cs": "C#",
    ".kt": "Kotlin",
    ".rs": "Rust",
    ".sql": "Postgresql"
}


def get_solution_file(folder):
    for file in folder.iterdir():
        if file.is_file() and file.suffix.lower() in LANGUAGE_MAP:
            return file
    return None


def count_lines(file):
    if file is None:
        return 0
    with open(file, encoding="utf-8", errors="ignore") as f:
        return len(f.readlines())


def parse_problem(folder):

    readme = folder / "README.md"

    if not readme.exists():
        return None

    text = readme.read_text(encoding="utf-8", errors="ignore")

    title = "Unknown"
    difficulty = "Unknown"
    url = ""

    m = re.search(r'<h2><a href="([^"]+)">(.+?)</a></h2>', text)

    if m:
        url = m.group(1)

        raw = re.sub("<.*?>", "", m.group(2))

        title = raw

    d = re.search(r'<h3>(Easy|Medium|Hard)</h3>', text)

    if d:
        difficulty = d.group(1)

    solution = get_solution_file(folder)

    pid = folder.name.split("-")[0]

    return {

        "id": int(pid),

        "folder": folder.name,

        "title": title,

        "difficulty": difficulty,

        "url": url,

        "language": LANGUAGE_MAP.get(solution.suffix.lower(), "Unknown") if solution else "Unknown",

        "solution": solution.name if solution else "",

        "loc": count_lines(solution),

        "modified": folder.stat().st_mtime

    }


def scan_repository():

    problems = []

    for item in Path(".").iterdir():

        if not item.is_dir():
            continue

        if item.name.startswith("."):
            continue

        if item.name == "scripts":
            continue

        data = parse_problem(item)

        if data:
            problems.append(data)

    problems.sort(key=lambda x: x["id"])

    return problems
