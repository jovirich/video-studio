---
title: 04_prompts — prompt cards
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, pipeline-engineer]
---

# 04_prompts

One prompt card per generated asset, written and reviewed **before** the asset
exists.

## What goes here

```
04_prompts/
├── PC-XX-S00E00-0000_<slug>.prompt.yaml    one card per generated asset
└── overrides.md                            deviations from the line's style block,
                                            each with a stated reason
```

Card naming is fixed by
[../../../standards/naming_conventions.md](../../../standards/naming_conventions.md)
§ Prompt cards. The slug describes **content**, never tool or settings:
`walls-establishing` is right, `mj-v7-ar169-stylize250` is wrong — those belong in
`parameters`, where they are queryable.

Template: [_TEMPLATE_card.prompt.yaml](_TEMPLATE_card.prompt.yaml).
Studio-scoped cards reusable across productions live in
[../../../prompts/](../../../prompts/) with `PC-STUDIO-` IDs.

## Why cards exist at all

A prompt card is a **record**, not a text string. Four things follow from that, and
each is the answer to a specific way productions go wrong:

| Property | The failure it prevents |
|---|---|
| **Reviewable before generation** | Once a striking image exists, the argument about whether it should exist is much harder to win. Reviewing the card is the only moment the question is cheap. |
| **Versioned, never overwritten** | "Why does shot 42 look different now" is otherwise unanswerable, and the answer is usually a prompt edit nobody recorded. |
| **Structured, not a blob** | `studio_ops promptlib render` targets more than one vendor from one card. A hand-assembled string is locked to the tool it was written for, which is a problem the first time a vendor changes its terms. |
| **Carries the evidence basis** | A reconstruction is a claim about the past made in pictures. The card is where that claim is attached to the record that grounds it. |

Together with the seed and parameters recorded in
[../manifest.yaml](../manifest.yaml), a card makes a generated shot
**reproducible** — which is what turns "that image looks wrong" from an argument
into an examination.

## Before this stage starts

- **Script lock is signed.** The gate blocks this stage. Generating against an
  unlocked script inverts the direction of authority between the argument and the
  footage.
- A shot record exists for every shot a card will serve
  ([../03_storyboard/](../03_storyboard/)).
- The vendor's terms are current in the model terms register
  ([../../../rights/permissions/](../../../rights/permissions/)) and permit
  commercial documentary use. A tool whose terms do not permit the use does not
  enter the pipeline, however good it is.

## Before this stage can be left

The **sensitivity** gate runs its second of three passes here — over the whole
prompt set, before a single generation run. Additionally:

1. **Every generated asset has a card.** No card, no run; the adapters take a card
   ID, not a string.
2. **Reconstruction cards carry an evidence basis.** The schema requires it. An
   empty basis means the image asserts a past that nothing in the record supports.
3. **No card depicts a named person without a clearance reference.** The schema
   requires `person_ref` and `clearance_ref` together with
   `depicts_named_person: true`. Synthesising a historical figure's likeness or
   voice is prohibited outright — consent is impossible, so the question does not
   arise.
4. **Style overrides carry reasons.** An override without a reason fails review,
   because the accumulation of unexplained overrides is how a production's look
   drifts one defensible step at a time.
5. **Third-party inputs carry rights notes.** Feeding uncleared material to a model
   is a rights event, not a technical step.

## Prohibitions that no review can waive

From [../../../core/01_provenance_and_ai_disclosure.md](../../../core/01_provenance_and_ai_disclosure.md) §2 —
absolute, no override flag:

- Generating anything intended or likely to be taken for a genuine historical item.
  A generated asset may never carry the `archival` provenance class; the schema
  refuses the combination.
- Synthesising a real or historical person's likeness or voice without documented
  consent or estate clearance.
- Filling an evidentiary gap. If the research does not know, the model does not get
  to decide.
- Generating sacred, initiatory, or restricted material without an advisory ruling.
- Generating identifiable victims of documented violence.
