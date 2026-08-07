---
title: locations — places, sites, routes, regions
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [research-lead, cultural-advisor]
---

# locations

`LOC-*` profiles for every place the line depicts.

```
locations/
└── profiles/   LOC-XX-0000_<slug>.md
```

Template: [../../records/_TEMPLATE_location.md](../../records/_TEMPLATE_location.md).

Like character profiles, these hold **no facts** — only references to claims. The
prose contextualises; the claims assert.

## Coordinates are for map production, not for asserting extent

A latitude and longitude place a marker on a base map. They do not establish that a
polity controlled a territory, that a settlement occupied a site continuously, or
that a border ran anywhere. **Extent is a claim**, with evidence and a confidence
register, and a map that draws a hard boundary is asserting a precision that most
sources do not support.

`coordinate_precision` (`exact`, `approximate`, `regional`, `unlocated`, `withheld`)
is what a map render reads to decide whether it may draw a point, a zone, or nothing.
Defaulting it to `exact` is how a map acquires a confidence the record never had.

## Withholding a location is sometimes the correct answer

`site_status.location_withheld: true` for sites where publishing coordinates would
invite looting, trespass, or desecration. The schema then requires
`coordinate_precision: withheld`, so the two cannot drift apart.

This is not hypothetical caution. A documentary is a discovery mechanism for people
who were not looking, and an archaeological site named and located on a popular
platform has a measurably worse year afterwards.

## Reconstructing a place

`depiction.material_evidence` is what a reconstruction must be built from —
excavation reports, standing structures, contemporary descriptions, photographs.

`depiction.unattested_elements` is the field that does the real work: features **not**
evidenced — roof forms, upper storeys, interiors, surface finishes. The instruction
that follows from it is to **compose around them** rather than invent them. Frame past
the roofline, hold the interior in shadow, keep the unattested detail out of focus.

A generative tool will supply every one of those elements confidently and
attributably to nothing. Naming them in advance is what turns "the model decided" into
"we decided not to show it".

`period_ambience` records what a place is asserted to have sounded like. Ambience is
reconstruction, and it is the one reconstruction that routinely ships without anyone
deciding it was one.

## Naming

`period_name` is primary in historical sequences. `modern_name` is given once for
orientation and **never silently substituted** — substituting it tells the viewer the
place has one real name and it is the current one.
