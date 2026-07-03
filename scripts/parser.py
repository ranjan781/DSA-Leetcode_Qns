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
    ".sql": "SQL"
}


def get_solution_file(folder: Path):
    for file in folder.iterdir():
        if file.is_file() and file.suffix.lower() in LANGUAGE_MAP:
            return file
    return None


def count_lines(file):
    if not file:
        return 0

    with open(file, encoding="utf-8", errors="ignore") as f:
        return len(f.readlines())


def parse_problem(folder: Path):

    readme = folder / "README.md"

    if not readme.exists():
        return None

    text = readme.read_text(encoding="utf-8", errors="ignore")

    title = "Unknown"
    difficulty = "Unknown"
    url = ""

    title_match = re.search(
        r'<h2><a href="([^"]+)">(.+?)</a></h2>',
        text,
        re.DOTALL,
    )

    if title_match:
        url = title_match.group(1)

        title = re.sub("<.*?>", "", title_match.group(2)).strip()

    diff_match = re.search(
        r'<h3>(Easy|Medium|Hard)</h3>',
        text,
        re.IGNORECASE,
    )

    if diff_match:
        difficulty = diff_match.group(1).title()

    solution = get_solution_file(folder)

    try:
        pid = int(folder.name.split("-")[0])
    except:
        return None

    modified = readme.stat().st_mtime

    if solution:
        modified = max(
            modified,
            solution.stat().st_mtime
        )

    return {
        "id": pid,
        "folder": folder.name,
        "title": title,
        "difficulty": difficulty,
        "url": url,
        "language": LANGUAGE_MAP.get(
            solution.suffix.lower(),
            "Unknown"
        ) if solution else "Unknown",
        "solution": solution.name if solution else "",
        "loc": count_lines(solution),
        "modified": modified,
    }


def scan_repository():

    problems = []

    root = Path(".")

    for item in root.iterdir():

        if not item.is_dir():
            continue

        if item.name.startswith("."):
            continue

        if item.name == "scripts":
            continue

        if not re.match(r"^\d+", item.name):
            continue

        problem = parse_problem(item)

        if problem:
            problems.append(problem)

    problems.sort(key=lambda x: x["id"])

    return problems
