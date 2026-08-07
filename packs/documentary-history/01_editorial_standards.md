---
doc: bible/01
title: Editorial standards
status: active
version: 0.1.0
owners: [showrunner, research-lead]
---

# 01 — Editorial standards

## 1. The accuracy standard

A statement may appear in narration, on-screen text, or a graphic only if it meets
the evidence standard in [02_evidence_and_sourcing.md](02_evidence_and_sourcing.md)
and is expressed at a level of certainty the evidence supports.

Three failure modes are treated as equally serious:

| Failure | Example shape | Why it is equally bad |
|---|---|---|
| **False statement** | Asserting something the sources do not support. | Obvious. |
| **Overclaimed statement** | Stating as settled what is contested; giving a precise date where sources give a range. | Indistinguishable from a false statement to a viewer who cannot check. |
| **Misleading true statement** | A true fact placed so as to imply something false; a real image captioned to suggest a different time or place. | Deceives more efficiently than a lie, and is harder to retract. |

The third is the one that kills documentaries. Most of the review effort in
[08_review/](../templates/episode/08_review/) is aimed at it.

## 2. Registers of certainty

Narration must select a register that matches the evidence. These map to the
`confidence` field on every claim record.

| Register | Use when | Verbal form |
|---|---|---|
| `established` | Multiple independent sources at required tier agree; no live scholarly dispute. | Plain assertion. "The city walls enclosed X." |
| `probable` | Good evidence, some gaps, no serious counter-position. | "The evidence indicates…", "Most likely…" |
| `contested` | Competent scholars hold materially different positions. | Name the positions. "Historians divide on this. One reading holds… another holds…" |
| `inferred` | Not attested directly; reconstructed from adjacent evidence. | "No record survives of X, but Y and Z together suggest…" |
| `traditional` | Held in oral tradition or received account; not independently corroborated. | Attribute the tradition. "In the accounts kept by…", never "It is said that…" (which attributes to nobody). |
| `unknown` | The honest answer. | Say so. "We do not know." |

A script that never uses `unknown` across a full episode is not a careful script; it
is an incurious one. The Research Lead should treat its absence as a smell.

## 3. Attribution discipline

- **Passive attribution is banned.** "It is believed", "some say", "historians think"
  without a named referent are prohibited patterns and are flagged by
  `studio_ops validate --canon`.
- Where a position belongs to a named scholar or tradition, name it.
- Where a colonial-era record is the only source, say so, and say what that record's
  author was in a position to know. See
  [../research/methodology/bias_register.md](../research/methodology/bias_register.md).
- Numbers get their basis. "An estimated N, on the basis of X" — never a bare figure.

## 4. Corrections

1. Any contributor or viewer may report an error. The intake path is a
   `[source]` or `[sensitivity]` issue, or the public correction address.
2. The Research Lead triages within **5 working days**.
3. If confirmed:
   - **Material error** (changes a viewer's understanding): the episode is
     re-cut or, if re-cut is impractical, an on-screen correction card is added and
     the description carries the correction at the top.
   - **Minor error** (spelling, name form, date within stated range): corrected in
     the description and the correction log.
4. Every correction is recorded in the production line's `corrections.md`, which is
   append-only and public. Nothing is silently deleted.
5. Corrections are not embarrassments to be minimised. A visible correction log is
   the strongest available evidence that the rest of the work is honest.

## 5. Conflicts of interest

Declared in the episode brief. A conflict exists where a contributor, advisor, or
funder has a personal, financial, political, communal, or institutional stake in how
a subject is portrayed. Declaration does not disqualify; concealment does.

## 6. Reconstruction and dramatisation

Reconstructed sequences are permitted and are governed by
[03_narrative_doctrine.md](03_narrative_doctrine.md) §5 and
[04_visual_language.md](04_visual_language.md) §6. Two rules are absolute:

- A reconstruction is visually and audibly distinguishable from evidence.
- A reconstruction does not put specific words in a specific historical person's
  mouth unless those words are documented, in which case they are attributed to the
  document on screen.

## 7. Anonymous and sensitive contributors

Where a contributor's safety depends on anonymity, the source record is held with
restricted access and the on-screen credit is anonymised. The Research Lead and
Showrunner hold the identity; it does not enter the git repository in any form.
See [../docs/runbook/restricted_records.md](../docs/runbook/restricted_records.md).

## 8. Political and contemporary material

Historical work touches live politics, especially where it concerns borders,
succession, land, and violence within living memory.

- The series does not adjudicate present-day political disputes.
- Where a historical question is load-bearing for a current dispute, that fact is
  stated plainly rather than pretended away.
- Where a period is within living memory, testimony from those who lived it is
  sought before secondary literature is treated as final.

## 9. Enforcement

| Standard | Gate | Validator |
|---|---|---|
| §1, §2 | Fact-check | `validate --sources` checks every claim ID resolves at required tier |
| §3 | Fact-check | `validate --canon` flags passive-attribution patterns |
| §4 | Post-publish | corrections log presence checked at delivery |
| §5 | Greenlight | brief requires a conflicts field |
| §6 | Picture lock | reconstruction shots require the `reconstruction` flag on the shot record |
