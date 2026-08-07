---
title: Asset storage
status: active
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer]
---

# Asset storage

**Maturity: DESIGNED, NOT BUILT.** Nothing in this runbook is implemented. The
`ASSET_STORE_*` variables in [`.env.example`](../../.env.example) are read by no code;
`studio_ops pipeline` exits NOT BUILT; no round trip — ingest → manifest → conform →
package — has ever been run. Follow the contract by hand and record what you did. See
[../architecture/refinements_before_episode_one.md](../architecture/refinements_before_episode_one.md)
item 7.

## The contract, in one line

> **Media never goes into git. The manifest does.**

Everything else here follows from that sentence.

## Why the split

| | Git | Asset store |
|---|---|---|
| Holds | Records, scripts, prompt cards, manifests, checklists — text | Media: scans, recordings, renders, stems, masters, style anchors |
| Sized in | Kilobytes | Terabytes |
| History | Permanent and complete, by design | Versioned by convention; supersession is a new file, never an overwrite |
| Copied to | Every clone, forever | Nothing, unless explicitly pulled |

A 4 GB render committed once is in the history of every clone forever, and git does
not forget it when you delete the file. Two commits like that and a fresh clone takes
half an hour, which is the point at which people stop cloning and start emailing
files, which is the point at which provenance stops.

The manifest is the join. It is text, it is in git, it is diffable and reviewable, and
it is what a gate signs against. The bytes it points at live somewhere a gate never
has to read.

## Path convention

```
<store-root>/
  <studio>/
    <line>/
      sources/                 SRC-scoped originals: scans, recordings, transcripts
        SRC-NG-0042/
          SRC-NG-0042_kano-chronicle-scan_p001.tif
      productions/
        S01E01_slug/
          generated/           model output, pre-post
          post/                upscales, grades, plates
          renders/             sequence and cut renders
          stems/               M&E and full mix stems
          masters/             delivered masters
      anchors/                 STA-* style anchors, versioned, checksummed
```

Rules:

1. **The first path segment after the line is the record type**, so a path says what a
   thing is without opening it.
2. **A file under `sources/` sits in a folder named for its source record ID.** That is
   the join back to `SRC-*`, and it is why the ID goes in the folder name and not only
   in the filename.
3. **Names follow `standards/naming_conventions.md`**: no spaces, ASCII only, ISO
   dates, numeric zero-padded versions (`_v01`), no `final`/`latest`/`new`.
4. **Nothing is overwritten.** A revised asset is a new file with a new version
   suffix and a new manifest entry. The old entry stays; supersession is recorded, not
   performed by deletion.
5. `05_assets/`, `masters/`, `renders/`, and `stems/` are in the validators' tolerated
   -missing list — a *link* into them is a specification, not a broken reference. That
   tolerance exists precisely because these paths are correct and their contents are
   correctly absent from git.

## Configuration

From [`.env.example`](../../.env.example). `.env` is gitignored and must never be
committed; the CI secret scan rejects a tracked `.env`, `*.pem`, `*.key`, or
`service_account*.json`.

| Variable | Meaning | Notes |
|---|---|---|
| `ASSET_STORE_DRIVER` | `local` \| `s3` \| `r2` \| `gcs` | Start with `local`. Prove the round trip before adding a network. |
| `ASSET_STORE_LOCAL_PATH` | Store root for the `local` driver | Defaults to `../ahs-assets` — a **sibling** of the repo, never inside it. Inside the repo it will eventually be committed by accident. |
| `ASSET_STORE_BUCKET` | Bucket name | `s3`/`r2`/`gcs` |
| `ASSET_STORE_REGION` | Region | `s3`/`gcs` |
| `ASSET_STORE_ENDPOINT` | Custom endpoint | Required for `r2`; used for S3-compatible stores |
| `ASSET_STORE_ACCESS_KEY_ID` / `ASSET_STORE_SECRET_ACCESS_KEY` | Credentials | Never in git. Rotate on any suspected exposure — see [incident_response.md](incident_response.md). |

No asset-store variable is required to run `python -m studio_ops validate`. Validation
is offline by design, so a validation result never depends on a bucket being
reachable. See [environment.md](environment.md).

### Driver notes

| Driver | Use for | Watch |
|---|---|---|
| `local` | Development, single-operator work, the first round-trip proof | It is one disk. It is not a backup. |
| `s3` | Team scale, lifecycle rules, versioning | Enable bucket versioning and object lock before ingesting anything you cannot regenerate. |
| `r2` | Same as `s3` without egress charges — relevant when an editor pulls a large working set repeatedly | Requires `ASSET_STORE_ENDPOINT` |
| `gcs` | Where the rest of the stack already is | — |

