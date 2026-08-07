---
title: Visual identity — Nigeria line
status: template
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# Visual identity — Nigeria line

The line's look, written so a prompt card can inherit it.

Maturity: **NOT STARTED**. Every value below is `TBD — Visual Director`. This is the
`visual_identity` decision in [studio.yaml](../../../studio.yaml), `unresolved`, and
it blocks every prompt card in this line.

## 1. Before filling any of this in

**A look is not chosen from references. It is derived from the material.**

The line's imagery is largely `reconstruction` and `interpretive`, and every
reconstruction is grounded in a material fact — architecture from excavation or
standing structures, textiles from surviving examples, tools from collections, with the
shot record naming them
([pack 04 §6](../../../../../packs/documentary-history/04_visual_language.md)). A look
decided before the archive landscape is surveyed is a look the evidence will have to be
made to fit, and the direction of that pressure is always the same: toward the image
that already exists.

So the order is:

1. [Archive landscape survey](../sources/archive_landscape.md) — **NOT STARTED**.
   What material evidence exists, and what does not.
2. Advisory coverage — [../advisory/README.md](../advisory/README.md) — **NOT
   STARTED**. What may be depicted at all.
3. This document.
4. Style anchors, then prompt cards.

Filling this in ahead of 1 and 2 produces a look that has to be defended rather than
one that has to be applied.

**Every value below carries three fields when it is filled: the decision, the reason,
and what it prevents.** A look with no stated reason gets overridden per sequence by
whoever is generating that day, which is precisely the incoherence the look exists to
stop.

## 2. Palette

| | |
|---|---|
| Primary | `TBD — Visual Director` |
| Secondary | `TBD` |
| Accent | `TBD`, and **reserved for one specific narrative function**, stated. An accent used for emphasis and for a category at the same time teaches the viewer nothing. |
| What is excluded | `TBD.` Name the colours the line does not use. An exclusion list is more useful to a prompt than an inclusion list, because a generator will supply anything not forbidden. |
| Derivation | `TBD.` State what the palette is derived *from* — material evidence, landscape, light — and cite it. A palette derived from other documentaries about the region inherits their assumptions along with their colours. |
| Relationship to studio brand | Independent. Brand colour is identity; this is photography ([README.md](README.md) §5). |

## 3. Lens set

| | |
|---|---|
| Set | `TBD — Visual Director.` A closed set of focal-length equivalents, and only those. |
| Rationale per focal length | `TBD.` What each is for. A set with no assigned use is a list. |
| Depth of field | `TBD.` Consistent with the chosen lens and stop. **Resist the shallow default** — generated tools default to it, and historical exteriors read false at f/1.4 ([pack 04 §2](../../../../../packs/documentary-history/04_visual_language.md)). |
| Height and angle | `TBD.` Eye level is the studio default. Low angles ennoble and high angles diminish; both are editorial choices requiring a stated reason, and on this line's subject matter both are read as positions. |
| Motion | Motivated only. Roughly one third of shots locked. A drifting camera on every shot is the signature tell of generated video, and it is the first thing an audience learns to spot. |

**A defined lens set is the cheapest way to buy coherence** across generated material.
It costs one decision and it constrains every prompt card thereafter.

## 4. Grade and show LUT

| | |
|---|---|
| Working space | `TBD.` Rec.709 / Gamma 2.4 for a 709 deliverable; ACEScct if HDR ever comes into scope. |
| Delivery | Rec.709, 100 nit reference — [standards/delivery_specs.md](../../../../../standards/delivery_specs.md) |
| Show LUT | `TBD — Visual Director.` **One** per line, versioned, in [library/luts/](../../../../../library/luts/). |
| Shot-level grading | Works **under** the show LUT, never around it. A shot graded around the LUT is a shot that will not match after a LUT revision, and the mismatch surfaces at picture lock. |
| Versioning | `TBD.` A LUT change after any generation is a re-grade of everything already produced. Version it, date it, and record which productions used which. |

## 5. Light behaviour

Studio-wide rules apply and are not restated
([pack 04 §3](../../../../../packs/documentary-history/04_visual_language.md)): light
has a source and a direction in every frame, consistent within a scene; time of day is
chosen, recorded on the shot record, and consistent across a sequence; practical
sources behave physically.

What this line decides:

| | |
|---|---|
| Characteristic light | `TBD — Visual Director.` Quality, direction, colour temperature, contrast ratio. |
| Times of day in the vocabulary | `TBD.` A closed set, with what each is used for. |
| Interior behaviour | `TBD.` How light enters, and from what. |
| Night | `TBD.` Including what the light sources are and how they fall off. |
| What is prohibited | `TBD.` Generated imagery routinely violates source-and-direction consistency; naming the specific violations this line rejects makes the QC check fast instead of subjective. |

