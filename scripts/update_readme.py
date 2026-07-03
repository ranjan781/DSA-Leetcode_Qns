from pathlib import Path

from parser import scan_repository
from generator import (
    generate_stats,
    generate_progress,
    generate_recent,
    generate_languages,
    generate_date,
)
from utils import update_section

README = Path("README.md")


def main():

    if not README.exists():
        raise FileNotFoundError("README.md not found")

    print("Scanning repository...")

    problems = scan_repository()

    print(f"Found {len(problems)} problems.")

    readme = README.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    sections = {
        "stats": generate_stats(problems),
        "progress": generate_progress(problems),
        "recent": generate_recent(problems),
        "languages": generate_languages(problems),
        "date": generate_date(),
    }

    for key, value in sections.items():
        readme = update_section(
            readme,
            key,
            value
        )

    README.write_text(
        readme,
        encoding="utf-8"
    )

    print("=" * 60)
    print("✅ README Updated Successfully")
    print("=" * 60)
    print(f"Total Problems : {len(problems)}")


if __name__ == "__main__":
    main()
