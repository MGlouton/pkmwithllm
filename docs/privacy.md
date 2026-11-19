# Privacy

This is an orientation, not legal advice.

## What leaves your device
Your notes stay files on your disk. But every file the agent reads, and everything you type in a session, is sent to the provider of the model the agent uses, and may be processed outside the EU and Switzerland. Check your provider's terms for retention and training use, and the settings of your account.

If Git sync is on, the vault is also stored at your Git host.

## What the template does
- `private/` is excluded from Git by `.gitignore` and denied to Claude Code in `.claude/settings.json` (read, write, edit and common shell commands). Keep health, finance, legal and identity documents there.
- `CLAUDE.md` tells the agent to stop and tell you when a note contains such data, other people's personal data, or an employer's internal data, and never to file it into the wiki.
- `CLAUDE.md` forbids storing passwords, tokens and ID numbers anywhere in the vault.

The deny rules reduce the risk of mistakes; they are not a security boundary. A determined command can still read any file the agent's process can read. If something must never reach a model provider, keep it outside the vault folder.

## Other people's data
Notes about other people are personal data under the EU GDPR and the Swiss FADP. For a purely personal vault the household exemption usually applies, but sending such notes to a cloud model is still a transfer to a third party. Prefer topics over people: write "what I learned about negotiating", not a page about a colleague.

## Work data
Data from your employer or its clients does not belong in a private vault processed by a private AI account, whatever the tool. Use the tools your employer provides for that, and bring only public or sanitised results into the vault.

## Options that keep data in the EU or on your device
- A European model provider, for example [Mistral AI](https://mistral.ai) (France), used through an open-source agent such as [opencode](https://opencode.ai) or [Aider](https://aider.chat).
- A local model through [Ollama](https://ollama.com) (open source). Expect weaker results on long, multi-step tasks than with large cloud models.
- A European Git host such as Codeberg, or a self-hosted Forgejo, for sync.

Check the current terms and data locations of any provider yourself before you choose; they change.
