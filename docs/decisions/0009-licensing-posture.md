---
adr: 0009
title: Licensing posture — infrastructure vs productions
status: proposed
date: 2026-08-07
deciders: [platform-owner, showrunner]
supersedes: none
superseded_by: none
---

# ADR 0009 — Licensing posture

> **Status: proposed.** This ADR is open. [LICENSE](../../LICENSE) currently states
> the conservative default (all rights reserved) pending a decision. Resolving this
> is a Phase 1 item on the [roadmap](../../ROADMAP.md).

## Context

The repository holds material under several different regimes, and a single licence
line at root cannot honestly cover all of them:

| Layer | What it is | Natural posture |
|---|---|---|
| Platform engine — `core/`, `standards/`, `prompts/`, `templates/`, `automation/`, `ops/` | Original work by the studio. Schemas, tooling, prompt scaffolding, process. | Could be open |
| Canon packs — `packs/` | Editorial method. Genuinely useful to other producers. | Could be open |
| Studios and lines — `studios/` | Research, scripts, entity records, claims | Proprietary |
| Third-party material | Archival media, interviews, music, fonts, LUTs | Governed individually; the repo licence is irrelevant to them |
| Generated outputs | Vendor terms vary by tool and plan tier | Governed by `rights/permissions/model_terms_register.md` |

The awkwardness is that the repository's most *distinctive* contribution is arguably
the infrastructure and the method — the evidence chain, the prompt-card discipline,
the gate framework — while its commercial value is in the productions.

## Options

**A. All rights reserved throughout.** Current default. Simplest, zero risk, zero
external benefit.

**B. Open the engine and packs; keep studios proprietary.** Permissive licence
(Apache-2.0 or MIT) on `core/`, `standards/`, `prompts/`, `templates/`, `automation/`,
`ops/`, `packs/`. Proprietary on `studios/` and `rights/`.

- *For:* Other producers making AI-assisted documentary face exactly these problems.
  Publishing the method is a credibility asset in a field with a trust deficit, and
  it invites scrutiny of the standards, which strengthens them.
- *Against:* Requires per-directory licence files and discipline about what goes
  where. Contributor agreements need to distinguish the layers.
- *Note:* Apache-2.0 over MIT, for the patent grant and the explicit contribution
  clause.

**C. Open the engine, publish the canon as documentation under CC BY-SA.** As B, but
canon text under a content licence rather than a software one — arguably the better
fit, since the Bible and packs are prose, not code.

- *Against:* `SA` has viral implications a downstream commercial user may not want,
  which reduces adoption of the method — the opposite of the goal.
- *Variant:* CC BY, without ShareAlike.

**D. Open everything including research records.** Radical transparency: the source
registry and claim records public.

- *For:* Maximum credibility. Makes the evidence layer independently checkable,
  which is the strongest possible answer to "how do we know this is true?"
- *Against:* Many source records will carry restricted access conditions, community
  protocols, and contributor anonymity. Publishing the registry wholesale would
  breach agreements. A *curated* public subset is the workable version of this and
  is already planned as the per-episode sources page.

## Recommendation

**B, with C's variant for prose** — Apache-2.0 on code and schemas, CC BY 4.0 on
`core/` and `packs/` text, proprietary on `studios/` and `rights/`.

The published per-episode evidence layer already delivers most of D's credibility
benefit without D's disclosure risk.

## Decision

`TBD — Showrunner and Platform Owner.`

## Consequences to work through once decided

- Per-directory `LICENSE` files, and a root `LICENSE` that maps them
- Contributor agreement distinguishing engine contributions from production work
- `NOTICE` file if Apache-2.0
- Public repository split, or a mirror, if `studios/` stays private
- Attribution expectations for anyone adopting a canon pack
