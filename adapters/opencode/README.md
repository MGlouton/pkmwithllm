# Adapter: opencode

[opencode](https://opencode.ai) is an open-source coding agent that works with many model providers, including local models. That makes it the route for people who want their notes to stay in the EU or on their own machine.

## Install
Copy `opencode.jsonc` into your vault folder. Nothing else is needed for rules and skills.

## What you get
| Part | How |
|---|---|
| Rules | opencode reads `AGENTS.md` by itself (it falls back to `CLAUDE.md` only where no `AGENTS.md` exists) |
| Skills | opencode searches `.opencode/skills/`, and for compatibility also `.claude/skills/` and `.agents/skills/`, so the kit's skills are found as they are |
| Session-start report | opencode's docs name no session-start event, so `AGENTS.md` tells the agent to run `python3 scripts/session_start.py` first. You can also start a session with "run the session-start report" |
| Extra safety net | `opencode.jsonc` denies reading and editing a `private/` folder and asks before `git push` |

## Models
- Local: opencode finds a running [Ollama](https://ollama.com) at `http://127.0.0.1:11434` by itself, without an account. Small local models struggle with long, multi-step routines such as the weekly review; try `ingest` and `query` first.
- European provider: opencode's provider page does not list Mistral. Mistral's API can be added as an OpenAI-compatible provider in `opencode.jsonc` (see "Custom provider" in the opencode providers docs); the base URL and model names come from Mistral's documentation. Not tested here.

## Open points
- opencode's permissions page shows an allow-all base policy and also says unmatched actions default to "ask". Check how your version behaves with `opencode.jsonc` before relying on the deny rules.

## Checked
Against the opencode docs (rules, skills, permissions, plugins, providers) on 2026-11-19. Not yet tested in a real session.
