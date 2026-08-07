---
title: Restoration and upscaling
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, pipeline-engineer]
---

# Restoration and upscaling

The modality with the sharpest ethical line in the whole library, and the one most
easily crossed by accident.

## The line

**Upscaling invents detail.** That is what it does. A model asked to add pixels adds
plausible pixels — grain that was not there, edges that were never resolved, faces
that were never legible.

On generated material this is routine and unremarkable. On **genuine archival
material it is an evidentiary act**, because the resulting image now shows things the
original does not.

| Material | Permitted | Condition |
|---|---|---|
| Generated stills and clips | Yes | Logged as a post-process step |
| 3D renders | Yes | Logged |
| Contemporary footage you shot | Yes | Logged |
| **Archival photographs and film** | **Restricted** | Non-generative correction only, unless a documented exception |
| **Documents and manuscripts** | **No generative enhancement** | Legibility work is non-generative only |

## Non-generative vs generative correction

The distinction that makes archival work possible at all:

**Non-generative** — levels, contrast, colour balance, dust and scratch removal,
stabilisation, deinterlacing, perspective correction, grain management. These
*reveal* what is present. Permitted on archival material, logged.

**Generative** — upscaling with detail synthesis, face restoration, inpainting,
colourisation, frame interpolation. These *add* what is absent. Not applied to
archival material without a documented exception, and never silently.

[adobe](adobe/) is the recommended tool for archival work precisely because the two
categories are separable in it.

## Colourisation

Deserves its own note. Colourising a monochrome photograph asserts colours the record
does not contain — of skin, textile, dye, paint, and landscape. Every one of those is
a factual claim, and for historical subjects they are frequently claims the evidence
cannot support.

Where a pack permits it at all, it requires: an evidence basis for the colour choices,
an on-screen indication that the image has been colourised, and the original shown or
available. The default position is not to.

## Frame interpolation

Interpolating archival film to a higher frame rate changes the motion character of the
original, which is itself historical information — early film speeds are contested and
the "corrected" version encodes someone's guess. Log it, and prefer showing the
original cadence.

## Vendors

| Vendor | Note |
|---|---|
| [topaz](topaz/) | Upscale and interpolate, stills and video. Model choice matters per source. |
| [magnific](magnific/) | Explicitly synthesises detail. **Never on archival material.** |
| [krea](krea/) | Real-time creative enhancement. Same boundary. |
| [adobe](adobe/) | Non-generative correction, cleanly separable from generative fill. |

## Always

- Keep the original. Restoration is additive to the archive, never a replacement.
- Log every step in the asset's `post_process` array: what was done, with what tool.
- Where the custodian's licence restricts alteration — many do — check before, not
  after. Cropping and colouring are commonly restricted by archive agreements.
- Show the restoration on screen when it is material to what the viewer is being asked
  to see.

## Upscaling generated material

Routine, and still recorded. Two practical notes:

- Upscale **after** the still is approved, not before. Upscaling an image you then
  reject is wasted cost.
- Excessive upscaling produces a characteristic over-detailed, over-sharpened surface
  that reads as artificial. Native resolution plus a modest upscale beats a large one.
