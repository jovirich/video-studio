---
title: Locations — Nigeria line
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# Locations

The register of places that appear on screen in this line.

Maturity: **DESIGNED** for structure, **NOT STARTED** for content. **This register is
empty.** No location record exists.

## 1. What this register holds

| | |
|---|---|
| ID scope | `LOC-NG-NNNN` — permanent, never reused, allocated by the toolkit |
| Records | [profiles/](profiles/) — `<ID>_<slug>.yaml`, ASCII filenames |
| Schema | `standards/schemas/location.schema.json` |
| Owner | Research Lead |
| State | empty |

A record exists for every place named on screen or depicted specifically — settlement,
site, structure, landscape feature, route, or region
([pack 02 §7](../../../../../packs/documentary-history/02_evidence_and_sourcing.md)).
A polity is not a place; it takes `ORG-NG-*`. The distinction matters because a polity
and the ground it controlled change independently, and conflating them is how a map
ends up asserting something no source supports.

## 2. The rule that governs the record's content

> **A location record holds no facts. It holds identity, name decisions, and references
> to claims.**

The record does not state what a place was, who built it, when it was occupied, how
large it was, or what happened there. Every one of those is a statement the production
will make on screen and belongs in a `CLM-NG-*` record with a confidence register and
sources.

What the record carries:

| Field | Content |
|---|---|
| `name_on_screen` | The period-appropriate form, recorded as a decision with its reason |
| `name_forms` | Modern, historical, external, and contested forms, each marked for what it is |
| `claims` | The claim IDs that reference this place |
| `geography` | Coordinates or extent **as a claim**, with its own confidence register — never a bare point where the sources give a region |
| `pronunciation` | IPA and a reference recording from a speaker |
| `sensitivity` | Sacred sites, burial grounds, and contested territory carry `review-required` at minimum |
| `depiction` | What may be reconstructed, and on what material basis |

## 3. Naming, and why it is not a spelling matter

The period-appropriate name is primary; the modern name is given once for orientation
and is **never silently substituted**
([pack 09 §3](../../../../../packs/documentary-history/09_localization.md)). A colonial
or external name is not the primary form, and may appear once, parenthetically, clearly
marked as what it is. Contested names are given with the dispute named.

Substituting a modern name for a historical one is not a convenience for the viewer.
It is an assertion of continuity between a present-day place and a past one — a claim
that frequently does not hold, that no source was asked to support, and that the
production made without noticing it was making it.

## 4. Depiction, reconstruction, and maps

Two constraints bear on this register more than any other.

**Reconstruction is grounded in a material fact or it is not made.** Architecture comes
from excavation or standing structures; the shot record names them
([pack 04 §6](../../../../../packs/documentary-history/04_visual_language.md)). Where a
feature is unattested, the honest instrument is composition — frame below the
roofline — not a plausible invention. The location record is where the attested
material basis is registered, so that a prompt card can inherit it and a reviewer can
check it before generation rather than after.

**Maps assert more than they appear to.** Historical borders are drawn as zones of
influence rather than crisp lines unless a treaty line is being depicted and cited;
modern national borders are never drawn over pre-colonial periods without an explicit
on-screen note that they are a modern overlay for orientation; every map states its
projection and cites its geographic and historical sources
([pack 04 §8](../../../../../packs/documentary-history/04_visual_language.md)). A crisp
line is a claim about the precision of the evidence, and it is usually a false one.

## 5. Sensitivity

Sacred sites, shrines, burial grounds, and human remains are advisory categories
requiring review **before generation**, not before publication
([pack 07 §2](../../../../../packs/documentary-history/07_cultural_sensitivity.md)).
Once a striking image of a place exists, the conversation about whether it should
exist becomes much harder to win, which is why the review sits where it does.

Contested territory, land, and title claims that bear on present-day disputes carry the
same flag. The series does not adjudicate present-day disputes
([pack 01 §8](../../../../../packs/documentary-history/01_editorial_standards.md)); a
map is one of the easiest ways to adjudicate one by accident.

## 6. Before anything is added here

No research lead. No advisory contact. No archive landscape survey — and the survey is
what establishes whether a place's material record exists at all.
[../README.md](../README.md) §2.
