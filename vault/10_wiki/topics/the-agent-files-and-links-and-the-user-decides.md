---
type: topic
date: 2026-11-19
tags: [wiki/topic]
related: ["[[adr-0001-markdown-is-the-only-source-of-truth]]"]
---
# The agent files and links, and the user decides

This vault splits the work in two. The user collects material, writes daily notes and makes every decision that needs judgement: what matters, what is true, what to do next. The agent does the bookkeeping that people tend to skip: it turns inbox notes into wiki pages, links them, keeps [[index]] and [[log]] current, finds broken links and contradictions, and prepares the weekly review with facts and questions.

Two rules keep the split honest. The agent never writes in the user's own layers (daily notes, the reflection in a weekly note, `private/`), and it marks every draft the user should check with `review: needed`. The user answers with comments in the text, and the agent processes them.

The idea comes from Andrej Karpathy's description of an [LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): raw sources the model only reads, a wiki the model writes, and a schema file with the rules (here: `CLAUDE.md`).
