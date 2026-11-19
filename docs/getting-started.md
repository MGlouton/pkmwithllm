# Getting started

About an hour for the setup, then a few weeks of use before you change much.

## 1. What you need
- A Markdown editor. [Obsidian](https://obsidian.md) is free for personal use, but not open source. Open-source alternatives that read the same files include [Logseq](https://logseq.com) (in Markdown mode) and any text editor; you lose some Obsidian views, not the method.
- An AI agent that can read and write files in a folder, for example [Claude Code](https://code.claude.com/docs) or the open-source [opencode](https://opencode.ai). A chat model works too, with more copying. Which agent needs what: [agents.md](agents.md).
- Python 3 for the two scripts.
- Optional: Git, for history and sync.

Before you start, read [privacy.md](privacy.md): it explains what leaves your device.

## 2. Copy the vault
Copy the `vault/` folder of this repository to where you want your notes, for example `~/Notes/myos`. Rename it as you like. Then copy the files of your agent's adapter from `adapters/` into it (each adapter's README says which).

## 3. Open it
- In Obsidian: "Open folder as vault" and pick the folder.
- In your terminal: `cd` into the folder and start the agent (`claude` for Claude Code, `opencode` for opencode). The agent runs the session-start report, by a hook or because `AGENTS.md` tells it to.

## 4. Adapt the rules
Read `AGENTS.md` once with the agent. Ask it to change what does not fit: the language of your notes, folder names, which data counts as private for you, how you want lists and dates written. Keep the file short.

## 5. First week
1. Say "ingest" to file the welcome note in the inbox. Look at the new page, the index line and the log entry.
2. Capture a few things you care about: paste an article link, a thought, a summary of a book chapter.
3. Write a daily note in `20_daily/` (copy `_template.md`) on most days. Short is fine.
4. Ask a question with "what do I know about …".
5. At the end of the week, say "weekly review" and write your reflection in the note it prepares.
6. At the end of each session, say "handover", and start the next one with the line the agent gives you.

## 6. Other agents
The rules are in `AGENTS.md`, which most coding agents read. Claude Code reads `CLAUDE.md`, so its adapter adds a one-line `CLAUDE.md` that imports `AGENTS.md`. For opencode, chat-only use and any other agent, see [agents.md](agents.md).

## 7. Sync and backup (optional)
A Git repository gives you history and lets several devices share the vault:

```bash
git init
```

```bash
git add -A && git commit -m "Start my vault"
```

Push only to a private remote. GitHub works with Claude Code's cloud sessions, which clone from GitHub. If you prefer a European host, [Codeberg](https://codeberg.org) (a non-profit in Germany) or a self-hosted [Forgejo](https://forgejo.org) are options; check Codeberg's terms on private repositories before you rely on it (not verified here). On the desktop, the Obsidian Git community plugin can commit and sync on a timer.

Private documents stay outside the vault, so they never reach the Git host either. Back them up separately, for example on an encrypted drive.

## 8. After two weeks
Say "harness review". The agent reads the friction lines of your work threads and proposes at most three changes to the rules or skills. That is how the vault adapts to you.
