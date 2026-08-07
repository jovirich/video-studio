---
title: AI-use statement — reusable credits block
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [showrunner, pipeline-engineer]
---

# AI-use statement

The reusable block referenced by
[../../../core/01_provenance_and_ai_disclosure.md](../../../core/01_provenance_and_ai_disclosure.md) §3
as disclosure level 3. It appears in the credits of every production and, in
condensed form, in the platform description.

Unlike everything else in this directory, **this file is not `_TEMPLATE_` prefixed**,
because its structure is fixed platform-wide. What varies per production is which
tools filled which rows. Copy it into the production's `10_publish/`, fill the
table, delete the unused rows, and delete the guidance sections at the bottom.

---

## The block

> ### How this was made
>
> This film was made with generative tools. We say so in detail because the
> technique is legitimate to the degree that it is disclosed and bounded, and
> because a viewer cannot judge what they cannot see.
>
> | Used for | Tool | What it did |
> |---|---|---|
> | Reconstruction imagery | TBD — vendor and model | Still images depicting scenes for which no photographic record exists |
> | Reconstruction motion | TBD | Movement applied to reconstruction stills |
> | Interpretive imagery | TBD | Visual figures for subjects not directly depictable |
> | Restoration and cleanup | TBD | Repair of damage to genuine archival material, without altering its content |
> | Narration voice | TBD | Synthetic narration, licensed from a consenting living performer |
> | Music and texture | TBD | Score and atmospheric texture |
> | Sound effects | TBD | Utility effects and designed sound |
> | Maps and graphics | TBD | Rendering of maps, charts, and timelines |
> | Captions and translation drafting | TBD | First-pass drafts, reviewed and corrected by named people below |
> | Research assistance | TBD | Locating and summarising material that was then read in full and verified against the original |
>
> **Every shot built by these tools carries a mark on screen for its full
> duration.** Where you do not see that mark, you are looking at genuine archival
> material, a photograph of a real object, or footage shot in the present day.
>
> **What we did not do.** No image, document, recording, or artefact in this film
> was generated to be taken for a genuine historical item. No real or historical
> person's likeness or voice was synthesised. No evidentiary gap was filled by a
> model: where the record is silent, the film says so. No generative tool made a
> factual claim — every fact stated here was entered by a researcher and traced to
> a source.
>
> **Where the pictures come from.** A per-shot provenance record for this film —
> which tool, which prompt, which evidence — is published at TBD — URL.
>
> **The people this film depends on.** Generative tools change what the work costs;
> they do not change whom it belongs to. The scholars, translators, language
> consultants, and knowledge holders credited below were paid for their work,
> named at their own request or anonymised at it, and given the opportunity to
> review the material they informed before release.

---

## Filling it in

| Field | Where the answer comes from |
|---|---|
| Tool names | The `generation.tool` blocks in the production's `manifest.yaml` — never from memory |
| Rows to keep | One per category actually used. Delete the rest; a row reading "not used" is noise that hides the rows that matter. |
| Provenance URL | The published provenance summary for this production |
| Narration voice row | Delete entirely if narration is a human performance. Do not write "human narration" here — the absence of the row is the statement. |

## Rules that do not vary per production

1. **Category, not marketing.** Name what the tool did in terms a viewer can check
   against what they saw. "AI-enhanced visuals" is not a disclosure.
2. **The negative list is not optional.** "What we did not do" is the part a
   sceptical viewer is actually looking for, and it is the part that costs
   something to write honestly. If any line of it is not true of this production,
   the production does not ship — the line is not edited.
3. **No hedge on the mark.** If a labelled shot went out unlabelled, the statement
   is false, and a false disclosure is worse than none: it converts an error into a
   claim.
4. **Substitution is stated.** Where a tool stood in for a craft role —
   illustration, VO, score — say so, rather than leaving the absence of that credit
   unexplained. The person who would have had that credit notices.
5. **The provenance link resolves before publication**, not after. A dead
   disclosure link is read, correctly, as a disclosure that was never intended to be
   checked.

## The test this block is written against

> **If a viewer learned exactly how this shot was made, would they feel informed or
> deceived?**

If the honest answer is "deceived", no wording here fixes it. The shot does not
ship. Everything above is an attempt to make that judgement mechanical enough to
survive a deadline.
