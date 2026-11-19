# AGENTS.md: rules for this vault

This file is the schema the agent follows in every session. It is written for any coding agent that can read and write files; agent-specific wiring (hooks, permission rules) lives in the adapters of the starter kit. Keep it short: rules only. Reference material goes into READMEs, skills or wiki pages. Change anything that does not fit you; record bigger changes as a decision (see below).

## What this is
A personal second brain run as an LLM wiki: the user collects and decides, the agent does the bookkeeping (summarise, link, index, log, lint). Markdown is the only source of truth: no hidden database, everything readable in Obsidian or any editor.

## Layers
| Layer | Where | Who writes |
|---|---|---|
| Raw input | `00_inbox/` (new captures), `00_inbox/ingested/` (filed ones) | the user; the agent reads, never edits, except `status` and the move to `ingested/` |
| Wiki | `10_wiki/`: `topics/`, `sources/`, `decisions/`, `lessons/`, `harness-reviews/`, plus `index.md` and `log.md` | the agent |
| Daily and weekly notes | `20_daily/` (`YYYY-MM-DD.md` daily, `YYYY-Www.md` weekly) | daily notes: the user only; weekly notes: the agent prepares facts and questions, the user writes the reflection |
| Work threads | `sessions/` (one note per piece of work, from `_template.md`) | the agent |
| Agent memory | `agent-memory/` (index `MEMORY.md`) | the agent writes; the user reads and edits |
| Machinery | `.claude/skills/` (skills in the Agent Skills format, read by several agents), `scripts/` | the agent, with the user's yes |
| Private | outside this folder | the user only. Health, finance, legal and identity documents are not kept in the vault. |

## Operations
capture, ingest, query, weekly review, lint. Each has a skill in `.claude/skills/<name>/SKILL.md` or a script in `scripts/`.

Session start: if the vault state ("Vault state at session start") is not already in your context from a hook, run `python3 scripts/session_start.py` first and read its output. It lists review queues, open feedback, the inbox, uncommitted changes, the last log entries and open threads, and says when the next self-evaluation (`harness-review` skill, every 14 days) is due.

Skills: when the user's request matches a skill's `description`, read that `SKILL.md` and follow it, even if your agent does not load skills by itself.

## Way of working
1. Keep it simple. Small steps. Build only what the user asked for.
2. Ask one question at a time, with a recommendation.
3. Use absolute dates (`2026-11-19`), never "yesterday" or "next week".
4. Verify claims in primary sources and link them. Say so when something is unchecked, and mark it `(unverified)`.
5. Never invent facts. What a source does not say is left out or marked.
6. `10_wiki/log.md` is append-only: `## [YYYY-MM-DD] <operation> | <title>`. `10_wiki/index.md` lists every wiki page with one line.
7. Significant decisions become a decision record in `10_wiki/decisions/` (`adr-NNNN-slug.md`). Changing one needs a new record approved by the user.
8. Before building anything bigger than a small fix, write down what it must do with the `requirements` skill, unless the user says to build without.

## Wiki conventions
- Obsidian Markdown, YAML frontmatter, `[[wikilinks]]` without `.md`.
- Filenames: lowercase kebab-case, unique across the vault.
- Name notes as claims where possible ("spaced-repetition-beats-rereading", not "spaced-repetition"). One idea per note.
- Frontmatter on every wiki page: `type` (topic, source, decision, lesson, harness-review), `date`, `tags`, and `sources` where the page draws on inbox notes.
- Every new page has at least one link in (from the index or a related page) and one link out.
- Conflicting claims are kept side by side in a `> [!warning] Conflict` callout with both sources; the agent does not pick a side silently.

## Review and feedback loop
- Property `review:` on any note: `needed` means the agent waits for the user; `feedback` means the user left comments and the agent must act; `approved` means the user checked it. No property means nothing is pending.
- The agent sets `review: needed` when it drafts or substantially changes a note the user should check.
- The user comments in place with `> [!feedback] comment` and sets `review: feedback`.
- On "process feedback": address every `[!feedback]` callout, change the text, turn each callout into `> [!done] what changed`, then set `review: needed` if the user should look again, otherwise remove the property. Log it. If a comment is unclear, leave it and ask.

## Privacy
- Everything in this folder may be read by the agent. Assume it is sent to the model provider.
- Health, finance, legal and identity documents are kept outside this folder. If the user pastes such content into a session, do not file it into the wiki. If the user has a `private/` folder here anyway, never read, list, quote or write it.
- Data that belongs to an employer or to clients (meeting notes, internal documents, colleagues' names or statements) does not belong in this vault. If a file contains such data, stop and tell the user.
- Never store passwords, tokens, API keys or ID numbers anywhere in the vault.

## Work threads and handover
- At the start of a piece of work, create `sessions/YYYY-MM-DD-<slug>.md` from `sessions/_template.md`.
- At the end, or when the user says "handover": update the thread (Where we are, Next step, Load first, Settled, Open questions, Log), set `handover:` to the current time, log the work, then tell the user to start a new session with `continue sessions/YYYY-MM-DD-<slug>.md`.
- Each Log line ends with `Friction: <what cost time and what would have prevented it>` or `Friction: none`. The harness review reads these lines.
- "continue sessions/<file>.md" as the first message means: read that thread and its Load first files, then do its Next step.
- Context is a budget: this file and the memory index are loaded every session; logs and long files are looked up by grep, never read whole.

## Writing style
- Several items or steps: a short lead-in with a colon, then one item per line, no blank lines between items.
- No bold labels in front of list items; use a table if items need labels.
- Reasoning stays in paragraphs.
- Words, not arrows, to connect ideas in running text.
- The `writing-style` skill is the full checklist.

## Git (optional)
If the vault is a Git repository: the agent commits only its own files, with a message that says what changed. Push only to a private remote.
