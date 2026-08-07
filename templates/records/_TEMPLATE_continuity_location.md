---
id: CNL-XX-0000                 # allocate against the line's continuity/locations/ directory
type: continuity_location
line: TBD
title: TBD
status: draft
version: 0.1.0
updated: "TBD"
owners: [visual-director]

entity: LOC-XX-0000             # omit for an invented setting under a narrative pack

canonical_name: TBD

# The moment being depicted, not the place's whole history. A location shown at two
# periods needs two records — materials, vegetation, and skyline all move.
era:
  display: TBD
  basis: TBD
  claims: []

architecture:
  building_forms: TBD
  # Technique and finish, not just material. Coursing, temper, render, and tool marks
  # are what make a wall read as built rather than extruded.
  wall_construction: TBD
  # Frequently unattested. If so, say so here AND add it to unattested_elements, then
  # frame below the roofline rather than letting the model invent one.
  roof_form: TBD
  openings: TBD
  scale_and_storeys: TBD
  decoration: TBD
  state_of_repair: TBD          # uniform newness is a tell; so is uniform ruin
  evidence: []

# Doubles as the allow-list the anachronism pass runs against.
materials: []
# - { material: TBD, used_for: TBD, appearance: TBD, evidence: [SRC-XX-0000] }

# The geometry a camera has to obey. Getting this wrong is what makes two shots of
# one place feel like two places.
spatial:
  street_width: TBD             # drives lens choice and how many figures fit plausibly
  layout: TBD
  elevation_and_terrain: TBD
  sightlines: TBD               # what is visible from where — keeps a reverse angle honest
  boundaries: TBD               # what lies just beyond frame, so a wide shot invents nothing
  geometry_asset: TBD           # 3D scene file, if built rather than prompted

# A wrong plant is an anachronism a local audience reads instantly, and crops date a
# scene precisely.
vegetation: []

weather_and_season:
  season: TBD
  conditions: TBD
  ground_state: TBD             # dust, mud, standing water — breaks constantly, obvious in a cut
  sky: TBD
  consistency_rule: TBD         # may it vary, and where — silent variation reads as carelessness

# Light is what makes a frame read as photographed rather than assembled, and it is
# where generated imagery most reliably violates physics.
lighting_language:
  time_of_day: TBD
  primary_source: TBD
  direction: TBD                # FIXED for the location, so every shot agrees
  quality: TBD
  practical_sources: []         # fire lights warm, moves, and falls off fast
  shadow_behaviour: TBD
  atmosphere: TBD

camera_language:
  lens_set: []                  # from the line's defined set — the cheapest coherence available
  typical_heights: []
  movement_rules: TBD           # what is permitted and what motivates it; drift is the tell
  coverage_pattern: TBD
  avoid: TBD                    # angles exposing unattested geometry

# Ambience asserts what a place sounded like. It is reconstruction, held to the same
# standard as image. Wrong birdsong is heard instantly.
soundscape:
  ambience: TBD
  animals_and_birds: []
  human_activity: TBD
  languages_audible: []
  forbidden_sounds: []          # the audio equivalent of forbidden_objects
  evidence: []

reference_imagery:
  establishing_anchor: STA-XX-0000    # the canonical wide; every angle checks against it
  anchor_set: []
  approved_seeds: []
  source_photography: []              # present-day capture is `contemporary`, never `reconstruction`

# The highest-value field in this record. Built from what the anachronism pass
# actually catches, so it compounds across a season.
#
# severity: anachronism | evidence-contradicted | culturally-prohibited | style-breach
# culturally-prohibited is a hard stop routed to the sensitivity gate, never a
# negative-prompt term.
#
# Required to be non-empty at status: locked. An empty list at lock means nobody has
# run an anachronism pass yet.
forbidden_objects: []
# - { forbidden: TBD, why: TBD, severity: anachronism }

# Compose around these; do not let the model fill them. Should agree with
# camera_language.avoid.
unattested_elements: []
# - { element: TBD, how_handled: composed-around, open_questions: [QST-XX-0000] }

drift_test:
  run_on: TBD
  shots_tested: TBD
  angles_tested: []
  held: TBD
  failure_modes: []

appears_in: []
---

# TBD — canonical name

> Copy to `<line>/continuity/locations/CNL-XX-NNNN_<slug>.md`. Do not fill this file
> in place.

## Why this location needs a continuity record

`TBD` — a place seen once does not need one. A place seen from more than one angle
does, and that threshold is lower than people expect: two shots of the same courtyard
from different angles is already the failure case.

## How it is held

`TBD` — prompted with anchors, or built as geometry. Geometry solves the problem
outright rather than mitigating it, and for reconstruction work it has a second
advantage: you can only model what is evidenced, so the limits of the evidence stay
visible while you work.

## What we do not know

`TBD` — prose expansion of `unattested_elements`, and how the camera works around
each. Naming what you cannot see is more useful than describing what you can.
