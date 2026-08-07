---
title: Continuity registry — Nigeria line
status: active
maturity: DESIGNED
version: 0.1.0
updated: "2026-08-07"
owners: [visual-director]
---

# Continuity registry

Empty. No continuity record exists yet.

## What this solves

Generative tools have no memory. Ask for the same character three times and you get
three people; ask for the same courtyard three times and you get three courtyards.
Across twenty shots that is fatal, and across a season it is what makes AI-assisted
work look like a mood board — beautiful shot to shot, incoherent across a cut.

Prompt discipline does not fix it. Something external has to hold the canonical
version, and this is that thing.

## Two records per subject, not one

| Record | Answers | Lives in |
|---|---|---|
| `CHR-*` / `LOC-*` | *Who were they? Where was it? What does the evidence say?* | [`../characters/`](../characters/), [`../locations/`](../locations/) |
| `CNC-*` / `CNL-*` | *What does the model produce, every time?* | here |

They are separate because they answer to different authorities. The evidence record
answers to sources. The continuity record answers to what actually came out of the
tool. Fusing them would let wardrobe decisions sit alongside claims, and would make
it impossible to depict one person at two life stages — which needs two continuity
records and exactly one entity record.

The link runs one way: a continuity record names its `entity`. Where an appearance
choice rests on evidence, the field cites the claim. Where it does not, the record
says so in `historical_uncertainty` — which is most of it, for most historical
characters, and saying so is the point.

## What each record carries

**Characters** — canonical name, age range, appearance (skin tone with a measurable
reference, hair, build, facial structure, posture, hands), distinctive features and
their cultural weight, wardrobe *sets* rather than loose items, jewellery and what it
signifies, the reference block (face anchor, anchor set, approved seeds with their
model version, trained adapter, drift test), voice, **forbidden variations**, and
historical uncertainty.

**Locations** — era, architecture and construction technique, materials as an
allow-list, spatial geometry and sightlines, vegetation, weather and ground state,
lighting language, camera language, soundscape, reference imagery, **forbidden
objects**, and unattested elements.

Full field definitions with the reasoning:
[`continuity_character.schema.json`](../../../../../standards/schemas/continuity_character.schema.json),
[`continuity_location.schema.json`](../../../../../standards/schemas/continuity_location.schema.json).

## The three fields that earn their keep

**`forbidden_variations` / `forbidden_objects`.** Built from what the anachronism
pass actually catches, so they compound across a season. This is the one negative
list genuinely worth inheriting into every prompt. It is also the field most often
left empty, which is why a locked location record is required to have one — an empty
forbidden list at lock means nobody has run an anachronism pass.

**`approved_seeds`, with model and version.** A seed does not transfer between
models, or between versions of one model. Recording a bare seed records nothing.

**`drift_test`.** Required before a record can lock. It asks the only question that
matters: does this mechanism *actually* hold across angles and lighting? An untested
continuity mechanism is an assumption, and the cheapest place to discover it fails is
shot 3, not shot 40.

## Severity is not a negative prompt

`forbidden` entries carry a severity. `anachronism` and `style-breach` feed the
negative prompt. **`culturally-prohibited` does not** — it routes to the sensitivity
gate as a hard stop.

A negative prompt is a statistical nudge that a model may or may not honour.
Treating it as a safeguard is a category error with consequences outside the studio.

## Creating a record

```bash
python -m studio_ops new-record --type continuity_character --line ng-nigeria   # NOT BUILT
```

Until the allocator exists, copy from
[`templates/records/`](../../../../../templates/records/) and allocate the ID by hand
against this directory — checking for a collision first. See
[`standards/id_system.md`](../../../../../standards/id_system.md).

## Status

| | |
|---|---|
| Schemas | DESIGNED |
| Records here | none |
| Drift test methodology | DESIGNED, never run |
| Allocator (`new-record`) | NOT BUILT |

Nothing here has been exercised. The first test is
[Experimental Production 001](../productions/).
