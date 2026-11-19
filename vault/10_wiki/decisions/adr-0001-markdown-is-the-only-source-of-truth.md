---
type: decision
date: 2026-11-19
status: accepted
tags: [wiki/decision]
related: ["[[the-agent-files-and-links-and-the-user-decides]]"]
---
# ADR-0001: Markdown is the only source of truth

## Context
A second brain must outlive any single app, and the agent must be able to read and write it with ordinary file tools.

## Decision
All notes are plain Markdown files with YAML frontmatter in one folder tree. There is no database, no app-specific storage and no hidden index. Views (for example Obsidian Bases) only read the files.

## Consequences
- Any editor can open the vault, and Git can version it.
- Search stays simple (grep, or the editor's search) until the vault grows past a few hundred pages; revisit then.
- Structure lives in conventions (folders, frontmatter, links), which `AGENTS.md` defines and `wiki_lint.py` checks.
