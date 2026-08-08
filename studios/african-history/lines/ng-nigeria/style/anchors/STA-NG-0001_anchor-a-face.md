---
id: STA-NG-0001
type: style_anchor
line: ng-nigeria
title: Character A — canonical face anchor
status: locked
version: "1.0.0"
updated: "2026-08-08"
owners: [visual-director]
sensitivity: review-required

anchor_kind: character

# The bytes, and the hash of the bytes. The hash is the anchor; the path is only
# where the bytes currently sit. Verified before every generation run — an anchor
# whose file can change without notice is not an anchor.
file: ng-nigeria/productions/EXP001/generated/EXP001_ANCHOR_PC-NG-EXP001-0001_v0.2.0_c01.png
sha256: 1ff0c6f5ce7cd3fc3977d3ba129c7949be770dd6723b9cd6ada8568568162f05

# This anchor is itself generated, so it carries its own provenance.
derived_from: AST-NG-EXP001-0001

applies_to: [CNC-NG-0001]

description: >
  Character A's face, fixed. Held constant: the long-oval face, strong jaw and
  pronounced cheekbones; short tightly coiled hair with the hairline visible; the full
  beard and moustache; and above all the SMALL VERTICAL SCAR THROUGH THE CENTRE OF THE
  CHIN, on the midline, reading as a hairless parting in the beard.

  Free to vary: expression, head angle, lighting, wardrobe, and everything about the
  environment. This anchor fixes who the person is, not how a shot is lit.

  The scar is the binary check. A render that loses it, or places it off the midline,
  fails regardless of how convincing the face looks.

notes: >
  LABORATORY DESIGN. A is invented and is not representative of any real person,
  people, or culture, at any period. The skin-tone target is a continuity reference,
  not an ethnicity classifier. EXP-001 is permanently non-publishable.
---

# Style anchor STA-NG-0001 — Character A's face

## Provenance

Generated in **interactive mode** through the ChatGPT UI on 2026-08-07 from prompt card
`PC-NG-EXP001-0001` at card version **0.2.0**, and ingested as `AST-NG-EXP001-0001`.

The vendor is OpenAI. **The exact model snapshot is not known**, and is recorded as
unverifiable rather than guessed. An interactive surface does not tell the operator
which snapshot served the request, so the pinned identifier that `run_plan.yaml` names
for API execution cannot be asserted here. Recording it anyway would have made an
unverifiable claim look like a verified one.

That has a consequence worth stating plainly: **this anchor is not reproducible.** It
can be re-used, because the bytes and their hash are fixed, but it cannot be
regenerated, because nothing here identifies what produced it precisely enough. The
first API-mode anchor will be reproducible; this one is not.

## Why this candidate

It is the only candidate generated from card v0.2.0, and it was approved on inspection
rather than by comparison. The four files that appeared alongside it named this same
card, but were 627×627 — quadrants of a single 2×2 composite, carrying the superseded
lateral scar. They are quarantined, and none of them is an alternative to this.

## What it proves

**The midline feature landed on the first attempt.** Across twelve earlier candidates a
lateral mark reached the specified side once. A midline mark has no side to get wrong,
and this render bears that out: the scar is unambiguous, centred, and legible through
the beard rather than hidden by it.

That was the open question when the feature moved from the eyebrow to the chin. It is
now answered, and the answer is the reason this anchor can be approved at all.

## History

| Version | Date | Change | Cause | Shots already inheriting |
|---|---|---|---|---|
| 1.0.0 | 2026-08-08 | Created and approved | First anchor generated from card v0.2.0; midline scar confirmed | none |

Locked on approval. Changing it now would not update anything downstream — it would
make future shots inconsistent with earlier ones. Supersede instead, and regenerate
deliberately.
