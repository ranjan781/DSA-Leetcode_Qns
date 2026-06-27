#!/usr/bin/env python3
from __future__ import annotations
import json, re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT          = Path(__file__).resolve().parents[1]
README_PATH   = ROOT / "README.md"
STATS_PATH    = ROOT / "stats.json"
PROBLEMS_PATH = ROOT / "problems.json"

LANGUAGE_MAP = {
    ".cpp":"C++",".cc":"C++",".cxx":"C++",".c":"C",
    ".java":"Java",".py":"Python",".js":"JavaScript",
    ".ts":"TypeScript",".go":"Go",".rs":"Rust",
    ".cs":"C#",".kt":"Kotlin",".swift":"Swift",
    ".rb":"Ruby",".php":"PHP",
}
D_EMOJI = {"Easy":"🟢","Medium":"🟡","Hard":"🔴"}
BASE    = "https://github.com/ranjan781/DSA-Leetcode_Qns/tree/main"

@dataclass
class Problem:
    folder:str; number:int; title:str
    difficulty:str; language:str; mtime:datetime
    topics:list[str] = field(default_factory=list)

def title_from_folder(f):
    n,slug = f.split("-",1)
    return int(n)," ".join(w.capitalize() for w in slug.split("-"))

def bar(pct,w=20):
    n=round(pct/100*w); return "█"*n+"░"*(w-n)

def load_problems():
    stats = json.loads(STATS_PATH.read_text(encoding="utf-8"))
    ptopics = {}
    if PROBLEMS_PATH.exists():
        data = json.loads(PROBLEMS_PATH.read_text(encoding="utf-8"))
        ptopics = {k:v.get("topics",[]) for k,v in data.items()}

    problems=[]
    for item in sorted(ROOT.iterdir()):
        if not item.is_dir() or not re.match(r"^\d{4}-",item.name): continue
        number,title = title_from_folder(item.name)
        src = sorted(f for f in item.iterdir() if f.is_file() and f.name!="README.md")
        lang = LANGUAGE_MAP.get(src[0].suffix.lower(),"Unknown") if src else "Unknown"
        diff = (stats.get("leetcode",{}).get("shas",{})
                .get(item.name,{}).get("difficulty","unknown").capitalize())
        mtime = datetime.fromtimestamp(item.stat().st_mtime, tz=timezone.utc)
        problems.append(Problem(item.name,number,title,diff,lang,mtime,
                                ptopics.get(item.name,[])))
    return stats, problems

