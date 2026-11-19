# Your vault

Copy this folder to where you keep your notes, open it in Obsidian as a vault and in your agent as the project folder, and copy the files of your agent's adapter into it (see `adapters/` in the starter kit). Then read `AGENTS.md` and adapt it.

| Folder | Purpose |
|---|---|
| `00_inbox/` | Drop new notes, links and clippings here. The agent files them with `ingest`. |
| `10_wiki/` | The wiki the agent maintains. Start at `index.md`. |
| `20_daily/` | Your daily notes (yours only) and the weekly review notes. |
| `sessions/` | One note per piece of work, so a new session can continue where the last one stopped. |
| `agent-memory/` | What the agent should remember about how you work. You can read and edit it. |
| `.claude/skills/` | Skills in the Agent Skills format. Claude Code and opencode read this folder; other agents are pointed to it by `AGENTS.md`. |
| `scripts/` | The session-start report and the wiki linter (Python 3). |

Keep health, finance, legal and identity documents outside this folder: whatever is inside can reach the model provider.

The two pages in `10_wiki/` are examples. Keep them, change them or delete them (and their lines in `index.md`).
