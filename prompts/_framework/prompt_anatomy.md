---
title: Prompt anatomy
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, pipeline-engineer]
---

# Prompt anatomy

How to fill a prompt card so the render is repeatable, reviewable, and consistent
with everything around it.

## The card is structured because the string is not reviewable

A 200-word prompt string is a wall of text in which a reviewer cannot find the claim,
the sensitivity risk, or the anachronism. The same content in fields can be read
selectively: the Cultural Advisor reads `subject` and `constraints`; the Research
Lead reads `evidence_basis` and `period_markers`; the Visual Director reads
`camera`, `light`, and `inheritance`.

## Field by field

### `target.intent` — one sentence

What this shot must accomplish **in the cut**. Not what it depicts — what it does.

> ✅ "Establish that the settlement is larger than the viewer has been led to expect."
> ❌ "Wide shot of a settlement."

If the intent cannot be stated, the shot is decoration and should be cut before it is
generated.

### `subject` — specific, always

Name the people, place, and period. Never a region, never an era, never a continent.

> ✅ "Three metalworkers at a shaft furnace, working in the early morning"
> ❌ "African craftsmen at work"

Models carry a strong prior toward generic, placeless pastiche and will produce it
whenever the prompt permits. Specificity is the only reliable counter, and it is
required by the sensitivity standards of most packs.

### `period_markers` — the most important field

Concrete material detail that fixes the moment in time. This is what separates a
grounded reconstruction from a costume-drama average.

Cover, where relevant: building materials and technique; textiles, dyes, and weave;
tools and their materials; vessels and containers; crops and food; animals present
and absent; weapons; writing surfaces; imported goods and their origin; personal
adornment; lighting technology.

Each marker should be traceable to something in `evidence_basis`. A marker nobody can
source is an invention, and it will be the detail an expert viewer notices first.

### `setting` — where the light and space come from

Terrain, structures, vegetation, water, weather, season, and the spatial relationship
between them. Terrain drives light, and light is what makes a frame read as
photographed rather than assembled.

### `composition` and `camera`

Camera comes from the line's defined lens set. A defined lens set is the cheapest
available purchase of coherence — three or four focal lengths used consistently look
like one production; unconstrained focal lengths look like a mood board.

Movement requires a motivation. Unmotivated drift on every shot is the single
clearest tell of generated video.

### `light`

Source, direction, quality, time of day. Must be consistent within a scene and
physically plausible: fire lights warm, moves, and falls off fast; overcast light has
direction even when soft; a single interior window does not illuminate a whole room
evenly.

Generated imagery violates light logic constantly, and it is a primary QC check.

### `palette` and `texture`

Inherited from the line's style block. Override only with a reason, because palette
drift across a sequence is invisible while generating and glaring in a cut.

### `negative`

See [negative_library.md](negative_library.md). Keep it short and specific to this
shot. Long inherited negative lists cost tokens, dilute the positive prompt, and on
several models actively degrade output.

### `evidence_basis`

Required for `reconstruction`. Claims and sources grounding what is depicted. If it
would be empty, the class is `interpretive`, not `reconstruction` — and if the shot
genuinely needs to be depictive but nothing supports it, the shot does not exist.

### `constraints`

Named person, sacred material, violence, human remains. These flags route the card to
the sensitivity gate **before** generation. Setting them honestly is cheaper than
having a striking, unusable image argued over afterwards.

## Order matters, per model

Most image models weight earlier tokens more heavily. The renderer emits fields in an
order tuned per vendor; the cheat sheets record what each expects. Do not reorder by
hand — change the renderer, so every card benefits.

## Length

| Modality | Typical useful range |
|---|---|
| Image | 40–120 words. Beyond ~150, most models start ignoring the tail. |
| Video | Shorter than image. Motion models handle one clear action far better than three. |
| Voice | Direction, not description. Pace, emphasis, emotional register. |
| Music | Instrumentation, tempo, texture, function. Avoid genre labels that carry cultural specificity you have not cleared. |

## The reviewer's questions

A card is ready when someone else can answer all of these from the card alone:

- What is this shot for?
- What is depicted, specifically — who, where, when?
- What grounds it in evidence?
- Where does its look come from, and what did it override?
- What could go wrong culturally or ethically?
- If this render is wrong, what would we change?
