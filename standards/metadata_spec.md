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
updated: 2026-08-07
owners: [role-slug, ...]
---
```

### Record documents add their type block

```yaml
---
id: CHR-NG-0007
type: character
line: ng-nigeria
title: ...
status: draft
version: 0.1.0
updated: 2026-08-07
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
| `status` | enum | `draft`, `review`, `locked`, `superseded`, `retracted` |
| `version` | semver | Bump minor on substantive change, patch on correction |
| `updated` | date | ISO. Set by the toolkit on write, not by hand. |
| `owners` | list | Role slugs from [../ops/roles.md](../ops/roles.md), not names — people change roles |
| `claims` | list | Claim IDs this record depends on |
| `sources` | list | Source IDs |
| `sensitivity` | enum | `none`, `review-required`, `held` |
| `advisory_ref` | string | Required when `sensitivity: held` |
| `superseded_by` | string | Required when `status: superseded` |
| `retraction_reason` | string | Required when `status: retracted` |

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
[../bible/06_ai_disclosure_and_ethics.md](../bible/06_ai_disclosure_and_ethics.md) §4
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
