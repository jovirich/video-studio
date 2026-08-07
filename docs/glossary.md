---
doc: bible/11
title: Glossary
status: active
version: 0.1.0
owners: [pipeline-engineer]
---

# 11 — Glossary

Terms of art used across this repository. Where a term has a general meaning and a
specific meaning here, the specific meaning governs.

## Structure

| Term | Meaning here |
|---|---|
| **Studio** | The whole enterprise: African History Studio. The top tier of the repo. |
| **Production line** (or **line**) | A country- or region-scoped strand of production, e.g. `ng-nigeria`. Owns its own research, characters, locations, advisory board, and visual identity; inherits everything at studio level. |
| **Slate** | A line's roadmap of planned and in-progress episodes. |
| **Episode** | One self-contained unit of production with its own folder and its own gates. |
| **Sequence** | A contiguous group of shots serving one narrative beat. The unit at which style is inherited. |
| **Shot** | The atomic visual unit. Has a record, a provenance class, and (if generated) a prompt card. |

## Evidence

| Term | Meaning here |
|---|---|
| **Source record** | `SRC-*`. A described, tiered, critiqued item of evidence. Lives in `sources/registry/records/`. |
| **Claim** | `CLM-*`. A single factual statement with a confidence register and its supporting sources. Lives in `sources/registry/claims/`. |
| **Claim ID reference** | `{{CLM-NG-0117}}` inline in a script. Stripped at render; compiled into the citation appendix. |
| **Tier** | T1–T5 classification of a source's evidentiary weight. See [02_evidence_and_sourcing.md](02_evidence_and_sourcing.md) §2. |
| **Register** | The level of certainty a statement claims: `established`, `probable`, `contested`, `inferred`, `traditional`, `unknown`. |
| **Open question** | A recorded gap in the evidence. Lives in `research/open_questions/`. Not a failure — a research artefact. |
| **Corroboration** | Support from an *independent* source. Two sources sharing an upstream origin are one source. |
| **Critique block** | The mandatory interrogation of a source: who made it, for whom, with what interest, and what its silence means. |

## Generation

| Term | Meaning here |
|---|---|
| **Prompt card** | `PC-*`. A versioned, structured, reviewable specification for one generated asset. Not a text string — a record. See [../prompts/README.md](../prompts/README.md). |
| **Style block** | The inheritable visual specification a prompt card receives from its sequence and line. |
| **Style anchor** | A fixed, versioned reference image with a checksum, referenced by ID from prompt cards to hold continuity. |
| **Provenance class** | What kind of image a shot is: `archival`, `contemporary`, `artefact`, `reconstruction`, `interpretive`, `graphic`, `text_on_screen`. |
| **Reconstruction** | Generated depiction grounded in evidence, labelled as such. |
| **Interpretive** | Generated imagery that evokes rather than depicts. Also labelled. |
| **Manifest** | `manifest.yaml`. The episode's ledger of every asset, generated or not, with full provenance. |
| **Seed** | The value that makes a generation reproducible. Recorded on every generated asset. |
| **Chain** | A multi-tool recipe: e.g. still → upscale → motion → grade. Lives in `prompts/chains/`. |

## Process

| Term | Meaning here |
|---|---|
| **Gate** | A named review with a named owner and a checklist. Six exist: fact-check, sensitivity, rights, script lock, picture lock, audio lock, plus technical QC at delivery. |
| **Lock** | The point after which a stage's output cannot change without a documented re-open. |
| **Advisory hold** | A stop on work imposed by any contributor via a sensitivity issue, released only by a written Cultural Advisor ruling. |
| **Greenlight** | The decision to begin an episode. Requires a brief, a question, an advisory coverage check, and a budget. |
| **Source lock** | The point after which the research pack is fixed for scripting. New evidence after source lock requires a re-open. |
| **Canon** | The Bible plus the schemas. What `validate --canon` enforces. |
| **Line bible** | A production line's addendum to the studio Bible, covering only what is line-specific. |

## Technical

| Term | Meaning here |
|---|---|
| **`studio_ops`** | The Python toolkit in `automation/`. Invoked as `python -m studio_ops` or `studio`. |
| **Asset store** | Where media lives. Not git. Configured by `ASSET_STORE_*` in `.env`. |
| **Record** | Any YAML or front-mattered Markdown file validated against a schema in `standards/schemas/`. |
| **Adapter** | A stub interface to a generation vendor in `automation/studio_ops/adapters/`. Deliberately not implemented; wiring one is a deliberate act with a cost ceiling. |
| **M&E** | Music and effects stem — the full mix minus narration and dialogue, required for dubbing. |
| **C2PA / Content Credentials** | Cryptographic provenance metadata attached to media. Applied at delivery where supported. |
