---
name: requirements
description: Write, check and change requirements before building something in or for the vault (a new skill, script, template or routine). Three modes. Write: draft a spec with the user. Check: test a spec against a Definition of Ready. Change: record a change to a spec that is already ready. Use when the user says "spec", "write a spec for X", "requirements", "is this spec ready?", "the requirement changed", or before building something that has no spec. Never reads private material.
---

# Requirements: write, check, change

Follows `AGENTS.md`. Principles from requirements engineering (IREB CPRE) in plain language: problem before solution, every requirement checkable, assumptions written down.

## Rules
1. One feature, one spec, one status. Chat and thread notes point to the spec and never hold requirements of their own.
2. The spec lives next to what it describes, as `spec-<slug>.md` (for a skill: inside the skill's folder). Ask if unclear.
3. Status in the frontmatter: `draft`, `ready`, `building`, `done` or `dropped`. Only the user sets `ready` and `done`.
4. Goal and who it serves come first, in the user's words. Think about the real person who will use it: what they already know, where they are, where they will get stuck.
5. Every requirement has an ID (`R1`, `Q1`, `C1`), says one thing and can be checked. No "fast" or "simple" without a number or an observable test.
6. Assumptions are written as assumptions (`A1`) with how to check them. Check the cheap ones at once.
7. Ask one question at a time, with a recommendation. A bare "ok" after several points: restate your reading and ask for a clear yes.
8. A spec fits on one page (about 150 lines). A bigger feature is split.

## Mode 1: Write
1. Copy `feature-spec-template.md` (this folder) to the path from rule 2, status `draft`, `review: needed`.
2. Fill it with the user, one question at a time, updating the file after each answer: goal, who uses it, context and boundary, functional requirements, quality requirements, constraints (privacy: EU GDPR and Swiss FADP where personal data is involved), acceptance criteria (Given/When/Then for the main path, errors and edge cases), out of scope, assumptions.
3. When the user has nothing to add, run Mode 2 and report.

## Mode 2: Check (Definition of Ready)
Answer each line with yes, no or unclear and one reason, as a `> [!check] Definition of Ready (YYYY-MM-DD)` callout at the top of the spec:

| # | Criterion | Question |
|---|---|---|
| 1 | Value | Is the goal stated, with who benefits and how success is seen? |
| 2 | Context | Are the boundary and the touched parts named? |
| 3 | Clear | Does each requirement say one thing, without vague words? |
| 4 | Checkable | Does each requirement map to an acceptance criterion? |
| 5 | Errors and edges | Are error states and edge cases covered? |
| 6 | Constraints | Are privacy and other constraints written? |
| 7 | Consistent | No conflict with decisions or rules in the vault? |
| 8 | Assumptions | Is every assumption listed, and the cheap ones checked? |
| 9 | Scope | Is out of scope written, and is it small enough to build in one go? |
| 10 | Agreed | Has the user read the spec? |

Fix what is clearly wrong; ask about the rest. Recommend `ready` only when all lines are yes.

## Mode 3: Change
1. Name the change in one line and which requirements and criteria it touches.
2. Say what it costs: what is already built and changes.
3. Ask for a yes, then edit in place and add a row to the spec's `## Changes` table (date, what, why, decided by).

## Done when
The spec has a goal, IDs on every requirement, acceptance criteria for main path and errors, assumptions, out of scope, a current Definition of Ready callout and a log line `## [YYYY-MM-DD] spec | <feature>: <write|check|change>`.
