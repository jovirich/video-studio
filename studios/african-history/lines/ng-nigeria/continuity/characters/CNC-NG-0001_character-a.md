---
id: CNC-NG-0001
type: continuity_character
line: ng-nigeria
title: Character A — the worker (invented)
status: draft
version: 0.1.0
updated: "2026-08-07"
owners: [visual-director]

# No `entity` link. A is invented for EXP-001 and answers to no evidence record,
# because there is no historical person for them to answer to.

canonical_name: A

# ---------------------------------------------------------------------------
# DIRECTORIAL — every field below marked TBD is a decision for the Showrunner or
# Visual Director. They are deliberately unresolved. See DIRECTOR_DECISIONS.md.
#
# The whole test is meaningless if these are not fixed BEFORE generation: drift is
# measured against this record, so a record written after the fact simply describes
# whatever the model happened to produce.
# ---------------------------------------------------------------------------

age_range:
  low: TBD
  high: TBD
  life_stage: TBD
  basis: >
    directorial — A is invented and no evidence constrains this. Pick a range narrow
    enough to be falsifiable: "30–40" is checkable, "adult" is not.
  claims: []

appearance:
  skin_tone: TBD
  # A swatch asset or a named value, NOT a word. "Deep brown" is not checkable and
  # two reviewers will score it differently. The acceptance threshold for skin tone
  # is 20/20 with no allowance, so it needs something a person can hold against a
  # frame. Generate or select a swatch and reference it here.
  skin_tone_reference: TBD
  hair: TBD
  # Style, length, texture, and how it sits. Include FACIAL HAIR here if any — the
  # schema has no separate field for it, which is a finding.
  body_build: TBD
  height_relative: TBD
  # Relative to B, not absolute. Absolute height means nothing to a generator; a
  # two-shot needs to know who is taller and by roughly how much.
  facial_structure: TBD
  eyes: TBD
  posture_and_gait: >
    TBD — needed for shot 10 (walking) and shot 13 (turn). Posture is routinely
    forgotten until a motion shot looks like a different person.
  hands: >
    TBD — A's hands are on screen at 85mm in shots 02 and 11, working cord. This is
    the highest-risk detail in the set: hands are the reliable generative failure
    point, and here they are the subject rather than incidental. An occupied hand
    generates far better than an idle one, which the shot plan already assumes.

distinctive_features: []
# TBD — optional, and worth considering deliberately rather than by default.
# A single unambiguous feature makes drift much easier to SCORE, because it is
# binary: present and correct, or not. Without one, `same_person` scoring leans on
# gestalt judgement, which is exactly what the shot plan is trying to avoid.
# If added: `always_visible: true` so it can be checked in every shot.

# PRIMARY wardrobe. One set only. The shot plan does not require a change of
# clothes, and adding one would introduce a second variable into a test whose whole
# point is isolating identity drift.
wardrobe:
  - set_id: primary
    when_worn: all twenty shots
    items:
      - TBD — upper garment
      - TBD — lower garment
    materials: [undyed plant-fibre cloth, hand-woven]
    colours: [TBD]
    construction: >
      Hand-sewn, irregular seam, no machine stitching and no regular selvedge — see
      the location's forbidden_objects.
    condition: >
      Worked-in. Soft from washing, slightly dusty at the hem. Not new, not ragged.
    evidence: []
    reference_images: []

# ACCESSORIES. The schema field is `jewellery_and_adornment`, which is a slightly
# narrower word than "accessories" — a working cord at the wrist is neither jewellery
# nor adornment. Recorded here anyway as the nearest existing field; flagged as a
# finding rather than adding a new one under the freeze.
#
# Deliberately minimal, and NOTHING that signifies status, office, or rank. An item
# that signifies is a claim about a person, and A is invented — there is nothing for
# it to be a claim about. It would also pull the setting toward a real culture,
# which is the one thing this production must not do.
jewellery_and_adornment: []

