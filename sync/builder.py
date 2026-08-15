#!/usr/bin/env python3
"""
builder.py — assemble the MyLeetcode repo from sync/submissions.json.

Steps:
  1. Reorganize EXISTING solution files into Striver A2Z step folders via `git mv`
     (matched by the LeetCode slug in each file's header), preserving your content.
     This also normalizes filenames and fixes wrong problem numbers.
  2. Generate NEW solution files: exact code from submissions.json + the approach
     breakdown from approaches.json, wrapped in your header format.
  3. Regenerate README.md by scanning every solution file.

Run:  python3 sync/builder.py            (apply)
      python3 sync/builder.py --dry-run  (show what would happen, change nothing)
"""
import argparse
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent      # repo root
SYNC = ROOT / "sync"

# ---------------------------------------------------------------- taxonomy --
# Authoritative folder per problem number (Striver A2Z steps). Edit freely.
FOLDER = {
    1: "03_Arrays", 2: "06_Linked_List", 4: "04_Binary_Search", 7: "01_Math",
    9: "01_Math", 11: "10_Sliding_Window_Two_Pointer", 13: "05_Strings",
    15: "03_Arrays", 18: "03_Arrays", 19: "06_Linked_List", 20: "09_Stack_and_Queues",
    26: "03_Arrays", 27: "03_Arrays", 31: "03_Arrays", 33: "04_Binary_Search",
    34: "04_Binary_Search", 35: "04_Binary_Search", 36: "03_Arrays", 48: "03_Arrays",
    49: "05_Strings", 53: "03_Arrays", 54: "03_Arrays", 56: "03_Arrays",
    61: "06_Linked_List", 66: "03_Arrays", 69: "04_Binary_Search",
    70: "16_Dynamic_Programming", 73: "03_Arrays", 74: "04_Binary_Search",
    75: "03_Arrays", 81: "04_Binary_Search", 83: "06_Linked_List", 88: "03_Arrays",
    118: "03_Arrays", 121: "03_Arrays", 125: "05_Strings", 128: "03_Arrays",
    136: "08_Bit_Manipulation", 141: "06_Linked_List", 152: "03_Arrays",
    153: "04_Binary_Search", 162: "04_Binary_Search",
    167: "10_Sliding_Window_Two_Pointer", 169: "03_Arrays", 189: "03_Arrays",
    190: "08_Bit_Manipulation", 191: "08_Bit_Manipulation", 217: "03_Arrays",
    229: "03_Arrays", 238: "03_Arrays", 242: "05_Strings", 268: "03_Arrays",
    283: "03_Arrays", 300: "16_Dynamic_Programming", 322: "16_Dynamic_Programming",
    338: "08_Bit_Manipulation", 347: "11_Heaps", 485: "03_Arrays", 493: "03_Arrays",
    509: "16_Dynamic_Programming", 540: "04_Binary_Search", 560: "03_Arrays",
    645: "03_Arrays", 704: "04_Binary_Search", 875: "04_Binary_Search",
    1011: "04_Binary_Search", 1143: "16_Dynamic_Programming", 1283: "04_Binary_Search",
    1482: "04_Binary_Search", 1539: "04_Binary_Search", 1552: "04_Binary_Search",
    1752: "03_Arrays", 1838: "04_Binary_Search", 2149: "03_Arrays",
}

# Fallback for problems not explicitly mapped (future daily syncs): first matching tag.
TAG_FOLDER = [
    ("Stack", "09_Stack_and_Queues"), ("Queue", "09_Stack_and_Queues"),
    ("Linked List", "06_Linked_List"), ("Heap (Priority Queue)", "11_Heaps"),
    ("Trie", "17_Tries"), ("Binary Search Tree", "14_BST"),
    ("Tree", "13_Binary_Trees"), ("Graph", "15_Graphs"),
    ("Dynamic Programming", "16_Dynamic_Programming"),
    ("Binary Search", "04_Binary_Search"), ("Bit Manipulation", "08_Bit_Manipulation"),
    ("Sliding Window", "10_Sliding_Window_Two_Pointer"),
    ("Two Pointers", "10_Sliding_Window_Two_Pointer"),
    ("String", "05_Strings"), ("Greedy", "12_Greedy"),
    ("Math", "01_Math"), ("Array", "03_Arrays"),
]

EXT = {"cpp": ".cpp", "python3": ".py", "python": ".py", "java": ".java", "c": ".c"}
LANG_LABEL = {"cpp": "C++", "python3": "Python", "python": "Python", "java": "Java", "c": "C"}


def folder_for(num, topics):
    if num in FOLDER:
        return FOLDER[num]
    for tag, fol in TAG_FOLDER:
        if tag in (topics or []):
            return fol
    return "99_Misc"


def type_label(folder):
    name = re.sub(r"^\d+_", "", folder).replace("_", " ")
    return "Sliding Window / Two Pointer" if "Sliding" in name else name


def clean_name(title):
    t = re.sub(r"[,:'’]", "", title)
    words = re.split(r"[\s\-]+", t)
    return "".join(w[:1].upper() + w[1:] if w else "" for w in words)


def canon_filename(rec):
    return f"{int(rec['frontend_id']):03d}_{clean_name(rec['title'])}{EXT.get(rec['lang'], '.txt')}"


def canon_path(rec):
    return ROOT / folder_for(int(rec["frontend_id"]), rec.get("topics")) / canon_filename(rec)


