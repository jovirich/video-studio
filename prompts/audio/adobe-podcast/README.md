---
title: Adobe Podcast
modality: audio
vendor: adobe-podcast
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Adobe Podcast

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Speech enhancement and restoration of poor recordings.

## Weak at

Not a generation tool.

## Control surface

- Speech enhance
- Noise and reverb reduction
- Level matching

## Gotchas

- Enhancement alters a recording. On interview and archival audio, log it as a post-process step — and never let it change meaning.
- Aggressive enhancement introduces artefacts that sound like a different voice.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: adobe-podcast
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
