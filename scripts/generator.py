from collections import Counter
from datetime import datetime


def bar(value, total):

    if total == 0:
        return "░" * 20

    filled = int((value / total) * 20)

    return "█" * filled + "░" * (20 - filled)


def generate_stats(problems):

    total = len(problems)

    easy = sum(x["difficulty"] == "Easy" for x in problems)

    medium = sum(x["difficulty"] == "Medium" for x in problems)

    hard = sum(x["difficulty"] == "Hard" for x in problems)

    return f"""
| Metric | Value |
|---|---:|
| Total Solved | **{total}** |
| 🟢 Easy | **{easy}** |
| 🟡 Medium | **{medium}** |
| 🔴 Hard | **{hard}** |
"""


def generate_progress(problems):

    total = len(problems)

    easy = sum(x["difficulty"] == "Easy" for x in problems)

    medium = sum(x["difficulty"] == "Medium" for x in problems)

    hard = sum(x["difficulty"] == "Hard" for x in problems)

    return f"""
### 🟢 Easy

{bar(easy,total)} {easy}

### 🟡 Medium

{bar(medium,total)} {medium}

### 🔴 Hard

{bar(hard,total)} {hard}
"""


def generate_recent(problems):

    latest = sorted(
        problems,
        key=lambda x: x["modified"],
        reverse=True
    )[:10]

    lines = [
        "| # | Problem | Difficulty | Language |",
        "|---|---|---|---|"
    ]

    emoji = {
        "Easy":"🟢",
        "Medium":"🟡",
        "Hard":"🔴"
    }

    for p in latest:

        lines.append(

            f"| {p['id']} | [{p['title']}]({p['url']}) | {emoji.get(p['difficulty'],'⚪')} {p['difficulty']} | {p['language']} |"

        )

    return "\n".join(lines)


def generate_languages(problems):

    counter = Counter()

    for p in problems:
        counter[p["language"]] += 1

    text = [
        "| Language | Solutions |",
        "|---|---:|"
    ]

    for lang, cnt in counter.items():

        text.append(

            f"| {lang} | {cnt} |"

        )

    return "\n".join(text)


def generate_date():

    return datetime.utcnow().strftime("%d %B %Y %H:%M UTC")
