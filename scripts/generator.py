
from datetime import datetime


def progress_bar(value, total=100):

    filled = int(value / total * 20)

    return "█" * filled + "░" * (20 - filled)


def generate_stats(problems):

    total = len(problems)

    easy = sum(p["difficulty"] == "Easy" for p in problems)
    medium = sum(p["difficulty"] == "Medium" for p in problems)
    hard = sum(p["difficulty"] == "Hard" for p in problems)

    return f"""
| Metric | Count |
|------|------:|
| Total Solved | **{total}** |
| 🟢 Easy | **{easy}** |
| 🟡 Medium | **{medium}** |
| 🔴 Hard | **{hard}** |
"""


def generate_progress(problems):

    total = max(len(problems), 1)

    easy = sum(p["difficulty"] == "Easy" for p in problems)
    medium = sum(p["difficulty"] == "Medium" for p in problems)
    hard = sum(p["difficulty"] == "Hard" for p in problems)

    return f"""
Easy

{progress_bar(easy,total)} {easy}

Medium

{progress_bar(medium,total)} {medium}

Hard

{progress_bar(hard,total)} {hard}
"""


def generate_recent(problems):

    rows = []

    for p in problems[:10]:

        rows.append(
            f"| {p['title']} | {p['difficulty']} | {p['language']} |"
        )

    return (
        "| Problem | Difficulty | Language |\n"
        "|---|---|---|\n"
        + "\n".join(rows)
    )


def generate_languages(problems):

    counter = {}

    for p in problems:
        counter[p["language"]] = counter.get(p["language"],0)+1

    rows=[]

    for lang,count in sorted(counter.items(),key=lambda x:x[1],reverse=True):

        rows.append(f"| {lang} | {count} |")

    return "| Language | Solutions |\n|---|---:|\n" + "\n".join(rows)


def generate_date():

    return datetime.now().strftime("%d %B %Y %H:%M UTC")
