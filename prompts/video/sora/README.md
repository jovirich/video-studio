---
title: Sora
modality: video
vendor: sora
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Sora

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Complex multi-element scene coherence over longer durations.

## Weak at

Precise shot-level control.

## Control surface

- Text-to-video and image-to-video
- Duration
- Remix and extend
- Storyboard-style sequencing

## Gotchas

- Extending compounds drift. Two shorter clips with a cut usually beat one extended clip.
- Strong for establishing and atmospheric shots; less so where a specific action must land on a frame.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: sora
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
