---
# ---------------------------------------------------------------------------
# STYLE ANCHOR — a fixed reference that holds a look consistent.
# Copy to <line>/style/anchors/STA-XX-0000_<slug>.md with a toolkit-allocated
# ID. Do not fill this template in place.
#
# Referenced from prompt cards via `inheritance.style_anchors`, and from
# character and location records via `style_anchors`.
#
# No schema exists for this record type yet; front matter follows the minimum in
# ../../standards/metadata_spec.md plus the ID system.
# ---------------------------------------------------------------------------
id: STA-XX-0000
type: style_anchor
line: xx-line-code
title: TBD — what this anchor holds constant
status: draft
version: "0.1.0"
updated: "2026-08-07"
owners: [visual-director]
sensitivity: review-required

# entity | location | material | palette | grade | lighting | texture |
# composition | graphic_system
#
# What kind of consistency this anchor enforces. An entity anchor holds a face
# or a form; a grade anchor holds a look across shots generated weeks apart.
anchor_kind: TBD

# The record this anchor is the appearance of, where it has one.
anchors_entity: TBD — CHR-XX-0000 / LOC-XX-0000 / OBJ-XX-0000, or `n/a`

# The reference image or clip itself. Media lives in the asset store, never in
# git.
asset: TBD — AST-XX-S00E00-0000, or the asset store path
asset_origin: TBD — generated / photographed / licensed / studio library

# The card that produced it, where the anchor is itself generated. An anchor
# with no card cannot be regenerated, which makes it a single point of failure
# for everything downstream of it.
source_prompt_card: TBD — PC-XX-S00E00-0000, or `n/a`

# What this anchor is grounded in, where it depicts something historical. An
# anchor propagates: a wrong detail in an anchor becomes a wrong detail in every
# shot that inherits it, and it becomes consistent, which makes it read as
# researched.
evidence_basis: []              # TBD — CLM-XX-0000, SRC-XX-0000

# locked | provisional | superseded
# A provisional anchor may still change. A locked one may not, because shots
# already inherit it.
anchor_status: provisional
# superseded_by: STA-XX-0000
---

# Style anchor — TBD

> Copy this file; do not fill it in place.

## Why style anchors exist

A generative model has no memory between runs. Asked twice for the same person, it
produces two people; asked across a season, it produces a different person per
production, each internally plausible and none of them the same.

An anchor is a fixed reference, recorded with an ID, that every card depicting that
entity or look feeds back in. It is the mechanism by which a face, a building, a
textile, a palette, or a grade stays the same across shots, sequences, productions,
and seasons.

Without anchors, continuity is maintained by whoever is generating that week
remembering what last month looked like. That works for roughly six weeks.

## What this anchor holds

TBD — precisely what must stay constant, and what is free to vary.

An anchor that constrains too much produces thirty near-identical shots. One that
constrains too little does not anchor anything. Naming both lists is the work.

| Held constant | Free to vary |
|---|---|
| TBD | TBD |

## What it is grounded in

TBD — for anything depicting a real person, place, or object: the evidence behind
each held feature, and which held features are **not** evidenced.

An anchor propagates. A detail invented once at anchor stage appears in every
inheriting shot, consistently, and consistency is what makes an invention read as
research. This section is the only place that gets caught.

## How to use it

TBD — which cards should inherit this anchor, at what weight, and in combination with
what else.

## Deviation

Any card departing from this anchor records an **override with a stated reason** in
its `inheritance.overrides` block. An override without a reason fails review, because
unexplained overrides accumulate — each defensible alone — until the look has drifted
with no single decision having caused it.

## History

| Version | Date | Change | Cause | Shots already inheriting |
|---|---|---|---|---|
| 0.1.0 | TBD | Created | TBD | TBD |

The last column decides whether a change is an edit or a supersession. Changing a
locked anchor that shots already inherit does not update those shots — it makes them
inconsistent with everything generated afterwards. Supersede instead, and re-generate
deliberately.
