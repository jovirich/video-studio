---
id: CNC-XX-0000                 # allocate against the line's continuity/characters/ directory
type: continuity_character
line: TBD
title: TBD
status: draft
version: 0.1.0
updated: "TBD"
owners: [visual-director]

# The evidence record this renders. Omit entirely for an invented character under a
# narrative pack. Where it is present, canonical_name must match that record's
# naming.on_screen exactly.
entity: CHR-XX-0000

canonical_name: TBD

age_range:
  low: TBD
  high: TBD
  life_stage: TBD
  # Why this range. Cite claims where evidence constrains it; write "directorial"
  # where it does not. Do not leave this blank and let the model decide.
  basis: TBD
  claims: []

# Written as a model needs to read it: concrete nouns, not evaluative adjectives.
# "Close-cropped, greying at the temples" beats "distinguished".
appearance:
  skin_tone: TBD
  # A swatch asset or a named value, not a word. QC needs something to compare
  # against, and a show LUT will crush skin tone unless someone is watching.
  skin_tone_reference: TBD
  hair: TBD
  body_build: TBD
  # Relative to others in frame. Absolute height means nothing to a generator.
  height_relative: TBD
  facial_structure: TBD
  eyes: TBD
  # Matters for motion generation and is always forgotten until a clip looks wrong.
  posture_and_gait: TBD
  # Hands are the reliable failure point. Say what they should look like and what
  # they are usually doing — an occupied hand generates far better than an idle one.
  hands: TBD

# Scars, scarification, tattoos, body modification, disability. Bodily markings are
# frequently meaningful rather than decorative; getting one wrong is a substantive
# error, not a cosmetic one.
distinctive_features: []
# - feature: TBD
#   location_on_body: TBD
#   always_visible: true
#   evidence: [SRC-XX-0000]
#   cultural_note: TBD
#   advisory_ref: ADV-XX-0000

# A SET is what appears together in a scene. Recording items individually and hoping
# they combine correctly is how continuity breaks.
wardrobe: []
# - set_id: everyday
#   when_worn: TBD
#   items: [TBD]
#   materials: [TBD]      # fibre, weave, dye — the period marker doing most of the work
#   colours: [TBD]
#   construction: TBD     # how made and fastened; machine stitching is the classic tell
#   condition: TBD        # uniform pristine costume is a tell of its own
#   evidence: [SRC-XX-0000]
#   reference_images: []

# Separate from wardrobe because adornment carries status, office, or initiatory
# meaning that clothing does not. A non-empty `signifies` makes the item a claim
# about the person and it needs evidence.
jewellery_and_adornment: []

references:
  # One canonical face anchor. If a production needs two, it has two characters or
  # two life stages — make a second record.
  facial_reference: STA-XX-0000
  anchor_set: []
  # A seed does not transfer between models, or between versions of one model.
  # Recording a bare seed records nothing.
  approved_seeds: []
  # - { seed: TBD, vendor: TBD, model: TBD, model_version: TBD, prompt_card: PC-XX-S00E00-0000, note: TBD }
  trained_adapter: {}
  # Required before this record can lock. The only question that matters: does the
  # mechanism actually hold? Cheapest place to find out it does not is shot 3.
  drift_test:
    run_on: TBD
    shots_tested: TBD
    angles_tested: []
    lighting_tested: []
    held: TBD
    failure_modes: []     # where it broke — more useful than where it held

# Only for a character who is heard. Core prohibits synthesising a real or historical
# person's voice outright, so for a documentary character this is normally EMPTY and
# the alternative is a credited actor reading a documented quotation.
voice: {}

# The most valuable field here, and the one most often left empty. Feeds the negative
# prompt and gives QC something falsifiable.
#
# severity: anachronism | evidence-contradicted | culturally-prohibited | style-breach
#
# culturally-prohibited is a HARD STOP routed to the sensitivity gate — never a
# negative-prompt term. A negative prompt is a statistical nudge; treating it as a
# safeguard is a category error with consequences outside the studio.
forbidden_variations: []
# - { forbidden: TBD, why: TBD, severity: anachronism }

# Where the depiction goes beyond the evidence — which, for most historical
# characters, is most of it. Recording it is what keeps the rendering honest and
# tells the shot list where to compose around a gap rather than invent one.
#
# how_handled: composed-around | generic-to-period | directorial-choice-disclosed | shot-cut
# composed-around is preferred: framing is the honest tool for uncertainty.
historical_uncertainty: []
# - element: TBD
#   what_is_known: TBD
#   what_is_not: TBD
#   how_handled: composed-around
#   claims: []
#   open_questions: [QST-XX-0000]

appears_in: []
---

# TBD — canonical name

> Copy to `<line>/continuity/characters/CNC-XX-NNNN_<slug>.md`. Do not fill this file
> in place; the naming validator will catch it, but catch it yourself first.

## Why this character needs a continuity record

`TBD` — one paragraph. A character appearing in a single shot does not need one. A
character appearing across a sequence does, and the threshold is roughly three shots
or any appearance in more than one production.

## What holds the identity

`TBD` — which mechanism, and its known drift limits. The realistic options are a
character reference, a trained adapter, or a cast performer with likeness rights.
State which, and what the drift test showed.

## What we do not know

`TBD` — prose expansion of `historical_uncertainty`. Written so a reviewer can
attack it. If this section is short for a pre-photographic subject, it is probably
wrong rather than well-researched.
