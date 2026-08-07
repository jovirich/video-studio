---
id: CNL-NG-0001
type: continuity_location
line: ng-nigeria
title: Workshop interior and yard (invented)
status: draft
version: 0.1.0
updated: "2026-08-07"
owners: [visual-director]

# No `entity` link. This place is invented for EXP-001 and answers to no evidence
# record, because there is no historical entity for it to answer to.

canonical_name: Workshop interior and yard

era:
  display: "no period claimed — invented setting"
  basis: >
    EXP-001 makes no historical claims. Nothing here asserts a time or place, and
    nothing in it may be reused for a production that does.
  claims: []

architecture:
  building_forms: >
    A single rectangular workroom with one door to a walled yard. Low, wide, and
    built for working in rather than living in.
  wall_construction: >
    Rammed earth over a timber frame, finished by hand. Tool marks and finger runs
    visible in raking light; the surface is uneven at grazing angles and flat when
    lit head on. This is the texture that carries the light.
  roof_form: >
    Timber rafters and thatch, seen only as shadow and silhouette above the frame
    line. Deliberately never resolved — see unattested_elements.
  openings: >
    One high window in the long wall, roughly two metres up, unglazed, with a plain
    timber lintel. One door to the yard, wider than a person.
  scale_and_storeys: >
    Single storey. Roughly six metres by four. Ceiling high enough that the window
    light falls without hitting the opposite wall.
  decoration: None. This is a workroom.
  state_of_repair: >
    Worked-in, not ruined and not new. The floor is polished by use near the bench
    and dusty at the edges. One wall has a repair patch of slightly different colour.
  evidence: []

materials:
  - material: rammed earth
    used_for: walls
    appearance: warm mid-tone, matte, visibly hand-finished, dust-coloured in the light beam
  - material: unplaned timber
    used_for: bench, door frame, lintel, rafters
    appearance: grey-brown, split grain, no varnish or paint, worn smooth where hands fall
  - material: fired clay
    used_for: vessels, a shallow bowl on the bench
    appearance: unglazed, matte, slightly irregular rims
  - material: undyed cloth
    used_for: garments, a cloth over the bench end
    appearance: off-white to oatmeal, visible weave at close range, soft-worn
  - material: twisted plant-fibre cord
    used_for: the work in hand
    appearance: pale, fibrous, catches the light along its twist
  - material: iron
    used_for: one hand tool
    appearance: dark, matte, not shiny; worn bright only at the working edge

spatial:
  street_width: >
    Not a street. The yard is roughly four metres across, walled, with the workshop
    door on one side.
  layout: >
    WORKING SURFACES. One bench along the long wall beneath the window: split timber
    slab, waist height, roughly two metres long, worn smooth in a band where hands
    fall. Nothing else in the room is worked on.

    PROP ZONES, fixed for the whole test so that props do not migrate between shots.
    Zone 1, bench left: two clay vessels and a shallow bowl, always in this order.
    Zone 2, bench centre: the work in hand — coiled cord and one iron tool. Zone 3,
    bench right: a folded cloth, unused. Zone 4, floor beneath the bench: a larger
    clay vessel, half in shadow. Zone 5, wall right of the door: nothing, kept clear
    as negative space for the two-shot.

    FIXED ENVIRONMENTAL ANCHORS — the elements a viewer uses to know it is the same
    room, and which must therefore appear identically wherever they are in frame:
    the window and its timber lintel; the repair patch on the long wall left of the
    window; the door opening and its threshold step; the worn band on the bench.

    Door in the short wall to camera right of the bench. Clear floor between them.
  elevation_and_terrain: Flat. A single low step at the door threshold.
  sightlines: >
    From the bench, the door and yard beyond are visible over the worker's left
    shoulder. From the door, the bench is three-quarters on. These two must agree in
    every reverse — it is the main geometry check.
  boundaries: >
    Beyond the yard wall: sky and the top of one tree. Nothing else is ever
    established, so no wide shot may invent a settlement.
  geometry_asset: TBD

vegetation:
  - plant: one tree beyond the yard wall
    where: visible only as canopy above the wall line
    seasonal_state: in leaf

