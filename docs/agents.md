# Using the kit with different agents

The method does not depend on one agent. The vault is Markdown, the rules are in `AGENTS.md`, the skills follow the [Agent Skills](https://agentskills.io) format and the scripts are plain Python. Only the wiring differs: how an agent finds the rules, whether it loads skills by itself, whether it can run a script at session start, and how it blocks paths. That wiring lives in [`adapters/`](../adapters/).

## What is shared and what is per agent

| Part | Shared core (`vault/`) | Per agent (`adapters/`) |
|---|---|---|
| Rules | `AGENTS.md` | a pointer file where the agent reads another name (`CLAUDE.md` for Claude Code) |
| Skills | `.claude/skills/<name>/SKILL.md` with `name` and `description` | nothing for agents that read this folder; otherwise `AGENTS.md` tells the agent to read the matching skill |
| Session-start report | `scripts/session_start.py`, plus a rule in `AGENTS.md` to run it first | a hook where the agent has one |
| Privacy | private documents stay outside the vault folder | deny rules as an extra safety net |

## Agents at a glance

| | Claude Code | opencode | Chat only |
|---|---|---|---|
| Licence | proprietary | open source | depends on the provider |
| Models | Anthropic | many providers, local models through Ollama | the chat's own |
| Reads `AGENTS.md` | only without a `CLAUDE.md`, or with a setting; the adapter's `CLAUDE.md` imports it | yes | you paste it |
| Skills | `.claude/skills/` | `.opencode/skills/`, `.claude/skills/`, `.agents/skills/` | you paste the `SKILL.md` |
| Session start | `SessionStart` hook | rule in `AGENTS.md` (no session-start event documented) | run the script, paste the output |
| Path deny rules | `settings.json`; not enforced for scripts that open files themselves | `opencode.jsonc` `permissions` | not applicable |
| Adapter | [claude-code](../adapters/claude-code/) | [opencode](../adapters/opencode/) | [chat-only](../adapters/chat-only/) |
| Checked | docs, 2026-11-19; used daily in the original vault | docs, 2026-11-19; not yet tested in a session | 2026-11-19 |

Sources: [Claude Code memory](https://code.claude.com/docs/en/memory), [skills](https://code.claude.com/docs/en/skills), [hooks](https://code.claude.com/docs/en/hooks), [permissions](https://code.claude.com/docs/en/permissions); [opencode rules](https://opencode.ai/docs/rules), [skills](https://opencode.ai/docs/skills), [permissions](https://opencode.ai/docs/permissions), [providers](https://opencode.ai/docs/providers); [agents.md](https://agents.md); [Agent Skills specification](https://agentskills.io/specification).

## Other agents
Many coding agents read `AGENTS.md`; the [agents.md](https://agents.md) site lists, among others, OpenAI Codex, Gemini CLI, Aider, goose, Cursor and Zed. For any of them:
1. Copy `vault/` and check that the agent reads `AGENTS.md` (ask it: "what are your rules for this folder?").
2. If it loads Agent Skills, point it to `.claude/skills/` or copy the folder to where it looks. If not, the rule in `AGENTS.md` makes it read the matching `SKILL.md` when a request fits.
3. If it has a session-start hook, run `python3 scripts/session_start.py` there; otherwise the rule in `AGENTS.md` covers it.
4. Look up how it blocks paths and commands, and add the same safety net as the other adapters.

An adapter for another agent is a welcome contribution; see [CONTRIBUTING.md](../CONTRIBUTING.md).

## Things to know
- These tools change often. Each row above says when it was checked; check your agent's current docs before relying on a detail.
- Smaller and local models follow long skills less reliably. Start with `ingest` and `query`, and shorten a skill if the model keeps skipping steps.
- Whatever agent you use, what it reads goes to its model provider unless the model runs on your machine. See [privacy.md](privacy.md).
