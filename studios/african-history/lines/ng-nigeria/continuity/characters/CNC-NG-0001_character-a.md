---
id: CNC-NG-0001
type: continuity_character
line: ng-nigeria
title: Character A — the worker (invented)
status: draft
version: 0.3.0
updated: "2026-08-07"
owners: [visual-director]

# No `entity` link. A is invented for EXP-001 and answers to no evidence record.
# See the laboratory-design notice in the body.

canonical_name: A

age_range:
  low: 38
  high: 42
  life_stage: adult
  basis: directorial — A is invented; no evidence constrains this
  claims: []

appearance:
  skin_tone: deep brown
  # CONTINUITY REFERENCE, NOT AN ETHNICITY CLASSIFIER. This value exists so two
  # people scoring twenty frames reach the same verdict. It describes a target for
  # THIS invented character under the anchor's neutral lighting and nothing else.
  #
  # Tolerance matters as much as the target: the same skin renders differently
  # backlit (shot 06), in low key (09), and in open shade (14, 15). Score against
  # the swatch AS RENDERED UNDER THAT SHOT'S LIGHTING VARIANT, not against the
  # anchor. Without that, shots 06 and 09 fail for physics rather than for drift,
  # and the 20/20 threshold becomes unmeetable for the wrong reason.
  skin_tone_reference: >
    target digital swatch approximately #70452F, measured on the cheek under the
    anchor's even neutral lighting. Hue and relative value are what must hold across
    lighting variants; absolute luminance is expected to move with the light.
  hair: >
    Short, tightly coiled black hair. Low, even profile with a clearly visible
    natural hairline. FACIAL HAIR: short, neatly maintained full beard and moustache.
    (Recorded here because the schema has no separate facial-hair field — finding G8.)
  body_build: >
    Lean, strong working build. Defined shoulders and forearms, without bodybuilder
    proportions.
  height_relative: approximately 8–10 cm taller than B
  facial_structure: >
    Long-oval face. Moderately broad nose. Pronounced cheekbones. Strong jaw, not
    oversized.
  eyes: deep-set, dark brown
  posture_and_gait: >
    Upright, economical. Works with weight settled and shoulders low. Needed for
    shot 10 (walking) and shot 13 (the turn), where bearing carries identity before
    the face resolves.
  hands: >
    Working hands, consistent with the forearms — used, not soft. On screen at 85mm
    in shots 02 and 11, occupied with cord. The highest-risk detail in the set:
    hands are the reliable generative failure point and here they are the subject.

# The single most valuable field for SCORING. Binary rather than gestalt: present
# and correct, or not.
distinctive_features:
  - feature: small vertical scar through the centre of the chin
    location_on_body: chin, on the midline
    always_visible: true
    evidence: []
    cultural_note: >
      Invented. Carries no meaning, marks no status, and is not a practice of any
      real culture. It exists solely to make identity drift checkable.

      MIDLINE BY DESIGN. The first version of this record specified a scar on the
      RIGHT eyebrow. Across eight anchor candidates the surface placed it on the
      specified side once. A feature whose side the generator cannot hold is useless
      as a binary identity check — every scored frame becomes an argument about
      whether a flipped mark counts as drift. A midline feature cannot be mirrored,
      so the check is reliable by construction rather than by luck.

wardrobe:
  - set_id: primary
    when_worn: all twenty shots
    items:
      - plain unpatterned short-sleeved work tunic, earth-toned
      - simple lower wrap or trousers as the fictional design requires
      - simple neutral work footwear, where visible
    materials: [matte natural-looking cloth]
    colours: [earth tone — muted, unsaturated]
    construction: >
      Plain. No logos, embroidery, symbols, motifs, or decorative detail of any kind.
      Nothing that could read as belonging to a real culture.
    condition: Worked-in. Soft from washing, dust at the hem. Not new, not ragged.
    evidence: []
    reference_images: []

# `jewellery_and_adornment` is the nearest existing field for accessories — finding
# G8. Nothing here signifies status, office, or rank.
jewellery_and_adornment:
  - item: one plain dark working cord around the left wrist
    materials: [dark plant-fibre cord]
    worn_where: left wrist
    signifies: nothing — it is a working cord, not adornment
    evidence: []
    reference_images: []

