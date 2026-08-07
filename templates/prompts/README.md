---
title: Prompt templates — see prompts/_framework and the prompt card
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, pipeline-engineer]
---

# Prompt templates

**The prompt card template is
[../production/04_prompts/_TEMPLATE_card.prompt.yaml](../production/04_prompts/_TEMPLATE_card.prompt.yaml).
The framework and the vendor library are [../../prompts/](../../prompts/). Not here.**

This directory holds no template of its own, and the absence is deliberate: a second
prompt card template would drift from the first, and the two would disagree about a
schema that only one of them tracks.

## Where to go

| You want | Go to |
|---|---|
| To write a prompt card for one generated asset | [../production/04_prompts/_TEMPLATE_card.prompt.yaml](../production/04_prompts/_TEMPLATE_card.prompt.yaml) |
| To understand how a prompt is constructed | [../../prompts/_framework/prompt_anatomy.md](../../prompts/_framework/prompt_anatomy.md) |
| To choose and record seeds properly | [../../prompts/_framework/seed_discipline.md](../../prompts/_framework/seed_discipline.md) |
| A starting negative set | [../../prompts/_framework/negative_library.md](../../prompts/_framework/negative_library.md) |
| What a vendor's parameters mean | [../../prompts/_framework/parameter_glossary.md](../../prompts/_framework/parameter_glossary.md) and the cheat sheet in `prompts/<modality>/<vendor>/` |
| To judge whether an output is usable | [../../prompts/_framework/evaluation_rubric.md](../../prompts/_framework/evaluation_rubric.md) |
| A multi-tool recipe | [../../prompts/chains/](../../prompts/chains/) |
| The schema a card validates against | [../../standards/schemas/prompt_card.schema.json](../../standards/schemas/prompt_card.schema.json) |
| How cards are named | [../../standards/naming_conventions.md](../../standards/naming_conventions.md) § Prompt cards |

## Two scopes of card

| Scope | ID | Lives in | For |
|---|---|---|---|
| **Production** | `PC-XX-S00E00-0000` | that production's `04_prompts/` | One asset in one production |
| **Studio** | `PC-STUDIO-0000` | [../../prompts/](../../prompts/) | A card reusable across productions — a texture, a transition element, a graphic treatment |

A studio-scoped card is promoted from a production one that proved useful. Promotion
is deliberate: it copies the card, gives it a new ID, and strips the
production-specific `target` block. Cards do not become studio-scoped by being used
twice.

## The rule that matters more than any template

**A prompt card is a record, not a text string.** It is versioned, never overwritten;
reviewable before generation; structured so `studio_ops promptlib render` can target
more than one vendor from it; and it carries the evidence a reconstruction is built
from.

Editing a card in place destroys the answer to "why does this shot look different
now", which is a question that gets asked. Bump the version, record what changed and
why, and let git keep the previous one.
