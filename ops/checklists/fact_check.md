---
title: Fact-check gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# Fact-check — checklist

| | |
|---|---|
| **Gate key** | `fact_check` |
| **Owner** | `research-lead` |
| **Stage** | `08_review` |
| **Blocks** | `picture_lock`, `09_delivery` |
| **Packs** | documentary-history |
| **Completed copy** | `08_review/checklists/fact_check.md` in the production folder |

This gate is at stage `08_review` and **blocks picture lock, which is at
`06_edit`** — so it happens before the cut locks, not after. Reading the folder
numbers as a sequence puts this review a full cycle too late
([../workflow_states.md](../workflow_states.md) §4).

Script lock checked that every statement carries a claim ID. This gate checks that
every ID still resolves, at tier, **in the material as it now exists** — including
everything that was never in the script.

## What this signature certifies

> Every claim referenced in the locked script resolves to a claim record at the
> required tier; on-screen text, graphics, maps, and the production description have
> been checked to the same standard as narration.

## Checks

### Narration

- [ ] Every `{{CLM-*}}` reference in the locked script resolves to a claim record that exists
- [ ] Every resolved claim is at the tier its register requires, **as of today** — a claim downgraded since script lock is a blocker, not a note
- [ ] No claim has been retracted or superseded since script lock without the script being updated
- [ ] The spoken register still matches the claim's register after the edit. Trimming a qualifying clause for time converts a `probable` into an `established`
- [ ] Every figure spoken carries its basis and its `attested` / `estimated` / `modelled` marking

### Everything that is not narration

This is where fact-check gates fail. The script was checked twice; these were checked
once, or not at all.

- [ ] **On-screen text**: titles, lower thirds, dates, name spellings, quotations — each checked to the same standard as narration, with claim IDs where they assert
- [ ] **Quotations**: verified against the source, with the source named on screen; translation credited
- [ ] **Graphics and timelines**: every asserted date, figure, and sequence carries a claim ID; sources on the graphic or in the credits
- [ ] **Maps**: projection stated; historical borders drawn as zones of influence rather than crisp lines unless a treaty line is being depicted and cited; every map cites its geographic **and** historical sources
- [ ] **Modern borders** are never drawn over pre-modern periods without an on-screen note that they are a modern overlay for orientation
- [ ] **Data graphics**: no truncated axes, uncertainty shown, source and date in frame — per [../../standards/data_graphics.md](../../standards/data_graphics.md)
- [ ] **The production description, title, and chapter titles**: a title implying a claim the production does not make is an accuracy failure, not a marketing decision
- [ ] **The thumbnail**: does not depict something the production shows to be false, and is not presented as a photograph

### Reconstructions as assertions

- [ ] Every `reconstruction` shot's `evidence_basis` still resolves to live claim and source records
- [ ] No reconstruction asserts a contested detail as settled. Where a detail is contested, the shot was framed around it
- [ ] No named figure appears in a way the record does not support in its specifics
- [ ] Ambience is checked as a claim: species, languages, industry, and animals in a soundscape are period- and place-specific assertions

### The three failure modes

Checked deliberately, because they are not equally visible
([../../packs/documentary-history/01_editorial_standards.md](../../packs/documentary-history/01_editorial_standards.md) §1):

- [ ] **False statement** — nothing asserted that the sources do not support
- [ ] **Overclaimed statement** — nothing settled that is contested; no precise date where sources give a range
- [ ] **Misleading true statement** — no true fact placed so as to imply something false; no real image cut so as to suggest a different time or place; no juxtaposition that asserts a causal link the evidence does not

The third is the one that kills documentaries and the only one that requires watching
the cut rather than reading the script.

### Record hygiene

- [ ] Open questions arising during review are registered, not carried in a reviewer's head
- [ ] Any claim corrected during this pass is corrected on the **record**, not only in the cut
- [ ] The corrections log exists and is ready to be published alongside, empty at launch

## Do not sign if

- **Any claim ID does not resolve.** A dangling reference means either the script or
  the registry moved and nobody noticed.
- **On-screen text, maps, or graphics were not checked** because "they came from the
  script". They did not — they were made by someone else, later, from a brief.
- **The description or title was written by someone other than the people who made
  the production and has not been checked.** It is the first factual claim the
  audience meets, and it is routinely the only one nobody fact-checked.
- **A misleading juxtaposition survives because both shots are individually
  accurate.** Both being true is the mechanism, not the defence.
- **You are being asked to sign so the cut can lock.** This gate blocks picture lock
  by design. Mark it `blocked` and name the blockers.
- **You signed `source_lock` on this production.** See
  [../roles.md](../roles.md) §5.1 — this is the doubled-role case with the sharpest
  conflict, because it is the same person checking their own research pack twice.

## Signature

| Field | Value |
|---|---|
| Role | `research-lead` |
| Person | |
| Date | |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
