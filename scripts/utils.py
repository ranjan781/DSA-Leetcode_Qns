import re

SECTIONS = {
    "stats": (
        "<!-- AUTO_STATS_START -->",
        "<!-- AUTO_STATS_END -->",
    ),
    "progress": (
        "<!-- AUTO_PROGRESS_START -->",
        "<!-- AUTO_PROGRESS_END -->",
    ),
    "recent": (
        "<!-- AUTO_RECENT_START -->",
        "<!-- AUTO_RECENT_END -->",
    ),
    "languages": (
        "<!-- AUTO_LANG_START -->",
        "<!-- AUTO_LANG_END -->",
    ),
    "date": (
        "<!-- AUTO_DATE_START -->",
        "<!-- AUTO_DATE_END -->",
    ),
}


def replace_section(readme, start, end, content):

    pattern = re.compile(
        re.escape(start)
        + r".*?"
        + re.escape(end),
        re.DOTALL,
    )

    new = f"{start}\n{content}\n{end}"

    return pattern.sub(new, readme)


def update_section(readme, key, content):

    start, end = SECTIONS[key]

    return replace_section(readme, start, end, content)
