---
title: Archive landscape survey — Nigeria line
status: template
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# Archive landscape survey

> **Status: NOT STARTED.** This document is the **template for a survey**, not a
> survey. It contains no finding about where evidence for this line exists, because no
> survey has been conducted and no research lead has been named.
>
> **This blocks the line from opening.** Condition 3 of the three in
> [bible/00_charter.md](../../../bible/00_charter.md) §2 is *"the archive landscape
> has been surveyed and recorded in the line's `sources/archive_landscape.md`"*, and
> the [production_line schema](../../../../../standards/schemas/production_line.schema.json)
> refuses `line_status: open` while `archive_landscape_surveyed` is false. It is false.

## 1. What this document is for

Stage 2 of the [research protocol](../../../../../packs/documentary-history/methodology/research_protocol.md):
**map where evidence could exist before assessing what you can reach.**

The order matters and it is the entire point of doing this at line level rather than
per production. A researcher who starts from what is reachable builds a picture of
the past shaped by cataloguing, digitisation, and translation budgets — three
processes that have their own history and their own interests, and none of which
tracked where the history was. The survey exists to make that shaping *visible* and
therefore correctable, rather than invisible and therefore inherited.

A completed survey answers a question the studio will be asked in public and should be
able to answer without flinching: **why these episodes, and not others?** "Because the
material was there" is an honest answer only if the studio knows where the material
was *not*, and says so.

Second purpose, equally load-bearing: **the distribution of what survives is itself
historically informative and frequently belongs on screen.** Where the record thins,
where it stops, whose record it is, and what it was made for are findings about the
past, not merely constraints on the production. See §3.

## 2. What the survey must record

Every section below is filled by the Research Lead, reviewed by the Cultural Advisor,
and cited like any other evidence — a survey finding is a claim about the present-day
state of the record and carries source records like anything else.

### 2.1 Where evidence could exist

Mapped **before** any assessment of reachability, so that the map is not pre-truncated
by the budget.

- [ ] National, regional, and local repositories, and their catalogues
- [ ] Institutional archives: religious, commercial, administrative, legal, educational
- [ ] Museum and university collections, in-region and ex-region
- [ ] Excavation reports, site archives, and the material record
- [ ] Oral tradition holders, and the institutions that have recorded them
- [ ] Community- and family-held material, including material in private hands
- [ ] Existing scholarship, **including work not published in English**
- [ ] Datasets, surveys, and administrative series
- [ ] Media and periodical archives
- [ ] Personal papers and correspondence collections

For each: what it is, who holds it, what period and subject it covers, its catalogue
state, and how it was learned about. `TBD — Research Lead` for every row. **Do not
populate this list with plausible entries.** An unverified repository in a survey is
worse than a blank row, because a later researcher will treat it as checked.

### 2.2 What is accessible, and on what terms

| Field | Records |
|---|---|
| Physical access | Whether the holding can be visited, by whom, with what permission, and at what cost |
| Remote access | Whether catalogues, finding aids, or items are consultable at a distance |
| Reproduction | Whether copies can be obtained, in what form, at what fee, and how long it takes |
| Access conditions | Any condition attached to access — and specifically **whether editorial input is a condition**, which is disclosed on screen or the material is not used ([bible/00_charter.md](../../../bible/00_charter.md) §6) |
| Rights position | What the studio may publish, and under what licence. `pending` never ships. |
| Cost and lead time | Real numbers, including travel, fees, and turnaround — because [research protocol Stage 3](../../../../../packs/documentary-history/methodology/research_protocol.md) requires budgeting for reaching primary material, and a production whose budget cannot reach it shrinks its scope rather than proceeding on secondary material while implying otherwise |

### 2.3 What is held outside the region

Recorded as its own section, not as a footnote to §2.1, because it is a structural
feature of the record rather than an inconvenience.

- Which material sits outside the region, in which kinds of institution, and how it
  got there
- Whether the holding institution's catalogue is more complete, more searchable, and
  more cited than the in-region record of the same material
- What that asymmetry does to citation frequency

**Citation frequency tracks removal, not significance**
([bias_register.md](../../../../../packs/documentary-history/methodology/bias_register.md)
§ Survival bias). Material that left is catalogued, photographed, published, and
therefore cited; material that stayed frequently is not. A production that weights
evidence by how often it is cited will systematically over-weight what was taken, and
will do so while believing it is simply following the literature.

Where the studio uses such material, the record of its removal is itself frequently
worth stating on screen. Record what is known about it here.

### 2.4 What is undigitised, uncatalogued, or lost

- Holdings with no catalogue, or a catalogue not consultable remotely
- Holdings catalogued but not digitised, and what reaching them would actually cost
- Material known to have existed and known to be lost, damaged, or destroyed, and how
  that is known
