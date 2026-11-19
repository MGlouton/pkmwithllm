# pkmwithllm: a personal knowledge vault that an AI agent maintains

A starter kit for a personal second brain in plain Markdown. You collect and decide, an AI agent does the bookkeeping: it files notes, links pages, keeps an index and a log, answers questions with citations and prepares your weekly review. Everything stays readable in [Obsidian](https://obsidian.md) or any text editor, with no hidden database.

The kit comes from a personal vault that has been in daily use since October 2026. It shares the method and the machinery, not the content.

## Who this is for 

You may find it useful if:
- you already take notes in Markdown, or want to start;
- you have an AI agent that can read and write files, for example [Claude Code](https://code.claude.com/docs) or the open-source [opencode](https://opencode.ai), or at least a chat model;
- you are comfortable with a folder of text files and a little Git;
- you want the AI to do the filing and you to keep the judgement.

It is not a product or an app. It is a folder you copy, adapt and own.

## What you get

| Part | Where | What it does |
|---|---|---|
| Vault template | [`vault/`](vault/) | Folders for inbox, wiki, daily notes, work threads and agent memory |
| Rules file | [`vault/AGENTS.md`](vault/AGENTS.md) | The schema any agent follows: layers, who writes where, naming, review loop, privacy, handover |
| Skills | [`vault/.claude/skills/`](vault/.claude/skills/) | Repeatable routines in the open [Agent Skills](https://agentskills.io) format: `ingest`, `query`, `weekly-review`, `requirements`, `self-check`, `writing-style`, `harness-review` |
| Scripts | [`vault/scripts/`](vault/scripts/) | A session-start report (what waits for whom) and a wiki linter (broken links, pages missing from the index) |
| Adapters | [`adapters/`](adapters/) | The wiring per agent: [Claude Code](adapters/claude-code/), [opencode](adapters/opencode/), [chat only](adapters/chat-only/) |
| Guides | [`docs/`](docs/) | How it works, getting started, using different agents, privacy, and an interview prompt that helps you design your own variant |

## Quick start

1. Click **Use this template** (or download the ZIP) and copy the `vault/` folder to where you keep notes.
2. Copy the files of your agent's adapter from [`adapters/`](adapters/) into that folder.
3. Open the folder in Obsidian as a vault, and in your agent as the project folder.
4. Read [`vault/AGENTS.md`](vault/AGENTS.md) once and change what does not fit you (language, folders, privacy rules).
5. Start a session. The agent runs the session-start report and shows the state of the vault.
6. Drop a note or a link into `00_inbox/` and say "ingest".

The full walk-through, including Git sync and what to keep out of any cloud, is in [docs/getting-started.md](docs/getting-started.md). Which agent needs what is in [docs/agents.md](docs/agents.md). If you would rather design your own variant first, paste [docs/interview-prompt.md](docs/interview-prompt.md) into any chat model; it interviews you and proposes an architecture. A German version is in [docs/interview-prompt.de.md](docs/interview-prompt.de.md).

## How it works, in short

The vault follows Andrej Karpathy's [LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) idea: raw sources the model only reads, a wiki the model writes, and a schema file with the rules. On top of that come a review loop (the agent marks drafts `review: needed`, you comment in place, the agent processes your comments), work threads that let a new session continue without questions, and a self-evaluation every 14 days that turns friction into rules or checks. Details and diagrams: [docs/how-it-works.md](docs/how-it-works.md).

## Privacy

Whatever the agent reads goes to its model provider. Keep health, finance, legal and identity documents outside the vault folder; the rules also tell the agent to stop when a note holds health, finance, legal or identity data, or data from your employer. If you need your data to stay in the EU or Switzerland, use an EU provider or a local model; options are in [docs/privacy.md](docs/privacy.md).

## Status

Version 0.1.0, first public release. The skills and scripts run in the original vault; this generic version was tested on the empty template, and the opencode adapter only against its documentation. See [CHANGELOG.md](CHANGELOG.md).

## Contributing

Questions, ideas and fixes are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first, and never post personal notes in an issue. Security problems go through [SECURITY.md](SECURITY.md).

## Licence

[MIT](LICENSE). The `writing-style` skill is based on [blader/humanizer](https://github.com/blader/humanizer) (MIT); its notice is kept in the skill file.
