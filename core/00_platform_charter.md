---
doc: core/00
title: Platform charter
status: active
version: 0.2.0
updated: 2026-08-07
owners: [platform-owner]
---

# 00 — Platform charter

## 1. What this is

**video-studio** is a production platform for AI-assisted film and video. It is not
a show, and it is not a single studio. It is the engine, the standards, and the
tooling that any number of studios run on.

The first studio built on it is **African History Studio**, whose first production
line is **Nigeria**. Neither of those facts is baked into the platform.

## 2. The four tiers

```
PLATFORM        video-studio/
  the engine    core canon, canon packs, schemas, prompt library, templates,
                automation, shared library, rights registers, ops framework
      │
      ▼
STUDIO          studios/african-history/
  the brand     declares which canon pack it runs, adds its own bible and brand,
                owns its production lines
      │
      ▼
LINE            studios/african-history/lines/ng-nigeria/
  the strand    a coherent body of work — a region, a season strand, a series.
                Owns its research, sources, entities, language, advisory, style.
      │
      ▼
PRODUCTION      .../productions/S01E01_slug/
  the unit      one episode, film, short, or piece. Eleven pipeline stages.
```

Each tier answers one question:

| Tier | Question |
|---|---|
| Platform | How is any video made here, safely and traceably? |
| Studio | What kind of work is this, and by what editorial standard? |
| Line | What body of material does this strand cover, and who advises on it? |
| Production | What is this specific piece, and has it passed its gates? |

## 3. Canon packs

A **canon pack** is the genre-specific editorial rulebook a studio adopts. It supplies
what core deliberately omits: evidence standards, narrative doctrine, visual and
sonic language, sensitivity procedure, localisation policy, and the gate set.

| Pack | For | Status |
|---|---|---|
| [documentary-history](../packs/documentary-history) | Historical documentary. Heavy evidence chain, nine gates, advisory authority. | active |
| `_TEMPLATE_pack` | Skeleton for authoring a new pack | template |

Packs that would be authored the same way, when needed: narrative fiction, brand and
corporate film, explainer and educational, music and performance, promotional.

**A new genre does not require a new repository or a refactor.** It requires a pack.
This is the load-bearing claim of the architecture and is tested in
[../ROADMAP.md](../ROADMAP.md) Phase 6.

## 4. Spinning up new work

| You want to… | You do | Touches |
|---|---|---|
| Make another episode of Nigeria | `studio_ops new-production --line ng-nigeria` | the line only |
| Open Ghana inside African History Studio | `studio_ops new-line --studio african-history --code gh-ghana` | that studio only |
| Start a completely different show, same genre | `studio_ops new-studio --code <x> --pack documentary-history` | studios/ only |
| Start a different *kind* of video entirely | `studio_ops new-pack --code <genre>` then `new-studio --pack <genre>` | packs/ + studios/ |

Nothing on that table requires changing `core/`, `standards/`, `prompts/`,
`templates/`, or `automation/`. If it ever does, that is an architecture finding and
it goes in [../docs/architecture/evolution.md](../docs/architecture/evolution.md).

## 5. What the platform guarantees

Regardless of studio or genre, every production on this platform:

1. **Is traceable.** Every asset has a provenance record. Nothing enters an edit
   without one.
2. **Is disclosed.** Generated material is labelled, in-frame and in metadata.
3. **Is cleared.** Nothing ships with a rights status of `pending`.
4. **Is gated.** A human signs each gate. No path exists from generation to
   publication without signatures.
5. **Is reproducible.** Prompt cards, seeds, and parameters are recorded, so a shot
   can be regenerated or explained years later.
6. **Is accessible.** Captions on every deliverable; contrast and legibility checked.

These are the platform's product. Everything else is a pack's business.

## 6. What the platform refuses

Enumerated in [01_provenance_and_ai_disclosure.md](01_provenance_and_ai_disclosure.md) §2
and binding on every studio. In summary: no fabricated evidence, no unconsented
likeness or voice, no autonomous publication, no passing generated material off as
found material.

A studio may not adopt a pack that loosens these. A pack that tried would fail
validation.

## 7. Governance

| Role | Scope |
|---|---|
| **Platform Owner** | Core canon, schemas, tooling, pack approval |
| **Pack Owner** | One canon pack |
| **Showrunner** | One studio |
| **Line Lead** | One production line |

Role definitions and the responsibility matrix are in [../ops/roles.md](../ops/roles.md).
Where a studio is small, one person may hold several of these — except across gates
on the same production, which is prohibited by
[04_review_gate_framework.md](04_review_gate_framework.md) §5.

## 8. Naming

The repository is `video-studio`. The platform is unbranded on purpose. Studios carry
the brands — *African History Studio* is a studio name, not the platform's, and
nothing in `core/`, `standards/`, `prompts/`, or `automation/` should ever mention it.

If platform-level material starts referring to African history, the tiers are leaking.
That is the failure signal recorded in the evolution log.
