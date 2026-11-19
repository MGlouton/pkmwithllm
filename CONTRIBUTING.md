# Contributing

Thanks for taking the time. This is a small personal project shared as a starting point, so the bar is simple: keep it small, generic and private.

## Ways to help
- Ask a question or report something unclear: open an issue with the "Question or problem" form.
- Suggest an idea: open an issue with the "Idea" form before you write a pull request, so we can agree it fits.
- Fix a typo, a broken link or a bug in a script: a pull request is fine straight away.

## What fits
- Generic routines that help one person run a Markdown vault with an AI agent.
- Changes that make the kit easier to adapt (fewer assumptions, clearer rules).
- Support for other agents (for example an `AGENTS.md` variant) as long as Claude Code keeps working.

## What does not fit
- Content from your own vault: personal notes, names, employer or client data, screenshots that show them.
- Features that need a server, a database or an account with a specific vendor.
- Large rule sets. Fewer, sharper rules beat more rules.

## Before you open a pull request
1. Run the checks from the repository root:
   ```bash
   python3 vault/.claude/scripts/wiki_lint.py
   ```
   ```bash
   python3 vault/.claude/scripts/session_start.py
   ```
2. Check your diff for anything personal: names, e-mail addresses, places, tokens, paths from your own machine.
3. Add a line to `CHANGELOG.md` under "Unreleased".
4. Keep the writing style of the repo: plain words, absolute dates, lists with one item per line.

## Code of conduct
This project follows the [Code of Conduct](CODE_OF_CONDUCT.md). By taking part you agree to it.

## Licence of contributions
By contributing you agree that your contribution is licensed under the [MIT licence](LICENSE) of this repository.
