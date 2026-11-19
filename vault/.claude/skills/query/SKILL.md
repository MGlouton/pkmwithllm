---
name: query
description: Answer a question from the wiki with citations. Use when the user asks "what do I know about X", "what did I decide about Y", "ask my brain", or any question the vault may answer. Reads 10_wiki first, then raw inbox notes, and says which. Never reads private/.
---

# Query: ask my brain

Follows `CLAUDE.md`.

## Steps
1. Read `10_wiki/index.md`. Pick the pages that could answer the question, and follow their `related:` links one hop.
2. Read those pages. If the wiki cannot answer, search `00_inbox/` with grep and say clearly that the answer comes from raw notes.
3. Answer in a few sentences or a short list. Cite every claim with `[[page-name]]`. Quote exact values (dates, numbers) instead of paraphrasing them.
4. Keep three things apart: what the notes say, what is unverified or conflicting (show `[!warning] Conflict` callouts, do not pick a side), and what the notes do not cover. If nothing fits, say "not in the vault". Never fill a gap from general knowledge without saying so.
5. If the answer is a useful synthesis that is not yet a page, offer to file it with the ingest rules. Write only after the user says yes.
6. Log `## [YYYY-MM-DD] query | <question>` only when something was filed or a gap worth tracking was found.

## Boundaries
- `private/` is off limits. If the question concerns health, finances or legal matters, say that this lives there and you cannot look.
- Inbox notes with `status: skipped-sensitive` are not quoted.