Whichever driver, the *path convention above does not change*. That is the point of
having a driver abstraction, and it is why the round trip should be proved on `local`
first: a driver swap must be a configuration change and nothing else.

## Integrity: SHA-256 on every asset

**Every asset gets a SHA-256 at ingest, recorded in the manifest, before anything else
happens to it.**

| Point | Action |
|---|---|
| Ingest | Hash the file as received. Record hash, byte size, and ingest timestamp in the manifest entry. |
| Any transfer between stores or machines | Re-hash on arrival; compare. |
| Conform into an edit | Re-hash; refuse the clip on mismatch. |
| Delivery / package | Re-hash everything in the package; the hash list ships with the chain of title. |
| Annual backup verification | Re-hash a sample — see below. |

Hashing is not about malice. It is about silent corruption: a truncated transfer, a
bad sector, a sync tool that resolved a conflict by picking one side, a "helpful"
cloud client that re-encoded a file. All of these are quiet, and all of them are
discovered at the worst moment without a hash.

A hash also makes a **style anchor** meaningful. An anchor referenced by ID from a
prompt card only holds continuity if the bytes behind the ID never change; the
checksum is what turns that from a hope into a check.

## Backup rule

> **Two copies, in two locations, one of them offline. Verified annually.**

| Element | Requirement | Why that element |
|---|---|---|
| Two copies | Independent media, not two folders on one disk | One disk fails |
| Two locations | Geographically separate | Fire, flood, theft, and building access do not respect folders |
| One offline | Physically disconnected, or immutable/object-locked so no live credential can delete it | Ransomware and a mistaken `rm -rf` both propagate to every *connected* copy, including the cloud one |
| Verified annually | Restore a random sample and compare hashes. Record the date and the result. | An unverified backup is a belief. Restores fail for boring reasons — expired credentials, a changed path convention, an unreadable archive format — and every one of them is discovered during a restore unless you look first. |

Retention for source material is set by the pack:
[`02_evidence_and_sourcing.md`](../../packs/documentary-history/02_evidence_and_sourcing.md)
§8 — life of the studio plus seven years, or shorter where a contributor's consent
form set a shorter term. **The consent form wins.** Restricted material has its own
rules; see [restricted_records.md](restricted_records.md).

## When a hash mismatches

A mismatch means the file is not the file the manifest describes. It does not tell you
which one is wrong.

1. **Stop using the file.** Do not conform it, do not render with it, do not overwrite
   the other copy with it. If it is already in a cut, mark the shot and continue —
   step 6 decides what happens to the cut.
2. **Do not re-hash and update the manifest.** Overwriting the recorded hash with the
   current one converts an integrity failure into a silent falsehood, permanently.
   This is the only genuinely irreversible mistake in this procedure.
3. **Establish which copy is right.** Hash the same asset in every location — primary,
   secondary, offline. A majority agreeing with the manifest means the odd one out is
   corrupt. Everything disagreeing with the manifest means the manifest entry itself
   is suspect, or the asset was overwritten in place at some point.
4. **Restore from a copy whose hash matches the manifest.** Re-hash after restoring.
   Record the restore in the manifest entry's notes with the date, the source copy, and
   who did it.
5. **If no copy matches**, the asset is lost as-manifested. Then:
   - *Generated asset*: regenerate from its prompt card and seed. That is what
     reproducibility is for. The regenerated file is a **new** asset ID with its own
     hash and a note referencing the lost one — it is not the same asset, and pretending
     otherwise breaks the provenance chain.
   - *Source scan or recording*: re-request from the custodian. If the custodian
     relationship or the item is gone, the source record's status becomes
     `retracted` with a reason, and every claim depending on it drops register or is
     cut. Do not leave a claim standing on evidence that no longer exists.
6. **If the asset is in a locked cut or a published master**, this is an incident.
   Follow [incident_response.md](incident_response.md) and tell the Pipeline Engineer
   and the gate owner who signed the lock.
7. **Record it**, in the manifest entry and in the production's notes. A mismatch is a
   finding about the storage layer, not only about one file. Two in a year on the same
   volume is the volume telling you something.

## Doing this by hand today

Until `studio_ops pipeline` exists, the contract holds and is executed manually: *(NOT BUILT)*

```bash
# 1. Hash before anything else
sha256sum "SRC-NG-0042_kano-chronicle-scan_p001.tif"

# 2. Copy to the store at the conventional path (never move — copy, verify, then remove)
# 3. Re-hash at the destination and compare
# 4. Add the manifest entry by hand: asset id, path, sha256, bytes, ingested_at, by
# 5. Commit the manifest. Never the media.
```

Step 4 is the one that gets skipped under pressure, and it is the only one that makes
the other four mean anything.
</content>
