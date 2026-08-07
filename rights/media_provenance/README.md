---
title: Media provenance
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer, rights-and-clearances]
---

# Media provenance

How the provenance of a production travels with the media once it leaves the
repository.

Inside the repository, provenance is the manifest. Outside it, the manifest is not
present — a viewer has an MP4, a platform has a transcode, an archive has a master.
This folder is about the four mechanisms that carry the claim across that boundary,
and about which of them actually survive it.

Canon: [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §3
and §4; [../../standards/metadata_spec.md](../../standards/metadata_spec.md) § Media
metadata; [../../standards/delivery_specs.md](../../standards/delivery_specs.md).

**Nothing in this folder is IMPLEMENTED.** Every mechanism below is either **DESIGNED**
or **NOT BUILT**, and the table says which. No master has been produced, no manifest
has been frozen, no hash has been embedded, and no Content Credential has been signed.

## The four mechanisms

| # | Mechanism | What it carries | Survives re-encode? | Maturity |
|---|---|---|---|---|
| 1 | **The frozen manifest** | Everything: every asset, its origin, its prompt card, its seed, its clearance reference | n/a — it does not travel with the media | **DESIGNED** |
| 2 | **`provenance_manifest_sha256` in media metadata** | A 64-hex fingerprint binding this file to one exact manifest | No — container metadata is commonly stripped | **NOT BUILT** |
| 3 | **C2PA / Content Credentials** | Signed assertions generated from the manifest | Sometimes — platform-dependent, and the platform decides | **NOT BUILT** |
| 4 | **The published provenance summary** | A human-readable per-production page: which shots were generated, with what, from which prompt | Yes — it is a separate published artefact and nothing can strip it | **NOT BUILT** |

They are listed in decreasing order of completeness and **increasing order of
durability**. That inversion is the whole design problem: the richest record is the one
that travels worst, and the one that survives everything is a web page the studio
publishes itself.

## 1. The manifest

`manifest.yaml` per production, validated against
[../../standards/schemas/asset_manifest.schema.json](../../standards/schemas/asset_manifest.schema.json).

Every asset that reaches the edit appears in it — generated or not. An archival scan
needs provenance at least as much as a render does, and the schema requires the block
for both. Per asset: `sha256`, `origin`, `provenance_class`, the generation block
(tool, model, prompt card, seed, parameters, inputs, who and when) for generated
material, and the acquisition block (source record, `clearance_ref`, credit line,
restrictions) for everything else.

At delivery the manifest is **frozen** — `frozen: true` — and from that moment it is
the object the delivered media is bound to. Freezing is not a formality: an unfrozen
manifest can be edited after a master is cut, and a provenance record that can change
after the fact evidences nothing.

The mechanism that makes the manifest more than documentation is the **conform step**:
an asset absent from the manifest cannot be conformed into the edit, and the pipeline
refuses it. That refusal is the platform's traceability guarantee. It is **DESIGNED**
and **NOT BUILT** — `automation/studio_ops/pipeline/manifest.py` does not exist. Today
the guarantee rests on people, which is to say it rests on nothing that can be
audited.

## 2. The manifest hash in media metadata

The packaging step writes `provenance_manifest_sha256` — the SHA-256 of the frozen
manifest file — into the delivered file's container metadata, alongside title, episode,
copyright, language, description, and creation date
([../../standards/metadata_spec.md](../../standards/metadata_spec.md) § Media metadata).

What this buys, precisely: given a file and a copy of the manifest, anyone can prove
they belong together. Change one byte of the manifest and the hash no longer matches;
re-cut the master and the manifest is re-frozen and re-hashed. It is a binding, not a
signature — it says *this file was delivered against this manifest*, and it says
nothing about who made either.

What it does not buy: durability. Container metadata is routinely stripped by upload
pipelines, transcoders, and social platforms. Treat mechanism 2 as reliable for the
studio's own archive and for a direct delivery to a broadcaster, and as unreliable for
anything a platform has re-encoded.

**Maturity: NOT BUILT.** No packaging step exists.

## 3. C2PA / Content Credentials

Applied at delivery **where the distribution platform supports it**
([../../standards/delivery_specs.md](../../standards/delivery_specs.md);
[../../packs/documentary-history/04_visual_language.md](../../packs/documentary-history/04_visual_language.md) §7
treats metadata as one of the three disclosure layers).

Assertions are generated from the manifest rather than authored separately, so there is
one source of truth and no second description of the same production to drift.

Three honest caveats, all of which belong in the design and not in a footnote after
launch:

- **Support is the platform's decision, not the studio's.** Whether credentials survive
  an upload, and whether they are displayed if they do, is checked per platform and
  per delivery. Core/03 already frames this as something to verify rather than assume.
- **Signing requires an identity and a key.** Who signs, with what credential, and how
  that key is held and rotated is `TBD`. Owner: Pipeline Engineer, with the Showrunner
  on the identity question, before the first delivery. This is not a detail — an
  unsigned assertion is a claim with nobody behind it.
- **A credential is not a truth claim.** It states what was done to the file and by
  whom. It does not state that the content is accurate. Nothing in this platform's
  disclosure posture should imply otherwise.

**Maturity: NOT BUILT.**

## 4. The published provenance summary

Core/01 §3 level 4: a per-production provenance summary published alongside the
production, generated from the manifest by `studio_ops report provenance`. *(NOT BUILT)*

> A viewer who wants to know exactly which shots were generated, with which tool, from
> which prompt, can find out.

This is the mechanism that does not depend on anyone else's pipeline. It cannot be
stripped by a transcoder, does not need a platform to support a standard, and does not
require the viewer to have a tool. It is also the one that makes the other three
verifiable from outside: given the summary and the file, a third party can check the
claim.

It is generated, never written. A hand-written provenance page is a second description
of the production, and the second description is the one that is out of date.

**Maturity: NOT BUILT.** `studio_ops report provenance` does not exist. Until it does,
the platform's most distinctive disclosure commitment is a specification.

## When published material changes

If a production is re-cut, re-graded, or altered after publication — including as the
result of a request in [../permissions/takedown_log.md](../permissions/takedown_log.md) —
then:

1. The manifest is re-frozen and re-hashed. The old hash is retained in history, not
   overwritten.
2. The delivered media carries the new hash.
3. Any Content Credentials are re-generated and re-signed.
4. **The published provenance summary is re-published**, and it says that it changed
   and when.

A silent edit to published material is a provenance failure. The whole point of level 4
disclosure is that the record matches what the audience can actually watch; a summary
describing a master that no longer exists is worse than no summary, because it is
confidently wrong.

## What this folder does not contain

- **Media.** Binaries live in the asset store; git holds manifests. See
  [../../CONTRIBUTING.md](../../CONTRIBUTING.md) § Writing rules.
- **Per-production manifests.** They live with their production, not here. This folder
  holds the *specification* of how provenance travels, not the instances.
- **Any claim that a mechanism works.** Nothing here has been exercised. The first
  thing that would move any row above off **NOT BUILT** is the asset-store round trip
  named in [../../docs/status.md](../../docs/status.md) § What "TESTED" would require:
  ingest → manifest → conform → package.
