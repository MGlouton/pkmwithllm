#!/usr/bin/env python3
"""Lint the wiki: broken wikilinks, pages missing from the index, missing frontmatter, orphans,
review values outside the schema, and memory files missing from claude-memory/MEMORY.md.

Run from anywhere: python3 .claude/scripts/wiki_lint.py [--strict]
--strict exits with status 1 when a problem is found (for CI). Never reads private/."""
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
WIKI, MEMORY = ROOT / "10_wiki", ROOT / "claude-memory"
SKIP = {"private", ".git", ".obsidian", ".trash", "node_modules"}
REVIEW_VALUES = {"needed", "feedback", "approved"}
nfc = lambda s: unicodedata.normalize("NFC", s)  # macOS file names are often NFD
link_re = re.compile(r"\[\[([^\]|#\\]+)")
code_re = re.compile(r"```.*?```|`[^`\n]*`", re.S)


def md_files(base):
    return [p for p in base.rglob("*.md") if not SKIP & set(p.relative_to(ROOT).parts)]


def main():
    problems = []
    all_md = md_files(ROOT)
    targets = {nfc(p.stem) for p in all_md} | {nfc(p.relative_to(ROOT).with_suffix("").as_posix()) for p in all_md}
    targets |= {nfc(p.name) for p in ROOT.rglob("*") if p.is_file() and not SKIP & set(p.relative_to(ROOT).parts)}
    pages = {nfc(p.stem): p for p in md_files(WIKI)}
    inbound = {name: 0 for name in pages}

    for name, p in pages.items():
        text = p.read_text(encoding="utf-8", errors="ignore")
        body = code_re.sub("", text)
        for link in link_re.findall(body):
            link = nfc(link.strip())
            if link not in targets:
                if name != "log":  # the log is history and may name renamed pages
                    problems.append(f"BROKEN LINK   {p.relative_to(ROOT)} -> [[{link}]]")
            elif link in inbound and link != name:
                inbound[link] += 1
        m = re.search(r"^review:\s*(\S+)", text, re.M)
        if m and m.group(1) not in REVIEW_VALUES:
            problems.append(f"REVIEW VALUE  {p.relative_to(ROOT)}: review: {m.group(1)}")
        if not text.startswith("---") or not re.search(r"^type:", text[:500], re.M):
            problems.append(f"NO FRONTMATTER/type {p.relative_to(ROOT)}")

    index_file = WIKI / "index.md"
    index = nfc(index_file.read_text(encoding="utf-8")) if index_file.exists() else ""
    if not index:
        problems.append("MISSING       10_wiki/index.md")
    for name, p in pages.items():
        if name in ("index", "log"):
            continue
        if f"[[{name}" not in index:
            problems.append(f"NOT IN INDEX  {p.relative_to(ROOT)}")
        if inbound[name] == 0:
            problems.append(f"ORPHAN        {p.relative_to(ROOT)} (no inbound link)")

    mem_index = MEMORY / "MEMORY.md"
    if mem_index.exists():
        listed = mem_index.read_text(encoding="utf-8")
        for p in MEMORY.glob("*.md"):
            if p.name != "MEMORY.md" and f"({p.name})" not in listed:
                problems.append(f"MEMORY        {p.relative_to(ROOT)} is not listed in MEMORY.md")

    for line in problems:
        print(line)
    print(f"{len(problems)} problem(s) in {len(pages)} wiki page(s)")
    if problems and "--strict" in sys.argv:
        sys.exit(1)


if __name__ == "__main__":
    main()
