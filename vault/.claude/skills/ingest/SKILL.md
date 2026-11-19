---
name: ingest
description: File unprocessed notes from 00_inbox/ into the wiki in 10_wiki/. Use when the user says "ingest", "process my inbox", "file this", or pastes a note, link or text and wants it kept. Also handles "capture" (saving pasted text into the inbox first). Never reads private material.
---

# Ingest: inbox to wiki

Follows `AGENTS.md`. Raw input stays untouched; the wiki is the compiled, linked version.

## Capture (the user pastes text or a link instead of a file)
1. Write `00_inbox/YYYY-MM-DD-<slug>.md` with the text verbatim and frontmatter `type: capture`, `date`, `source` (URL or "pasted"), `status: new`.
2. Continue with ingest unless the user said "just capture".

## Steps
1. List `00_inbox/*.md` with `status: new` or no status. If there are none, say so and stop.
2. Privacy check first: if a note holds health, finance, legal or identity data, credentials, other people's personal data or an employer's internal data, do not file it. Tell the user to move it out of the vault, and set the note `status: skipped-sensitive`.
3. Read `10_wiki/index.md` to find pages the note touches.
4. Decide per note, and propose before writing if it would create more than three pages or change an existing page's claims:
   - update existing pages: add the fact with its source, keep older claims, mark contradictions with a `> [!warning] Conflict` callout naming both sources;
   - create a new page only for something that deserves one, in `topics/`, `sources/`, `lessons/` or `decisions/`.
5. New pages: kebab-case unique filename, title as a claim where possible, one idea per page, frontmatter (`type`, `date`, `tags`, `sources: ["[[inbox-note]]"]`), at least one link out and one link in.
6. Never invent facts. What the source does not say is left out or marked `(unverified)`.
7. Update the inbox note: `status: ingested`, `ingested: YYYY-MM-DD`, `wiki:` list of pages touched. Move it to `00_inbox/ingested/`.
8. Add one line per new page to `10_wiki/index.md` and append `## [YYYY-MM-DD] ingest | <title>` to `10_wiki/log.md`.
9. Report in a few lines: pages created, pages updated, conflicts, open questions.

## Done when
Every touched page is in the index, `python3 scripts/wiki_lint.py` shows no new problem, the inbox note says `status: ingested`, and the log has an entry.
