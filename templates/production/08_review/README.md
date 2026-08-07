---
title: 08_review — fact-check, sensitivity, rights, notes
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [research-lead, cultural-advisor, rights-and-clearances]
---

# 08_review

Three gates converge here, owned by three different people, and none of them is the
person who made the thing. That separation is the point: the most common review
failure is not incompetence but proximity — the person who made it cannot see it.

## What goes here

| File | Template | Owner |
|---|---|---|
| `FCK-XX-S00E00-0000_fact-check.md` | [_TEMPLATE_fact_check_report.md](_TEMPLATE_fact_check_report.md) | Research Lead |
| `cut_notes_v<NN>.md` | [_TEMPLATE_cut_notes.md](_TEMPLATE_cut_notes.md) | whoever is giving notes |
| `sensitivity_pass_03.md` | pack checklist | Cultural Advisor |
| `rights_review.md` | pack checklist | Rights & Clearances |
| `holds.md` | — | any contributor may open one |

The completed gate checklists themselves are committed at the paths named in
[../production.yaml](../production.yaml). The canonical checklist set is the pack's:
[../../../packs/documentary-history/checklists/](../../../packs/documentary-history/checklists/)
and [../../../ops/checklists/](../../../ops/checklists/).

## Before this stage starts

- **Script lock is signed** — the fact-check runs against a fixed script, because a
  fact-check against a moving one checks nothing.
- **Picture lock is signed** for the sensitivity and rights passes over the cut.
- The manifest is complete: every asset present, with a rights status and a label
  state.

## The three gates

### Fact-check — Research Lead

Certifies that every claim referenced in the locked script resolves to a claim
record at the required tier — and that **on-screen text, graphics, maps, and the
episode description have been checked to the same standard as narration.**

That last clause is the one that gets skipped. A map asserts an extent. A timeline
asserts a sequence and, by adjacency, a cause. The description is the text most
likely to be quoted back at the studio, and it is usually written last, quickly, by
whoever is available.

### Sensitivity — Cultural Advisor (third pass)

Over the locked cut: premise, prompt set, and now the assembled thing. This gate
carries **hold authority the Showrunner cannot unilaterally override**. A hold takes
effect immediately, is released only in writing by the Cultural Advisor, and the
person who raised it is never penalised for having raised it.
[../../../core/04_review_gate_framework.md](../../../core/04_review_gate_framework.md) §6.

### Rights — Rights & Clearances

Certifies that **no asset in the manifest is at `pending`**, that model terms were
re-checked at delivery rather than at the start of the production, that the cue
sheet is complete, and that chain of title assembles.

Terms change. A tool cleared at prompt stage may not be cleared at delivery, and the
only way to know is to check again.

## Before this stage can be left

All three gates signed, plus:

- **Every finding is resolved or accepted in writing.** An unresolved finding
  carried into delivery is a finding that will be resolved in public.
- **A correction path exists for anything accepted as a known limitation.** See
  [../../records/_TEMPLATE_correction.md](../../records/_TEMPLATE_correction.md).

## A note on separation of duties

No person signs two gates on the same production
([../../../core/04_review_gate_framework.md](../../../core/04_review_gate_framework.md) §5).
On a small team this is the first constraint to come under pressure, and the
pressure is always framed as pragmatism. Being flagged for it is a staffing signal,
not a paperwork problem — the correct response is to find a fourth person, not to
sign twice.
