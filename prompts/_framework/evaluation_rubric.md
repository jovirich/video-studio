---
title: Evaluation rubric
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# Evaluation rubric

How to judge a generated asset before it enters an edit. Used at selection time by
whoever generated it, and again at the pack's picture-lock equivalent.

The rubric exists because "does it look good?" is not a reviewable standard, and
because the failure that matters most — a plausible image that is quietly wrong — is
the one that looks best.

## The order matters

Judge in this order. Stop at the first failure; there is no point assessing the
composition of a shot that will be rejected for anachronism.

### 1. Is it honest? (blocking)

- [ ] Provenance class assigned, and correct
- [ ] Nothing in it invites being mistaken for archival or captured material
- [ ] If reconstruction: every depicted element traces to the evidence basis
- [ ] No named person depicted without clearance
- [ ] No sacred, restricted, or funerary material without a ruling
- [ ] Nothing depicted that the pack prohibits

**Fail here and the asset is deleted, not fixed.** Regenerating from a corrected card
is cheaper than arguing about whether a striking image can be salvaged — and the
argument is easier to have before the image exists, which is why the card is reviewed
first.

### 2. Is it accurate? (blocking)

- [ ] Anachronism pass complete: materials, textiles, tools, crops, architecture,
      weapons, writing, animals, imported goods
- [ ] Everything shown is attested, or is generic enough not to assert anything
- [ ] Any text in frame is correct in script, language, and orthography
- [ ] Geography and terrain consistent with the location record
- [ ] Skin tone rendered correctly across everyone in frame

This is where generated imagery fails most often and most embarrassingly, because
models default to a generic pan-historical vocabulary that is wrong everywhere and
obviously wrong to anyone who knows the subject.

### 3. Is it consistent? (blocking)

- [ ] Style anchor honoured; look matches the sequence around it
- [ ] Light direction, quality, and time of day match the scene
- [ ] Palette within the production's range
- [ ] Recurring characters and locations match their anchors
- [ ] Lens and depth of field from the defined set
- [ ] Grade compatible with the show LUT

Consistency failures are invisible while generating and glaring in a cut. Judge
against the neighbouring shots, not in isolation.

### 4. Is it technically sound? (blocking)

- [ ] Anatomy: hands, limbs, eyes, consistent count of people
- [ ] No garbled pseudo-text
- [ ] No duplicated or merged features
- [ ] Native resolution adequate; any upscale logged
- [ ] Video: temporally stable across the whole clip, not just frame one
- [ ] Video: physics plausible for water, fire, cloth, hair, crowds
- [ ] Safe zones hold for every deliverable aspect ratio

### 5. Does it work? (judgement)

- [ ] It accomplishes the `target.intent` stated on the card
- [ ] It cuts with the shots either side
- [ ] Composition serves the shot's job, not its own
- [ ] It does not draw attention to itself as an image

### 6. Is it beautiful? (last, and it is last for a reason)

A shot that passes 1–5 and is merely good is better than a shot that is beautiful and
fails any of them. The order of this rubric is its main content.

## Recording the judgement

Every assessed render gets a `runs[]` entry: `selected`, `rejected`,
`reference-only`, or `superseded`, plus a note.

**The note on a rejection is the valuable part.** "Rejected — synthetic-looking
weave on the wrapper, model defaults to machine-woven texture" is worth more to the
next person than any number of accepted shots. It is how a prompt library improves
rather than merely accumulating.

## Batch discipline

Generate a batch, assess against 1–4 mechanically, then choose on 5–6 from what
survives. Choosing on beauty first and then checking accuracy is the reliable way to
end up arguing for a shot you have already fallen for.
