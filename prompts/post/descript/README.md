---
title: Descript
modality: post
vendor: descript
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Descript

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Transcript-driven editing, rough assembly, caption drafting.

## Weak at

Not a finishing tool.

## Control surface

- Transcription
- Text-based rough cut
- Filler-word removal
- Caption export

## Gotchas

- Removing a hesitation is fine. Removing a qualification is an edit to meaning — the transcript view makes both equally easy, which is the risk.
- Never use voice-synthesis editing on a contributor's testimony.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: descript
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
