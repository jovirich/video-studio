---
title: EXP-001 — decisions blocking the four diagnostic shots
status: draft
maturity: NOT STARTED
version: 0.1.0
updated: "2026-08-07"
owners: [showrunner, visual-director]
---

# Decisions needed before shots 01, 04, 06, 18

Everything else in EXP-001 is scaffolded and waiting. These are the only calls that
block the first four renders.

**Why these four shots.** 01 baseline, 04 profile, 06 backlit, 18 two-shot — the four
hardest cases in the plan. If the mechanism fails here it fails everywhere, and four
shots cost an hour where twenty cost a day. Do not generate the other sixteen until
these are scored.

**Fix these before generating, not after.** Drift is measured *against* this record.
A record written to match whatever came out is not a measurement, it is a description.

---

## 1. Character A — appearance `[CNC-NG-0001]`

Needed for all four shots.

| Decision | Note |
|---|---|
| **Apparent age range** | Narrow enough to be falsifiable. "30–40" is checkable; "adult" is not. |
| **Skin tone + visual reference** | A **swatch or named value**, not a word. The acceptance threshold is 20/20 with no allowance, so a scorer needs something to hold against a frame. |
| **Hair** — style, length, texture | |
| **Facial hair**, if any | No separate schema field; record it under `appearance.hair`. |
| **Body build** | |
| **Height** — relative to B | Absolute height means nothing to a generator. |
| **Facial structure** | The field shot 04 will break first. |
| **Distinctive feature** — optional but recommended | One unambiguous, always-visible feature turns `same_person` scoring from gestalt judgement into a binary check. Without one you are scoring by feel, which is what the plan is trying to avoid. |
| **Primary wardrobe** — upper, lower, colours | One set only. A costume change adds a variable to a test about identity. |
| **Accessories** | Recommended: none. Nothing may signify status, office, or rank. |

## 2. Character B — appearance `[CNC-NG-0002]`

Needed for shot 18 only, but decide it **with A's record open**.

B exists to answer whether the mechanism holds two people *separately* or collapses
them toward one face. If A and B are close in face, age, build, or silhouette, a
convergence failure becomes indistinguishable from ordinary drift — and that is the
most valuable single result in the run.

Same field list as A, plus:

| Decision | Note |
|---|---|
| **How B is unambiguously not A** | Face, age, build, silhouette. Different hair alone is not enough. |
| **A second distinctive feature**, different from A's | Makes shot 18 scoreable rather than arguable. |

## 3. The continuity mechanism — both characters

| Decision | Note |
|---|---|
| **Which mechanism holds identity** | Character reference image · trained adapter · (cast performer is out of scope here). |
| **Same mechanism for A and B** | Strongly recommended. Mixing them confounds shot 18 — a failure could be the mechanism or the mixture, with no way to tell. |
| **Vendor, model, and model version** | Pin the version. A seed does not transfer across a model update, so an unpinned version makes every recorded seed worthless. |

## 4. Two visual anchors

| Decision | Note |
|---|---|
| **A's facial reference** `[references.facial_reference]` | The single canonical face. Every later shot is scored against this frame. Must exist before shot 01 is *accepted*. |
| **The location establishing anchor** `[CNL-NG-0001]` | The canonical wide of the workshop. Every other angle checks against it. |

---

## Not needed yet

So the list above stays short:

- The other sixteen shots' records and prompt cards
- Location geometry, if it is being blocked in 3D — decide after the four
- Any drift-test result — that is the *output* of these four shots
- Anything about EXP-002

## Already decided — no action

Subject, shot plan, stress axes, acceptance thresholds, scoring columns, the
workshop's architecture, materials, prop zones, light direction, camera-safe
geography, lighting variants, and all forbidden objects. See
[`03_storyboard/shot_plan.md`](03_storyboard/shot_plan.md) and
[`CNL-NG-0001`](../../continuity/locations/CNL-NG-0001_workshop.md).
