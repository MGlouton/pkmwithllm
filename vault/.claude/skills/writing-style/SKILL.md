---
name: writing-style
description: Rewrite English or German prose so it reads like a person wrote it, without changing what it says. Use when the user says "writing style", "humanize", "sounds like AI", "edit the style", or as a final pass on a page others will read. Finds AI tells (not X but Y, forced triads, bold labels, arrows, summary closers, inflated words, vague authorities) and rewrites whole paragraphs. Never adds facts. Never reads private/.
---

# Writing style: write like a person, not like a model

Based on [blader/humanizer](https://github.com/blader/humanizer) v3.1.0 (MIT licence, copyright its authors), whose patterns draw on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Adapted for a Markdown vault, in English and German. This notice must stay in the file.

Ground rule: the aim is better text, not hiding AI use. Most problems are vague content and missing weighting, not single words. Swapping words alone is not a fix.

## Never touch
Frontmatter, `[[wikilinks]]`, callouts, code, paths, URLs, numbers, dates, names, quotes from sources, table structure. No new facts, figures, sources or examples. Uncertainty markers ("assumption", "unverified") stay. If a claim looks unsupported, flag it in the report.

## Voice
If `voice.md` exists in this folder, match its sentence length, word choice and punctuation; it overrides the general rules below. Write one from a sample of your own text when you have the time.

## Patterns
Patterns 1 to 6 justify an edit on one sighting. Weak ones need a second tell in the same paragraph.

| # | Pattern | Example | Fix |
|---|---|---|---|
| 1 | Not X but Y, contrast framing | "not a fix but a rebuild"; «nicht nur …, sondern auch» | State the claim directly |
| 2 | One-line closers, summary sentences | "In short, it works." | Cut, or merge into the paragraph |
| 3 | Sayings that sound deep | "Trust is the currency of teamwork." | Replace with the specific claim |
| 4 | Writing about the text | "Let's unpack …", "This section covers …" | Start with the fact |
| 5 | Arguing with no one | Rejects an option nobody proposed | Remove |
| 6 | Chatbot residue | "I hope this helps", "As of my last update" | Remove |
| 7 | Forced triads | three adjectives in a row | Keep only items that differ in substance |
| 8 | Bold as decoration, bold labels | "**Key point:** …" | Remove the bold |
| 9 | Arrows as connectors | "capture → file" | Write the verb |
| 10 | Inflated significance | "pivotal", "seamless", "robust", «ganzheitlich» | Say what the thing does, or drop it |
| 11 | Filler connectors | "moreover", "furthermore", «darüber hinaus» | Delete |
| 12 | -ing riders | "…, highlighting its role" | Cut unless a source says it |
| 13 | Vague authority | "Experts believe", «Studien zeigen» | Name and link the source, or cut |
| 14 | Avoiding "is" and "has" | "serves as", "boasts", «stellt … dar» | Use "is", "has" |
| 15 | Repeated openings | three sentences starting with "We" | Merge or vary |
| 16 | Stacked hedges (weak) | "may potentially" | One qualifier, if justified |
| 17 | Dashes everywhere (weak) | " — " mid-sentence | Comma, colon, full stop, brackets |
| 18 | Passive without actor (weak) | "Results are saved" | Name who does it |
| 19 | Heading repeated in first sentence | "## Goal" then "The goal is …" | Delete the restatement |
| 20 | Decorative headings | emojis, Title Case, "Conclusion: The Road Ahead" | Sentence case, plain words |

## Lists
Several items side by side: a short lead-in with a colon, then one item per line, no blank lines between. Numbered for sequences. No bold labels; use a table if items need labels. Reasoning stays in paragraphs.

## Content checks
- Each thought appears once.
- Arguments are weighted (what matters most and why), not just listed.
- A named method is actually used, not only mentioned.
- Recommendations cite a source or a comparable case, or say that none exists.

## Workflow
1. Read the whole text once. Mark every tell, strongest first.
2. Rewrite paragraph by paragraph around each paragraph's main point. Vary sentence length. Keep every claim, link and number.
3. Audit: compare old and new. Did a fact, link, number or qualifier disappear or appear? Undo it. Search again for the tells that most often survive: 1, 2, 7, 8, 9, 17.
4. File mode: edit in place, set `review: needed` if the text changed a lot, and log `## [YYYY-MM-DD] edit | Writing-style pass: <page>`. Pasted text: return the new version and a short list of changes.
5. Report the patterns found and any content issue flagged but not fixed.

## Limits
Word lists change with each model generation; the structural patterns last. Do not judge whether a person or an AI wrote a text; no detector is reliable.
