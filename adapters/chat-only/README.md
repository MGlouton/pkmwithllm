# Adapter: chat only (no file access)

If you only have a chat model (in a browser, an app, or a model your employer approved for private use), you can still use the method. The chat cannot read or write your files, so you are the hands: you paste in, it drafts, you save.

## How a session works
1. Start a new chat and paste `AGENTS.md`, then the `SKILL.md` of the routine you want (for example `.claude/skills/ingest/SKILL.md`).
2. Paste the material: the inbox note, the index (`10_wiki/index.md`) and the wiki pages the note touches.
3. Ask for complete files back, each in its own code block with its path, plus the lines to add to `index.md` and `log.md`.
4. Save the files yourself and run the linter if you can: `python3 scripts/wiki_lint.py`.
5. For the next session, paste the thread note from `sessions/` instead of explaining again.

## What you give up
- No session-start report unless you run `python3 scripts/session_start.py` and paste its output.
- No automatic linking across the whole vault: the model sees only what you paste.
- More copying, so keep sessions to one routine at a time.

## Privacy
Paste only what you would be fine sending to the chat's provider. Check whether your chats are used for training, and switch it off if you can.