references:
  # facial_reference is OMITTED, not TBD: it is pattern-constrained to an STA-* id,
  # and for an optional typed field "not yet decided" is absence (finding G6).
  # The anchor SPECIFICATION now exists as prompt card PC-NG-EXP001-0001; the id
  # goes here once the rendered anchor has director approval.
  anchor_set: []
  # MANDATORY per run: vendor, model, exact model/version identifier, reference
  # image id/hash, seed, prompt-card id, parameters, returned asset id, asset
  # sha256. A seed does not transfer between model versions — an entry without the
  # version identifier is worthless.
  approved_seeds: []
  # Deliberately empty for EXP-001. No trained LoRA or custom adapter: the first
  # experiment establishes a baseline with reference-image conditioning alone, so
  # that a later adapter run has something to be compared against.
  trained_adapter: {}
  # drift_test is the OUTPUT of shots 01, 04, 06, 18 — added after they run, and
  # required before this record can lock.

# A is never heard. EXP-001 generates no audio.
voice: {}

forbidden_variations:
  - forbidden: any change of garment between shots
    why: the test isolates identity drift; a second costume adds a variable
    severity: style-breach
  - forbidden: convergence toward B in face, build, or silhouette
    why: >
      Shots 18 and 19 exist to detect exactly this. A and B must remain
      distinguishable by age, facial geometry, hair, build, height, silhouette, and
      distinctive feature.
    severity: style-breach
  - forbidden: loss of the chin scar, or its appearance off the midline
    why: >
      It is the binary identity check. Absent, scoring reverts to gestalt judgement —
      which is exactly what the shot plan was written to avoid. Off-centre is also a
      fail: the whole point of a midline mark is that there is no side to get wrong.
    severity: style-breach
  - forbidden: jewellery, beadwork, worked metal adornment
    why: adornment that signifies would make A a depiction of a real culture's practice
    severity: culturally-prohibited
  - forbidden: scarification, body marking, or hairstyle carrying cultural meaning
    why: >
      Would require an advisory ruling that does not exist. NOTE THE SEVERITY: this
      routes to the sensitivity gate as a hard stop, never to a negative prompt.
    severity: culturally-prohibited
  - forbidden: patterned, embroidered, or motif-bearing cloth
    why: pattern is the fastest way an invented garment acquires a false cultural referent
    severity: culturally-prohibited
  - forbidden: footwear of modern construction, eyeglasses, wristwatch, any manufactured object
    why: invented pre-industrial setting; visible in shots 08, 10, 14, 20
    severity: anachronism

# Inapplicable rather than empty — A is invented, so there is no fact of the matter
# to be uncertain about. The field assumes a historical subject (finding G9).
historical_uncertainty: []

appears_in: [EXP001]
---

# Character A — the worker

> ## Laboratory design — invented, and not representative of anywhere
>
> A is **invented for a continuity stress test**. Every visual detail here is
> laboratory design, chosen for what it does to a camera and for nothing else.
>
> **A is not a depiction of, and does not represent, any real person, people, or
> culture.** No garment, adornment, hairstyle, facial feature, tool, or practice
> associated with A is offered as historically representative of Benin, Nigeria,
> West Africa, or anywhere else, at any period. There is no evidence basis because
> there is no claim.
>
> The skin-tone swatch is a **continuity reference, not an ethnicity classifier**.
> It exists so that two people scoring twenty frames reach the same verdict.
>
> EXP-001 is permanently non-publishable, and nothing here may be reused by a
> production that makes historical claims.

## Why A needs a continuity record

A appears in **17 of 20 shots** and is put through every stress the plan has:
profile, backlight, low key, overhead, occlusion, expression change, walking, a
back-of-head turn, an indoor-to-outdoor transition, a two-shot, and a crowd.

Drift is a function of repetition. A character seen three times tells you nothing.

## What holds the identity

**Reference-image conditioning. No trained adapter.**

That is deliberate. An adapter would very likely hold better — and would tell us
nothing about how much better, because there would be no baseline. EXP-001
establishes the floor with the cheapest mechanism; a later run with an adapter is
then a comparison rather than an assertion.

**The same mechanism, vendor, model, and version for both A and B**, fixed across all
four diagnostic shots. Mixing mechanisms would confound shot 18: a failure could be
the mechanism or the mixture, with no way to tell which.

## The scar is the instrument, and it is midline for a reason

The chin scar is not decoration. It converts `same_person` from a gestalt judgement
into a binary check — present and correct, or not — and it is the single thing that
makes two-shot scoring defensible rather than arguable.

**It moved from the eyebrow to the chin because of evidence.** The first eight anchor
candidates put the eyebrow scar on the specified side once. A generator that cannot
reliably control which side a mark lands on makes a lateral feature worthless as a
check: a flipped scar is indistinguishable from drift, and every scored frame becomes
an argument.

A midline mark has no side to get wrong. The check now holds by construction.

If a render loses it, or places it off-centre, that render fails regardless of how
convincing the face looks.

## What we do not know

Nothing. A is invented, so `historical_uncertainty` is empty by design rather than by
omission — there is no fact of the matter. For a real character record this section
would be the longest on the page.