references:
  # `facial_reference` and `drift_test` are OMITTED, not set to TBD.
  #
  # They are typed and pattern-constrained — an STA-* id, an integer, a boolean — and
  # `TBD` is only legal in free-text fields. For these, "not yet decided" is properly
  # expressed by absence, and the schema treats them as optional for exactly that
  # reason. Writing TBD into them fails validation, which is the schema working.
  #
  # facial_reference: STA-NG-NNNN   <- the single canonical face. Every later shot is
  #                                    scored against it. Must exist before shot 01 is
  #                                    ACCEPTED, not after.
  # drift_test:                     <- added once shots 01, 04, 06, 18 have been run.
  #                                    It is the OUTPUT of those shots, not an input,
  #                                    and the schema requires it before this record
  #                                    can reach status: locked.
  anchor_set: []
  # A seed does not transfer between models, or between versions of one model.
  # Record vendor, model, AND model_version with every seed, or the entry is useless.
  approved_seeds: []
  trained_adapter: {}

# A is never heard. EXP-001 generates no audio at all.
voice: {}

forbidden_variations:
  - forbidden: any change of garment between shots
    why: >
      The shot plan tests identity drift, not wardrobe continuity. A second costume
      would add a variable and make a failure ambiguous.
    severity: style-breach
  - forbidden: jewellery, beadwork, or worked metal adornment
    why: >
      Adornment that signifies status or office would make A a depiction of a
      specific culture's practice. EXP-001 must not become that.
    severity: culturally-prohibited
  - forbidden: scarification, body marking, or hairstyle carrying cultural meaning
    why: >
      Same reason, and it would require an advisory ruling that does not exist. Note
      the severity: this routes to the sensitivity gate as a hard stop, NOT to a
      negative prompt.
    severity: culturally-prohibited
  - forbidden: footwear of any modern construction
    why: invented pre-industrial setting; visible in shots 08, 10, 14, 20
    severity: anachronism
  - forbidden: eyeglasses, wristwatch, or any manufactured object on the person
    why: as above
    severity: anachronism

# Not applicable. A is invented, so there is nothing about them that is uncertain —
# there is simply nothing to be certain OF. This field assumes a historical subject
# and is empty by design here, not by omission. Flagged as a finding.
historical_uncertainty: []

appears_in: [EXP001]
---

# Character A — the worker

> ## Laboratory design — invented, and not representative of anywhere
>
> A is **invented for a continuity stress test**. Every visual detail recorded here is
> laboratory design, chosen for what it does to a camera and for nothing else.
>
> **A is not a depiction of, and does not represent, any real person, people, or
> culture.** No garment, adornment, hairstyle, tool, or craft practice associated with
> A is offered as historically representative of Benin, Nigeria, West Africa, or
> anywhere else, at any period. There is no evidence basis because there is no claim.
>
> EXP-001 is permanently non-publishable, and nothing here may be reused by a
> production that makes historical claims.

## Why A needs a continuity record

A appears in **17 of the 20 shots**. That is the point: drift is a function of
repetition, and a character seen three times tells you nothing.

A is put through every stress the plan has — profile, backlight, low key, overhead,
occlusion, expression change, walking, a back-of-head turn, an indoor-to-outdoor
transition, a two-shot, and a crowd. If identity survives all of that, the mechanism
works. If it survives some, the finding is *which conditions it survives*, and that
tells the production what it may and may not shoot.

## What holds the identity

`TBD — Visual Director.` The realistic options, with their known limits:

| Mechanism | Holds | Degrades on |
|---|---|---|
| Character reference image | Front and three-quarter | Profile, strong lighting change |
| Trained adapter | More angles, more robustly | Cost and setup; becomes a versioned production asset |
| Cast performer with likeness rights | Everything | Out of scope for EXP-001 |

Whichever is chosen, record it here with the drift test result. **An untested
continuity mechanism is an assumption**, and the cheapest place to discover it fails
is shot 03, not shot 40 — which is why the shot plan runs 01, 04, 06, 18 first.

## What we do not know

Nothing. A is invented, so `historical_uncertainty` is empty by design rather than by
omission — there is no fact of the matter to be uncertain about. The field exists for
records that answer to evidence, and A does not.

For a real character record this section would be the longest one on the page.
