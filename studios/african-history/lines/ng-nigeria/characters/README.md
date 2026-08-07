---
title: Characters — Nigeria line
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# Characters

The register of people and collective actors who appear on screen in this line.

Maturity: **DESIGNED** for structure, **NOT STARTED** for content. **This register is
empty.** No character record exists, and none may be created before a research lead is
named and the evidence chain is available to support one.

## 1. What this register holds

| | |
|---|---|
| ID scope | `CHR-NG-NNNN` — permanent, never reused, allocated by the toolkit |
| Records | [profiles/](profiles/) — `<ID>_<slug>.yaml`, ASCII filenames |
| Schema | `standards/schemas/character.schema.json` |
| Owner | Research Lead |
| State | empty |

A record exists for **every person and collective actor named on screen**
([pack 02 §7](../../../../../packs/documentary-history/02_evidence_and_sourcing.md)).
"Collective actor" covers a lineage, a dynasty, a guild, a community, a professional
body, or any group the narration treats as acting — a group that acts in a script is
an entity and needs the same consistency discipline as an individual. Polities and
institutions take `ORG-NG-*`; a person takes `CHR-NG-*`.

The register's purpose is mechanical: it is what makes cross-production consistency
**checkable rather than hopeful**. Without it, the same person is spelled two ways
across three episodes, is given two different titles, and is described as doing two
incompatible things — and nobody notices, because nobody is holding all three episodes
in their head at once.

## 2. The rule that governs the record's content

> **An entity record holds no facts. It holds identity, name decisions, and references
> to claims.**

This is the studio's version of the platform-wide separation between evidence and
assertion ([ADR 0002](../../../../../docs/decisions/0002-claims-as-records.md)). A
character record does not state what someone did, when they lived, what they ruled, or
what happened to them. Each of those is a statement the production will make on
screen; each therefore belongs in a `CLM-NG-*` record with a confidence register and
sources, and appears here only as a claim ID.

What the record does carry:

| Field | Content |
|---|---|
| `name_on_screen` | The form used on screen — **a decision, recorded with its reason**, per [pack 09 §3](../../../../../packs/documentary-history/09_localization.md) |
| `name_forms` | Alternative, historical, and external forms, each marked for what it is |
| `claims` | The claim IDs that reference this entity. Everything substantive lives there. |
| `dates` | A `dateRange`, which itself carries the claim IDs supporting it and a confidence register — never a bare year |
| `pronunciation` | IPA transcription and a reference recording from a speaker, stored against the record in the asset store |
| `sensitivity` | `none` / `review-required` / `held`, with the advisory ruling reference where applicable |
| `depiction` | Whether and how this entity may be depicted in generated imagery |

If a field on a record cannot be written without asserting something about the past, it
is the wrong field and the content belongs in a claim.

## 3. Why the discipline is strict here specifically

Two failure modes converge on this register.

**Name forms.** Which name a person or people is given on screen is a decision with
consequences, not a spelling matter. The form used by the people concerned is primary
unless a documented reason overrides; exonyms and colonial forms are not primary and
may appear once, parenthetically, clearly marked; contested forms are given with the
dispute named rather than resolved silently by editorial preference. Several widely
used names in the literature are external impositions, and inheriting one because it
is what the sources say is how a production reproduces the imposition while citing it.
The record is where that decision is written down once and then applied mechanically.

**Depiction.** Generative tools will produce a face for any name on request, and
[core/01 §2](../../../../../core/01_provenance_and_ai_disclosure.md) prohibits
synthesising a real person's likeness without documented consent — which is impossible
for a historical figure. Named individuals are additionally constrained by
[pack 03 §6](../../../../../packs/documentary-history/03_narrative_doctrine.md);
unnamed and crowd figures are not. The record carries the depiction position so that a
prompt card cannot be written against an assumption nobody checked, and so that the
constraint is visible at the moment a shot is planned rather than at picture lock.

Where the entity is a named ancestor of living families, or where succession or title
is contested, the record carries `sensitivity: review-required` at minimum and the
advisory register rules before generation
([pack 07 §2](../../../../../packs/documentary-history/07_cultural_sensitivity.md)).

## 4. The great-man hazard

Named individuals are documented; the people who made a polity work usually are not.
Building a production around the documented individual **because the evidence is
there** smuggles in a theory of history
([bias_register.md](../../../../../packs/documentary-history/methodology/bias_register.md)
§ Framing bias in our own work).

A full and well-maintained character register makes that hazard *more* acute, not
less, because it makes the individual the convenient unit of narrative. The
counterweight is the collective-actor record and the discipline of asking, per
production, who is absent from this register and why.

## 5. Before anything is added here

No research lead. No advisory contact. No archive landscape survey. The line is
`candidate` — [../README.md](../README.md) §2.

Adding a character record now would mean deciding a name form without a Cultural
Advisor and asserting an identity without a source. Both are the specific failures
this line's structure exists to make hard.
