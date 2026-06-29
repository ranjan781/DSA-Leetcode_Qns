
import re


def replace_section(content: str, start: str, end: str, new_content: str):
    """
    Replace everything between two markers.
    """

    pattern = rf"{re.escape(start)}.*?{re.escape(end)}"

    replacement = (
        start
        + "\n"
        + new_content.strip()
        + "\n"
        + end
    )

    return re.sub(
        pattern,
        replacement,
        content,
        flags=re.DOTALL,
    )
