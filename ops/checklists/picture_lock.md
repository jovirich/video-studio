---
title: Picture lock gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# Picture lock — checklist

| | |
|---|---|
| **Gate key** | `picture_lock` |
| **Owner** | `visual-director` |
| **Stage** | `06_edit` |
| **Blocks** | `07_audio_post`, `09_delivery` |
| **Blocked by** | `fact_check`, `sensitivity` — both must be `signed` first |
| **Packs** | documentary-history. The other three packs combine this with audio in [picture_audio_lock.md](picture_audio_lock.md) |
| **Completed copy** | `06_edit/checklists/picture_lock.md` in the production folder |

The per-shot QC list below is
[../../packs/documentary-history/04_visual_language.md](../../packs/documentary-history/04_visual_language.md)
§10, which names this gate as the place it is enforced. It runs **per generated
shot**, not once for the cut. A cut of 300 shots means 300 passes, and the discipline
of that is the point — the failures are per-shot and they do not announce themselves.

## What this signature certifies

> The cut is final. Every generated shot passed anatomy, anachronism, light
> consistency, skin-tone, and temporal stability checks. Every reconstruction and
> interpretive shot carries its label. Vertical and square safe zones hold.

## Per generated shot

Repeat for every generated shot in the cut.

- [ ] **Anatomy**: hands, limbs, eyes, and the count of people are correct and consistent across the shot
- [ ] **Text in frame**: no garbled pseudo-script; any lettering is deliberate and correct
- [ ] **Anachronism pass complete and recorded**: materials, textiles, crops, weapons, writing, architecture, animals, and imported goods each checked against period. This is where generated imagery fails most often and most embarrassingly, because models default to a generic pan-historical vocabulary
- [ ] **Light direction** consistent with the scene, and with a source that exists in the frame's logic. Generated imagery routinely violates this
- [ ] **Skin-tone rendering** matches the line standard. The single most common failure in both generation and grading; the show LUT must not crush or desaturate it
- [ ] **Style anchor ID** referenced and honoured
- [ ] **Temporal stability**: no flicker, morph, or drift across the clip
- [ ] **Provenance class assigned**; label applied where the class requires it
- [ ] **Prompt card and seed recorded** in the manifest

## The cut

- [ ] The cut is final. Not "final pending notes"
- [ ] Aspect discipline holds: one ratio for the body; any change is a deliberate device, never a tool default
- [ ] Frame rate conform is correct on every generated clip, and the conform method is recorded on the asset
- [ ] Optical-flow retiming artefacts checked for specifically — they survive grading and are cheapest to catch here
- [ ] Motion is motivated. Roughly a third of shots are locked; a drifting camera on every shot is the signature tell of generated video
- [ ] Depth of field is consistent with the stated lens and stop. Historical exteriors read false at f/1.4
- [ ] Shot-level grading works **under** the show LUT, never around it
- [ ] No continuous shot mixes `archival` and `reconstruction` material. A cut is required at the boundary
- [ ] Time of day is recorded per shot and consistent across each sequence

## Labels

- [ ] Every `reconstruction` and `interpretive` shot carries the in-frame mark for its **full duration**
- [ ] The mark sits inside title safe, holds contrast ≥ 3:1, is legible at 360p, and is never obscured by a caption
- [ ] The sequence-level explainer card appears at the first labelled shot
- [ ] No generated asset carries the `archival` provenance class

## Framing and safe areas

- [ ] Title safe 90%, action safe 93%
- [ ] **9:16 and 1:1 safe zones hold** — no critical information outside either. Vertical cutdowns are crops, not re-generations; a second generated vertical doubles cost and guarantees continuity drift
- [ ] On-screen text ≥ 1/20 frame height for body copy, contrast ≥ 4.5:1 measured
- [ ] Text is on separate layers in the project, so a textless master is a render and not a rebuild

## Text rendering

Per [../../packs/documentary-history/09_localization.md](../../packs/documentary-history/09_localization.md) §8:

- [ ] All diacritics and tone marks present and correctly positioned
- [ ] No mojibake, no fallback-glyph boxes, no dropped combining marks
- [ ] The font covers every character used, in every language on screen
- [ ] Right-to-left text renders correctly where it appears
- [ ] Names match the entity records **exactly** — checked mechanically, not by eye

## Prerequisites

- [ ] `fact_check` is `signed`
- [ ] `sensitivity` pass 3 of 3 is `signed`
- [ ] No advisory hold is open on any shot, sequence, or asset in the cut
- [ ] Every asset in the cut has a manifest entry

## Do not sign if

- **Any generated shot has not been through the per-shot list.** Sampling is not
  checking. The failures are per-shot and independent; a clean sample says nothing
  about the shot next to it.
- **The anachronism pass was done by eye, in one viewing.** It is a recorded pass
  against a named list, and it is the check most likely to be skipped because it is
  slow and the shot looks beautiful.
- **`fact_check` or `sensitivity` is not yet `signed`.** They block this gate by
  design; locking first and reviewing after inverts the entire structure.
- **A shot survives because regenerating it is expensive.** Regeneration is cheaper
  now than after audio post, and vastly cheaper than after publication.
- **Safe zones were checked on the 16:9 master only.** The vertical crop is where
  captions and marks collide with the frame edge, and nobody looks at it until the
  cutdown is due.
- **You signed another gate on this production.**

## Signature

| Field | Value |
|---|---|
| Role | `visual-director` |
| Person | |
| Date | |
| Shots checked | of |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
