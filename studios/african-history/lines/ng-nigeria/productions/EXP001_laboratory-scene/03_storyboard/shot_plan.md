---
title: EXP-001 shot plan — continuity stress test
status: draft
maturity: NOT STARTED
version: 0.2.0
updated: "2026-08-07"
owners: [visual-director]
---

# EXP-001 — shot plan

**Purpose: continuity stress test only.** Not a sequence, not a scene, not a story.
Twenty shots designed to make identity drift *if it is going to*, and to make the
drift measurable when it does.

No shot records exist yet. `shots/` is empty.

## The one metric

**Primary: visual identity drift across 20 shots.**
**Secondary: location and style drift.**

Nothing else is being measured. Not composition, not beauty, not whether it looks
like a documentary. A shot that is ugly and on-model passes. A shot that is beautiful
and off-model fails.

## Design the plan to break things

A shot list that avoids hard cases proves nothing. Identity usually survives a
straight-on medium shot and fails under a lighting change — so the plan is weighted
toward the conditions that actually break continuity, not the ones that flatter it.

| # | Shot | Distance | Angle | Light | Stress being applied |
|---|---|---|---|---|---|
| 01 | A, reference frame | MS | front | key from window, ¾ front | **The baseline.** Every later shot is scored against this and against the record. |
| 02 | A | CU | front | as 01 | Distance change alone. The easiest case; if this drifts, stop. |
| 03 | A | MS | ¾ left | as 01 | First angle departure |
| 04 | A | MS | profile left | as 01 | **Profile.** Reference-based methods degrade sharply here. |
| 05 | A | MS | ¾ right | as 01 | Does it hold symmetrically, or only on the trained side? |
| 06 | A | MCU | front | **backlit** | **Lighting change with angle held.** Isolates light as the variable. |
| 07 | A | MS | ¾ left | backlit | Angle *and* light together — the compound case |
| 08 | A | WS | front | overhead, hard | Small in frame; does identity survive low pixel coverage? |
| 09 | A | MCU | front | low key, single source | Deep shadow across half the face |
| 10 | A | MS | ¾ | key from window | **Walking.** Motion blur and pose change. |
| 11 | A | CU | front | as 01 | **Partial occlusion** — hand or object across the face |
| 12 | A | MCU | ¾ | as 01 | **Expression change** from neutral |
| 13 | A | MS | rear→turn | as 01 | Back of head turning to ¾. The hardest single-subject case. |
| 14 | A | MS | front | **exterior daylight** | **Indoor→outdoor transition.** Different light entirely. |
| 15 | A | MCU | ¾ | exterior daylight | Sustained in the new environment |
| 16 | B | MS | front | as 01 | **Second character baseline.** |
| 17 | B | MCU | ¾ | backlit | B under the same stress as A |
| 18 | **A + B** | MS two-shot | front | as 01 | **Two references in one frame.** Where most mechanisms break. |
| 19 | **A + B** | MS | ¾, unequal distance | as 01 | Do they converge toward one face? |
| 20 | **A in a crowd** | WS | front | as 01 | **Crowded frame.** Does A remain findable and on-model? |

A appears in 17 of 20. That is deliberate: drift is a function of repetition, and a
character seen three times tells you nothing.

**Wardrobe visibility** varies across the set — full-length in 08, 10, 14, 18, 20;
above-waist elsewhere. A wardrobe set that only ever appears from the chest up has
not been tested.

## Scoring — per shot, against the record, not by feel

Judging a sequence by feel is how a production convinces itself continuity held.
Every shot is scored independently against the continuity record and against shot 01.

`08_review/drift_score.csv`, one row per shot:

