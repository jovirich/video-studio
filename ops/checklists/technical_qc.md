---
title: Technical QC gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer]
---

# Technical QC — checklist

| | |
|---|---|
| **Gate key** | `technical_qc` |
| **Owner** | `pipeline-engineer` |
| **Stage** | `09_delivery` |
| **Blocks** | `10_publish` |
| **Packs** | All four. Required by [../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §8 — no pack may drop it |
| **Completed copy** | `09_delivery/checklists/technical_qc.md` in the production folder |

This is the universal gate. It exists because it is where the platform's own
guarantees — traceable, disclosed, cleared, gated, reproducible, accessible — stop
being claims and get verified. Everything else in a pack is negotiable by genre. This
is not.

## What this signature certifies

> Delivery specs are met, captions validate, the provenance manifest is complete and
> frozen, rights are cleared, disclosure is applied where the pack requires it, and the
> package is assembled with its evidence layer.

## Pack applicability

| Pack | Adds |
|---|---|
| documentary-history | Content Credentials applied where supported; evidence layer generated (sources page, provenance summary, corrections log) |
| product-marketing | Rights cleared **including music and fonts** |
| narrative | Production-level AI disclosure present in credits and description |
| fashion-film | Rights cleared including music and fonts; synthetic-human disclosure present where required; package assembled **per deliverable variant** |

Items marked *(pack)* below apply only under the named pack. Everything else applies
to every production on this platform.

## Checks

### Provenance

- [ ] Every asset in the cut has a manifest entry. No exceptions, including stock, graphics, and fonts
- [ ] Every generated asset records vendor, model, **version**, prompt card ID, seed, parameters, inputs, `generated_at`, and `generated_by`
- [ ] Every `reconstruction`-class asset records its `evidence_basis` *(documentary-history)*
- [ ] No asset carries the `archival` provenance class that was generated
- [ ] Post-process steps are recorded on each asset — upscale, grade, retime, cleanup
- [ ] Generated-clip conform method recorded per asset: `retime`, `frame-blend`, `optical-flow`, or `native`
- [ ] The manifest is **frozen**: its hash is recorded and embedded in the delivered master's metadata

### Labels and disclosure

- [ ] Every `reconstruction` and `interpretive` shot carries the in-frame mark for its full duration *(documentary-history)*
- [ ] The mark sits inside title safe, holds contrast ≥ 3:1, is legible at 360p, and is never obscured by a caption *(documentary-history)*
- [ ] The sequence-level explainer card appears at the first labelled shot *(documentary-history)*
- [ ] Credits name every generative tool used, by category
- [ ] Production-level AI disclosure present in credits **and** description *(narrative)*
- [ ] Synthetic-human disclosure present on screen where a synthetic human appears *(fashion-film)*
- [ ] Content Credentials (C2PA) applied on every deliverable whose platform supports them

### Rights

- [ ] No asset in the manifest has a rights status of `pending`
- [ ] Model terms re-checked at delivery for every vendor used, with the date recorded
- [ ] Cue sheet complete, including original score
- [ ] Font licence tier covers broadcast/streaming use and the seat count actually used
- [ ] LUT, plugin, and stock SFX licences permit commercial redistribution in a finished film
- [ ] Chain of title assembles from the clearance log without gaps

Full category list: [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §2.

### Picture — measured against [../../standards/delivery_specs.md](../../standards/delivery_specs.md)

- [ ] Resolution, frame rate, codec, chroma, bit depth, colour space, transfer, and scan match the spec for each master
- [ ] Frame rate is exactly 24.000p on the documentary body — not 23.976, not 24.0 nominal
- [ ] Video levels legal, 64–940 at 10-bit. No illegal blacks, no superwhites
- [ ] Title safe 90%, action safe 93%
- [ ] 9:16 and 1:1 safe zones hold — no critical information outside either
- [ ] Bitrate meets the floor for each web variant
- [ ] Textless master renders from the separated text layers, not rebuilt

### Audio

- [ ] 48 kHz; 24-bit on masters
- [ ] Integrated loudness on target for each variant: −14 LUFS streaming, −23 LUFS ±0.5 broadcast
- [ ] True peak ≤ −1.0 dBTP on every deliverable
- [ ] Loudness range 6–12 LU
- [ ] Dialogue/VO short-term −18 to −12 LUFS
- [ ] Noise floor ≤ −60 dBFS on narration
- [ ] All six stems present, full length, sample-accurate, one file each: `vo`, `testimony`, `music`, `ambience`, `sfx`, `me`
- [ ] The **M&E stem exists**. It is mandatory from the first production, not when a localisation deal appears

### Captions and text

- [ ] SRT and VTT present per language; TTML where the platform requires styling
- [ ] UTF-8, NFC normalised, no BOM
- [ ] Max 2 lines, max 42 characters per line, 1.0–7.0 s duration, ≤ 20 cps reading speed, ≥ 2 frames between cues
- [ ] Speaker ID present wherever more than one speaker appears
- [ ] Non-speech cues bracketed for accessibility captions
- [ ] Captions repositioned where they would collide with on-screen text
- [ ] Caption files validate against the locked audio, not against an earlier cut
- [ ] On-screen text ≥ 1/20 frame height for body copy; contrast ≥ 4.5:1 **measured**, not eyeballed
- [ ] All diacritics and tone marks present and correctly positioned; no mojibake, no fallback glyphs, no dropped combining marks

### Metadata and package

- [ ] Embedded metadata: title, production code, version, studio, year, copyright, language
- [ ] Provenance manifest hash embedded, so the delivered file ties to the exact record set that produced it
- [ ] Package assembled to the structure in [../../standards/delivery_specs.md](../../standards/delivery_specs.md) § Delivery package
- [ ] `documents/` contains cue sheet, chain of title, credits, provenance summary, sources page, and corrections log
- [ ] Evidence layer generated from records rather than written by hand *(documentary-history)*
- [ ] A package exists per deliverable variant and aspect ratio *(fashion-film)*

## Do not sign if

- **Any asset is in the cut without a manifest entry.** The pipeline is specified to
  refuse this; if you are looking at it, either the refusal did not run or someone
  worked around it. Both are worse than the missing entry.
- **Any rights status is `pending`.** There is no provisional delivery and no
  partial sign-off pending a licence that is "coming".
- **The manifest is not frozen**, or its hash does not match what is embedded in the
  master. An unfrozen manifest means the delivered file cannot be tied to a record set.
- **Any number above was eyeballed.** Loudness, true peak, contrast, and caption
  reading speed are measured values. "Looks fine" is not a measurement, and this gate
  is the last place the difference can still be caught cheaply.
- **Captions were auto-generated and not corrected** against the script and the VO
  record sheet.
- **You signed another gate on this production.**
  [../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §5.
- **Any check above is unticked**, including the ones you believe do not apply. A
  check that does not apply is marked `not-required` with a reason, in the note field.

## Signature

| Field | Value |
|---|---|
| Role | `pipeline-engineer` |
| Person | |
| Date | |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |

Commit this file with the signature. A signature without a committed checklist is not
a signed gate.
