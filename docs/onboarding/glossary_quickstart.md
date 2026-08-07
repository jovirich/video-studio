---
title: Glossary quickstart
status: active
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer]
---

# Glossary quickstart

Fifteen terms. These are the ones that appear in the first hour and whose ordinary
meanings will mislead you. Full reference: [../glossary.md](../glossary.md), which
governs where the two differ.

## Structure

**1 · Platform** — this repository, `video-studio`. The engine: core canon, canon
packs, schemas, prompt library, templates, automation. It is not a show and not a
studio, and nothing in it names one.

**2 · Studio** — a brand and a body of work, in `studios/<code>/`. Declares exactly
**one canon pack**, which determines the editorial rules and gate set its productions
are held to. *Not* a physical place, and not the repository.

**3 · Line** (production line) — a coherent strand within a studio, in
`studios/<code>/lines/<line>/`. Usually a region or a series. Owns its research,
sources, entities, language policy, advisory board, and visual identity. This is where
the actual records live.

**4 · Production** — one episode, film, or short. Eleven pipeline stages, gated. The
only tier at which a specific piece exists.

**5 · Canon pack** — the genre rulebook in `packs/`. Supplies what `core/`
deliberately omits: evidence standards, narrative doctrine, visual and sonic language,
sensitivity procedure, and the **gate set**. Core defines what a gate *is*; the pack
says which gates *exist*. `documentary-history` is the first one.

## Evidence

**6 · Source record** (`SRC-*`) — one described, tiered, critiqued item of evidence.
A citation is a location; a source record is an interrogation.

**7 · Claim** (`CLM-*`) — one factual statement, with a confidence register and an
evidence array of sources. **Facts live here, not in scripts.**

**8 · Claim reference** — `{{CLM-NG-0117}}`, written inline in a script. Stripped at
render, compiled into the citation appendix. A script contains references, never bare
facts.

**9 · Tier** — T1 to T5, the *kind of verification a claim needs*, not a ranking of
whose knowledge counts. T1 primary/archival · T2 peer-reviewed · T3 reputable general
· T4 oral testimony and tradition · **T5 never citable**.

**10 · T5** — worth its own entry. Everything else: undated web pages, aggregators,
popular video, and **any output of a language model**. A model may help you locate,
summarise what you have read, or structure notes. Its assertions are leads, never
sources. This is the rule most likely to erode under deadline.

**11 · Register** — the certainty a statement claims: `established`, `probable`,
`contested`, `inferred`, `traditional`, `unknown`. A property of the evidence, not of
the writer's confidence. Under time pressure you lower the register; you never raise
the claim.

**12 · Critique block** — the mandatory interrogation on every source record: who made
this, for whom, what were they in a position to know, what interest shaped it, what has
happened to it since, and what its silence means.

## Process and tooling

**13 · Gate** — a named point where a **specific human** certifies a **specific claim**
against a **written checklist** and records a signature. Blocking, not advisory. A
review without all four properties is feedback, which is valuable and is not a gate.
**No person signs two gates on the same production.**

**14 · Prompt card** (`PC-*`) — a prompt as a versioned YAML *record*, not a string:
structured fields, inherited style, evidence basis where it depicts a reconstruction,
and an append-only `runs` history. Reviewable **before** generation, which is the only
point at which review is cheap.

**15 · NOT BUILT** — a first-class status, not an apology. One of four maturity
labels — DESIGNED / IMPLEMENTED / TESTED / NOT BUILT — used in documents, commit
messages, and conversation. A bare ✅ is banned. Nothing here is currently TESTED.

## Three more you will hit by Thursday

**Advisory hold** — any contributor may freeze work on an item by raising a sensitivity
issue. Released only by a written Cultural Advisor ruling. The Showrunner cannot
release it. The person who raised it is never penalised.

**Manifest** — `manifest.yaml`, the production's ledger of every asset and its
provenance. Git holds the manifest; the asset store holds the media.

**`studio_ops`** — the Python toolkit in `automation/`, run as
`python -m studio_ops`. Four validators run today; everything else reports NOT BUILT
and exits non-zero rather than succeeding quietly.
</content>
