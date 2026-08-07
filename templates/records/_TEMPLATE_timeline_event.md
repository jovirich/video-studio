---
# ---------------------------------------------------------------------------
# TIMELINE EVENT — an event on the line's timeline.
# Schema: ../../standards/schemas/timeline_event.schema.json
# Copy to <line>/timeline/events/EVT-XX-0000_<slug>.md with a toolkit-allocated
# ID. Do not fill this template in place.
#
# A timeline is a GRAPHIC, and a graphic asserts. Every event is backed by
# claims for that reason. See ../../standards/data_graphics.md § Timelines.
# ---------------------------------------------------------------------------
id: EVT-XX-0000
type: timeline_event
line: xx-line-code
title: TBD — short handle for indexes and for the timeline label
status: draft
version: "0.1.0"
updated: "2026-08-07"
owners: [research-lead]
sensitivity: review-required

# One sentence, at the confidence the evidence supports. This is the text that
# appears next to the mark, and it is read in isolation by someone scanning a
# graphic — so it cannot rely on a hedge stated elsewhere.
summary: TBD — one sentence

dating:
  earliest: TBD
  latest: TBD
  display: TBD — how the date is spoken and captioned
  calendar: TBD — Gregorian, Hijri, regnal, relative
  basis: TBD — how the dating was arrived at
  confidence: TBD — established | probable | contested | inferred | traditional | unknown
  claims: []

# year | decade | generation | century | reign | relative | unknown
#
# Drives how the event is DRAWN. A tick on a specific year asserts year-level
# precision, and most dating does not support it — a century-resolution event
# rendered as a point on a year axis is a false precision the record explicitly
# did not claim, made by the layout rather than by anyone.
dating_resolution: TBD

# attested | inferred | traditional | disputed
#
# Visually distinguished on timeline graphics and keyed. A timeline that draws
# an inferred event identically to an attested one has laundered the difference
# through design — the layer where a viewer is least equipped to notice.
attestation: TBD

participants:
  characters: []                # TBD — CHR-XX-0000
  organisations: []             # TBD — ORG-XX-0000

locations: []                   # TBD — LOC-XX-0000

# Explicit relationships between events.
#
# ADJACENCY READS AS CAUSATION. A viewer looking at two marks in sequence infers
# a link whether or not anybody asserted one. This list is the set of links the
# production actually asserts, each with its own confidence and its own claims —
# and the rule that follows is binding on layout: IF A LINK IS NOT ASSERTED
# HERE, THE GRAPHIC MUST NOT IMPLY IT.
relations:
  - event: EVT-XX-0000
    # precedes | follows | causes | contributes-to | responds-to |
    # concurrent-with | contradicts-account-of
    #
    # `causes` is the one to be slow about. `contributes-to` is usually the
    # honest relation and is almost always the one the evidence supports.
    relation: TBD
    confidence: TBD
    claims: []

# At least one claim is required by the schema. An event with no claim is a mark
# on a graphic asserting that something happened, on nobody's authority.
claims:
  - CLM-XX-0000

open_questions: []              # TBD — QST-XX-0000
appears_in: []
notes: TBD
---

# TBD — event handle

> Copy this file; do not fill it in place.

## What happened, and how we know

TBD — orientation for a reader coming cold. Every substantive statement points at a
claim in the front matter.

## Why this dating resolution

TBD — what fixes the date, how loosely, and what a tighter resolution would require.

The most common error on a timeline is not a wrong date. It is a right date drawn at
a resolution the evidence never supported, which reads to a viewer as certainty that
nobody claimed and nobody can defend.

## Relations not asserted

TBD — the adjacent events this one is **not** claimed to have caused, where a viewer
would naturally infer that it did.

Recording the non-relation is what tells the graphic designer to separate the marks,
break the axis, or key them differently. Left unrecorded, the layout asserts the
link by default and no one signed off on it.
