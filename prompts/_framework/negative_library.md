---
title: Negative prompt library
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# Negative prompt library

## First: most negatives are cargo cult

The long negative lists that circulate — sixty comma-separated terms copied between
users — mostly do nothing. On several current models they actively degrade output by
diluting the conditioning and consuming the token budget the positive prompt needs.

**Negatives are for a specific, observed, recurring failure.** Add one because you
saw the problem, not because a list had it.

Test before adopting: generate with and without, same seed, and look. If you cannot
see the difference, the negative is noise.

## Modern models often do not need them

Newer models with strong prompt adherence respond better to **stating what you want**
than to listing what you do not. "Overcast, flat light, no visible sun" beats a
positive prompt plus `--no sunlight`. Reach for a positive statement first.

## Where negatives genuinely earn their place

### Style leakage

The most common real use. When a model's house aesthetic contradicts the production's
visual identity:

```
oversaturated, HDR, heavy vignette, bokeh, lens flare, shallow depth of field,
golden hour, cinematic colour grade
```

Every one of those is a default that must be actively removed for a documentary look.
This block is usually worth inheriting at the line level.

### Anachronism, per production

The highest-value negatives, and they are always production-specific. Build them from
what your anachronism QC pass actually catches, not in advance:

```
plastic, synthetic fabric, machine stitching, modern footwear, wristwatch,
power lines, corrugated metal roofing, concrete blocks, printed text
```

Add to this list every time the QC pass finds something. It is the one negative block
that compounds in value across a season.

### Composition failures

```
text overlay, watermark, signature, border, frame, split screen, collage, tiling
```

### Anatomy

Diminishing returns on current models; still occasionally useful:

```
extra fingers, malformed hands, extra limbs, fused figures
```

Reframing usually works better: give hands an object to hold, keep crowds at
mid-ground or further.

## What never belongs in a negative prompt

**Cultural and ethical constraints.** A negative prompt is not a safeguard. If a shot
must not depict sacred material, that is a `constraints` flag on the card routing it
to review — not a word in a negative list that the model may or may not honour.

Confusing the two is a category error with real consequences: it treats a soft
statistical nudge as a hard boundary.

## Inheritance

Negatives inherit like everything else: line → sequence → card. Keep the card-level
list to what is specific to *that shot*. If the same negative appears on ten cards, it
belongs in the line's style block.

Long inherited chains are a smell — they usually mean the positive prompt is
underspecified.

## Per-vendor syntax

Differs sharply: a dedicated field, a `--no` flag, weighted tokens, or unsupported
entirely. The renderer handles it per vendor; the card just lists terms. Do not write
vendor syntax into the card.

## Maintaining this file

Add an entry when a negative demonstrably fixed a recurring problem, with a note on
which model and what it fixed. Remove entries that stop earning their place — models
change, and a negative that was essential a year ago may now be inert or harmful.
