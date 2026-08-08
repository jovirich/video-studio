---
# ---------------------------------------------------------------------------
# STYLE ANCHOR — a fixed reference that holds a look consistent.
# Copy to <line>/style/anchors/STA-XX-0000_<slug>.md with a toolkit-allocated
# ID. Do not fill this template in place.
#
# Referenced from prompt cards via `inheritance.style_anchors`, and from
# continuity records via `facial_reference` and `anchor_set`.
#
# Front matter follows standards/schemas/style_anchor.schema.json. That schema is
# authoritative; if the two disagree, `studio_ops validate --templates` fails.
# ---------------------------------------------------------------------------
id: STA-XX-0000
type: style_anchor
line: xx-line-code
title: TBD — what this anchor holds constant
status: draft
version: "0.1.0"
updated: "2026-01-01"
owners: [visual-director]
sensitivity: review-required

# look | character | location | material | light | palette | texture | graphic
#
# What kind of consistency this anchor enforces. A `character` anchor holds a face
# or a form; a `look` anchor holds a grade across shots generated weeks apart.
anchor_kind: look

# THE BYTES, AND THE HASH OF THE BYTES.
#
# The hash is the anchor; the path is only where the bytes currently sit. An
# anchor whose file can change without notice is not an anchor, so the hash is
# verified before every generation run. Media lives in the asset store, never in
# git.
file: TBD — asset store path, under library/style_refs/
sha256: TBD — 64 hex characters, computed from the delivered bytes

# If this anchor is itself a generated asset, its asset ID — so the anchor's own
# provenance is traceable. An anchor with no traceable origin cannot be
# regenerated, which makes it a single point of failure for everything
# downstream of it.
# derived_from: AST-XX-S00E00-0000

# Entity IDs, sequence IDs, or 'line' for a line-wide anchor.
applies_to: []

# WHAT THIS ANCHOR FIXES, IN WORDS, so a human can tell whether a render honoured
# it. Name both lists: what is held constant AND what is free to vary. An anchor
# that constrains too much produces thirty near-identical shots; one that
# constrains too little does not anchor anything.
description: >
  TBD

# supersedes: STA-XX-0000
# superseded_by: STA-XX-0000

# notes: >
#   Anything that depicts a real person, place, or object: which held features
#   are evidenced, and which are NOT. An anchor propagates — a detail invented
#   once at anchor stage appears in every inheriting shot, consistently, and
#   consistency is what makes an invention read as research.
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

Recorded in the `description` field above, not here. Restating it in two places is
how the two drift apart.

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
