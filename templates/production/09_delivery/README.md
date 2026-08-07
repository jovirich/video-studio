---
title: 09_delivery — the delivery package
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer]
---

# 09_delivery

Where the production becomes a set of files that can leave the building. The
technical QC gate — the one gate every canon pack has, whatever its genre — is
signed here, because this is where the platform's own guarantees are verified rather
than assumed.

## Package structure

From [../../../standards/delivery_specs.md](../../../standards/delivery_specs.md)
§ Delivery package. Assembled by `studio_ops pipeline package` (**NOT BUILT** —
[../../../docs/status.md](../../../docs/status.md)).

```
S00E00_v01/
├── master/            archival master + textless master
├── web/               H.264 / H.265 renders
├── audio/             full mix + all stems, including M&E
├── captions/          per language, SRT + VTT
├── artwork/           thumbnails, title card, key art
├── documents/         cue_sheet.csv, chain_of_title.pdf, credits.md,
│                      provenance_summary.md, sources.md, corrections.md
└── manifest.yaml      the production manifest, frozen at delivery
```

`master/` renders live under `masters/` in the working tree and are gitignored —
they are large and derivable. The package is assembled outside git; what git holds
is the manifest and the documents.

## The documents folder is not an afterthought

Everything in `documents/` is generated from records that already exist. If any of
them cannot be generated, the corresponding record set is incomplete, and that is
the finding — not the missing document.

| Document | Generated from | What its absence means |
|---|---|---|
| `cue_sheet.csv` | Music cues and their rights basis | Blocks the rights gate; a cue sheet assembled after delivery is assembled from memory |
| `chain_of_title.pdf` | Clearance records, consents, releases | The studio cannot show it has the right to distribute what it is distributing |
| `credits.md` | Contributor records and the AI-use statement | Somebody who was promised a credit does not get one |
| `provenance_summary.md` | The manifest | The per-episode disclosure the platform promises does not exist |
| `sources.md` | The claim and source registry | The evidence layer that distinguishes this work from an essay is missing |
| `corrections.md` | The line's corrections log | Corrections have nowhere to land after publication |

## Freezing the manifest

At delivery, [../manifest.yaml](../manifest.yaml) is set to `frozen: true`, hashed,
and the hash is embedded in the delivered media metadata. A file in the world can
then be tied back to the exact record set that produced it.

This is the strongest traceability claim the platform makes, and it is worth being
precise about what it is not: it does not prove the claims are true. It proves that
what shipped is what the records describe, and that the records were not edited
afterwards to fit.

## Before this stage starts

Every one of these is signed:

| Gate | Owner |
|---|---|
| Fact-check | Research Lead |
| Sensitivity (third pass) | Cultural Advisor |
| Rights | Rights & Clearances |
| Picture lock | Visual Director |
| Audio lock | Audio Lead |

**No asset in the manifest is at `rights_status: pending`.** Not "expected to clear".
The rights gate blocks this stage for exactly this reason: an asset that clears after
delivery cleared too late, and one that does not clear after delivery is a takedown.

## Before this stage can be left

The **technical QC** gate is signed by the Pipeline Engineer, certifying:

1. **Delivery specs met** — resolution, frame rate, codec, colour space, levels,
   loudness, true peak. Measured and reported, not asserted.
2. **Captions validate** — encoding, line count, characters per line, reading speed,
   cue gaps, speaker IDs.
3. **The provenance manifest is complete and frozen.**
4. **Content Credentials applied** where the platform supports them.
5. **The package is assembled** at the structure above.
6. **The evidence layer is generated** — sources page, provenance summary,
   corrections log.

## What is not checked here

Whether the production is any good, and whether the claims are true. Technical QC
verifies that the signatures exist, the specs are met, and nothing skipped a gate.
Truth is a human's signature at the fact-check gate; this gate only checks that the
signature is there and that the file it applies to is the file that shipped.
