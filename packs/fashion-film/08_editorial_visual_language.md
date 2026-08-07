---
doc: packs/fashion-film/08
title: Editorial visual language
status: template
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# 08 — Editorial visual language

> **Fill state.** The *rules* below are pack canon. The *look* — palette, grade, lens
> character, movement vocabulary — is `TBD` per studio and per season, specified in the
> studio's `style/` folder. A pack that shipped a house look would be prescribing the
> one thing a fashion brand's identity consists of.

Fashion film is the genre on this platform with the most permitted visual invention and
the least tolerance for incoherence. A campaign is not a film; it is a system that
produces dozens of assets, in several ratios, over months, made by different people, and
it must read as one thing. Generative tools make each individual asset easier and the
coherence harder, in the same proportion.

## 1. Look

Specified per season in the studio's `style/` folder, in language a prompt card can
inherit ([../../prompts/README.md](../../prompts/README.md) § Inheritance). What must
be specified — values are TBD, the categories are not:

| Element | Must state |
|---|---|
| **Palette** | Primary, secondary, and one accent with a named function. **Plus the garment-safe rule at §2** |
| **Grade** | One show LUT per campaign, in `library/luts/`, versioned. Shot-level work happens under it, never around it |
| **Lens set** | A fixed, small set. A defined set is the cheapest coherence available and is what makes independently generated shots cut together |
| **Depth of field** | Consistent with the chosen lens and stop. Generative tools default to shallow; shallow hides texture, and texture is the garment |
| **Light** | Quality, direction, and ratio. Light has a source and a direction in every frame and it is consistent within a scene — the platform-wide failure mode ([documentary-history](../documentary-history/04_visual_language.md) §3) |
| **Texture and atmosphere** | Grain, haze, bloom, and their limits. Every one of these degrades fabric read |
| **Typography** | Display and text faces, licensed for the delivery territories, with full diacritic coverage for every language the campaign ships in. Choose before designing — coverage eliminates most faces |
| **Style anchors** | A fixed, versioned, checksummed set in [../../library/style_refs/](../../library/style_refs/), referenced by ID from every prompt card |

**The garment sits above the look.** Where a look choice and garment accuracy conflict,
garment accuracy wins — [05_garment_fidelity.md](05_garment_fidelity.md) §4 verifies on
the graded frame, so a grade that breaks colour tolerance is a grade that fails, not a
tolerance that flexes.

## 2. The garment-safe constraint on look

Three look decisions routinely destroy garment fidelity, and each is worth naming
because each is made by someone who is not thinking about garments at the time.

| Decision | What it destroys | Constraint |
|---|---|---|
| A heavily stylised grade — crushed, tinted, bleached, or heavily saturated | **Colour.** The garment ships one colour and reads another | The show LUT is evaluated against every garment in the campaign before lock, not against a hero frame. Same discipline as the skin-tone evaluation at [06_body_and_representation.md](06_body_and_representation.md) §4 |
| Very shallow focus, heavy diffusion, heavy grain, or aggressive denoise | **Texture.** Weave, knit, pile, and sheen disappear or change | At least one shot per garment holds texture at the resolution of the texture macro. Editorial may show less; it may not show different |
| Extreme motion effects — heavy blur, speed ramps, interpolation | **Drape.** Fabric appears to move with a weight it does not have | Interpolation across garment motion is constrained at [05_garment_fidelity.md](05_garment_fidelity.md) §3. Any retimed garment motion is verified against the movement pass |

## 3. Movement

- **Motivated, and largely still.** A drifting camera on every shot is the signature
  tell of generated video. In fashion it additionally destroys the read of the garment,
  which is the only thing the shot is for.
- **The garment moves, or the camera does.** Rarely both. When both move, neither
  reads.
- **Model movement is directed, not incidental.** How a garment is meant to move —
  where it swings, where it holds, where it settles — is a styling decision recorded
  with the garment's behaviour notes ([05_garment_fidelity.md](05_garment_fidelity.md) §2).
- **Temporal stability is checked per clip.** Flicker, morph, and drift are QC failures,
  and in fashion they show first in fabric and hair.

## 4. Styling coherence across a campaign

The unit of review is the campaign, not the shot. Coherence is held by three
mechanisms, in order of authority:

1. **The campaign system** (§5) — the written specification everything inherits.
2. **Versioned anchors** — style anchors, garment reference captures, character and
   location anchors where figures recur across assets.
3. **Prompt inheritance** — every prompt card inherits its style block from the
   campaign; an override records why.

What is checked across the campaign, not within a shot:

- [ ] Styling is consistent per look — a garment worn one way in one asset and another
      way in another is a continuity error unless the campaign says it is a variation
- [ ] Hair and makeup states are declared per look and hold across every asset in it
- [ ] Accessories, footwear, and layering are recorded per look; a missing belt between
      two assets in the same look reads as an error
- [ ] Grade is identical across assets within a campaign, including cutdowns
- [ ] Representation range holds **across the campaign**
      ([06_body_and_representation.md](06_body_and_representation.md) §2) — this is the
      axis that only exists at campaign scale
- [ ] Skin-tone rendering holds across every asset and every variant
- [ ] Every garment's five properties verify in every asset it appears in

## 5. Campaign systems

A campaign is declared before the first asset, not assembled from what got made.
[pack.yaml](pack.yaml) requires `collection`, `season`, and `deliverable_variants` on
the production record.

