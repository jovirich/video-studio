---
doc: bible/02
title: Evidence and sourcing
status: active
version: 0.1.0
owners: [research-lead]
---

# 02 — Evidence and sourcing

This is the load-bearing document of the studio. Everything else is style.

## 1. The core rule

> **No factual statement reaches a script without a claim ID, and no claim ID
> exists without at least one source record.**

Scripts do not contain facts. Scripts contain *references to claims*. The claim
holds the fact, the confidence level, the sources, and the reviewer signature.

```
                sources/registry/records/SRC-NG-0042.yaml   ← the evidence
                                  ▲
                                  │ cited by
                 sources/registry/claims/CLM-NG-0117.yaml   ← the fact + confidence
                                  ▲
                                  │ referenced by
   productions/ng-nigeria/episodes/S01E01/02_script/narration.md   ← the script
              "... the walls enclosed a substantial area {{CLM-NG-0117}} ..."
```

`studio_ops validate --sources` walks that chain for every reference in every
script. A broken link fails the build. This is not bureaucracy; it is the only way
a small team can honestly answer "where did that come from?" eighteen months later.

## 2. Source tiers

| Tier | Definition | Sufficient alone? |
|---|---|---|
| **T1** | Primary and archival: documents, inscriptions, excavation reports, contemporaneous accounts, material objects with provenance, datasets. | Yes, for `established`, with the caveats in §4. |
| **T2** | Peer-reviewed secondary scholarship: monographs from academic presses, refereed journal articles, critical editions. | Yes, for `established`. |
| **T3** | Reputable general: museum and archive catalogue entries, encyclopedias of record, serious journalism, institutional publications. | No. Supports `probable` at best; requires a T1 or T2 to reach `established`. |
| **T4** | Oral testimony, tradition, and community knowledge, recorded under the protocol in [../research/methodology/oral_history_protocol.md](methodology/oral_history_protocol.md). | Sufficient for the `traditional` register. Not converted into `established` by volume alone. |
| **T5** | Everything else: undated web pages, aggregators, AI output, popular video, social media, uncited compilations. | **Never citable.** May be used to find a lead; never to support a claim. |

**T5 includes any output of a language model.** A model may help locate, summarise,
or structure; its assertions are leads, not sources. This rule is absolute and is
the reason [../prompts/text/](../../prompts/text) contains research *assistance*
templates and no research *authority* templates.

### 2.1 On T4 and the hierarchy

The tier numbers describe *what kind of verification a claim needs*, not *what kind
of knowledge is worth more*. Oral tradition frequently preserves what written
archives never recorded, and colonial-era T1 documents are often less reliable about
African societies than the T4 testimony of people inside them. The correct response
is not to flatten the tiers but to use the right register: T4 material carries the
`traditional` register with named attribution, and it is entirely legitimate for a
T4 account to *contradict* a T1 colonial record on screen, with both stated.

Never launder a T4 account into `established` by finding a T3 that repeats it.
Circular sourcing through repetition is the most common failure in popular history.

## 3. Corroboration requirements

| Target register | Requirement |
|---|---|
| `established` | ≥2 independent sources, at least one T1 or T2. Independence means not derived from a common upstream source — check this explicitly. |
| `probable` | ≥1 T1/T2, or ≥2 T3 that are demonstrably independent. |
| `contested` | Sources for **each** position, at required tier, recorded on the claim. |
| `inferred` | The adjacent evidence recorded, plus a written inference chain on the claim record. |
| `traditional` | ≥1 T4 recorded under protocol, with the holder and context of transmission named. |
| `unknown` | Record what was searched and where, so the next researcher does not repeat it. |

## 4. Interrogating the source, not just citing it

A citation is a location, not a warrant. Every source record carries a
`critique` block answering:

1. **Who made this, when, and for whom?**
2. **What were they in a position to know?** (An eyewitness to a battle knows one
   flank. A treasury clerk knows what was recorded, not what was traded.)
3. **What interest did they have?** Colonial administrators, missionaries, rival
   dynasties, and modern nation-states all had reasons to shape a record.
4. **What has happened to it since?** Translation, transcription, restoration,
   selective preservation, and archival rearrangement all edit the record.
5. **What does its silence mean?** Absence of evidence in a record that would not
   have recorded the thing anyway is not evidence of absence.

The [bias register](methodology/bias_register.md) holds the recurring
patterns so this is not re-derived per source.

## 5. Claim IDs

```
CLM-<LINE>-<NNNN>      e.g. CLM-NG-0117
SRC-<LINE>-<NNNN>      e.g. SRC-NG-0042
SRC-STUDIO-<NNNN>      for cross-line sources
```

IDs are permanent and never reused. A retracted claim is marked `retracted`, keeps
its ID, and records what replaced it. Deleting a claim record destroys the audit
trail that justifies keeping the whole system.

Claims are referenced in prose as `{{CLM-NG-0117}}`. The reference is stripped at
render time and compiled into the episode's citation appendix by
`studio_ops report bibliography`.

## 6. Numbers, dates, and quantities

- Give ranges where sources give ranges. A false precision is a false statement.
- Distinguish **attested**, **estimated**, and **modelled** figures. Record which on
  the claim.
- Currency, distance, and area conversions record the conversion basis and its own
  source.
- Population and casualty figures for pre-census periods are almost always modelled.
  State the model and its author on screen when the number is load-bearing.
- Calendar conversions (Hijri, regnal, agricultural, and local reckonings) record the
  conversion method used.

## 7. Named entities

Every person, place, polity, and organisation that appears on screen gets a record
in the production line's `characters/` or `locations/` folder, carrying:
- the name form used on screen and why it was chosen ([09_localization.md](09_localization.md) §3),
- alternative and historical name forms,
- the claims that reference it.

This is what makes cross-episode consistency mechanical instead of hopeful.

## 8. Retention

Source scans, recordings, transcripts, and correspondence are retained in the asset
store under the source record's ID for the life of the studio plus seven years, or
per the consent form where a contributor set a shorter term. Restricted material
follows [../docs/runbook/restricted_records.md](../../docs/runbook/restricted_records.md).

## 9. What a researcher does when the evidence runs out

In order:
1. Record an open question in [../research/open_questions/](../../templates/records).
2. Change the register down, not the claim up.
3. If the sequence cannot survive the honest register, cut the sequence.
4. Never fill the gap with a plausible reconstruction stated as fact. Never ask a
   model to fill it.

Step 4 is the reason this document exists.
