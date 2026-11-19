---
name: harness-review
description: Self-evaluation of the AI setup (the "harness": AGENTS.md, memory, skills, scripts, hooks, wiki routines) every 14 days. Reads what happened since the last review (friction lines in work threads, lessons, lint, rule growth), proposes at most three changes and records the outcome in 10_wiki/harness-reviews/. Use when the session-start report says HARNESS REVIEW DUE, or the user says "harness review", "how is our setup doing", "improve the setup". Not for checking one result (that is self-check). Never reads private material.
---

# Harness review: is the setup still getting better?

Learnings that stay on a page change nothing. Every 14 days this review turns them into rules, checks or deletions. Every mistake should become a rule, a skill change or a check, not just a fixed result. The user decides, the agent prepares; keep it to about 15 minutes of the user's time.

## Step 1: Collect (by grep; never read logs whole)
`LAST` is the date of the newest page in `10_wiki/harness-reviews/` (none: the vault's first log entry).
1. Friction since `LAST`: `grep -h 'Friction:' sessions/*.md`, keeping dated lines after `LAST` and skipping `Friction: none`.
2. Lessons in `10_wiki/lessons/` since `LAST`, and how many are enforced by a check versus text only.
3. Wiki health: `python3 scripts/wiki_lint.py | tail -20`.
4. Rule growth: lines of `AGENTS.md`, number of memories in `agent-memory/`, number of skills.
5. Threads: open threads not updated for 7 days.
6. Open items carried over from the last review.

## Step 2: Evaluate
One or two lines each, with evidence:
1. Repeats: which friction appeared twice or more? A repeat needs a check (script, hook, lint) or, if none is possible, a sharper rule in the right place.
2. Enforcement: which text-only rule was broken? Can it become a check?
3. Pruning: which rule, memory, skill or hook was not needed, is duplicated or is obsolete? Fewer, sharper rules beat more rules.
4. Cost: did `AGENTS.md` or the memory index grow? Is the growth worth it?
5. Fit: does a finding conflict with a decision record? Then the change needs a new one.

## Step 3: Propose
At most three changes, most useful first. For each: what changes, in which file, what type (rule, skill, script, hook, deletion), the evidence. Ask one at a time, with a recommendation. Build small accepted changes in the same session.

## Step 4: Record
Write `10_wiki/harness-reviews/YYYY-MM-DD-harness-review.md`:

```markdown
---
type: harness-review
date: YYYY-MM-DD
next_review: YYYY-MM-DD
tags: [wiki/harness-review]
---
# Harness review YYYY-MM-DD

## In short
Two or three sentences: is the loop running, what changes.

## Data since the last review
| Measure | Last review | Now |
|---|---|---|
| Friction lines (repeats) | | |
| Lessons total / text only | | |
| Lint problems | | |
| AGENTS.md lines, memories, skills | | |

## Findings
## Changes decided
## Declined or postponed
## Carried to the next review
```

`next_review` is the date plus 14 days; the session-start report reads it. Add the page to `10_wiki/index.md` and log `## [YYYY-MM-DD] review | Harness review`.

## If the user declines
Set `next_review` on the newest review page to the date the user names (default: 7 days later).