Light-direction consistency is a **primary QC check** on every generated shot. Writing
the rule vaguely here makes that check unenforceable later.

## 6. Texture and material

| | |
|---|---|
| Surface vocabulary | `TBD — Visual Director` |
| Grain / noise treatment | `TBD.` Constraint: **no treatment that reads as photographic age or archival provenance.** A film-grain or aged-print treatment on a `reconstruction` shot invites the viewer to read it as found material, which is the standing prohibition in [core/01 §2](../../../../../core/01_provenance_and_ai_disclosure.md) achieved by grade rather than by prompt. |
| Atmosphere | `TBD.` Haze, dust, and smoke are period and place claims when they carry information, and generator defaults when they do not. |
| Resolution and detail | `TBD.` Where detail is unattested, composition is the honest instrument — frame it out rather than invent it. |

## 7. Skin-tone rendering intent

**This section is mandatory, must be explicit, and is checked on every shot with
people.** It is not a preference and it is not left to the colourist.

> Skin tone is the single most common failure in generated imagery and in grading. The
> line's style doc must state the skin-tone rendering intent explicitly, and the QC
> pass checks it on every shot with people. Do not let a show LUT crush or desaturate
> skin.
> — [pack 04 §4](../../../../../packs/documentary-history/04_visual_language.md)

| | |
|---|---|
| Rendering intent | `TBD — Visual Director.` Written as a **specification**, not an aspiration: target luminance ranges, hue placement, saturation behaviour, and how the range varies across the people the line depicts. "Natural" is not a specification. |
| Show LUT interaction | `TBD.` Verified across the **full** tonal range the line will depict, not on one reference frame. This is where a LUT chosen on a landscape fails: it looks superb on the ground and crushes the people standing on it. |
| Under- and over-exposure behaviour | `TBD.` How skin holds in the darkest and brightest shots in the vocabulary. |
| Generated-imagery bias | `TBD.` Generators carry their training data's lighting and rendering assumptions and will apply them by default. State what the line rejects, so a prompt card can counter it explicitly rather than a colourist repairing it afterwards. |
| QC | **Every shot with people.** Named step at picture lock ([pack 04 §10](../../../../../packs/documentary-history/04_visual_language.md)), recorded, not spot-checked. |
| Thumbnails | Same intent applies. Thumbnails are frequently graded separately for punch, which is exactly where the discipline gets abandoned — [brand/thumbnail_system.md](../../../brand/thumbnail_system.md) §5. |

What breaks if this is left implicit: the failure is silent, cumulative, and highly
visible to the audience the charter says the work must not fail
([bible/00_charter.md](../../../bible/00_charter.md) §3). Nobody flags it shot by shot,
and it is discovered as a pattern across a finished season, at which point the remedy
is a re-grade of everything.

## 8. Style anchor set

| | |
|---|---|
| Anchors | `TBD — Visual Director.` `STA-NG-*`, in [library/style_refs/](../../../../../library/style_refs/), one set per sequence type. |
| Form | **Specific files with checksums**, versioned. Not a mood board, not a folder someone maintains. |
| Reference from prompt cards | By ID, mandatory. A card with no anchor ID does not inherit anything. |
| Override policy | An override must state why, on the card. Unexplained overrides accumulate and the line's look drifts one shot at a time. |
| Provenance | Anchors are assets. Where an anchor is itself generated it carries a manifest entry, a prompt card, and a rights position like any other. |

**None exist**, and none can be produced before §2–§7 are decided — an anchor generated
from an undecided look becomes the de facto look by being the only concrete thing in
the folder.

## 9. QC checklist inherited

Every generated shot is checked at picture lock against
[pack 04 §10](../../../../../packs/documentary-history/04_visual_language.md):
anatomy, in-frame text, anachronism pass, light direction, **skin-tone rendering
against this document**, style anchor referenced and honoured, temporal stability,
provenance class and label, prompt card and seed in the manifest.

The anachronism pass is where generated imagery fails most often and most
embarrassingly — materials, textiles, crops, weapons, writing, architecture, animals,
and imported goods each checked against period — because models default to a generic
pan-historical vocabulary. This document is one of the two things that makes that check
tractable; the other is the research.

The checklists themselves live in [ops/checklists/](../../../../../ops/checklists/) and
are **NOT BUILT**.

## 10. Blocked on

- Archive landscape survey — [../sources/archive_landscape.md](../sources/archive_landscape.md), **NOT STARTED**
- Advisory coverage — [../advisory/README.md](../advisory/README.md), **NOT STARTED**
- A named Visual Director — `TBD` in [studio.yaml](../../../studio.yaml)

Downstream of this document: every prompt card, every style anchor, every generated
asset in this line.
