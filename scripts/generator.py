from collections import Counter
from datetime import datetime


def bar(value, total):
    if total == 0:
        return "░" * 20

    filled = round((value / total) * 20)
    return "█" * filled + "░" * (20 - filled)


def generate_stats(problems):

    total = len(problems)

    easy = sum(p["difficulty"] == "Easy" for p in problems)
    medium = sum(p["difficulty"] == "Medium" for p in problems)
    hard = sum(p["difficulty"] == "Hard" for p in problems)

    return f"""| Metric | Value |
|---|---:|
| Total Solved | **{total}** |
| 🟢 Easy | **{easy}** |
| 🟡 Medium | **{medium}** |
| 🔴 Hard | **{hard}** |
"""


def generate_progress(problems):

    total = len(problems)

    easy = sum(p["difficulty"] == "Easy" for p in problems)
    medium = sum(p["difficulty"] == "Medium" for p in problems)
    hard = sum(p["difficulty"] == "Hard" for p in problems)

    return f"""### 🟢 Easy

{bar(easy,total)} {easy}/{total}

### 🟡 Medium

{bar(medium,total)} {medium}/{total}

### 🔴 Hard

{bar(hard,total)} {hard}/{total}
"""


def generate_recent(problems):

    latest = sorted(
        problems,
        key=lambda x: x["modified"],
        reverse=True
    )[:10]

    emoji = {
        "Easy": "🟢",
        "Medium": "🟡",
        "Hard": "🔴",
        "Unknown": "⚪"
    }

    lines = [
        "| # | Problem | Difficulty | Language |",
        "|---|---|---|---|"
    ]

    for p in latest:

        title = p["title"]

        # Remove duplicate numbering
        if ". " in title:
            title = title.split(". ", 1)[1]

        lines.append(
            f"| {p['id']} | [{title}]({p['url']}) | {emoji.get(p['difficulty'],'⚪')} {p['difficulty']} | {p['language']} |"
        )

    return "\n".join(lines)


def generate_languages(problems):

    counter = Counter()

    for p in problems:
        counter[p["language"]] += 1

    rows = [
        "| Language | Solutions |",
        "|---|---:|"
    ]

    for lang, cnt in sorted(counter.items(), key=lambda x: (-x[1], x[0])):
        rows.append(f"| {lang} | {cnt} |")

    return "\n".join(rows)


def generate_date():

    return datetime.now().strftime("%d %B %Y • %H:%M")
