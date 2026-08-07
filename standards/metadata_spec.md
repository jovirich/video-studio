# Metadata specification

Every document and record in this repository carries structured metadata. This is
what makes the repository queryable — `studio_ops report` and every validator read
front matter, not prose.

## Markdown front matter

YAML, delimited by `---`, first thing in the file.

### Minimum for any document

```yaml
---
title: Human-readable title
status: draft | review | locked | superseded | retracted
version: 0.1.0
updated: "2026-08-07"    # quoted — see § Dates below
owners: [role-slug, ...]
---
```

### Capability documents add `maturity`

Any document describing a *capability* — a tool, a validator, a pipeline step, a
workflow — carries a maturity label. `status` describes the **document**; `maturity`
describes the **thing the document describes**. They are independent: a `locked`
specification of a `NOT BUILT` tool is a perfectly coherent state, and a common one.

```yaml
---
title: Schema validator
status: locked            # the doc is final
maturity: NOT_BUILT       # the code does not exist
---
```

| `maturity` | Means | Evidence required |
|---|---|---|
| `DESIGNED` | Structure or spec exists on paper. No code runs. | The document exists and is internally consistent |
| `IMPLEMENTED` | Code exists and executes. Not proven at production scale. | The command runs and produces output |
| `TESTED` | Exercised against a real workload, with a recorded, reviewable result. | A test run, report, or dated artefact |
| `NOT_BUILT` | Specified, no code. An honest state, not a failure. | — |

**A bare ✅ or "complete" is prohibited** in place of these labels. It reads as
*working* when it usually means *specified*.

Promotion requires naming the evidence, and the ledger at
[../docs/status.md](../docs/status.md) is updated in the **same commit** that changes
a capability's maturity.

### Record documents add their type block

```yaml
---
id: CHR-NG-0007
type: character
line: ng-nigeria
title: ...
status: draft
version: 0.1.0
updated: "2026-08-07"    # quoted — see § Dates below
owners: [research-lead]
claims: [CLM-NG-0117, CLM-NG-0118]
sources: [SRC-NG-0042]
sensitivity: none | review-required | held
advisory_ref: ADV-NG-0004     # required if sensitivity is held
---
```

### Episode documents add

```yaml
---
episode: S01E01
line: ng-nigeria
stage: 02_script
gate_blocking: script-lock | none
---
```

## Field reference

| Field | Type | Rules |
|---|---|---|
| `id` | string | Must match [id_system.md](id_system.md). Immutable. |
| `type` | enum | One of the schema types in [README.md](README.md) § Schema index |
| `line` | string | Production line code, or `studio` |
| `status` | enum | **Records:** `draft`, `review`, `locked`, `superseded`, `retracted`. **Standing documents** (canon, standards, ops, docs — things that are maintained rather than signed off): `active`, `template`, `deprecated`. The two vocabularies are separate because a record moves toward a signature and a standing document never does. |
| `version` | semver | Bump minor on substantive change, patch on correction |
| `updated` | date | ISO. Set by the toolkit on write, not by hand. |
| `owners` | list | Role slugs from [../ops/roles.md](../ops/roles.md), not names — people change roles |
| `claims` | list | Claim IDs this record depends on |
| `sources` | list | Source IDs |
| `sensitivity` | enum | `none`, `review-required`, `held` |
| `advisory_ref` | string | Required when `sensitivity: held` |
| `superseded_by` | string | Required when `status: superseded` |
| `retraction_reason` | string | Required when `status: retracted` |

## Dates are quoted

Always write `updated: "2026-08-07"`, with quotes.

Unquoted, YAML resolves it to a **date object**, not a string. Every schema types
date fields as strings via `_common#/$defs/isoDate`, so an unquoted date fails
validation — and worse, where a schema is lenient it passes while the ISO pattern is
never actually enforced, which is the silent version of the same bug.

This bites everyone once. It is called out here rather than left to be rediscovered.

## The `TBD` convention

A field whose value is not yet known is written as:

```yaml
runtime_target: TBD
```

or in prose as `TBD — <what is needed to resolve it>`.

- `TBD` is **legal** while `status` is `draft` or `review`.
- `TBD` is **illegal** at `status: locked` — the validator fails.
- A `TBD` in a `review`-status record must have a linked open question.

This is deliberate and important: it makes "we do not know yet" a first-class,
trackable state, so nobody is tempted to write something plausible to make a
template look finished.

## Media metadata

Applied to delivered media by the packaging step:

| Field | Source |
|---|---|
| `title`, `episode`, `season`, `series` | `episode.yaml` |
| `copyright` | studio config |
| `language` | line config |
| `description` | `10_publish/description.md` |
| `creation_date` | delivery date |
| `provenance_manifest_sha256` | hash of the frozen `manifest.yaml` |
| C2PA assertions | generated from the manifest |

## Asset records

Every asset in `manifest.yaml` carries the block defined in
[../bible/06_ai_disclosure_and_ethics.md](../core/01_provenance_and_ai_disclosure.md) §4
and validated by `asset_manifest.schema.json`. Required for **all** assets, not just
generated ones — an archival scan needs provenance at least as much as a render does.

## Anti-patterns

- **Names in `owners`.** Use role slugs. A record owned by "Chidi" becomes orphaned
  when Chidi changes role; a record owned by `research-lead` never does.
- **Free-text status.** `status: mostly done` fails validation, correctly.
- **Hand-edited `updated`.** The toolkit sets it. A hand-set date is a lie waiting
  to happen.
- **Duplicated facts in front matter.** Front matter holds *references*, not copies.
  If a date appears in both a claim record and a character record, they will diverge.
