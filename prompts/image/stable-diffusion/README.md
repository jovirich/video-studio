---
title: Stable Diffusion
modality: image
vendor: stable-diffusion
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Stable Diffusion

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Total control. ControlNet, LoRA, inpainting, regional prompting, local execution.

## Weak at

Requires assembly, tuning, and maintenance. Not a fast path to a first image.

## Control surface

- ControlNet: depth, canny, pose, normal, segmentation — the strongest storyboard-match tool available
- LoRA / adapters for style and character
- Inpainting and outpainting with masks
- Sampler, steps, CFG, scheduler
- Regional prompting for multi-subject frames

## Gotchas

- The correct choice when material must not leave the building — restricted archival scans, unpublished sources.
- Reproducibility depends on the exact model hash, VAE, sampler, and node graph. Record all of it, not just the seed.
- Base-model licence and any fine-tune's licence are separate questions.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: stable-diffusion
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
