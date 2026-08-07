---
title: Research protocol
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# Research protocol

The standard sequence for taking an episode from a question to a source-locked
research pack.

## Stage 1 — Frame the question

Before searching. An unframed search returns whatever is easiest to find, which for
African history means disproportionately colonial-era and Anglophone material.

Produce a research brief ([../briefs/_TEMPLATE_research_brief.md](../../../templates/records/_TEMPLATE_research_brief.md)) stating:

- the episode's question, and the sub-questions it decomposes into,
- what would count as an answer to each,
- what would *falsify* the working assumption,
- the periods, regions, and peoples in scope,
- known scholarly disputes touching the question,
- the languages the evidence is likely to be in.

That last point drives everything. If the relevant material is in Arabic, Ajami,
Portuguese, German, or an unwritten oral corpus, the research plan needs a
translator or a knowledge holder from the outset, not as a late discovery.

## Stage 2 — Survey the landscape

Map where evidence could exist before assessing what you can reach:

- archives and their catalogues, in-region and ex-region,
- museum and university collections,
- excavation reports and site archives,
- oral tradition holders and the institutions that recorded them,
- the existing scholarship, including work not in English,
- material culture in private and community hands.

Record the survey in the line's `sources/archive_landscape.md`. Note explicitly
what is **inaccessible** and why — held abroad, undigitised, restricted, lost,
uncatalogued. The distribution of what survives is itself historically informative
and frequently belongs on screen.

## Stage 3 — Prioritise

Rank by evidentiary weight against the question, not by convenience. The
accessible-first temptation is strong and systematically biases toward the coloniser's
record, because that is the record that was catalogued, digitised, and translated.

Budget explicitly for: travel to archives, digitisation fees, translation, and
consultation. If the budget cannot cover reaching the primary material, the episode's
scope shrinks — it does not proceed on secondary material while claiming otherwise.

## Stage 4 — Collect

For each item: create the source record **first**, then read.

Creating the record first forces the custody, access, and rights fields to be
captured while you are looking at the item, rather than reconstructed later from
memory. This sounds like a small thing and is not — reconstructed provenance is the
most common cause of a source record that cannot be verified when challenged.

```bash
python -m studio_ops new-record --type source --line ng-nigeria
```

Capture: full bibliographic detail, repository and reference number, access
conditions, rights status, and a local copy in the asset store where permitted.

## Stage 5 — Critique

The mandatory block. See [../../bible/02_evidence_and_sourcing.md](../02_evidence_and_sourcing.md) §4
and [bias_register.md](bias_register.md).

A source is not "reliable" or "unreliable". It is reliable *about certain things*.
The critique block's job is to establish which things.

## Stage 6 — Form claims

One claim per statement the episode will make. Set the confidence register from the
evidence, then check the corroboration requirement in
[../../bible/02_evidence_and_sourcing.md](../02_evidence_and_sourcing.md) §3.

**Check independence explicitly.** Record on each evidence entry which other sources
it is demonstrably not derived from. Repetition is not corroboration, and the most
common way a false claim survives into popular history is by being repeated across
sources that all trace to one original.

## Stage 7 — Record what is missing

Every gap becomes a `QST-*` record with what was searched. Gaps are findings.

## Stage 8 — Source lock

The Research Lead certifies that:

- [ ] Every claim required by the outline exists and is at its required tier
- [ ] Independence has been checked on every `established` claim
- [ ] Every contested claim has both positions recorded with named holders
- [ ] Every T4 source has a consent record and a named holder with stated standing
- [ ] Open questions are recorded, and none of them is load-bearing for a claim at
      `established`
- [ ] The critique block on every source is complete
- [ ] Consultation fees are paid or scheduled
- [ ] The archive landscape survey notes what could not be reached

After source lock, new evidence requires a documented re-open. This is deliberate
friction: without it, research continues indefinitely and the script never locks.

## What to do under time pressure

In order of preference, and this order is the protocol:

1. **Narrow the question.** A tighter question needs less evidence.
2. **Lower the register.** `probable` honestly beats `established` falsely.
3. **Cut the sequence.** A shorter episode is not a failure.
4. **Delay the episode.**

Not on the list: proceeding on thinner evidence while keeping the same confidence
level. That is the one move that cannot be undone after broadcast.
