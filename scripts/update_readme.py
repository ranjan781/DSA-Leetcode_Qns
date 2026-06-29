
from pathlib import Path

from parser import scan_repository
from generator import (
    generate_stats,
    generate_progress,
    generate_recent,
    generate_languages,
    generate_date,
)
from utils import replace_section


README = Path("README.md")


def main():

    problems = scan_repository()

    if not README.exists():
        print("README.md not found.")
        return

    text = README.read_text(encoding="utf-8")

    text = replace_section(
        text,
        "<!-- AUTO_STATS_START -->",
        "<!-- AUTO_STATS_END -->",
        generate_stats(problems),
    )

    text = replace_section(
        text,
        "<!-- AUTO_PROGRESS_START -->",
        "<!-- AUTO_PROGRESS_END -->",
        generate_progress(problems),
    )

    text = replace_section(
        text,
        "<!-- AUTO_RECENT_START -->",
        "<!-- AUTO_RECENT_END -->",
        generate_recent(problems),
    )

    text = replace_section(
        text,
        "<!-- AUTO_LANG_START -->",
        "<!-- AUTO_LANG_END -->",
        generate_languages(problems),
    )

    text = replace_section(
        text,
        "<!-- AUTO_DATE_START -->",
        "<!-- AUTO_DATE_END -->",
        generate_date(),
    )

    README.write_text(text, encoding="utf-8")

    print(f"README Updated Successfully!")
    print(f"Problems Found : {len(problems)}")


if __name__ == "__main__":
    main()
