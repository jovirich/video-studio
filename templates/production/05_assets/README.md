---
title: 05_assets — media, and why none of it is here
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer, visual-director]
---

# 05_assets

**Media never enters git. The manifest does.**

This directory is a shape, not a store. Every subfolder below ships with a
`.gitkeep` and nothing else, and that is the finished state.

```
05_assets/
├── stills/      generated and acquired still images
├── video/       generated and acquired moving image
├── voice/       narration, testimony, reference reads
├── music/       score, beds, stings
├── sfx/         effects and designed sound
├── graphics/    titles, lower thirds, charts, diagrams
├── maps/        map renders and their project files
└── archival/    scans and reproductions of genuine historical items
```

## Why media is not in git

Not preference. Four hard reasons:

1. **Git stores every version of every binary, forever.** A production's renders
   run to hundreds of gigabytes across versions. A repository that has ingested
   them once cannot be un-poisoned by deleting the files; the history keeps them,
   and every future clone pays for them.
2. **Diffs are meaningless on binaries**, so the thing git is for — showing what
   changed and letting a human review it — does not happen.
3. **Merge conflicts on a render are unresolvable.** There is no reconciling two
   versions of a frame.
4. **Rights and consent are revocable.** A cleared-then-refused image can be
   removed from an asset store. Removing it from git history means rewriting every
   downstream clone, and in practice it means it is still there.

The `05_assets` name is in the toolkit's ignore list
([../../../automation/](../../../automation/)), so validators do not walk it and
`.gitignore` keeps its contents out. A link *into* this directory is treated as a
specification rather than a broken reference, which is why the paths above resolve
in documentation without the files existing.

## What is the record, then

[../manifest.yaml](../manifest.yaml). One entry per asset, generated or not,
carrying:

| | |
|---|---|
| Identity | `asset_id`, `filename`, `store_path` |
| Integrity | `sha256`, `bytes` — computed on ingest, never typed by hand |
| Provenance | `origin` and either the full `generation` block or the full `acquisition` block |
| Meaning | `provenance_class`, and `evidence_basis` for reconstructions |
| History | `post_process`, ordered — every step that altered the asset |
| Disclosure | `label` — required, and whether applied |
| Rights | `rights_status` — nothing ships at `pending` |
| Review | sensitivity, anachronism, technical QC |

**An asset absent from the manifest cannot be conformed into the edit.** The
pipeline refuses it. That refusal is the mechanism behind the platform's
traceability guarantee — every other statement about traceability in this
repository is a description of that one behaviour.

## Naming

Fixed by [../../../standards/naming_conventions.md](../../../standards/naming_conventions.md)
§ Assets:

```
<EPISODE>_<SEQ>_<SHOT>_<class>_<slug>_v<NN>.<ext>
```

The slug describes **content**, never tool or settings. Tool, model, seed, and
parameters live in the manifest and on the prompt card, where they can be queried.
A filename that encodes settings is unreadable in a bin, unsearchable, and wrong the
moment the asset is re-rendered.

Versions increment on every re-generation or re-render. `_v01`, `_v02`. Never
`_final` — the validator rejects it, and the reason it rejects it is that `_final`
has never once in the history of post-production been final.

## The asset store

Where the bytes actually live, its layout, backup policy, and retention are the
Pipeline Engineer's, and are **NOT BUILT**. See
[../../../docs/status.md](../../../docs/status.md) for the honest position before
planning around it.

Two rules hold regardless of what the store turns out to be:

- **Unpublished archival scans, interview recordings, and restricted material never
  reach a third-party model endpoint** unless the vendor contract carries a
  no-training term and the source's permission covers that use.
  ([../../../core/01_provenance_and_ai_disclosure.md](../../../core/01_provenance_and_ai_disclosure.md) §6.)
- **Nothing is deleted from the store during a production.** Rejected runs are part
  of the record; a card's `runs` history references assets that were not selected,
  and deleting them breaks the audit trail that makes the selection reviewable.
