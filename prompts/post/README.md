---
title: Post-production
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, audio-lead, pipeline-engineer]
---

# Post-production

Edit, grade, graphics, mix, captions, delivery. Where generated material becomes a
production — and where the platform's guarantees are either honoured or quietly lost.

## Vendors

| Vendor | For |
|---|---|
| [resolve](resolve/) | Grade, conform, finish, mix, deliver. The colour-managed spine. |
| [premiere](premiere/) | Editorial and captions, Adobe ecosystem |
| [after-effects](after-effects/) | Motion graphics, maps, data graphics, the label overlay |
| [descript](descript/) | Transcript-driven rough assembly and caption drafting |
| [capcut](capcut/) | Social cutdowns and vertical variants |

## Four project-structure rules

These are set up **once, before the first cut**. Each is cheap now and expensive to
retrofit.

### 1. Text lives in its own layers

Titles, lower thirds, map labels, quotations, and the reconstruction mark are
separate layers, never baked into a shot. A textless master then becomes a render
rather than a rebuild, and localisation stays affordable.

### 2. The show LUT is the spine

One LUT per production, versioned in [../../library/luts/](../../library/luts/). Shot
grading works **under** it, never around it. A shot graded to look right without the
LUT will not survive the LUT being applied.

### 3. Stems are structural, not a delivery afterthought

Build the mix so that VO, testimony, music, ambience, SFX, and **M&E** fall out as
separate stems. Retrofitting an M&E stem when a localisation deal appears costs more
than producing it correctly from the start.

### 4. Every clip in the timeline traces to a manifest entry

The conform step checks it. An asset that reached the timeline without a provenance
record cannot be explained later, and by picture lock nobody remembers where it came
from.

## The conform step

```bash
# NOT BUILT — these commands do not exist yet. See docs/status.md.
python -m studio_ops pipeline conform --production <code>
```

Checks that every timeline clip resolves to a manifest asset; that generated assets
carry prompt card, seed, and tool version; that reconstruction-class assets carry an
evidence basis; that rights status is not `pending`; and that required labels are
applied.

**It refuses to pass an untracked file.** That refusal is the mechanism behind the
platform's traceability guarantee — everything else is documentation.

## Captions

Auto-generate, then **correct against the script and the VO record sheet**. Never
ship an uncorrected auto-caption: proper nouns are exactly what auto-transcription
gets wrong, and they are exactly what a regional audience notices.

Spec in [../../standards/delivery_specs.md](../../standards/delivery_specs.md)
§ Captions. Validate before delivery — malformed timing and dropped diacritics are
the common failures.

## Cutdowns

Vertical and square variants are **crops of the approved master**, using the safe
zones marked at storyboard. Never separate generations — a regenerated vertical
version drifts from the master and doubles the review surface.

A short-form piece that makes a claim absent from a gated production has bypassed the
entire review system. If a short deserves to exist on its own, it goes through the
gates on its own.

## Descript caution

Transcript-driven editing makes removing a hesitation and removing a qualification
equally easy — one keystroke each. The first is fine; the second changes meaning.

Never apply voice-synthesis editing (word replacement, overdub) to a contributor's
testimony. Edits within a testimony answer are marked visually with a cut, not hidden
behind a seamless splice.

## Delivery

Build export presets from
[../../standards/delivery_specs.md](../../standards/delivery_specs.md) once, and use
them. Hand-set exports drift, and the drift is invisible until a distributor rejects
a master.

```bash
# NOT BUILT — these commands do not exist yet. See docs/status.md.
python -m studio_ops pipeline package --production <code>
```

Assembles the delivery package: masters, web renders, stems, captions, artwork,
documents, and the frozen manifest whose hash is embedded in the media metadata.