def build_readme(stats, problems):
    lc     = stats.get("leetcode",{})
    easy   = int(lc.get("easy",0))
    medium = int(lc.get("medium",0))
    hard   = int(lc.get("hard",0))
    total  = int(lc.get("solved",len(problems)))
    nz     = total or 1
    lang_c = Counter(p.language for p in problems if p.language!="Unknown")

    ep,mp,hp = round(easy/nz*100),round(medium/nz*100),round(hard/nz*100)

    # ── DSA Topics ────────────────────────────────────────────────────────────
    tstats = defaultdict(lambda:{"Easy":0,"Medium":0,"Hard":0})
    for p in problems:
        for t in (p.topics or ["Uncategorised"]):
            d = p.difficulty if p.difficulty in ("Easy","Medium","Hard") else "Easy"
            tstats[t][d]+=1
    mx = max((sum(v.values()) for v in tstats.values()),default=1)
    dsa_rows=[]
    for t,c in sorted(tstats.items(),key=lambda x:-sum(x[1].values())):
        e,m,h=c["Easy"],c["Medium"],c["Hard"]; s=e+m+h
        dsa_rows.append(f"| {t} | {s} | 🟢 {e} | 🟡 {m} | 🔴 {h} | `{bar(round(s/mx*100),10)}` {round(s/mx*100)}% |")
    dsa_table = ("| Topic | Solved | Easy | Medium | Hard | Progress |\n"
                 "|---|---:|---:|---:|---:|---|\n"+
                 ("\n".join(dsa_rows) if dsa_rows else "| — | 0 | 0 | 0 | 0 | — |"))

    # ── LeetCode Topics ───────────────────────────────────────────────────────
    tmap = defaultdict(list)
    for p in problems:
        for t in (p.topics or ["Uncategorised"]): tmap[t].append(p)
    lc_lines=["<!---LeetCode Topics Start-->","# LeetCode Topics",""]
    ICONS={"Array":"📦","String":"🔤","Dynamic Programming":"🧮","Tree":"🌳",
           "Graph":"🕸️","Linked List":"🔗","Hash Table":"🗂️","Math":"➗",
           "Sorting":"🔃","Binary Search":"🔍","Stack":"📚","Two Pointers":"👆",
           "Sliding Window":"🪟","Bit Manipulation":"⚙️","Greedy":"💰",
           "Recursion":"🔁","Uncategorised":"📂"}
    for t in sorted(tmap):
        lc_lines += [f"## {ICONS.get(t,'🏷️')} {t}","",
                     "| # | Problem | Difficulty | Language |",
                     "|---|---------|-----------|----------|"]
        for p in sorted(tmap[t],key=lambda x:x.number):
            lc_lines.append(
                f"| {p.number} | [{p.title}]({BASE}/{p.folder}) "
                f"| {D_EMOJI.get(p.difficulty,'⚪')} {p.difficulty} | {p.language} |")
        lc_lines.append("")
    lc_lines.append("<!---LeetCode Topics End-->")
    lc_block = "\n".join(lc_lines)

    # ── Recently Added ────────────────────────────────────────────────────────
    recent = sorted(problems,key=lambda p:p.mtime,reverse=True)[:10]
    rec_rows = "\n".join(
        f"| {p.mtime.date()} | [{p.number}. {p.title}]({BASE}/{p.folder}) "
        f"| {D_EMOJI.get(p.difficulty,'⚪')} {p.difficulty} | {p.language} |"
        for p in recent) or "| - | - | - | - |"

    # ── Language table ────────────────────────────────────────────────────────
    lang_rows = "\n".join(f"| {l} | {c} |"
        for l,c in sorted(lang_c.items(),key=lambda x:-x[1])) or "| N/A | 0 |"

    # ── Now write the FULL README using markers ───────────────────────────────
    content = README_PATH.read_text(encoding="utf-8")

    def swap(text, start_marker, end_marker, new_body):
        """Replace everything between start_marker and end_marker."""
        pattern = re.compile(
            re.escape(start_marker) + r".*?" + re.escape(end_marker),
            re.DOTALL)
        replacement = start_marker + "\n" + new_body + "\n" + end_marker
        if pattern.search(text):
            return pattern.sub(replacement, text)
        return text  # marker not found — leave unchanged

    # Badges
    badges = "\n".join([
        f"![Total Problems](https://img.shields.io/badge/Total%20Problems-{total}-blue)",
        f"![Easy](https://img.shields.io/badge/Easy-{easy}-brightgreen)",
        f"![Medium](https://img.shields.io/badge/Medium-{medium}-orange)",
        f"![Hard](https://img.shields.io/badge/Hard-{hard}-red)",
        "![GitHub Stars](https://img.shields.io/github/stars/ranjan781/DSA-Leetcode_Qns)",
        "![Last Commit](https://img.shields.io/github/last-commit/ranjan781/DSA-Leetcode_Qns)",
        "![Repository Size](https://img.shields.io/github/repo-size/ranjan781/DSA-Leetcode_Qns)",
        f"![Language Count](https://img.shields.io/badge/Languages-{len(lang_c)}-informational)",
    ])

    stats_table = (
        "| Metric | Value |\n|---|---:|\n"
        f"| Total solved questions | {total} |\n"
        f"| Easy solved | {easy} |\n"
        f"| Medium solved | {medium} |\n"
        f"| Hard solved | {hard} |\n"
        f"| Number of folders | {len(problems)} |\n"
        f"| Number of source files | {sum(1 for p in problems for f in (ROOT/p.folder).iterdir() if f.is_file() and f.name!='README.md')} |\n"
        f"| Number of programming languages | {len(lang_c)} |"
    )

    diff_table = (
        "| Difficulty | Count | Percentage |\n|---|---:|---:|\n"
        f"| Easy | {easy} | {ep}% |\n"
        f"| Medium | {medium} | {mp}% |\n"
        f"| Hard | {hard} | {hp}% |"
    )

    progress = (
        f"**Easy**  \n{bar(ep)} {ep}%\n\n"
        f"**Medium**  \n{bar(mp)} {mp}%\n\n"
        f"**Hard**  \n{bar(hp)} {hp}%"
    )

    lang_table = f"| Language | Solutions |\n|---|---:|\n{lang_rows}"

    recently = f"| Date | Problem | Difficulty | Language |\n|---|---|---|---|\n{rec_rows}"

    # Use HTML comment markers for robust replacement
    content = swap(content, "<!--BADGES_START-->",     "<!--BADGES_END-->",     badges)
    content = swap(content, "<!--STATS_START-->",      "<!--STATS_END-->",      stats_table)
    content = swap(content, "<!--DIFF_START-->",       "<!--DIFF_END-->",       diff_table)
    content = swap(content, "<!--PROGRESS_START-->",   "<!--PROGRESS_END-->",   progress)
    content = swap(content, "<!--LANGUAGES_START-->",  "<!--LANGUAGES_END-->",  lang_table)
    content = swap(content, "<!--RECENT_START-->",     "<!--RECENT_END-->",     recently)
    content = swap(content, "<!--DSA_TOPICS_START-->", "<!--DSA_TOPICS_END-->", dsa_table)
    content = re.sub(
        r"<!---LeetCode Topics Start-->.*?<!---LeetCode Topics End-->",
        lc_block, content, flags=re.DOTALL)

    return content

def main():
    stats, problems = load_problems()
    updated = build_readme(stats, problems)
    README_PATH.write_text(updated+("" if updated.endswith("\n") else "\n"), encoding="utf-8")
    print(f"✅ Done — {len(problems)} problems")

if __name__=="__main__":
    main()
