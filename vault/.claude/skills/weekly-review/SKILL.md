---
name: weekly-review
description: Prepare the user's weekly review in 20_daily/ (facts of the week, recurring threads from the daily notes, open tasks, questions) and, once the user has written their reflection, file the follow-ups. Use when the user says "weekly review", "review my week", "prepare the review" or "I wrote my reflection". The agent collects facts and asks questions; the user writes the reflection; the agent never drafts conclusions. Never reads private/.
---

# Weekly review: the agent prepares and asks, the user reflects

Follows `CLAUDE.md`. Reviewing your own notes is how you understand them, so the thinking stays with the user.

## Rules
1. The user writes the reflection. The agent never fills `## My reflection`, never suggests answers to its own questions and never rewrites the user's text.
2. Facts come only from the vault: `10_wiki/log.md`, `git log`, properties, the lint script. Every item links to its note.
3. Daily notes are the user's raw layer: read them, never edit them. The one exception is a task checkbox after the user decided it in pass 2 (`- [x]` done, `- [-]` dropped or moved).
4. If the reflection contains health, finance, legal or identity details, do not file them anywhere; point to the passage and suggest `private/`.

## Pass 1: prepare (on "weekly review")
1. File `20_daily/YYYY-Www.md` (ISO week of today). If it exists, continue in it without overwriting the user's text. Period: since the last weekly note's `date`, else the last 7 days.
2. Collect from the vault root:
   - log headings in the period: `grep '^## \[' 10_wiki/log.md`;
   - `git log --since=<start> --oneline` if the vault is a Git repository;
   - review queues: notes with `review: needed` (waiting for the user) and `review: feedback` (waiting for the agent);
   - decisions with `status: proposed`;
   - inbox notes not yet ingested;
   - `python3 .claude/scripts/wiki_lint.py` (count only);
   - daily notes in the period, read in full. Threads are themes (a project, a worry, an idea, a person) that show up on two or more days, named in the user's words, with links to the days. At most five, strongest first. A thread that also appeared in the two previous weekly notes is a goal candidate;
   - open tasks: unchecked `- [ ]` lines in all daily notes, oldest first, at most ten;
   - one random wiki page not changed in 30 days, to revisit.
3. Ask three to five questions that only this week's facts make possible: open, not leading, one idea each. Always one about the strongest thread. No generic coaching questions.
4. Write the note from the template below with `review: needed`, then stop. Tell the user where it is and to say "I wrote my reflection" when done.

## Pass 2: follow up (on "I wrote my reflection")
1. Read `## My reflection`. If it is empty, say so and stop.
2. Propose follow-ups as one list and wait for a yes: tasks in the notes they belong to, wiki updates (ingest rules), decision records for decisions the user stated, links to existing notes, and for each open task the user's choice (keep, done, drop, move).
3. After the yes: write the changes, fill `## Follow-ups` (each line links to where it went), remove `review:` from the weekly note, and log `## [YYYY-MM-DD] review | Week YYYY-Www`.

## Template
```markdown
---
type: weekly
date: YYYY-MM-DD
week: YYYY-Www
review: needed
---
# Week YYYY-Www (YYYY-MM-DD to YYYY-MM-DD)

## What happened
- <log heading>, [[note]]

## Waiting
- For you: [[note]]
- For the agent: [[note]]
- Open decisions: [[adr-…]]
- Inbox: N notes not ingested. Lint: N problems.

## Threads from your days
- <theme in your words> (Mon, Wed, Thu): [[existing-note]] or no note yet

## Open tasks
1. <task> ([[YYYY-MM-DD]], N days old)

## Revisit
[[random-note]]: one line on what it says.

## Questions
1. …

## My reflection
<!-- yours: the agent does not edit this section -->

## Follow-ups
```

## Done when
Pass 1: the note exists with linked facts, three to five questions and an empty reflection. Pass 2: every follow-up links to where it went, the log has an entry, and the user's text is unchanged.
