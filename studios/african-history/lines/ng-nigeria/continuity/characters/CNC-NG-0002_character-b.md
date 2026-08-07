---
id: CNC-NG-0002
type: continuity_character
line: ng-nigeria
title: Character B — the second figure (invented)
status: draft
version: 0.3.0
updated: "2026-08-07"
owners: [visual-director]

# No `entity` link. B is invented for EXP-001.

canonical_name: B

age_range:
  low: 25
  high: 29
  life_stage: adult
  basis: >
    directorial. Deliberately a decade clear of A: if the two read as the same age, a
    convergence failure in shot 18 is indistinguishable from ordinary drift.
  claims: []

appearance:
  skin_tone: rich medium-deep brown
  # CONTINUITY REFERENCE, NOT AN ETHNICITY CLASSIFIER. Same caveat as A's record:
  # score against this swatch AS RENDERED UNDER THE SHOT'S LIGHTING VARIANT. Hue and
  # relative value must hold; absolute luminance moves with the light.
  #
  # B's swatch is deliberately separable from A's (#87583D vs #70452F). If the two
  # rendered close, a convergence failure in the two-shots would be invisible.
  skin_tone_reference: >
    target digital swatch approximately #87583D, measured on the cheek under the
    anchor's even neutral lighting.
  hair: >
    Tightly coiled black hair gathered into a compact high natural bun. Hairline
    visible. FACIAL HAIR: none. (Recorded here per finding G8.)
  body_build: medium to slender; noticeably different from A
  height_relative: approximately 8–10 cm shorter than A
  facial_structure: >
    Rounder face than A. Softer jaw. Broader cheek area. Medium-width nose.
  eyes: dark brown
  posture_and_gait: >
    More upright and compact than A. B enters through the door in shot 18 — bearing on
    entry is what makes B read as a different person before the face resolves.
  hands: >
    Consistent with build. Not the subject of any shot, unlike A's.

distinctive_features:
  - feature: small round dark birthmark centred on the bridge of the nose, between the brows
    location_on_body: bridge of the nose, on the midline between the brows
    always_visible: true
    evidence: []
    cultural_note: >
      Invented. Carries no meaning and marks no status. It exists solely to make
      identity drift checkable, and to be unambiguously different from A's mark —
      different feature, different place, different kind.

      MIDLINE BY DESIGN, for the same reason as A's. A cheek birthmark is lateral, and
      the surface proved it cannot reliably hold a side. Both features are now midline
      and in DIFFERENT places, so neither can be mirrored and the two remain
      distinguishable at a glance.

wardrobe:
  - set_id: primary
    when_worn: shots 16–20
    items:
      - plain muted work garment, silhouette clearly different from A's
    materials: [matte natural-looking cloth]
    colours: [muted — distinct in value from A's earth tone]
    construction: >
      Plain. No patterns, logos, embroidery, symbols, or motifs. Nothing that could
      read as belonging to a real culture.
    condition: Worked-in, and distinct from A's in cut rather than in quality.
    evidence: []
    reference_images: []

jewellery_and_adornment: []

references:
  # facial_reference OMITTED, not TBD (finding G6). The anchor SPECIFICATION is
  # prompt card PC-NG-EXP001-0002; the STA-* id goes here after director approval.
  #
  # B's anchor is shot under PHOTOGRAPHICALLY IDENTICAL conditions to A's. If the
  # two anchors differ in framing, lens, or light, every later comparison between
  # them is confounded and shot 18 cannot be scored.
  anchor_set: []
  # Same mandatory per-run record as A: vendor, model, exact version identifier,
  # reference image id/hash, seed, prompt-card id, parameters, asset id, sha256.
  approved_seeds: []
  # No trained adapter for EXP-001 — baseline first, by design.
  trained_adapter: {}

voice: {}

forbidden_variations:
  - forbidden: any change of garment between shots
    why: adds a variable to a test whose point is isolating identity drift
    severity: style-breach
  - forbidden: resembling A in face, age, build, height, or silhouette
    why: >
      B's entire purpose is to be distinguishable. Convergence toward A is THE result
      this character exists to detect, so any similarity destroys the measurement.
    severity: style-breach
  - forbidden: loss of the nose-bridge birthmark, or its appearance off the midline
    why: it is B's binary identity check, as the chin scar is A's
    severity: style-breach
  - forbidden: acquiring A's chin scar
    why: >
      The clearest possible signature of feature bleed between two reference-conditioned
      subjects. If it appears on B, the mechanism is mixing them.
    severity: style-breach
  - forbidden: jewellery, beadwork, worked metal adornment
    why: adornment that signifies would make B a depiction of a real culture's practice
    severity: culturally-prohibited
  - forbidden: scarification, body marking, or hairstyle carrying cultural meaning
    why: routes to the sensitivity gate as a hard stop, never to a negative prompt
    severity: culturally-prohibited
  - forbidden: patterned, embroidered, or motif-bearing cloth
    why: pattern is the fastest way an invented garment acquires a false cultural referent
    severity: culturally-prohibited
  - forbidden: footwear of modern construction, eyeglasses, any manufactured object
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
> culture.** No garment, hairstyle, facial feature, or practice associated with B is
> offered as historically representative of Benin, Nigeria, West Africa, or anywhere
> else, at any period. There is no evidence basis because there is no claim.
>
> The skin-tone swatch is a **continuity reference, not an ethnicity classifier**.
>
> EXP-001 is permanently non-publishable.

## Why B exists at all

B appears in five shots and could easily be cut. Cutting them would be a mistake.

**One character passing proves less than most people assume.** A mechanism can hold a
single identity perfectly and still collapse two identities toward each other the
moment both are in frame, because most reference conditioning acts on the whole image
rather than on a region of it. Shots 18 and 19 are the only place that failure is
visible, and it is the failure most likely to matter in real production, where
two-shots are unavoidable.

B is not a spare character. B is the instrument for the second-hardest question in the
test.

## Separation, by design

Every axis is deliberately clear of A:

| Axis | A | B |
|---|---|---|
| Age | 38–42 | 25–29 |
| Presentation | male | female |
| Height | taller by 8–10 cm | shorter |
| Face | long-oval, strong jaw, pronounced cheekbones | rounder, softer jaw, broader cheek |
| Hair | short tightly coiled, full beard | tightly coiled, compact high bun, no facial hair |
| Build | lean, angular | medium/slender, compact |
| Feature | scar, centre of chin | birthmark, bridge of nose |
| Swatch | `#70452F` | `#87583D` |

Different feature, different place, different kind — and both on the midline, so
neither can be mirrored. That is not fussiness: it is what makes a convergence failure
in shot 18 unambiguous rather than arguable.

## The bleed test

`forbidden_variations` includes **B acquiring A's chin scar**. If that appears, the
mechanism is not holding two subjects separately — it is mixing them — and that is a
cleaner, earlier signal than waiting to judge whether two faces "look similar".

Check for it explicitly in shots 18 and 19. It is the single most informative failure
the run can produce.

## What holds the identity

**The same reference-image mechanism as A**, same vendor, same model, same version,
fixed across all four diagnostic shots. A different mechanism per character would make
a shot-18 failure uninterpretable.
