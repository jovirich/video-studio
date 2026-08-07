---
title: Architecture
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner, pipeline-engineer]
---

# Architecture

## The documents

| Document | Answers |
|---|---|
| This file | What is the current shape, and what is the contract? |
| [evolution.md](evolution.md) | How did it get this shape, what did each move cost, and what should we watch for? |
| [spinning_up.md](spinning_up.md) | I want to make a different kind of video — which tier is it, and what do I run? |
| [refinements_before_episode_one.md](refinements_before_episode_one.md) | What is genuinely weak or undecided, and what does each weakness block? |
| [../decisions/](../decisions/) | What was decided, given what options, and how would we know it was wrong? |

Read this file for the contract, `evolution.md` for the reasoning, `spinning_up.md`
for the practice.

## The four-tier model

```
PLATFORM        video-studio/
  the engine    core canon · canon packs · schemas · prompt library · templates
                automation · shared library · rights registers · ops framework
      │
      ▼
STUDIO          studios/<code>/
  the brand     declares exactly one canon pack; adds its own bible and brand;
                owns its production lines
      │
      ▼
LINE            studios/<code>/lines/<line>/
  the strand    a coherent body of work — a region, a series, a season strand.
                Owns its research, sources, entities, language, advisory, style.
      │
      ▼
PRODUCTION      .../productions/<code>/
  the unit      one episode, film, or short. Eleven pipeline stages, gated.
```

Each tier answers exactly one question, and that is the placement test:

| Tier | Question | Placement test |
|---|---|---|
| Platform | How is any video made here, safely and traceably? | Would this rule still be right for a production with **no historical claims at all**? |
| Studio | What kind of work is this, and by what editorial standard? | Is it right for one **brand and mission**? |
| Line | What material does this strand cover, and who advises on it? | Is it about **one region or strand**? |
| Production | What is this specific piece, and has it passed its gates? | Is it about **one piece**? |

Between platform and studio sits the layer that makes the platform genre-neutral: a
**canon pack** ([`packs/`](../../packs/)) holds what is true of a *genre* — evidence
standards, narrative doctrine, visual and sonic language, sensitivity procedure,
localisation, and the gate **set**. [`core/`](../../core/) holds only what is true of
*any* production, including the gate **framework**: what a gate is, how it blocks,
how re-opening cascades, and separation of duties
([core/04](../../core/04_review_gate_framework.md)).

A studio declares one pack. That declaration determines what its productions are held
to. Forcing a brand film through an evidence chain produces theatre; letting a
history documentary skip one produces something worse.

## The `arch-2` structural contract

`arch-2` is the current version of the repository's *structural* contract, versioned
independently of its content. Five clauses:

| # | Clause | What breaks without it |
|---|---|---|
| 1 | **Four tiers, in order.** Platform → studio → line → production. No tier is skipped and none is added locally. | Line-specific material lands at studio level and the second line inherits assumptions that do not hold. |
| 2 | **A studio declares exactly one pack**, and the pack supplies its gate set as data (`gates.yaml`). | A production can exist with an undefined or negotiated gate set, which means gates become opinion. |
| 3 | **Precedence is `core > pack > studio > line > production`.** A lower layer may add constraints and tighten upper ones. It may never loosen one. | Exemptions accumulate at the bottom, where the deadline pressure is, and canon becomes a suggestion with paperwork. |
| 4 | **The platform is unbranded.** Nothing in `core/`, `standards/`, `prompts/`, `templates/`, or `automation/` names a studio or its subject matter. | The tiers leak. `grep -ri "african\|nigeria" core/ standards/ prompts/ templates/ automation/` returning anything is the failure signal. |
| 5 | **Spinning up new work touches no platform file.** `new-production`, `new-line`, `new-studio`, `new-pack` each touch only their own tier and below. | The abstraction is in the wrong place, and the finding goes in [evolution.md](evolution.md) rather than being worked around. |

Clause 5 is the load-bearing claim of the whole architecture and is deliberately
*untested* — it is [ROADMAP.md](../../ROADMAP.md) Phase 6, where a second line, a
second studio, and a second pack each try to break it.

A new `arch-N` is declared only when a change invalidates existing records or breaks
the folder contract. Everything smaller is an appended entry in the evolution log
without a version bump.

## Where the contract is enforced

Not all of it is, yet, and the difference matters:

| Clause | Enforcement | Maturity |
|---|---|---|
| Root and directory shape | `validate --root-hygiene` against `ROOT_DIRS` / `ROOT_WHITELIST` in [../../automation/studio_ops/paths.py](../../automation/studio_ops/paths.py) | **IMPLEMENTED** |
| Cross-tier links resolve | `validate --links` | **IMPLEMENTED** |
| Records match their schema | `validate --schemas` | **IMPLEMENTED** — including `pack.yaml` and `studio.yaml`, the two control records that carry clause 2 |
| Pack declares a complete, non-loosening gate set | `validate --packs` | **NOT BUILT** — a schema checks a pack's shape, not whether its declared checklists and documents exist |
| No person signs two gates on one production | `validate --canon` | **NOT BUILT** |
| Clause 5 — expansion touches no platform file | ROADMAP Phase 6, by hand | **NOT RUN** |

The honest per-capability account is [../status.md](../status.md); the open
weaknesses and what each one blocks are in
[refinements_before_episode_one.md](refinements_before_episode_one.md).

## How this shape came about

Briefly, because [evolution.md](evolution.md) has it properly:

- `arch-1` — studio → line → episode. Fixed the region problem
  ([ADR 0001](../decisions/0001-studio-not-show.md)). Left *genre* fused to the
  platform, so the repository root was still a historical-documentary studio.
- `arch-2` — platform → studio → line → production, with canon packs
  ([ADR 0005](../decisions/0005-platform-and-canon-packs.md)). Two tiers inserted,
  `bible/` split three ways, ~30 files moved, all cross-links rewritten, before any
  production existed.

The trigger for `arch-2` was a question rather than a defect: *what happens when we
want to make something that is not this?* That is the only class of question that
finds this kind of error while it is still cheap.

## Changing the architecture

1. Write an ADR — [../decisions/0000-template.md](../decisions/0000-template.md).
   Name the negative consequence and the falsification signal, or it is a preference
   rather than a decision.
2. Append an `AE-NNN` entry to [evolution.md](evolution.md). Never edit an existing
   entry; supersede it with a `revision` or `reversal`.
3. Bump `arch-N` only if records are invalidated or the folder contract changes.
4. If `paths.py` changed, update [../../CONTRIBUTING.md](../../CONTRIBUTING.md)
   § File placement in the same commit — the whitelist is stated in both places and
   they must agree.
</content>