# ------------------------------------------------------------- file bodies --
def header_body(rec, appr, folder):
    lines = [
        f"Problem: {rec['title']}",
        f"LeetCode: https://leetcode.com/problems/{rec['slug']}/",
        f"Topic: {type_label(folder)}",
        f"Difficulty: {rec['difficulty']}",
        "",
        "Approach:",
    ]
    lines += [f"- {b}" for b in appr["approach"]]
    if appr.get("comments"):
        lines += ["", "Comments:"] + [f"- {c}" for c in appr["comments"]]
    lines += ["", f"Time Complexity: {appr['time']}", f"Space Complexity: {appr['space']}"]
    return lines


def wrap_comment(body_lines, lang):
    inner = "\n".join(body_lines)
    if lang in ("python3", "python"):
        return f'"""\n{inner}\n"""'
    return f"/*\n{inner}\n*/"


def render_solution(rec, appr, folder):
    header = wrap_comment(header_body(rec, appr, folder), rec["lang"])
    return f"{header}\n\n{rec['code'].strip()}\n"


# --------------------------------------------------------------- repo scan --
def solution_files():
    for p in ROOT.rglob("*"):
        if p.is_dir():
            continue
        rel = p.relative_to(ROOT)
        if rel.parts[0] in ("sync", ".git"):
            continue
        if p.suffix.lower() in (".cpp", ".py", ".java", ".c"):
            yield p


def parse_slug(path):
    m = re.search(r"leetcode\.com/problems/([a-z0-9\-]+)", path.read_text(errors="ignore"))
    return m.group(1) if m else None


def git(*args):
    subprocess.run(["git", "-C", str(ROOT), *args], check=True)


def run(dry):
    subs = json.loads((SYNC / "submissions.json").read_text())
    approaches = json.loads((SYNC / "approaches.json").read_text())
    by_slug = {r["slug"]: r for r in subs}
    by_num = {int(r["frontend_id"]): r for r in subs}

    moved, generated, warnings = [], [], []
    present = set()

    # 1) reorganize existing files
    for p in sorted(solution_files()):
        if p.stat().st_size == 0:
            warnings.append(f"removed empty file (will regenerate): {p.relative_to(ROOT)}")
            if not dry:
                git("rm", "-f", str(p.relative_to(ROOT)))
            continue
        slug = parse_slug(p)
        rec = by_slug.get(slug)
        if rec is None:
            warnings.append(f"unmatched file (slug={slug}): {p.relative_to(ROOT)}")
            continue
        present.add(int(rec["frontend_id"]))
        target = canon_path(rec)
        if p.resolve() == target.resolve():
            continue
        moved.append((p.relative_to(ROOT), target.relative_to(ROOT)))
        if not dry:
            target.parent.mkdir(parents=True, exist_ok=True)
            git("mv", str(p.relative_to(ROOT)), str(target.relative_to(ROOT)))

    # 2) generate new files
    for num, rec in sorted(by_num.items()):
        if num in present:
            continue
        appr = approaches.get(str(num))
        if not appr:
            warnings.append(f"no approach for #{num} {rec['title']} — skipped")
            continue
        target = canon_path(rec)
        folder = target.parent.name
        generated.append(target.relative_to(ROOT))
        if not dry:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(render_solution(rec, appr, folder))
            git("add", str(target.relative_to(ROOT)))

    # 3) drop now-empty legacy folders
    if not dry:
        for d in sorted(ROOT.iterdir()):
            if d.is_dir() and d.name not in ("sync", ".git") and not any(d.iterdir()):
                d.rmdir()

    # 4) regenerate README
    if not dry:
        write_readme(by_num)

    print(f"[reorg] moved {len(moved)} existing files")
    for a, b in moved:
        print(f"    {a}  ->  {b}")
    print(f"[new]   generated {len(generated)} files")
    for b in generated:
        print(f"    + {b}")
    if warnings:
        print(f"[warn] {len(warnings)}")
        for w in warnings:
            print(f"    ! {w}")


def write_readme(by_num):
    rows = []
    for p in solution_files():
        m = re.match(r"(\d+)_", p.name)
        if not m:
            continue
        num = int(m.group(1))
        rec = by_num.get(num, {})
        title = rec.get("title") or p.stem.split("_", 1)[-1]
        difficulty = rec.get("difficulty") or ""
        lang = LANG_LABEL.get(rec.get("lang", ""), p.suffix.lstrip(".").upper())
        folder = p.parent.name
        link = f"[Link]({folder}/{p.name})"
        rows.append((num, title, type_label(folder), difficulty, lang, link))
    rows.sort()

    out = [
        "# MyLeetcode", "",
        "All the questions I go through and my approach and understanding of each problem.", "",
        "## 🚀 LeetCode Solutions", "",
        "- **Languages:** C++ & Python",
        "- **Structure:** organized by [Striver's A2Z DSA](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/) topics",
        "- **Status:** Actively updating",
        f"- **Total Solved:** {len(rows)}", "",
        "---", "",
        "## 📚 Problems", "",
        "| # | Problem | Type | Difficulty | Lang | Solution |",
        "|---|---------|------|------------|------|----------|",
    ]
    for num, title, typ, diff, lang, link in rows:
        out.append(f"| {num} | {title} | {typ} | {diff} | {lang} | {link} |")
    out += ["", "---", ""]
    (ROOT / "README.md").write_text("\n".join(out))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    run(args.dry_run)
