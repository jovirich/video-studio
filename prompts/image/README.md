---
title: Image generation
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# Image generation

The still is the foundation of almost every generated shot. Most video chains start
from a still that has already been reviewed, graded, and approved — because it is far
cheaper to iterate on a frame than on a clip, and because a reviewed still is
something a gate can actually assess.

See [../chains/still_to_motion.md](../chains/still_to_motion.md).

## Vendor comparison

Verify against each vendor's cheat sheet before relying on this; the field moves.

| Vendor | Strongest at | Weakest at | Control surface |
|---|---|---|---|
| [midjourney](midjourney/) | Aesthetic coherence, texture, light quality | Prompt adherence at detail level; text | Style refs, character refs, weights |
| [flux](flux/) | Prompt adherence, anatomy, legible text | House aesthetic is plainer | Open weights, LoRA, ControlNet |
| [stable-diffusion](stable-diffusion/) | Total control; runs locally | Requires assembly and tuning | Full ControlNet, LoRA, inpainting |
| [ideogram](ideogram/) | Text rendering in image | Photoreal texture | Text-focused controls |
| [firefly](firefly/) | Commercially-licensed training data | Conservative outputs | Adobe ecosystem integration |
| [imagen](imagen/) | Photoreal, strong adherence | Ecosystem-bound | Google stack |
| [dall-e](dall-e/) | Instruction following, conversational iteration | Fine aesthetic control | Chat-driven |
| [recraft](recraft/) | Vector, brand-consistent graphics | Photoreal scenes | Style sets |
| [leonardo](leonardo/) | Trained style consistency | Peak fidelity | Custom model training |

**Choose by what a shot needs, not by preference.** A production commonly uses two:
one for photoreal scenes, one for graphics and text. Both are recorded per card.

## Craft, common to all of them

### Specificity beats adjectives

Models resolve concrete nouns far better than evaluative adjectives. "Mud-brick wall,
weathered, with visible straw temper" produces a wall. "Ancient impressive wall"
produces a stock image of the idea of a wall.

### Period markers do the heavy lifting

A model's prior is a blurry average of everything it saw. Left unconstrained it
produces a generic, placeless composite that is subtly wrong everywhere and obviously
wrong to anyone who knows the subject. Concrete material detail is the only reliable
counter. See [../_framework/prompt_anatomy.md](../_framework/prompt_anatomy.md).

### Light before composition

Get the light right and a mediocre composition still reads as photography. Get the
composition right with implausible light and it reads as a render. State source,
direction, quality, and time of day, and keep them consistent across a sequence.

### Resist the default look

Most image models default toward: shallow depth of field, golden hour, symmetrical
composition, high micro-contrast, and a warm grade. Together these are the "AI look".
Every one of them is a choice you can override, and overriding them is most of what
separates cinematic output from generated output.

### Hands, crowds, and text

Still the reliable failure points. Mitigations: keep hands occupied with a described
object; keep crowds mid-ground or further; put deliberate text in as a graphics layer
in post rather than asking the model for it, unless using a text-specialist model.

### Aspect ratio is decided once

Generate at the production's primary ratio. Vertical variants are crops of the
approved master, never separate generations — a second generation guarantees
continuity drift and doubles the review surface.

## Continuity toolkit, strongest first

1. **Style anchors** — fixed reference files with checksums, in
   [../../library/style_refs/](../../library/style_refs/), referenced by ID from every card.
2. **Structure conditioning** — depth, edge, or pose maps from the storyboard frame.
   The most reliable way to make a generation match an approved composition.
3. **Character references** — for recurring figures. Degrades with angle and light change.
4. **Seeds** — micro-variation only. See [../_framework/seed_discipline.md](../_framework/seed_discipline.md).

## QC before a still is accepted

- [ ] Anatomy: hands, limbs, eyes, consistent count of people
- [ ] No garbled pseudo-text anywhere in frame
- [ ] Anachronism pass complete and recorded
- [ ] Light has a plausible source and direction, consistent with the scene
- [ ] Skin-tone rendering correct across everyone in frame
- [ ] Style anchor honoured
- [ ] Resolution native, or upscale logged as a post-process step
- [ ] Provenance class assigned; label applied if the pack requires it
- [ ] Prompt card and seed recorded in the manifest