weather_and_season:
  season: unspecified — warm, dry
  conditions: clear
  ground_state: dry, dusty
  sky: clear, no cloud detail established
  consistency_rule: >
    Fixed for the whole test. Weather does not vary between shots. Any variation is
    a continuity breakage and is recorded as one, not accepted as a creative choice.

# Light is what makes a frame read as photographed rather than assembled, and it is
# the single most common physical implausibility in generated imagery. Fixed here so
# that every shot in the sequence can be checked against it.
lighting_language:
  time_of_day: mid-morning
  primary_source: the single high window in the long wall
  direction: >
    Raking from frame left and above, roughly 40 degrees down. A visible beam falls
    on the bench and the floor short of the opposite wall. This direction does not
    change between shots — the sun does not move during one morning.
  quality: >
    Hard-edged where the beam lands, soft fill elsewhere from bounce off the earth
    floor. Dust in the beam.
  practical_sources: []
  shadow_behaviour: >
    Long, hard-edged shadows on the floor running away from the window. Shadow
    direction is the fastest continuity check in the whole set.
  atmosphere: Fine dust suspended in the light beam. Nothing heavier — no smoke, no haze.

camera_language:
  lens_set:
    - "35mm equivalent — the room, the two-shot, the door"
    - "50mm equivalent — the working medium shots"
    - "85mm equivalent — hands, face, the close work"
  typical_heights: [eye, bench height]
  movement_rules: >
    Locked frames throughout, with one exception: the walking shot may track. Nothing
    drifts. Unmotivated camera movement is the signature tell of generated video and
    it also hides drift, which would defeat the purpose of this test.
  coverage_pattern: >
    Bench as the anchor. Door and yard as the reverse. The two must be spatially
    consistent with each other.
  avoid: >
    Anything that resolves the roof, the ceiling above the rafters, or the world
    beyond the yard wall. Frame below the roofline.

soundscape:
  ambience: not in scope — EXP-001 generates no audio
  animals_and_birds: []
  human_activity: not in scope
  languages_audible: []
  forbidden_sounds: []
  evidence: []

reference_imagery:
  # establishing_anchor OMITTED rather than TBD — pattern-constrained to an STA-* id,
  # and absence is how an unset optional field is expressed. It is the canonical wide
  # of the workshop; every other angle is checked against it.
  anchor_set: []
  approved_seeds: []
  source_photography: []

# drift_test is OMITTED until shots 01, 04, 06, 18 have run. It is the output of
# those shots, not an input, and the schema requires it before this record can lock.

# The highest-value field in the record. Any one of these appearing in any of the
# twenty shots is an automatic fail for that shot, and one occurrence fails the run.
forbidden_objects:
  - forbidden: plastic in any form
    why: invented pre-industrial setting; the model reaches for it in vessels and cord
    severity: anachronism
  - forbidden: machine stitching or machine-woven regular cloth
    why: all textile here is hand-worked; regular selvedge is the classic tell
    severity: anachronism
  - forbidden: sawn, planed, or dimensioned timber
    why: timber is split and hand-worked; a straight milled edge breaks the material logic
    severity: anachronism
  - forbidden: glazed or wheel-perfect ceramic
    why: vessels are unglazed and hand-formed
    severity: anachronism
  - forbidden: corrugated metal, concrete, brick, cut stone
    why: the wall system is rammed earth over timber
    severity: anachronism
  - forbidden: glass, including in the window
    why: the window is unglazed; glass would also change the light entirely
    severity: anachronism
  - forbidden: printed or written text of any kind
    why: >
      Any script would place this somewhere. It must not. Models produce pseudo-script
      readily and it is the fastest way this invented setting acquires a false
      cultural referent.
    severity: evidence-contradicted
  - forbidden: masks, regalia, ceremonial dress, insignia of office
    why: >
      This is an ordinary workroom. Regalia would make it a depiction of a specific
      culture's practice, which EXP-001 must not become — and would require an
      advisory ruling that does not exist.
    severity: culturally-prohibited
  - forbidden: shrine, altar, ritual object, or religious symbol
    why: as above — sacred material requires a ruling; none exists
    severity: culturally-prohibited

# Compose around these. Do not let the model fill them. Agrees with camera_language.avoid.
unattested_elements:
  - element: the roof structure above the rafter line
    how_handled: composed-around
  - element: anything beyond the yard wall except sky and one tree canopy
    how_handled: composed-around
  - element: the far short wall of the workroom
    how_handled: composed-around

