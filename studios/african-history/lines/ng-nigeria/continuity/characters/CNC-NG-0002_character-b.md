---
id: CNC-NG-0002
type: continuity_character
line: ng-nigeria
title: Character B — the second figure (invented)
status: draft
version: 0.1.0
updated: "2026-08-07"
owners: [visual-director]

# No `entity` link. B is invented for EXP-001.

canonical_name: B

# ---------------------------------------------------------------------------
# DIRECTORIAL — every TBD below is yours. See DIRECTOR_DECISIONS.md.
#
# B exists to answer one question A cannot: does the mechanism hold two people
# SEPARATELY, or does it collapse them toward one face? So B's appearance decisions
# must be made against A's, not independently — see the note below the front matter.
# ---------------------------------------------------------------------------

age_range:
  low: TBD
  high: TBD
  life_stage: TBD
  basis: >
    directorial. Choose a range that is clearly distinct from A's. If A and B read as
    the same age, a convergence failure in shot 18 is indistinguishable from ordinary
    drift, and the test loses its most valuable result.
  claims: []

appearance:
  skin_tone: TBD
  skin_tone_reference: TBD
  # Whatever is chosen, the two skin-tone references must be checkable independently.
  # If A and B are close, a convergence failure will be invisible.
  hair: TBD
  # Include facial hair here if any — no separate schema field exists.
  body_build: TBD
  height_relative: >
    TBD — stated relative to A. Shot 19 is deliberately an unequal-distance two-shot,
    so the height relationship must be unambiguous or that shot cannot be scored.
  facial_structure: TBD
  eyes: TBD
  posture_and_gait: >
    TBD — B enters through the door in shot 18. Bearing on entry is what makes B read
    as a different person before the face is even resolved.
  hands: TBD

distinctive_features: []
# TBD. Strongly worth giving B one that A does not have, and vice versa. It converts
# `same_person` scoring on the two-shots from gestalt judgement into a binary check,
# which is the difference between a result and an opinion.

wardrobe:
  - set_id: primary
    when_worn: shots 16–20
    items:
      - TBD — upper garment
      - TBD — lower garment
    materials: [undyed plant-fibre cloth, hand-woven]
    colours: [TBD]
    # Choose a value or weave that separates B from A at a glance, including in
    # silhouette. Shot 20 puts A in a crowd; if B's cloth reads like A's, the crowd
    # shot cannot distinguish a convergence failure from a framing problem.
    construction: >
      Hand-sewn, irregular seam. No machine stitching, no regular selvedge.
    condition: Worked-in, and distinct from A's in wear pattern rather than in quality.
    evidence: []
    reference_images: []

# See the note in A's record: `jewellery_and_adornment` is the nearest existing field
# for accessories, and nothing here may signify status, office, or rank.
jewellery_and_adornment: []

references:
  # `facial_reference` and `drift_test` are OMITTED, not set to TBD — they are typed
  # and pattern-constrained, and `TBD` is only legal in free-text fields. For these,
  # "not yet decided" is expressed by absence, which is why the schema marks them
  # optional. Writing TBD into them fails validation: the schema working, not a bug.
  #
  # facial_reference: STA-NG-NNNN   <- the canonical face; must exist before shot 01
  #                                    is ACCEPTED. Use the SAME mechanism as A.
  # drift_test:                     <- the OUTPUT of shots 01/04/06/18, not an input.
  #                                    Required before this record can lock.
  anchor_set: []
  approved_seeds: []
  trained_adapter: {}

voice: {}

forbidden_variations:
  - forbidden: any change of garment between shots
    why: adds a variable to a test whose point is isolating identity drift
    severity: style-breach
  - forbidden: resembling A in face, hair, build, or garment
    why: >
      B's entire purpose is to be distinguishable. Convergence toward A is THE result
      this character exists to detect, so any deliberate similarity destroys the
      measurement.
    severity: style-breach
  - forbidden: jewellery, beadwork, or worked metal adornment
    why: adornment that signifies would make B a depiction of a real culture's practice
    severity: culturally-prohibited
  - forbidden: scarification, body marking, or hairstyle carrying cultural meaning
    why: as above; routes to the sensitivity gate, not to a negative prompt
    severity: culturally-prohibited
  - forbidden: footwear of modern construction, eyeglasses, or any manufactured object
    why: invented pre-industrial setting
    severity: anachronism

historical_uncertainty: []

appears_in: [EXP001]
---

# Character B — the second figure

> ## Laboratory design — invented, and not representative of anywhere
>
> B is **invented for a continuity stress test**, and every visual detail here is
> laboratory design chosen for what it does to a camera.
>
> **B is not a depiction of, and does not represent, any real person, people, or
> culture.** No garment, adornment, hairstyle, or practice associated with B is
> offered as historically representative of Benin, Nigeria, West Africa, or anywhere
> else, at any period. There is no evidence basis because there is no claim.
>
> EXP-001 is permanently non-publishable.

## Why B exists at all

B appears in only five shots, and could easily be cut. Cutting them would be a
mistake.

**One character passing proves less than most people assume.** A mechanism can hold a
single identity perfectly and still collapse two identities toward each other the
moment both are in frame — because most reference mechanisms condition the whole
image, not a region of it. Shots 18 and 19 are the only place that failure is
visible, and it is the failure most likely to matter in real production, where
two-shots are unavoidable.

So B is not a spare character. B is the instrument for the second-hardest question in
the test.

## Design B against A, not independently

Every appearance decision for B should be made **with A's record open**. The
requirement is not that B looks unusual — it is that B is *unambiguously not A*, in:

- **face** — different structure, not just different hair
- **age** — a visibly different range
- **build and height** — shot 19 is an unequal-distance two-shot and needs a clear relationship
- **silhouette** — shot 20 puts A in a crowd; B's outline must not read as A's at distance
- **one distinctive feature each**, ideally, which turns two-shot scoring from judgement into a check

If A and B are close on any of these, a convergence failure becomes indistinguishable
from ordinary drift, and the most valuable result in the run is lost.

## What holds the identity

`TBD — Visual Director`, and it should be the **same mechanism as A**. Using a
different mechanism for each character would confound the two-shot result: a failure
in shot 18 could then be the mechanism, or the mixture, and there would be no way to
tell which.

## What we do not know

Nothing — B is invented. `historical_uncertainty` is empty by design. See A's record
for why that field exists and why it is inapplicable here.
