---
title: Permissions
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [rights-and-clearances]
---

# Permissions

The four registers that together answer the only question a distributor, a broadcaster,
an insurer, or a rights holder ever actually asks: **can you prove you hold this?**

Canon: [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md).
Platform-level, for the reasons in [../README.md](../README.md).

## The four documents

| Document | Question it answers | Cadence | Maturity |
|---|---|---|---|
| [clearance_log.md](clearance_log.md) | For every third-party thing in the pipeline: who holds it, what did they grant, and who checked? | Continuous. Re-checked at picture lock and at delivery. | **DESIGNED**, empty |
| [model_terms_register.md](model_terms_register.md) | For every generative tool: what do its terms permit, at our tier, as of what date? | Re-checked **before every delivery** | **DESIGNED**, empty |
| [chain_of_title.md](chain_of_title.md) | For one finished production: can the studio grant what it is purporting to grant? | Assembled once, at delivery, per production | **DESIGNED**, template only |
| [takedown_log.md](takedown_log.md) | After publication: who asked for what to change, and what did the studio do? | On receipt | **DESIGNED**, empty |

## How they relate

```
   library/ asset          archival item        generated asset
        │                        │                     │
        └────────────┬───────────┘                     │
                     ▼                                 ▼
             CLEARANCE LOG  ◄────── references ── MODEL TERMS REGISTER
             CLR-* per grant        a dated row    per vendor, 7 questions
                     │                                  │
                     │  manifest.yaml points at CLR-*   │
                     ▼                                  │
              CHAIN OF TITLE  ◄────────────────────────-┘
              one per production, assembled at delivery
                     │
                     ▼   published
              TAKEDOWN LOG ──► corrections back into the clearance log
```

The direction of that last arrow is the part that gets skipped. A takedown that
reveals a bad clearance must change the clearance row, or the register goes on
describing a world the studio has already learned it was wrong about.

## Two registers, deliberately not one

The clearance log is about **the thing**: this photograph, this cue, this typeface.
The model terms register is about **the tool**: what this vendor's licence permits.

They are separate because they change on different clocks and are checked by different
means. A photograph's licence is fixed the day it is signed and expires on a known
date. A vendor's terms change silently and have to be re-read from the source. Merging
them would force one cadence onto both, and the cadence that would win is the slower
one.

The join between them is a generated asset's clearance row, which cites a **dated** row
in the model terms register — the terms as at the date of generation, not the terms as
they read today.

## The rule everything else hangs off

**Absent from the clearance log means uncleared.** Not "not yet documented". There is
no informal cleared state anywhere in this platform, and the rights gate treats a
missing row as a missing right. See [clearance_log.md](clearance_log.md).

Corollary, from [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §10:
**no production is delivered with any asset in `pending`.** There is no provisional
delivery, no conditional master, and no "we'll paper it after air".

## What is not here

- **The rights gate checklist** — `ops/checklists/rights_gate.md`, **NOT BUILT**.
  Core/02 §10 names it. Until it exists the gate has no written checklist, and by
  [../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §1 a
  review without a written checklist is feedback, not a gate. That is a real hole in
  the delivery path and it is worth saying so plainly.
- **The takedown procedure runbook** — `docs/runbook/takedown_procedure.md`,
  **NOT BUILT**. The log exists; the SLA, the decision authority, and the escalation
  path do not.
- **Signed agreements themselves.** These registers are an index over the agreements.
  The documents live in the studio's document store, referenced by path, and are not
  committed to git.
- **Anything jurisdiction-specific.** No register here states a legal rule. Where a
  position depends on one — public domain status, fair-dealing reliance, moral rights —
  the register records the position, the jurisdiction considered, and who advised.

## Tooling

| Command | Reads | Maturity |
|---|---|---|
| `studio_ops new-record --type clearance` | Allocates the next `CLR-*` serial | **IMPLEMENTED** |
| `studio_ops report chain-of-title --episode <code>` | Clearance log + frozen manifest → chain of title | **NOT BUILT** |
| `studio_ops validate --canon` | Flags manifest entries whose `clearance_ref` has no row | **NOT BUILT** |

Until those exist, every register here is maintained by hand by Rights & Clearances,
with IDs allocated in the same commit that uses them. See
[../../docs/status.md](../../docs/status.md).
