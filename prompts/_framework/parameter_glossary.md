---
title: Parameter glossary
status: active
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer]
---

# Parameter glossary

Cross-vendor concepts. Names differ by tool; the underlying mechanics mostly do not.
Vendor-specific spellings, ranges, and defaults live in each vendor's cheat sheet —
those change often, this does not.

## Sampling and adherence

| Concept | Also called | What it does | Practical note |
|---|---|---|---|
| **Guidance scale** | CFG, prompt adherence, guidance | How strictly the model follows the prompt vs. its own priors | Too high produces over-saturated, over-contrasted, brittle images. Mid-range almost always beats maximum. |
| **Steps** | iterations, sampling steps | Denoising iterations | Past a model-specific point, more steps cost money and change nothing. Find that point once per model and record it. |
| **Sampler** | scheduler, solver | The denoising algorithm | Affects texture and fine detail more than composition. Fix one per production for consistency. |
| **Seed** | — | Initialises noise; makes a render reproducible | **Always recorded.** See [seed_discipline.md](seed_discipline.md). |
| **Stylisation** | style strength, raw mode | How much house aesthetic the model applies | Documentary work generally wants this low. High stylisation is where "AI look" comes from. |

## Conditioning

| Concept | Also called | What it does |
|---|---|---|
| **Image reference** | img2img, image prompt, reference image | Uses an image as a starting point or a target |
| **Style reference** | style ref, sref, IP-adapter | Transfers look without transferring content. The primary continuity tool. |
| **Character reference** | cref, character consistency, identity lock | Holds a face or figure consistent across shots |
| **Structure reference** | ControlNet, depth, canny, pose, composition ref | Constrains geometry while leaving appearance free. The most reliable way to match a storyboard frame. |
| **Denoise strength** | image weight, transformation strength | How far from the input the output may travel |
| **Inpainting / outpainting** | vary region, generative fill/expand | Regenerate part of an image, or extend the frame |

**Rights note:** any third-party image used as a reference is a rights event. The
card's `inputs[].rights_note` is required for third-party material, and feeding
uncleared material to a model can breach both the source agreement and the vendor
terms.

## Output shape

| Concept | Notes |
|---|---|
| **Aspect ratio** | Compose in the production's primary ratio. Vertical variants are crops of a 16:9 master, never separate generations — a second generation guarantees continuity drift. |
| **Resolution** | Generate at the model's native competence, then upscale deliberately. Forcing a model past its native resolution produces duplicated features. |
| **Batch / variations** | Cheap exploration. Every kept variation gets its own asset record; discarded ones are recorded as `rejected` on the card so the same dead end is not re-tried. |
| **Tiling / seamless** | For textures and matte extension only. |

## Video-specific

| Concept | Notes |
|---|---|
| **Duration** | Most models degrade after a few seconds. Plan cuts around the model's reliable length rather than fighting it. |
| **Motion strength / amount** | Higher values increase drift, morphing, and identity loss. Documentary work usually wants restraint. |
| **Start / end frame** | Conditioning on a generated still is the most controllable path to motion, and is the basis of most chains in [../chains/](../chains/). |
| **Camera control** | Explicit pan / tilt / dolly / orbit. Prefer this over describing movement in prose — prose movement is interpreted loosely. |
| **Frame rate** | Native rate is recorded; conform to the delivery rate is a separate, logged step. |
| **Loop / extend** | Extending compounds drift. Two shorter clips with a cut generally beat one extended clip. |

## Audio-specific

| Concept | Notes |
|---|---|
| **Stability / variance** | Low variance is consistent and flat; high variance is expressive and unpredictable. Long-form narration usually wants moderate. |
| **Similarity / clarity** | How closely a cloned voice tracks its reference. Very high can reproduce reference artefacts. |
| **Style exaggeration** | Amplifies delivery. Small values only for documentary narration. |
| **Speaker boost / enhancement** | Processing that can subtly change timbre — log it as a post-process step. |
| **Pronunciation control** | Phoneme tags, IPA, SSML, or lexicon files. **Required** for any proper noun. Never trust default pronunciation of a name. |

## What the platform always records

Whatever the vendor calls them, the manifest records: `vendor`, `model`, `version`,
`seed`, the full `parameters` object as sent, `inputs`, `generated_at`,
`generated_by`, and `cost_usd`.

Vendor parameter names are deliberately unconstrained in the schema —
`parameters` is `additionalProperties: true` — because constraining them would mean
a schema change every time a vendor ships a feature. The cheat sheets carry the
documentation; the manifest carries the truth of what was actually sent.
