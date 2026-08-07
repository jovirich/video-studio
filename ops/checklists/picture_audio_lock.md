---
title: Picture and audio lock gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# Picture and audio lock — checklist

| | |
|---|---|
| **Gate key** | `picture_audio_lock` |
| **Owner** | `visual-director` |
| **Stage** | `06_edit` and `07_audio_post` |
| **Blocks** | `09_delivery` |
| **Packs** | narrative, product-marketing, fashion-film |
| **Completed copy** | `06_edit/checklists/picture_audio_lock.md` in the production folder |

Three packs combine picture and audio into one gate because their audio risk is lower
than documentary's — no evidentiary soundscape, no pronunciation obligation that
decides regional trust. Documentary-history keeps them separate:
[picture_lock.md](picture_lock.md) and [audio_lock.md](audio_lock.md).

Combining them concentrates a lot of certification in one signature. Read the whole
list; the temptation with a combined gate is to sign it on the picture and assume the
audio.

## What this signature certifies

> *narrative:* The cut is final. A continuity pass has been run across every recurring
> element — face, costume, prop, geography, time of day, weather. No temporal artefacts
> survive. Mix is in spec.
>
> *product-marketing:* The cut is final. Every product-interface shot is captured, not
> generated. Brand assets are current versions. Loudness and safe areas are in spec.
> Vertical and square crops hold.
>
> *fashion-film:* The cut is final. Colour is accurate to the physical garments under
> the show LUT. Styling continuity holds across the cut. Music is cleared. Vertical and
> square crops hold without cropping the garment out of frame.

## Checks — all packs

### Picture, per generated shot

- [ ] Anatomy: hands, limbs, eyes, and the count of people correct and consistent across the shot
- [ ] Text in frame: no garbled pseudo-script; any lettering is deliberate and correct
- [ ] Light direction consistent within the scene
- [ ] Skin-tone rendering correct across the full range of people shown, and not crushed or desaturated by the show LUT
- [ ] Temporal stability: no flicker, morph, or drift across the clip
- [ ] Style anchor referenced and honoured
- [ ] Prompt card, seed, and provenance class recorded in the manifest

### The cut

- [ ] The cut is final. Not "final pending notes"
- [ ] Frame rate conform correct on every generated clip; conform method recorded
- [ ] Optical-flow retiming artefacts checked for specifically
- [ ] Aspect discipline holds; ratio changes are deliberate devices, not tool defaults
- [ ] Shot-level grading works under the show LUT, never around it
- [ ] Title safe 90%, action safe 93%
- [ ] **9:16 and 1:1 safe zones hold** — no critical information outside either. Vertical variants are crops, not re-generations
- [ ] On-screen text ≥ 1/20 frame height for body copy; contrast ≥ 4.5:1 measured
- [ ] Text on separate layers, so a textless master is a render and not a rebuild

### Audio

- [ ] Integrated loudness on target per variant: −14 LUFS streaming, −23 LUFS ±0.5 broadcast
- [ ] True peak ≤ −1.0 dBTP; loudness range 6–12 LU
- [ ] Dialogue/VO seated at −18 to −12 LUFS short-term and intelligible over the bed
- [ ] All required stems rendered, full length, sample-accurate — including **M&E**
- [ ] Every music cue is in the cue sheet, including original score
- [ ] Composition and recording rights recorded separately for licensed cues
- [ ] No synthesised voice of a real person without documented consent — including of a historical figure, for whom no consent is possible
- [ ] Generated audio assets present in the provenance manifest
- [ ] Mix checked on a phone speaker as well as monitors
- [ ] Audio conformed to the final picture, not an earlier cut

## Pack-specific

### narrative — the continuity pass

Generative tools have no memory. Across a long sequence, faces, costumes, props,
geography, time of day, and weather drift unless something external holds them. This
is the gate where the anchors set at continuity lock are verified to have held.

- [ ] **Face**: every recurring character reads as the same person in every appearance
- [ ] **Costume**: garment, colour, wear state, and accessories consistent within a scene and correct across the timeline
- [ ] **Props**: recurring objects consistent in form and condition; a prop that ages does so in the right direction
- [ ] **Geography**: a location's layout, scale, and relative positions are the same each time it appears
- [ ] **Time of day and weather** continuous within a scene, and correct across cuts within a sequence
- [ ] No temporal artefacts survive: no flicker, no morph between shots, no drift within a shot
- [ ] Production-level AI disclosure is present in the credits and description
- [ ] **No fabricated document, newsreel, or synthetic archival photograph is presented as real inside the fiction.** This is the boundary that is easiest to cross by accident in a found-footage framing

### product-marketing

- [ ] **Every product-interface shot is captured, not generated.** No exceptions for resolution, cleanup, or "recreated from a design file"
- [ ] Screen recordings show the shipping build
- [ ] Brand assets — logo, wordmark, colour, typeface — are the **current** versions, checked against the brand source rather than against the last project
- [ ] Where speed is compressed for the edit, it is disclosed rather than implied as real-time
- [ ] Vertical and square crops hold without cropping the product or the call to action out of frame
- [ ] Claim substantiation is signed, or every claim in the cut is already listed for it

### fashion-film

- [ ] **Colour is accurate to the physical garments under the show LUT**, checked against the reference capture rather than against memory or the lookbook
- [ ] Texture, drape, closure, and finish match the reference capture in every shot
- [ ] Styling continuity holds across the cut: garment, accessories, hair, and makeup consistent within a look
- [ ] Music is cleared, including composition and recording rights, for every territory in the deliverable set
- [ ] Vertical and square crops hold **without cropping the garment out of frame** — the single most common failure in this pack's cutdowns
- [ ] Synthetic-human disclosure is present on screen where required
- [ ] Garment verification is signed
- [ ] Representation review is signed, and no hold is open

## Do not sign if

- **You checked the picture and assumed the audio.** This is the specific hazard of a
  combined gate, and the reason both lists are above your signature rather than
  someone else's.
- **Any generated shot has not been through the per-shot list.** Sampling is not
  checking.
- **Safe zones were checked on the 16:9 master only.**
- **A continuity break survives because regenerating the sequence is expensive**
  *(narrative)*. It is cheaper now than after audio post and vastly cheaper than after
  publication — which is exactly why continuity is gated before generation.
- **An interface shot was generated** *(product-marketing)*. Recapture it.
- **Garment colour was matched to the lookbook rather than to the reference capture**
  *(fashion-film)*. The lookbook is already a representation.
- **You signed another gate on this production.** Narrative pairs this with
  `continuity_lock` and fashion-film with `garment_verification`, both owned by this
  role — see [../roles.md](../roles.md) §5.1.

## Signature

| Field | Value |
|---|---|
| Role | `visual-director` |
| Person | |
| Date | |
| Shots checked | of |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
