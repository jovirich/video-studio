---
title: EXP-001 shot plan
status: draft
maturity: NOT STARTED
version: 0.1.0
updated: "2026-08-07"
owners: [visual-director]
---

# EXP-001 — shot plan

Twenty shots is not an arbitrary number. It is roughly the point at which continuity
mechanisms stop being anecdotally fine and start visibly failing — and it is small
enough to abandon and redo.

No shot records exist. `03_storyboard/shots/` is empty.

## Design the plan to break things

A shot list that avoids hard cases proves nothing. This one is deliberately
constructed to stress each mechanism, and the distribution matters more than the
content.

| Group | Count | What it stresses |
|---|---|---|
| **Location, varied angle** | 6 | Spatial continuity — the same place from wide, reverse, high, low, close, and through an opening. Sightlines must agree. |
| **Character A, varied angle** | 4 | Identity across front, three-quarter, profile, back-of-head-turning |
| **Character A, varied light** | 2 | The harder half. Identity usually survives angle and fails under a lighting change. |
| **Character B** | 3 | Whether the mechanism holds two people *separately* or converges them |
| **Both characters in frame** | 2 | The real test. Two references in one image is where most mechanisms break. |
| **Detail / material** | 2 | Period markers at close range, where anachronism is most visible |
| **Motion** | 1 | One shot taken to video, to test the still-to-motion chain and the conform step |

Twenty. At least four should be **deliberately awkward**: an angle the reference set
does not cover, a light the anchor was not built for, a two-shot at unequal distance.
The finding is in where it fails, not in where it holds.

## Rules for this plan

- **Locked frames on at least a third.** Unmotivated drift on every shot is the
  signature tell of generated video, and a plan that moves the camera constantly hides
  continuity failures behind motion.
- **One time of day.** Weather and ground state fixed in the location's continuity
  record. Any variation is a breakage, not a creative choice.
- **Lens set from the line's visual identity** — which does not exist yet, and is
  therefore a blocker. Improvising a lens set here would make the coherence finding
  meaningless.
- **Every shot carries a claim reference** where it asserts anything — including the
  detail shots, which assert material facts.
- **Compose around what is unattested.** If the roof form is unknown, frame below it.
  Where the plan does this, record it in the location's `unattested_elements`, because
  that decision is the useful output.

## Records to create

| Record | Count | Where |
|---|---|---|
| `SHT-NG-EXP001-0001` … `-0020` | 20 | [`shots/`](shots/) |
| `SEQ-NG-EXP001-001` (…`-002`) | 1–2 | in the shot records |
| `PC-NG-EXP001-0001` … | ~20 | [`../04_prompts/`](../04_prompts/) |
| `CNC-NG-….md` | 1–2 | [`../../../continuity/characters/`](../../../continuity/characters/) |
| `CNL-NG-….md` | 1 | [`../../../continuity/locations/`](../../../continuity/locations/) |
| `STA-NG-….md` | several | anchors, in `library/style_refs/` |

**Continuity records are written before the first generation, not after.** Building
them retroactively from whatever came out is how a production ends up with a
canonical version that is simply the first acceptable render — which is the failure
the narrative pack's `continuity_lock` gate exists to prevent.

## Order of work

1. Location continuity record, with `forbidden_objects` populated from the research
2. Character continuity records
3. Anchors generated and checksummed, one at a time, each assessed before the next
4. **Drift test** — a handful of throwaway renders across angle and light, recorded on
   the continuity record. If it fails here, change the mechanism now. This step costs
   an hour and saves the production.
5. Shot records
6. Prompt cards
7. Generate, assess against the evaluation rubric **in order**, record every run
   including rejections
8. Conform, edit, findings

Step 4 is the one that will be skipped under time pressure. It is also the one that
determines whether the other nineteen shots are worth generating.

## Measurements to capture per shot

Not optional — these are the experiment's data, and reconstructing them afterwards is
not possible.

- Attempts before an acceptable render, and why each was rejected
- Wall-clock time from card to accepted asset
- Generation cost
- Whether the continuity anchor held, judged against the anchor and not from memory
- Whether the shot needed a card field that does not exist
- Whether any card field went unused