- Material whose original order or provenance was lost in recataloguing — the item
  survives, its context does not
- Backlogs, closures, and holdings in institutional limbo

**Digitisation is not neutral.** What got scanned reflects present institutional
priorities and funding, and now determines what is searchable and therefore what gets
cited. Recording the undigitised portion is how a production avoids mistaking a
funding decision for a historical fact.

### 2.5 What is restricted

Restriction is not a single category and the survey must not flatten it.

| Kind | Records |
|---|---|
| Institutionally restricted | Closed periods, permission requirements, embargoes, legal restrictions |
| Restricted within the tradition | Material whose viewing, hearing, or recounting is restricted by initiation, office, gender, or age. **Wide availability online is not consent** ([pack 07 §3](../../../../../packs/documentary-history/07_cultural_sensitivity.md)). |
| Community-held | Material where an individual's consent is not sufficient to license it, and the survey records the community's decision-making body ([oral history protocol §8](../../../../../packs/documentary-history/methodology/oral_history_protocol.md)) |
| Sensitive by content | Human remains, burial, atrocity, identifiable victims, living lineages — categories requiring advisory review **before generation**, not before publication ([pack 07 §2](../../../../../packs/documentary-history/07_cultural_sensitivity.md)) |
| Personal data | Material whose handling is constrained regardless of its archival status |

The section is written **with the Cultural Advisor**, and it is written before anyone
approaches a holder. Establishing the boundary during a conversation is too late: it
puts the holder in a position where refusing is costly and disclosing is a breach.

### 2.6 What languages the material is in

Per body of material: the language, the script, and — where it is a translated or
transcribed record — every hop between the original and what the researcher will
actually read.

This section drives budget, schedule, and staffing more than any other. If the
relevant material is in a language nobody on the production reads, or exists as an
oral corpus rather than a document, the plan needs a translator or a knowledge holder
**from the outset**. Discovering it in week nine is a re-plan.

It also feeds two things outside research:

- The line's [language register](../languages/README.md), and through it the
  orthography decisions that determine typeface selection and therefore block all
  brand design ([brand/README.md](../../../brand/README.md) §3).
- The pronunciation workflow — every proper noun needs an IPA transcription and a
  reference recording from a speaker
  ([voice_policy.md](../languages/voice_policy.md)).

Record every translation hop explicitly. Each one is a place meaning shifted, and
retranslation from an intermediate language materially weakens the evidentiary chain
and is recorded on the claim when it happens.

### 2.7 What the distribution itself tells you

**The most important section, and the one most likely to be skipped**, because it is
the only one that is not a list.

Having mapped the record, state what its *shape* is evidence of. The recurring
patterns are already enumerated in the
[bias register](../../../../../packs/documentary-history/methodology/bias_register.md)
— written over oral, durable over perishable, coastal over interior, elite over
ordinary, conflict over continuity, removed over in situ — and the survey's job is to
say which of them apply to *this* line's record, where, and how strongly.

Write out, explicitly:

1. **Where the record is dense, and why.** Density is a property of who was recording
   and for what purpose, not of where more happened.
2. **Where it thins, and whether the thinning is about the past or about the
   recording.** Absence of evidence in a record that would not have recorded the thing
   anyway is not evidence of absence.
3. **Whose record it is.** For each major body of material: who made it, for whom, and
   what they were in a position to know.
4. **What periods read as empty on a timeline and are not.** Ordinary decades generate
   silence; crises generate documents. A timeline built from document volume is a
   timeline of crises.
5. **What this constrains about the productions this line can honestly make**, and
   what it means for the ordering of them. Choosing subjects by where the evidence is
   easy is a legitimate production constraint and becomes a dishonest implicit claim
   about where the history was the moment it goes unstated.
6. **Which of these findings belong on screen.** Frequently the nature of the
   surviving record is more interesting than the claim it supports, and saying so is
   the cheapest way this studio distinguishes itself from unsourced history content.

## 3. Completing this document

| Step | Owner |
|---|---|
| Conduct the survey | Research Lead — **not yet named** |
| Review §2.5 and §2.7 | Cultural Advisor — **not yet engaged** |
| Record each finding as a source record where it is a claim about the present-day record | Research Lead |
| Set `archive_landscape_surveyed: true` and `archive_landscape_doc` in [../line.yaml](../line.yaml) | Research Lead |
| Confirm the survey is complete enough to open the line | Showrunner |

A partially completed survey does not satisfy condition 3. The specific failure to
avoid is a survey that maps only what was reachable and calls itself finished — it
will be internally consistent, it will look thorough, and it will encode the
coloniser's cataloguing decisions as the shape of the past.

Re-surveying is expected at the close of each season and whenever a production reaches
into material the survey did not cover. The survey is a living document; a survey
unchanged after a season has not been used.
