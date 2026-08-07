---
title: Line skeleton
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [research-lead, showrunner]
---

# Line skeleton

The canonical folder for one production line — a coherent body of work: a region, a
series, a season strand. Copied by `studio_ops new-line --studio <studio> --code <code>`
into `studios/<studio>/lines/<code>/`.

Maturity: **DESIGNED**. The scaffolder is **NOT BUILT**
([../../docs/status.md](../../docs/status.md)).

## 1. What a line is for

A line is the level at which **research is shared and entities are consistent**.

That is not an organisational preference; it is the reason the tier exists. A person,
a place, or a claim appearing in three productions must be one record referenced
three times. Three copies diverge — not immediately, and not visibly, but by the
third season one of them says something the other two do not, and nobody knows which
is right or when it changed.

So the registries live here:

```
<line>/
├── line.yaml        the control record — status, opening conditions, languages
├── research/        briefs, open questions, fact-check reports, interview plans
├── sources/         the source and claim registries — SRC-*, CLM-*
├── characters/      CHR-* profiles: people, offices, lineages, collectives
├── locations/       LOC-* profiles: settlements, sites, routes, regions
├── timeline/        EVT-* events, and the relations between them
├── languages/       one entry per language on screen: orthography, diacritics, fonts
├── advisory/        the advisory register, rulings ADV-*, and the terms of engagement
├── style/           visual identity, lens set, palette, style anchors STA-*
└── productions/     the productions themselves, one folder each
```

`id_scope` on [line.yaml](line.yaml) — two uppercase letters — is what appears in
every record ID this line allocates. It is permanent. Changing it after records
exist orphans every reference to them.

## 2. A line is not open until three conditions are true

From the platform charter, and made checkable by `opening_conditions` on
[line.yaml](line.yaml):

| Condition | Why it blocks |
|---|---|
| **A Research Lead is named** | A line with no named lead has no accountable owner for the evidence, and evidence is the thing that fails silently |
| **An advisory contact is agreed** | Discovering at picture lock that nobody qualified has looked at the subject is not a review problem; it is a re-shoot |
| **The archive landscape is surveyed** | Without it, scope is set by guesswork and the first production discovers mid-research that its central question is unanswerable from available material |

`line_status: open` is the only status that permits greenlighting a production, and
the schema refuses `open` while any condition is false. The check is mechanical
because these three are precisely the conditions a schedule wants to defer.

The template ships as `candidate` with all three false. That is the honest starting
state, and turning any of them to `true` should require pointing at something.

## 3. Precedence

`core > pack > studio > line > production`.

A line may **add** constraints and **tighten** inherited ones. It may never loosen
one. If a line needs an exemption from a studio or pack rule, the rule is amended at
the layer that owns it, with that layer's signatures — see
[../../CONTRIBUTING.md](../../CONTRIBUTING.md) § Which layer does your change belong to.

The most common misplacement is putting a rule here that belongs one layer up
(because it is true of the whole studio) or one layer down (because it is true of
one production). The test is in that section of CONTRIBUTING.

## 4. Filling this in

Every substantive value in [line.yaml](line.yaml) is `TBD — <what is needed>`. The
sequence that usually works:

1. Name the Research Lead. Everything else has an owner once this is true.
2. Survey the archive landscape and write it down. This is the step that determines
   whether the line is viable, and it is the step most often skipped because it
   produces no visible output.
3. Agree the advisory contact, with a fee and terms —
   [../legal/advisor_agreement.md](../legal/advisor_agreement.md).
4. Record the languages, because font selection depends on the union of their
   diacritic coverage and a missing glyph discovered during the grade is a re-render
   of every title in the production.
5. Set the visual identity, so productions inherit a look instead of each inventing
   one.
6. Only then set `line_status: open`.
