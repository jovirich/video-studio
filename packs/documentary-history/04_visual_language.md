---
doc: bible/04
title: Visual language
status: template
version: 0.1.0
owners: [visual-director]
---

# 04 — Visual language

> **Fill state.** The *rules* below are studio policy. The *look* — palette, grade,
> lens character — is `TBD` per production line and is specified in each line's
> `style/` folder. A single continental look would be a mistake; Nigeria's line
> defines its own in [../productions/ng-nigeria/style/visual_identity.md](../../studios/african-history/lines/ng-nigeria/style/visual_identity.md).

## 1. The consistency problem

Generative tools do not have continuity. Two prompts written by the same person a
week apart will produce two different worlds. Left unmanaged, an AI-assisted
documentary looks like a mood board — beautiful shot to shot, incoherent across a
cut.

The studio solves this with three mechanisms, in order of authority:

1. **The look bible** — the line's `style/` folder: palette, grade, lens set, light
   behaviour, texture, atmosphere. Written in language a prompt can inherit.
2. **Style anchors** — a fixed, versioned set of reference images per line, per
   sequence type, stored in `library/style_refs/` and referenced by ID from every
   prompt card. Not "a vibe" — specific files with checksums.
3. **Prompt inheritance** — every prompt card inherits a `style_block` from its
   sequence, which inherits from the line. A prompt card that overrides the style
   block must say why. See [../prompts/README.md](../../prompts/README.md) § Inheritance.

## 2. Camera grammar

The show has a camera even though it has no camera. Treating generated imagery as
if a physical crew shot it is what separates cinematic from generated-looking.

| Element | Studio default |
|---|---|
| Format | 2K/4K UHD delivery, 16:9 primary. See [10_distribution_and_formats.md](../../core/03_distribution_and_formats.md). |
| Aspect discipline | One aspect ratio per episode body. Ratio changes are a deliberate device (e.g. archival inserts), never an artefact of tool defaults. |
| Frame rate | 24 fps for the documentary body. Generated clips are produced at native rate then conformed; conform method recorded on the asset. |
| Motion | Motivated only. A drifting camera on every shot is the signature tell of generated video. Roughly one third of shots should be locked. |
| Lens set | `TBD per line` — define a set (e.g. 24 / 35 / 50 / 85 equivalents) and use only those. A defined lens set is the cheapest way to buy coherence. |
| Depth of field | Consistent with the chosen lens and stop. Generated tools default to shallow; resist it — historical exteriors read false at f/1.4. |
| Height and angle | Eye level is the default. Low angles ennoble and high angles diminish; both are editorial choices requiring a reason. |

## 3. Light

`TBD per line`, but the following are studio-wide:
- Light has a **source and a direction** in every frame, and it is consistent within
  a scene. Generated imagery routinely violates this; it is a primary QC check.
- Time of day is chosen, recorded on the shot record, and consistent across a
  sequence.
- Practical sources (fire, lamp, window) behave physically. Fire lights warm, moves,
  and falls off fast.

## 4. Colour

| | |
|---|---|
| Working space | `TBD` — recommend Rec.709 / Gamma 2.4 for a 709 deliverable, ACEScct if HDR is in scope |
| Delivery | Rec.709, 100 nit reference, per [../standards/delivery_specs.md](../../standards/delivery_specs.md) |
| Grade | One show LUT per line, in `library/luts/`, versioned. Shot-level grading works *under* the show LUT, never around it. |
| Palette | `TBD per line`. Define a primary, a secondary, and one accent reserved for a specific narrative function. |
| Skin tone | The single most common failure in generated imagery and in grading. The line's style doc must state the skin-tone rendering intent explicitly, and the QC pass checks it on every shot with people. Do not let a show LUT crush or desaturate skin. |

## 5. Categories of image and how each is treated

Every shot on the shot list carries a `provenance_class`. It determines labelling,
treatment, and which gate applies.

