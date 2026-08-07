---
adr: 0005
title: Separate the platform from the editorial canon, via canon packs
status: accepted
date: 2026-08-07
deciders: [platform-owner, showrunner]
supersedes: partially 0001
superseded_by: none
---

# ADR 0005 — Separate the platform from the editorial canon, via canon packs

## Context

[ADR 0001](0001-studio-not-show.md) separated *region* from *studio*: Nigeria became
a production line rather than the subject of the repository. That was correct and it
did not go far enough.

The repository root was still a historical-documentary studio. `bible/` contained,
in one flat run of thirteen documents:

| Kind of rule | Examples | True of |
|---|---|---|
| Universal | AI disclosure, provenance, rights, delivery specs, accessibility | any video |
| Genre | source tiers, corroboration, narrative doctrine, cultural advisory authority, reconstruction labelling | historical documentary |
| Studio | mission, audience, scope, editorial independence | African History Studio |

Fusing them meant that any other kind of video — a narrative short, a brand film, an
explainer — would inherit an evidence chain it could not satisfy and a nine-gate set
that made no sense for it. Available responses were all bad:

1. **Fork the repository.** Immediate divergence of schemas, prompt library, and
   tooling. The shared engine stops being shared within a month.
2. **Grant exemptions per production.** Canon that routinely grants exemptions is
   not canon; it is a suggestion with paperwork.
3. **Water down the canon** so it fits everything. Then it constrains nothing, and
   the history work loses the rigour that was its entire justification.
4. **Accept that the platform only makes history documentaries.** Legitimate, but
   contradicts the stated intent.

The question that surfaced this — asked before any production existed — was: *what
happens when we want to make something that is not this?*

## Decision

Insert two tiers and split canon by scope.

```
PLATFORM   core canon, packs, schemas, prompts, templates, automation, rights, ops
  STUDIO   declares one pack; adds its own bible and brand
    LINE   research, sources, entities, language, advisory, style
     PROD  one episode / film / short
```

**`core/`** holds only what is true of *any* production: provenance and AI
disclosure, rights, distribution, accessibility, and the gate **framework** — what a
gate is, how it blocks, how re-opening cascades, separation of duties.

**A canon pack** holds what is true of *a genre*: evidence standards, narrative
doctrine, visual and sonic language, sensitivity procedure, localisation, and the
gate **set** — which gates exist, who owns them, what they certify.

**A studio bible** holds what is true of *one studio*: mission, audience, scope,
independence, corrections.

Precedence is `core > pack > studio > line > production`. A lower layer may add
constraints and tighten upper ones. It may never loosen. An exemption requires
amending the layer that owns the rule, with that layer's signatures.

The test for placement: **would this rule still be right for a production with no
historical claims in it at all?** If yes, core. If it is right for a whole genre,
pack. If it is right for one brand, studio.

## Consequences

**Positive**

- A new genre is `studio_ops new-pack`, not a fork. Tested at *(NOT BUILT)*
  [ROADMAP](../../ROADMAP.md) Phase 6.
- Genres with incompatible obligations coexist without either compromising. A brand
  film gets no fake fact-check gate; a history documentary cannot skip a real one.
- The engine — schemas, prompt library, automation, delivery specs, rights registers
  — is shared by everything, so improvements land everywhere.
- Core's prohibitions become genuinely universal, and no pack can weaken them. That
  is a stronger guarantee than a single-genre bible could make.
- Writing a pack forces a genre to state its own failure mode. That is a useful
  discipline in itself.

**Negative**

- **Four tiers.** More to learn, deeper paths, and with one studio it reads as
  over-engineering. It will read that way for as long as there is one studio.
- A contributor must know which of four layers a rule belongs to. Mitigated by the
  placement test above and by the PR template's Area block.
- Cross-layer links are long and fragile. Mitigated by the link validator.
- The refactor cost ~30 file moves and a full relink pass.

**Neutral**

- `studio_ops` gains `new-pack` and `new-studio` alongside `new-line`.
- Gate sets become data (`gates.yaml`) rather than prose. Better, but it is a change.

## Options rejected

**Keep three tiers; make the bible modular with genre flags.** Conditional canon
(`if genre == documentary`) inside single documents. Rejected: conditionals in
normative text are how policy documents become unreadable, and there is no clean
place to put a gate set.

**Separate repository per genre, sharing schemas via a package.** Rejected for the
same reason ADR 0001 rejected per-country repos: coordinated updates across repos do
not happen, and the shared package drifts.

**Defer until a second genre actually exists.** Seriously considered — speculative
generality is a real failure mode. Rejected on cost asymmetry: doing it now cost 30
file moves with no production in flight; doing it after episode one would have moved
every claim ID, asset path, and locked record. The intent to expand was explicit,
not hypothetical.

## Validation

Three failure signals, checkable:

1. **Studio names in platform files.** `grep -ri "african\|nigeria" core/ standards/ prompts/ templates/ automation/` should return nothing. If it does, the tiers are leaking.
2. **A second pack that is largely a copy of the first.** Means the shared material belonged in core and the split was made in the wrong place.
3. **Packs requesting core exemptions.** One suggests core over-reaches; a pattern means core was written from documentary assumptions rather than universal ones.

Recorded in [../architecture/evolution.md](../architecture/evolution.md) AE-006.