| Column | Values | Note |
|---|---|---|
| `shot` | SHT-…-0001 … 0020 | |
| `same_person` | pass / marginal / fail | Would a viewer accept this as the same individual? |
| `age_consistent` | pass / marginal / fail | Against `age_range` on the record |
| `facial_structure` | pass / marginal / fail | Against `appearance.facial_structure` |
| `hair` | pass / marginal / fail | Against `appearance.hair` |
| `skin_tone` | pass / marginal / fail | Against `appearance.skin_tone_reference` — measured, not eyeballed |
| `core_wardrobe` | pass / marginal / fail / n-a | `n-a` only where the garment is genuinely out of frame |
| `distinctive_features` | pass / marginal / fail / n-a | Each feature the record says is `always_visible` |
| `forbidden_present` | none / list | **Any forbidden object or variation appearing is an automatic fail for that shot** |
| `location_consistent` | pass / marginal / fail / n-a | Geometry, materials, light direction |
| `attempts` | integer | Renders before an acceptable one |
| `<dimension>_severity` | 1–5 | One per applicable dimension above. See the scale below. |
| `notes` | free text | Where it broke, under what condition |

### Drift severity, 1–5, per applicable dimension

Recorded alongside the pass/fail columns, in `<dimension>_severity`.

| | Meaning |
|---|---|
| **1** | No perceptible drift |
| **2** | Minor drift, identity clearly intact |
| **3** | Material drift requiring attention |
| **4** | Severe drift, identity unstable |
| **5** | Effectively a different character or environment |

**Binary pass/fail remains authoritative.** Severity exists for diagnosis and for
comparing mechanisms — it is what will make a later trained-adapter run comparable to
this reference-image baseline, rather than merely differently opinionated.

Two things it buys that pass/fail cannot: it distinguishes *nearly held* from
*collapsed*, which is the difference between tightening a prompt and changing the
mechanism; and it lets a failure be located — a set that scores 2s under backlight and
4s in profile says something specific about what may be shot.

Score severity even where the binary is a pass. A run of 2s that never fails is a
mechanism about to fail on shot 21.

**`marginal` is a fail for headline purposes.** It is recorded separately only so the
failure mode can be described precisely.

## Acceptance criteria

Deliberately brutal, and stated before the run so they cannot be softened after it:

| Criterion | Threshold |
|---|---|
| `same_person` | **20/20 pass.** Any fail means the mechanism does not hold. |
| `age_consistent`, `facial_structure`, `hair` | ≥18/20 pass, no fails in shots 01–09 |
| `skin_tone` | **20/20 pass.** A drifting skin tone is not a continuity nuisance; it is a representational failure. |
| `core_wardrobe` | ≥15/17 of the shots where it is in frame |
| `forbidden_present` | **0 occurrences across all 20.** One is a fail for the whole run. |
| `location_consistent` | ≥16/18 of the shots where the location is visible |
| Two-character shots (18, 19) | Both characters pass `same_person`, and **do not converge** |

Falling short is a *result*, not a failure of the experiment. The finding is which
condition broke it — backlight, profile, occlusion, or the second face — because that
tells the production what it may and may not shoot.

## Order of work

1. Continuity records for A, B, and the location, with `forbidden_*` populated
2. Anchors generated and checksummed
3. **Drift test on shots 01, 04, 06, 18** — the four hardest cases, first
4. If step 3 fails, change the mechanism and repeat. Do not generate the other sixteen.
5. Shot records and prompt cards for all twenty
6. Generate, scoring each shot as it lands
7. Findings

**Step 3 is the whole discipline.** Four shots will tell you what twenty would, and
generating nineteen shots before discovering the mechanism does not hold is exactly
the waste this experiment exists to prevent.

## Explicitly out of scope

Named so they are decisions rather than omissions, per the standing instruction:

- Narration, music, sound of any kind
- Story, sequence logic, or edit
- Any second adapter
- Any new schema, record type, or architecture

## Subject

`TBD` — see [`../README.md`](../README.md) § Subject and the open question in
[`../00_brief/brief.md`](../00_brief/brief.md).

The plan above is **subject-independent by construction**. Every stress axis —
distance, angle, light, occlusion, expression, motion, environment transition, second
character, crowd — applies unchanged to any subject. Whatever is chosen, this table
does not move.