appears_in: [EXP001]
---

# Workshop interior and yard

> ## Laboratory design — invented, and not representative of anywhere
>
> Every visual detail in this record is **laboratory design**: invented to give the
> continuity stress test something to hold onto. It is chosen for what it does to a
> camera — texture under raking light, a fixed shadow direction, a geometry that must
> agree in reverse — and for nothing else.
>
> **It is not a depiction of, and does not represent, the material culture of Benin,
> Nigeria, West Africa, or any real place or people, at any period.** No wardrobe,
> architecture, tool, craft process, furniture, or material here is offered as
> historically representative of anything. There is no evidence basis because there
> is no claim.
>
> EXP-001 is permanently non-publishable. Nothing in this record may be reused by a
> production that makes historical claims — such a production needs researched
> records with real sources, which is [EXP-002](../../productions/README.md).

See [EXP-001 § Subject](../../productions/EXP001_laboratory-scene/README.md).

## Why this location needs a continuity record

It is seen from six angles across the twenty shots, plus an exterior transition. Two
shots of the same room from different angles is already the failure case — geometry
that does not agree reads as two rooms, and no amount of prompt discipline fixes it.

The location is also carrying the **light**, which is fixed for the whole test.
Shadow direction is the fastest continuity check available: if it flips between two
shots, they are not the same morning.

## How it is held

`TBD — Visual Director.` Prompted with anchors, or blocked as geometry.

Geometry solves the problem outright rather than mitigating it, and for a room with a
sightline requirement — the bench and the door must agree in reverse — it is likely
worth the hour. See [`prompts/chains/geometry_conditioned.md`](../../../../../../prompts/chains/geometry_conditioned.md).

## What is deliberately not established

The roof, the far wall, and the world beyond the yard. Framing is the honest tool for
uncertainty, and here it does double duty: it keeps the setting from acquiring
specifics it has no basis for.

## Note on severity

Two forbidden entries are `culturally-prohibited` — regalia and sacred material.
Those do **not** go into a negative prompt. A negative prompt is a statistical nudge
that a model may or may not honour; treating it as a safeguard is a category error.
They route to the sensitivity gate as a hard stop, and if either appears in a render
the render is deleted rather than adjusted.

## Lighting variants required by the shot plan

**Schema note:** `lighting_language` holds one lighting state. The
[shot plan](../../productions/EXP001_laboratory-scene/03_storyboard/shot_plan.md)
deliberately varies light to stress identity, so the variants live here in the body
rather than in front matter. Adding a `lighting_variants` field would be a schema
change, and the architecture freeze is in force. Flagged as a finding.

The **base** state is the one in front matter, and shots not listed below use it
unchanged. Every variant keeps the window as the only source — the sun does not move
during one morning, and a variant that relocates the light is a different scene, not
a different setup.

| Variant | Shots | What changes | What must not change |
|---|---|---|---|
| **Base** | 01–05, 10–13, 16, 18–20 | — | — |
| **Backlit** | 06, 07, 17 | Subject placed between camera and window. Face falls into shadow; rim light on hair and shoulder edge. | Window position, beam angle, dust in beam |
| **Overhead hard** | 08 | Subject stands under the beam where it strikes the floor; light from above and slightly left. | Source is still the window, not an invented skylight |
| **Low key** | 09 | Subject stepped back from the beam; only bounce off the earth floor reaches the face. Half the face in deep shadow. | Shadow direction still runs away from the window |
| **Exterior daylight** | 14, 15 | The yard. Open sky, no direct beam, soft omnidirectional fill with a warm bounce from the earth wall. | Yard wall, tree canopy, threshold step |

Shot 14 is the **transition** and is the hardest lighting case in the set: the
subject moves from a hard directional interior beam to soft open shade in a single
shot. Identity that survives 06 and 09 separately may still fail here.

Two things to check on every variant, because they are what actually break:

1. **Shadow direction never flips.** It runs away from the window in every interior
   shot regardless of setup. A flipped shadow means the model relit the scene.
2. **Skin tone holds across all five variants.** This is the single most common
   failure in both generation and grading, and a variant that shifts it is a
   representational failure rather than a lighting note — see the acceptance
   threshold in the shot plan, which is 20/20 with no allowance.