| Class | What it is | Treatment |
|---|---|---|
| `archival` | Genuine historical photograph, film, or document. | Cleared through rights. Never altered beyond restoration. Restoration logged. Credited on screen. |
| `contemporary` | Present-day footage of a real place or object. | Location and date on screen or in the credit roll. |
| `artefact` | Photograph of a material object in a collection. | Institution credited. Object ID recorded. |
| `reconstruction` | Generated depiction of a historical scene, place, or person, grounded in evidence. | Labelled per §7. Evidence basis on the shot record. |
| `interpretive` | Generated imagery that is evocative rather than depictive — texture, abstraction, atmosphere. | Labelled per §7. |
| `graphic` | Maps, diagrams, timelines, data. | Sources on the graphic or in credits. Projection stated on maps. |
| `text_on_screen` | Quotations, titles, translations. | Quotation source on screen. Translation credited. |

Mixing `archival` and `reconstruction` within a single continuous shot is
prohibited. A cut is required at the boundary.

## 6. Reconstruction craft rules

- **Ground every reconstruction in a material fact.** Architecture from excavation
  or standing structures; textiles from surviving examples; tools from collections.
  The shot record names them.
- **Do not reconstruct what is not known.** If the roof form is unattested, frame
  below the roofline. Composition is the honest tool for uncertainty.
- **Faces.** Crowd and unnamed figures are free. Named individuals are constrained
  by [03_narrative_doctrine.md](03_narrative_doctrine.md) §6.
- **Anachronism check** is a named QC step: materials, textiles, crops, weapons,
  writing, architecture, animals, and imported goods are each checked against period.
  This is where generated imagery fails most often and most embarrassingly, because
  models default to a generic pan-historical vocabulary.

## 7. Labelling generated imagery

Every generated shot is labelled. The studio uses three simultaneous layers:

1. **In-frame** — a persistent, unobtrusive corner mark reading `RECONSTRUCTION` (or
   the line's localised equivalent) for the duration of any `reconstruction` or
   `interpretive` shot. Design spec in [../brand/labelling_system.md](../../studios/african-history/brand/labelling_system.md).
2. **Sequence-level** — a full card at the first reconstruction of each episode
   explaining what the mark means, and a statement in the credits.
3. **Metadata** — C2PA/Content Credentials on delivery where the platform supports
   it, plus the episode's own provenance manifest.

The mark is not an apology. Viewers who know what they are looking at trust the
material they are told is real.

## 8. Maps and data graphics

- State the projection. Historical borders are drawn as zones of influence, not
  crisp lines, unless a treaty line is being depicted and cited.
- Modern national borders are never drawn over pre-colonial periods without an
  explicit on-screen note that they are a modern overlay for orientation.
- Every map cites its geographic and historical sources.
- Data graphics follow [../standards/data_graphics.md](../../standards/data_graphics.md):
  no truncated axes, uncertainty shown, source and date in the frame.

## 9. Typography

`TBD per line`, specified in [../brand/](../../studios/african-history/brand). Constraints: one display face,
one text face, both licensed for broadcast and for the delivery territories; full
diacritic coverage for every language the line uses (see
[09_localization.md](09_localization.md) §2 — this eliminates most fonts, so choose
before designing).

## 10. QC checklist for every generated shot

Enforced at picture lock via [../ops/checklists/picture_lock.md](../../ops/checklists/picture_lock.md):

- [ ] Anatomy: hands, limbs, eyes, count of people consistent across the shot
- [ ] Text in frame: no garbled pseudo-script; any lettering is deliberate and correct
- [ ] Anachronism pass complete and recorded
- [ ] Light direction consistent with the scene
- [ ] Skin tone rendering matches the line standard
- [ ] Style anchor ID referenced and honoured
- [ ] Temporal stability (no flicker, morph, or drift) across the clip
- [ ] Provenance class assigned; label applied if required
- [ ] Prompt card and seed recorded in the manifest
