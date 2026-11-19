# Adapter: Claude Code

[Claude Code](https://code.claude.com/docs) is Anthropic's coding agent. It reads `CLAUDE.md`, not `AGENTS.md` (unless you change its "Project instructions" setting), so this adapter adds a one-line `CLAUDE.md` that imports the shared rules.

## Install
Copy both items into your vault folder, next to `AGENTS.md`:
- `CLAUDE.md` (contains only `@AGENTS.md`, which pulls in the shared rules)
- `.claude/settings.json` (merge it with your own if you already have one)

## What you get
| Part | How |
|---|---|
| Rules | `CLAUDE.md` imports `AGENTS.md` |
| Skills | Claude Code reads `.claude/skills/<name>/SKILL.md` by itself; type `/ingest` or just say "ingest" |
| Session-start report | a `SessionStart` hook runs `scripts/session_start.py` on startup, resume, clear and compact; its output lands in the session context |
| Extra safety net | deny rules for a `private/` folder, in case you keep one in the vault after all |

The deny rules stop Claude Code's own file tools, but not a script that opens files by itself; the Claude Code docs say so. That is why the kit keeps private documents outside the vault.

## Checked
Against the Claude Code docs (memory, skills, hooks, settings, permissions) on 2026-11-19.
