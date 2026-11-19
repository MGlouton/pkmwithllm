# Changelog

All notable changes are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0] - 2026-11-19
First public release.

### Added
- Agent-neutral vault template in `vault/`: inbox, wiki, daily and weekly notes, work threads and agent memory, with the shared rules file `AGENTS.md`.
- Skills in the Agent Skills format: `ingest`, `query`, `weekly-review`, `requirements`, `self-check`, `writing-style`, `harness-review`.
- Scripts in `vault/scripts/`: `session_start.py` (session-start report) and `wiki_lint.py` (wiki checks, `--strict` for CI).
- Adapters for Claude Code (`CLAUDE.md` importing `AGENTS.md`, session-start hook, deny rules), opencode (`opencode.jsonc`) and chat-only use.
- Guides: how it works, getting started, using different agents, privacy, and an interview prompt in English and German.
- Community files: licence (MIT), contributing guide, code of conduct, security policy, issue forms, pull request template and a check workflow.

### Known limits
- The opencode adapter is checked against opencode's documentation (2026-11-19) but not yet tested in a real session.
- Private documents are meant to stay outside the vault; deny rules in the adapters are a safety net, not a security boundary.
