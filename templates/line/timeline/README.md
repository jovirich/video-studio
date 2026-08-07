---
title: timeline — events and the relations between them
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# timeline

`EVT-*` records for the line's events, and the explicitly asserted relations between
them.

```
timeline/
└── events/   EVT-XX-0000_<slug>.yaml
```

Template: [../../records/_TEMPLATE_timeline_event.md](../../records/_TEMPLATE_timeline_event.md).
Rendering rules: [../../../standards/data_graphics.md](../../../standards/data_graphics.md).

## A timeline is a graphic, and a graphic asserts

This is the thing that makes timelines dangerous and this folder necessary. A
timeline makes three assertions at once, and two of them are usually made
accidentally:

1. **That the events happened** — deliberate, and backed by claims. The schema
   requires at least one claim per event.
2. **That they happened when the tick says** — usually accidental. A tick on a
   specific year asserts year-level precision. Most dating does not support it, and
   the graphic gives the viewer no way to tell.
3. **That the one caused, or led to, the next** — almost always accidental.
   **Adjacency reads as causation.** A viewer looking at two marks in sequence
   infers a link whether or not anybody asserted one.

## The two fields that defuse it

`dating_resolution` — `year`, `decade`, `generation`, `century`, `reign`, `relative`,
`unknown` — drives how the event is *drawn*. A century-resolution event rendered as a
point on a year axis is a false precision that the record explicitly did not claim.

`relations` — an explicit list, each entry naming the other event, the relation
(`precedes`, `causes`, `contributes-to`, `responds-to`, `concurrent-with`,
`contradicts-account-of`), its own confidence register, and the claims supporting it.

**If a link is not asserted here, the graphic must not imply it.** That is the rule,
and it constrains layout: two events with no asserted relation are not placed to
suggest one.

## Attestation is visually distinguished

`attestation` — `attested`, `inferred`, `traditional`, `disputed` — is keyed on the
rendered graphic, not flattened into a uniform set of marks. A timeline that draws an
inferred event identically to an attested one has laundered the difference through
design, and design is the layer where the viewer is least equipped to notice.
