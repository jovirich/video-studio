---
title: Video generation
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# Video generation

The expensive, least controllable, most improved-per-quarter part of the pipeline.
Assume anything specific here is out of date and check the cheat sheets.

## The governing constraint

**Every model degrades with duration.** Identity drifts, geometry morphs, physics
decays. The competent response is not to fight it with longer generations but to
**plan cuts around each model's reliable length**.

This is a storyboarding decision, not a generation decision, and making it late is
expensive. A sequence designed as six four-second shots will look better and cost
less than one designed as two twelve-second shots, on every model available.

## Vendor comparison

| Vendor | Strongest at | Notes |
|---|---|---|
| [runway](runway/) | Control surface, motion brush, camera controls, mature tooling | Broad ecosystem including act/performance transfer |
| [kling](kling/) | Motion realism, human movement, longer coherent takes | |
| [veo](veo/) | Prompt adherence, physical plausibility, native audio | Google stack |
| [sora](sora/) | Complex scene coherence, longer durations | |
| [luma](luma/) | Fast iteration, keyframe control, good start/end frame handling | |
| [pika](pika/) | Effects, stylised motion, quick turnaround | |
| [hailuo](hailuo/) | Subject consistency, strong image-to-video | |
| [wan](wan/) | Open weights; local and customisable | Where terms or privacy require self-hosting |
| [seedance](seedance/) | Multi-shot coherence | |
| [higgsfield](higgsfield/) | Camera-move presets and control | |

## Craft

### Image-to-video, nearly always

Text-to-video hands composition, light, palette, and subject to the model at once.
Image-to-video hands it a frame that has already been reviewed, graded, and approved,
and asks only for motion.

This is the single highest-leverage habit in the pipeline. It also means the
sensitivity and anachronism gates operate on a still, which is far easier to assess
than a clip.

### Motion is motivated or it is absent

Unmotivated camera drift on every shot is *the* signature of generated video. Roughly
a third of shots should be locked. When the camera moves, the shot record states why.

### One action per clip

Motion models handle one clear action well and three poorly. "A woman lifts a vessel"
works. "A woman lifts a vessel, turns, and walks toward the doorway as a child enters"
produces mush. Split it, or cut around it.

### Use explicit camera control where offered

Structured pan / tilt / dolly / orbit parameters are interpreted far more reliably
than the same movement described in prose. Prefer the parameter; record it.

### Physics is where it breaks

Water, fire, cloth, hair, granular materials, and crowd interaction are the reliable
failure points. Frame to avoid them, keep them brief, or hand them to a specialist
tool. Fire in particular tends to read as convincing for about two seconds.

### Generate long, cut short

Generate more than the cut needs and take the stable middle. The first and last
frames are frequently where artefacts live.

## Conform

Models output at their own native rate and duration. Every clip is conformed to the
delivery rate, and the method — `native`, `retime`, `frame-blend`, `optical-flow` —
is recorded on the asset record. Optical-flow retiming introduces artefacts that
survive grading and is checked at picture lock.

See [../../standards/delivery_specs.md](../../standards/delivery_specs.md) § Picture.

## Cost discipline

Video generation is where a budget disappears. Controls:

- `GENERATION_BUDGET_USD_PER_EPISODE` is a hard ceiling; adapters refuse past it.
- Cost per run is recorded on the prompt card, so cost per finished second is
  knowable rather than guessed.
- **Approve the still first.** Never iterate on motion to fix a composition problem.
- Rejected runs are recorded with a reason, so the same expensive dead end is not
  re-explored.

## QC before a clip is accepted

- [ ] Temporal stability: no flicker, morph, or identity drift across the clip
- [ ] Anatomy holds through the whole clip, not only frame one
- [ ] Motion is motivated and matches the shot record
- [ ] Physics plausible for water, fire, cloth, hair, crowds
- [ ] No frame introduces an anachronism the still did not have
- [ ] First and last frames usable, or trim points identified
- [ ] Conform method recorded
- [ ] Provenance class, label, prompt card, and seed in the manifest
