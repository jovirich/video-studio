---
title: EXP-001 — decisions and approvals
status: draft
maturity: NOT STARTED
version: 0.2.0
updated: "2026-08-07"
owners: [showrunner, visual-director]
---

# EXP-001 — what is decided, and what still needs you

## Locked — no action

Directorial calls made and written into the records. Nothing here needs revisiting
before the diagnostic shots.

| | Where |
|---|---|
| A — age, presentation, skin swatch `#70452F`, hair, beard, build, height, face, eyebrow scar, wardrobe, wrist cord | [`CNC-NG-0001`](../../continuity/characters/CNC-NG-0001_character-a.md) |
| B — age, presentation, skin swatch `#87583D`, hair, build, height, face, cheek birthmark, wardrobe | [`CNC-NG-0002`](../../continuity/characters/CNC-NG-0002_character-b.md) |
| Workshop — geometry, materials, prop zones, anchors, light direction, camera-safe geography, forbidden objects, lighting variants | [`CNL-NG-0001`](../../continuity/locations/CNL-NG-0001_workshop.md) |
| Mechanism — reference-image conditioning, same for both, **no trained adapter** | both character records |
| Shot plan, stress axes, acceptance thresholds, drift severity 1–5 | [`shot_plan.md`](03_storyboard/shot_plan.md) |
| Per-run recording requirements | both character records, `references.approved_seeds` |

---

## Waiting on you — 1. Choose the vendor

**Nothing can be generated until this is decided.** All three anchor cards carry
`vendor: TBD`, and no spend has been incurred.

| Decision | Constraint |
|---|---|
| **One vendor, one model, one exact version identifier** | The *same* one for A, B, and the workshop, held fixed across all four diagnostic shots. Mixing them makes a shot-18 failure uninterpretable. |
| **Terms verified** before first generation | Recorded in [`model_terms_register.md`](../../../../../rights/permissions/model_terms_register.md). Every row there currently reads `not yet checked`. The card's `terms_checked` field is filled that day and not before. |
| **A generation ceiling** for EXP-001 | The adapter refuses a priced run with no ceiling, so this is a hard blocker rather than an oversight. |

`local` stays the mechanics test. Its deterministic colour field proves the round
trip and cannot serve as a face anchor.

## Waiting on you — 2. Approve three visual assets

These are the only artefacts needing sign-off before production shots. Each has a
written specification and an acceptance checklist; **approval is against the
checklist, not against taste.**

| # | Asset | Specification | Becomes |
|---|---|---|---|
| 1 | **A's canonical face** | [`PC-NG-EXP001-0001`](04_prompts/PC-NG-EXP001-0001_anchor-a-face.prompt.yaml) | `CNC-NG-0001.references.facial_reference` |
| 2 | **B's canonical face** | [`PC-NG-EXP001-0002`](04_prompts/PC-NG-EXP001-0002_anchor-b-face.prompt.yaml) | `CNC-NG-0002.references.facial_reference` |
| 3 | **Workshop establishing wide** | [`PC-NG-EXP001-0003`](04_prompts/PC-NG-EXP001-0003_anchor-workshop-wide.prompt.yaml) | `CNL-NG-0001.reference_imagery.establishing_anchor` |

**No production shot may be generated until all three are approved.** An anchor
approved after the fact is not a measurement; it is a description of whatever the
model produced.

### The four things most likely to go wrong at approval

Worth checking deliberately, because each is easy to miss and expensive later:

1. **The scar on the wrong side.** Models mirror. A's scar is the **right** eyebrow.
   If the anchor has it left, every one of A's seventeen shots inherits the error.
2. **B acquiring A's scar.** Listed as a negative on B's card on purpose. If it
   appears at anchor stage, the vendor is already bleeding features between two
   similar prompts — and that is worth knowing before any production shot exists.
3. **The two anchors not matching photographically.** Same framing, lens, light,
   background. If they differ, a difference between the rendered characters could be
   the anchors rather than the mechanism, and shot 18 becomes uninterpretable.
4. **Workshop light from the wrong side.** It must rake from **frame left**. Nineteen
   later shots are checked against this frame for it; if the anchor is wrong, the
   whole set inherits the error and nothing can be scored.

---

## Not needed yet

So this list stays short:

- The other sixteen shot records and prompt cards
- Location geometry in 3D — decide after the four diagnostic shots
- Any drift-test result — that is the **output** of those shots, not an input
- Anything about EXP-002

## Nothing else is blocked

Every other field in the three continuity records is either filled or is properly an
output of the diagnostic run.
