# Changelog

All notable changes are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]
### Changed
- The core is agent-neutral: the rules file is `vault/AGENTS.md`, scripts moved to `vault/scripts/`, the memory folder is `vault/agent-memory/`, and the rules tell any agent to run the session-start report and read matching skills.
- Private documents stay outside the vault; the template no longer has a `private/` folder (deny rules remain as a safety net in the adapters).

### Added
- Adapters for Claude Code (`CLAUDE.md` importing `AGENTS.md`, hook and deny rules), opencode (`opencode.jsonc`) and chat-only use.
- Guide `docs/agents.md`: what is shared, what differs per agent, sources and check dates.

## [0.1.0] - 2026-11-19
### Added
- Vault template with inbox, wiki, daily notes, work threads, AI memory and a private folder that is excluded from Git and denied to the agent.
- Rules file `vault/CLAUDE.md`.
- Skills: `ingest`, `query`, `weekly-review`, `requirements`, `self-check`, `writing-style`, `harness-review`.
- Scripts: `session_start.py` (session-start report) and `wiki_lint.py` (wiki checks).
- Guides: how it works, getting started, privacy, and an interview prompt in English and German.
- Community files: licence, contributing guide, code of conduct, security policy, issue and pull request templates, and a check workflow.
