---
title: Timeline — Nigeria line
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# Timeline

The register of dated events for this line.

Maturity: **DESIGNED** for structure, **NOT STARTED** for content. **This register is
empty. No timeline has been populated, and populating one is research, not
scaffolding.**

## 1. What this register holds

| | |
|---|---|
| ID scope | `EVT-NG-NNNN` — permanent, never reused, allocated by the toolkit |
| Records | [events/](events/) — `<ID>_<slug>.yaml`, ASCII filenames |
| Schema | `standards/schemas/timeline_event.schema.json` |
| Owner | Research Lead |
| State | empty |

## 2. The rule that governs the record's content

> **An event record holds no facts. It holds identity, a dating, and references to
> claims.**

The record does not say what happened. What happened is a statement the production
will make, and it lives in a `CLM-NG-*` record with a confidence register, sources,
and an independence check. The event record is the hook that lets several claims be
ordered relative to one another and lets a graphic be built from records rather than
from someone's notes.

| Field | Content |
|---|---|
| `dates` | A `dateRange` — `earliest`, `latest`, `display`, `calendar`, `basis`, `confidence`, and the claim IDs supporting it |
| `claims` | Everything the production asserts about the event |
| `entities` | The `CHR-NG-*`, `LOC-NG-*`, and `ORG-NG-*` records involved |
| `sensitivity` | Atrocity, enslavement, and violence within living memory carry `review-required` at minimum |

## 3. Dating is a claim, and it is a range

The schema requires a **range** and a **display form**, because a point date is usually
false precision and false precision is a false statement
([pack 02 §6](../../../../../packs/documentary-history/02_evidence_and_sourcing.md)).

- Give the range the sources give. Narrowing it for a cleaner graphic is fabrication
  with a design justification.
- Record the **basis** — how the dating was arrived at — and distinguish **attested**,
  **estimated**, and **modelled**.
- Record the **calendar and the conversion method** where a source uses a reckoning
  other than the one on screen. Regnal, agricultural, lunar, and local reckonings do
  not convert cleanly, and an undocumented conversion is unreproducible.
- The `display` field is what is *spoken and shown*. It is written to be honest at
  speed — a range spoken as a range, an estimate spoken as an estimate.

## 4. What a timeline graphic silently asserts

A timeline is a graphic, and graphics carry the same evidence obligations as narration
([pack 04 §8](../../../../../packs/documentary-history/04_visual_language.md),
[standards/data_graphics.md](../../../../../standards/data_graphics.md)). Four
assertions are made by the *form* rather than by any entry, and each has to be
actively defeated:

1. **Even spacing implies even knowledge.** It is not. Density on a timeline tracks
   what generated documents, and wars, raids, and crises generate documents while
   ordinary decades generate silence
   ([bias_register.md](../../../../../packs/documentary-history/methodology/bias_register.md)
   § Survival bias). A timeline built from record volume is a timeline of crises
   presented as a history.
2. **A gap reads as emptiness.** It usually means nobody was recording, or what was
   recorded did not survive, or it survived and was never catalogued. Absence of
   evidence in a record that would not have recorded the thing anyway is not evidence
   of absence, and a blank stretch on screen says the opposite loudly.
3. **A tick mark reads as a fact.** Uncertainty must be visible in the mark itself —
   ranges drawn as ranges, not as points with a footnote nobody reads at 360p.
4. **Sequence reads as causation.** Ordering two events adjacently is an argument. If
   the production is making it, it makes it in narration with a claim behind it; if it
   is not, the graphic must not make it silently.

The honest timeline for a sparsely documented period frequently shows the *shape of
the record* alongside the events — and that is usually more interesting than the
events, not a caveat on them.

## 5. Series-level use

Because event records are line-scoped rather than production-scoped, they are what
keeps two productions from dating the same thing differently. Where two productions in
this line, or two lines in this studio, disagree about a dating, the disagreement is
resolved explicitly on the records — never left for a viewer to discover across
episodes.

## 6. Before anything is added here

**Do not populate this timeline as scaffolding.** It is the single most tempting file
in the repository to fill with "obvious" entries, and every entry would be an unsourced
historical claim inserted by someone who is not the research lead — because there is
no research lead ([../README.md](../README.md) §2).

The first entry here is created by the toolkit, by a named researcher, from a claim
that already has a source record and a critique block.
