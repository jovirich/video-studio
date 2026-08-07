---
adr: 0001
title: Build a studio, not a show
status: accepted
date: 2026-08-07
deciders: [showrunner, pipeline-engineer]
supersedes: none
superseded_by: none
---

# ADR 0001 — Build a studio, not a show

## Context

The brief was a cinematic AI documentary about Nigerian history, with an explicit
instruction to keep expansion open across African history more broadly.

Two shapes were available:

**A. Single show.** Top-level folders are `episodes/`, `research/`, `characters/`,
`locations/`. Nigeria is implicit — it is simply what the show is about.

**B. Studio with production lines.** Studio-level infrastructure, then a line per
country or region, then episodes inside a line.

Shape A is smaller, has shorter paths, and is what most documentary repos look like.
It is also what every project that later needed a second product wishes it had not
chosen.

## Decision

Shape B. Three tiers:

```
studio      bible, standards, prompts, templates, automation, library, brand, ops, docs
  └ line    productions/ng-nigeria/ — research, sources, characters, locations,
            timeline, languages, advisory, style
      └ ep  episodes/S01E01_slug/ — the eleven pipeline stages
```

Nigeria is `productions/ng-nigeria/`, line 01, opened first.

## Consequences

**Positive**

- Adding a country is `studio_ops new-line`, not a refactor or a fork. *(NOT BUILT)*
- The tier boundary forces an explicit question at write time: *is this rule
  universal or regional?* That question is nearly free to answer while writing and
  expensive to answer retroactively across a year of accumulated documents.
- ID scoping (`SRC-NG-*` vs `SRC-GH-*`) falls out of the structure rather than being
  bolted on.
- A line can be paused or closed without disturbing the others.
- Line-level advisory boards are structurally required rather than aspirational —
  the schema will not let a line open without one.

**Negative**

- One extra path segment on every line-scoped file.
- Contributors must learn which tier a change belongs to. Mitigated by the branch
  naming convention (`studio/*` vs `release/*`) and by the PR template's Area block.
- With exactly one line, the structure looks like over-engineering. It will look
  like over-engineering for as long as there is one line, which may be a while.

**Neutral**

- Studio-level tooling must be line-agnostic from day one. This is a discipline
  cost, not a code cost.

## Options rejected

**Monorepo with a `nigeria/` prefix but no studio tier.** Same path length, none of
the enforcement. The tier boundary is doing the work, not the folder name.

**Separate repos per country, sharing a git submodule of the Bible.** Submodules
would have made schema and prompt-library changes require coordinated updates across
every repo, and cross-line source records (which will exist — trade, migration, and
empire do not respect modern borders) would have no home.

## Validation

The decision is tested at Phase 6 of the [roadmap](../../ROADMAP.md): a second line
should reach greenlight without modifying `bible/`, `standards/`, or `automation/`.
If it cannot, the abstraction was placed wrong and the finding is recorded in
[../architecture/evolution.md](../architecture/evolution.md).
