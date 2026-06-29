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
        print("README.md not found")
        return

    problems = scan_repository()

    readme = README.read_text(encoding="utf-8")

    readme = update_section(
        readme,
        "stats",
        generate_stats(problems),
    )

    readme = update_section(
        readme,
        "progress",
        generate_progress(problems),
    )

    readme = update_section(
        readme,
        "recent",
        generate_recent(problems),
    )

    readme = update_section(
        readme,
        "languages",
        generate_languages(problems),
    )

    readme = update_section(
        readme,
        "date",
        generate_date(),
    )

    README.write_text(readme, encoding="utf-8")

    print("=" * 50)
    print("README Updated Successfully")
    print("=" * 50)
    print(f"Problems : {len(problems)}")


if __name__ == "__main__":
    main()