**The campaign record states:**

| Field | Why |
|---|---|
| **Collection and season** | Scopes every garment record and every rights term |
| **The looks** — each a named set of garments, styling, hair, and makeup | The unit styling coherence is checked against. Without named looks, "consistent styling" is unreviewable |
| **Garment manifest** — every `GRM` in the campaign | What `garment_verification` walks |
| **Deliverable variants** — every ratio, duration, and surface, declared up front | Composing for variants after the fact is the most expensive rework in this genre |
| **The single idea the campaign carries** | `brief_approval` certifies it ([gates.yaml](gates.yaml)) |
| **Music** and its clearance position | Fashion film routinely gets this wrong ([README.md](README.md)); the cue is chosen and cleared before the edit is built around it, not after |
| **Disclosure obligations** — synthetic human, retouching, per studio policy | So the mark is designed into the frame rather than added over it |
| **Asset version set** | Which versions of brand assets, LUTs, and anchors this campaign is built on |

## 6. Deliverable variants

Every campaign produces a set. They are designed for, not cropped into.

| Requirement | Rule |
|---|---|
| **Declared up front** | At `brief_approval`. Every ratio and surface, named |
| **The garment survives every crop** | `picture_audio_lock` certifies that vertical and square crops hold without cropping the garment out of frame ([gates.yaml](gates.yaml)). A vertical crop that centres on a face and loses the hem has removed the product |
| **Disclosure survives every crop** | A synthetic-human mark cropped out of the 9:16 has removed itself from the version most people will see. This is the most common real failure of a disclosure policy, and it is a delivery failure, not a design one |
| **Colour verifies on every variant** | Codecs, colour spaces, and platform re-encodes move colour — [05_garment_fidelity.md](05_garment_fidelity.md) §4 |
| **Captions on every deliverable** | Core, not negotiable ([../../core/00_platform_charter.md](../../core/00_platform_charter.md) §5 item 6) |
| **Silent-first composition** | Most surfaces autoplay muted. Anything carried only by audio is not carried |
| **Variants inherit their master's approvals** | Cut down from an approved master, never sideways from a work-in-progress. A variant carries the master's garment verification, stakeholder approval, and version set |
| **A variant can break a verification its master passed** | Re-crop, re-grade, and re-encode each touch the five properties. Verification is per variant |

Specs and packaging per
[../../core/03_distribution_and_formats.md](../../core/03_distribution_and_formats.md)
and [../../standards/delivery_specs.md](../../standards/delivery_specs.md).

## 7. How the visual identity is inherited by prompt cards

The mechanism, end to end. This is what makes the rest of the document enforceable
rather than aspirational.

```
campaign system  (look, palette, grade, lens set, movement, typography)
        │  inherited as a style_block
        ▼
sequence / look style block  (this look's styling, light, atmosphere)
        │  inherited
        ▼
prompt card  ──references──►  style anchor IDs        (library/style_refs/)
        │                     garment reference capture (GRM record — required)
        │                     design source IDs        (DSR record, where applicable)
        │                     synthetic_human flag     (where applicable)
        ▼
     shot  ──requires──►  garment_refs
```

Enforced by [pack.yaml](pack.yaml):

```yaml
record_extensions:
  shot:
    require: [garment_refs]
  prompt_card:
    require_reference_capture_for: [garment]
    flag: [synthetic_human]
```

Four rules on inheritance:

1. **A prompt card that overrides an inherited style block records why.** An
   unexplained override is indistinguishable from a mistake six weeks later, and
   usually is one.
2. **Anchors are referenced by ID, never described.** "On brand" is not a
   specification a generative tool can act on; a checksummed file is.
3. **A prompt card touching a garment cannot be written before that garment's
   reference capture exists.** This is why capture is a line-opening condition
   ([05_garment_fidelity.md](05_garment_fidelity.md) §2) — the dependency runs
   backwards from the prompt to the physical object.
4. **Anchor sets are versioned, and a new version lists what was generated against the
   old one.** Superseding silently is how half a campaign ends up in last season's
   grade.

## 8. Inheritance and enforcement

Adds to core; loosens nothing. Delivery, versioning, and archive per
[../../core/03_distribution_and_formats.md](../../core/03_distribution_and_formats.md).
Accessibility and captions per
[../../core/00_platform_charter.md](../../core/00_platform_charter.md) §5. Provenance
on every generated asset, including anchor material that was itself generated, per
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §4.
Music, font, and LUT clearance per
[../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §2 — the
clause fashion film most often discovers late.

| Standard | Gate | Mechanism |
|---|---|---|
| §1, §2 | `picture_audio_lock` | Colour accurate to the physical garments **under the show LUT** |
| §3, §4 | `picture_audio_lock` | Styling continuity holds across the cut and across the campaign |
| §5 | `brief_approval` | Collection, season, looks, deliverable variants, and the single idea declared up front |
| §6 | `picture_audio_lock`, `technical_qc` | Crops hold; disclosure survives every crop; captions present; package assembled per variant |
| §7 | `technical_qc` | Every shot carries `garment_refs`; every garment prompt card carries a reference capture; prompt card and seed in the manifest |

Checklists: [../../ops/checklists/](../../ops/checklists/). Gate definitions: [gates.yaml](gates.yaml).
