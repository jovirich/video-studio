---
title: Rights
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [rights-and-clearances]
---

# Rights

Platform-level. Everything a production must hold before it may be distributed, and
the evidence that it holds it.

The canon is [../core/02_rights_and_licensing.md](../core/02_rights_and_licensing.md).
This folder is where that canon is *kept* — the registers themselves. Where a rule
here and core/02 disagree, core/02 is correct and this folder is a bug.

## Contents

| Path | What it is | Maturity |
|---|---|---|
| [permissions/](permissions/) | Clearance log, model terms register, chain of title, takedown log | **DESIGNED** |
| [media_provenance/](media_provenance/) | How provenance travels with delivered media | **DESIGNED** |

## Why this is platform-level and not per-studio

Three reasons, in order of how expensive they are to get wrong.

**1. The obligation does not vary by genre.** A photograph used in a history
documentary and the same photograph used in a brand film are cleared against the same
questions: who holds it, for what media, in what territory, for how long, at what fee,
with what credit, under what restrictions. Canon packs exist because *editorial*
standards differ by genre — evidence tiers, gate sets, narrative doctrine. Rights
obligations do not differ by genre, so a pack has no business owning them, and a
studio-local copy of them would drift from core within one production.

**2. One clearance log per platform means nothing can be cleared twice and forgotten
once.** The failure this prevents is specific: a font, a LUT, a music bed, or a stock
SFX pack licensed for one studio's use gets reused by a second studio that never saw
the licence and does not know its seat count, its territory, or its expiry. With a
single register, the item has exactly one record, one clearance ID, and one status.
With per-studio registers it has two records that agree until the day the licence is
renewed in one of them.

**3. Shared assets need a shared register.** [../library/](../library/) is explicitly
cross-studio. Every item in it carries a licence, and that licence has to live
somewhere that both the studio that bought it and the studio that inherits it can
read. That place is [permissions/clearance_log.md](permissions/clearance_log.md).

## What is *not* here

- **Per-production clearance work.** The register is platform-level; the work of
  clearing a specific asset is a production's, and the resulting record is filed here
  with the production's scope in its ID.
- **The rights gate checklist.** That is `ops/checklists/rights_gate.md` — **NOT
  BUILT**. Core/02 §10 names it; nothing implements it yet.
- **The takedown *procedure*.** `docs/runbook/takedown_procedure.md` — **NOT BUILT**.
  The takedown *log* is here; the runbook that says who responds and how fast is not
  written. Until it is, the studio has a register with nothing feeding it, which is a
  known gap and not a resolved one.
- **Legal advice.** Nothing in this folder is a legal opinion, and no jurisdiction's
  rules are stated here as fact. Public-domain status, fair dealing, and moral rights
  are all jurisdiction-specific; core/02 §3 and §4 say what the studio's *posture* is,
  and a competent adviser says what the *law* is. The registers record which of those
  two a given entry rests on.

## The one rule that makes the rest work

**An item absent from the clearance log is uncleared.** Not "probably fine", not
"cleared but not written down". There is no informal cleared state, because an
informal cleared state is indistinguishable from an oversight six months later when
a distributor asks. See [permissions/clearance_log.md](permissions/clearance_log.md).

## Status

Every register in this folder is **DESIGNED** and **empty**. No clearance has been
recorded, no vendor's terms have been checked, no chain of title has been assembled,
and no takedown has been received — because no production exists. Emptiness here is
the correct state, not an omission. See [../docs/status.md](../docs/status.md).
