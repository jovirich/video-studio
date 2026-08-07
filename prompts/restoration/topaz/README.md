---
title: Topaz
modality: restoration
vendor: topaz
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Topaz

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Upscaling and frame interpolation for both stills and video.

## Weak at

Can invent detail that was not there.

## Control surface

- Model selection per source type
- Upscale factor
- Denoise and sharpen strength
- Frame interpolation

## Gotchas

- Upscaling archival material invents plausible detail. On genuine archival footage this is an evidentiary act — log it, keep the original, and consider whether it should be done at all.
- On generated material it is routine and still logged.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: topaz
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
