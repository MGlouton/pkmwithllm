#!/usr/bin/env python3
"""Print the vault state at session start: what waits for whom, open threads, recent log entries.

Run from anywhere: python3 scripts/session_start.py
Any agent can run it: Claude Code through the SessionStart hook in its adapter, other agents because
AGENTS.md tells them to run it first. Skips any private/ folder."""
import datetime as dt
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKIP = {"private", ".git", ".obsidian", ".trash", ".claude", "node_modules"}
TODAY = dt.date.today()


def notes():
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT)
        if not SKIP & set(rel.parts):
            yield rel, p.read_text(encoding="utf-8", errors="ignore")


def front(text):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    return dict(re.findall(r"^([\w-]+):\s*(.*?)\s*$", m.group(1), re.M))


def section(text, heading):
    m = re.search(rf"^## {heading}\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return " ".join(m.group(1).split()) if m else ""


def main():
    out = ["## Vault state at session start"]
    needed, feedback, callouts, inbox, threads = [], [], [], [], []
    for rel, text in notes():
        fm = front(text)
        if rel.name == "_template.md":
            continue
        review = fm.get("review", "")
        if review == "needed":
            needed.append(str(rel))
        elif review == "feedback":
            feedback.append(str(rel))
        n = len(re.findall(r"^> \[!feedback\]", text, re.M))
        if n:
            callouts.append(f"{rel} ({n})")
        if rel.parts[0] == "00_inbox" and len(rel.parts) == 2 and fm.get("status", "new") == "new":
            inbox.append(str(rel))
        if rel.parts[0] == "sessions" and fm.get("status", "open") == "open":
            threads.append((rel, fm, text))

    # Resume hint: the thread marked main: true, else the newest handover
    if threads:
        main_t = [t for t in threads if t[1].get("main") == "true"]
        pick = main_t[0] if main_t else max(threads, key=lambda t: t[1].get("handover", ""))
        out.append(f"RESUME: if the user's first message is just \"continue\", read {pick[0]} and its Load first files, then do its Next step.")
    for rel, fm, _ in threads:
        due = fm.get("check_due", "")
        if due and due <= TODAY.isoformat():
            out.append(f"SELF-CHECK DUE since {due}: {rel}, section 'Self-check'.")

    # Harness review every 14 days, read from the newest review page
    reviews = sorted((ROOT / "10_wiki" / "harness-reviews").glob("*.md"))
    if reviews:
        nxt = front(reviews[-1].read_text(encoding="utf-8", errors="ignore")).get("next_review", "")
        if nxt and nxt <= TODAY.isoformat():
            out.append(f"HARNESS REVIEW DUE (planned for {nxt}): offer to run the harness-review skill.")

    out.append(f"Waiting for the user, review: needed ({len(needed)})" + (": " + ", ".join(needed[:10]) if needed else ""))
    out.append(f"Waiting for the agent, review: feedback ({len(feedback)})" + (": " + ", ".join(feedback) if feedback else ""))
    if callouts:
        out.append("Unprocessed [!feedback] callouts: " + ", ".join(callouts))
    out.append(f"Inbox, not yet ingested ({len(inbox)})" + (": " + ", ".join(inbox[:10]) if inbox else ""))

    try:
        status = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True, timeout=10)
        if status.returncode == 0:
            out.append(f"Uncommitted changes: {len(status.stdout.splitlines())}")
    except (OSError, subprocess.TimeoutExpired):
        pass

    log = ROOT / "10_wiki" / "log.md"
    if log.exists():
        heads = [l for l in log.read_text(encoding="utf-8").splitlines() if l.startswith("## [")]
        out.append("Last log entries (10_wiki/log.md; older ones by grep, never the whole file):")
        out += [f"  {h}" for h in heads[-5:]]

    out.append(f"Open threads ({len(threads)}), see sessions/:")
    for rel, fm, text in sorted(threads, key=lambda t: str(t[0]), reverse=True)[:10]:
        nxt = section(text, "Next step")[:140]
        out.append(f"  {rel.stem} | next: {nxt}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
