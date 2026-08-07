---
title: Kling
modality: video
vendor: kling
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Kling

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Human motion realism and longer coherent takes.

## Weak at

Fine-grained camera control against Runway.

## Control surface

- Image-to-video and text-to-video
- Motion strength
- Duration presets
- Camera movement presets

## Gotchas

- Strong on people walking, working, and gesturing — the bulk of documentary reconstruction motion.
- Access and terms vary by region; verify the commercial position before relying on it.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: kling
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
