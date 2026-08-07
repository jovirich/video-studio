---
title: Suno
modality: audio
vendor: suno
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Suno

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Full musical pieces from a description, including structure.

## Weak at

Precise control over a specific cue's shape and timing.

## Control surface

- Style and instrumentation prompt
- Structure hints
- Instrumental mode
- Duration

## Gotchas

- Read the pack's music policy before use. Generating a pastiche of a living tradition to avoid paying its practitioners is the failure this tool makes easy.
- Terms on commercial use vary sharply by plan tier. Re-check before every delivery.
- Every cue goes on the cue sheet, generated or not.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: suno
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
