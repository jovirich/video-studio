---
title: Seed discipline
status: active
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer, visual-director]
---

# Seed discipline

## The rule

**Every generation records its seed. No exceptions, including rejected renders.**

A seed is the difference between "we made this image" and "we can explain and remake
this image". It costs nothing to record and cannot be recovered afterwards.

## Why rejects matter too

A rejected render tells you something a kept one does not: this seed, with this
prompt, produces the wrong thing. Recorded in `runs[]` with `outcome: rejected` and a
note, it stops the same dead end being re-explored by someone else — or by you, three
weeks later.

Across a season this is the difference between a prompt library that accumulates and
one that improves.

## Seeds and continuity

Seeds are one of four continuity tools and the weakest of them on its own:

| Tool | Holds | Strength |
|---|---|---|
| **Style anchors** | Overall look | Strongest. Fixed reference files with checksums, referenced by ID. |
| **Structure references** | Composition and geometry | Strong. Depth/pose/edge conditioning matches a storyboard frame reliably. |
| **Character references** | Identity across shots | Moderate. Degrades with angle and lighting change. |
| **Seeds** | Micro-detail within one prompt | Weak alone. A seed does not transfer meaning between different prompts. |

A common error is expecting a seed to carry a character between shots. It will not.
Seed-locking is for varying *one* prompt slightly and keeping everything else stable —
same subject, small change to light or lens.

## Practical patterns

**Exploration** — random seeds, wide batch, record every one. Cheap, and the
rejections are data.

**Refinement** — lock the seed, vary one prompt field at a time. This is the only way
to learn what a field actually does on a given model, and the finding goes in the
vendor cheat sheet.

**Sequence coherence** — same seed, same style anchor, same lens, varying only
subject position and camera. Holds better than varying seeds, though not perfectly.

**Regeneration after a note** — same seed, minimal prompt change. Changing the seed
and the prompt together means you cannot attribute the difference to either.

## Reproducibility is not guaranteed

Same seed and same prompt reproduce the same output **only** on the same model
version, with the same parameters, and often only on the same backend. Vendors
silently update models. This is not a reason to skip recording seeds; it is a reason
to also record `model`, `version`, and the full parameter set — which the manifest
schema requires.

Where a shot is load-bearing and expensive, keep the output file. Provenance lets you
explain a shot; it does not always let you rebuild it.

## Deterministic seeding

For scripted batches, derive seeds from the card ID so a run is reproducible without
a stored seed table:

```
seed = crc32(f"{prompt_card_id}:{run_index}") % 2**31
```

Derived seeds are still written to `runs[]`. The derivation is a convenience, not a
substitute for the record — the derivation function itself can change.

## Anti-patterns

| Pattern | Why it hurts |
|---|---|
| "I'll note the seed if the render is good" | Rejections carry the most information |
| Changing seed and prompt together | Attribution becomes impossible |
| Relying on a vendor's history UI as the record | Vendors expire history and change accounts |
| Reusing a seed across different prompts for consistency | Does not work; produces false confidence |
| Not recording seeds for upscales and variations | They are generations too, and they drift |
