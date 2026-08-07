---
title: Takedown log
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [rights-and-clearances, cultural-advisor]
---

# Takedown log

Every request to remove, restrict, correct, or re-attribute published material, and
what the studio did about it.

Canon: [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §9.

**Maturity: DESIGNED.** The register is **empty** — nothing has been published, so
nothing has been requested. The runbook that would say who responds, how fast, and who
decides is `docs/runbook/takedown_procedure.md`, which is **NOT BUILT**. A register
with no procedure behind it is a place to write things down, not a response capability,
and it should not be mistaken for one.

## What belongs here

Any approach from outside the studio asking that published material be changed or
withdrawn, whoever makes it and however it arrives:

- A rights holder asserting a claim over material the studio believed cleared.
- A community, custodian, or descendant asserting that material is restricted,
  sacred, or should not have been depicted — which is not a legal claim and is handled
  no less seriously.
- A contributor exercising a withdrawal term recorded in their consent scope.
- A platform acting on a third party's notice, with or without telling the studio
  first.
- A correction request that is substantive enough to affect the published work rather
  than the corrections log.

A complaint about the work's editorial position is **not** a takedown and does not
belong here. It belongs in the studio's corrections and feedback path. Mixing the two
makes both unreadable and makes the takedown register look busier — and therefore less
urgent — than it is.

## What must be recorded, and why

Two reasons this is a register rather than an inbox.

1. **Pattern.** Three separate requests about the same archive, the same community, or
   the same category of asset is a systemic finding about the studio's clearance
   practice, and it is invisible unless the requests sit in one table.
2. **Consistency.** The studio's answer to a request should not depend on who received
   the email. A visible history of what was decided, and on what basis, is the only
   thing that makes the next decision consistent with the last one.

## The register

**This table is empty.** The row below is a template.

| ID | Received | From | Contact route | Material | Production | Nature of request | Basis asserted | Related clearance | Acknowledged | Decision | Decided by | Action taken | Closed | Public note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `TD-0000` | `<YYYY-MM-DD>` | ⟨TEMPLATE ROW — DELETE ON FIRST REAL ENTRY⟩ `<who>` | `<how it reached the studio>` | `<what specifically>` | `<production code>` | `<removal / restriction / correction / re-attribution / consent withdrawal>` | `<what they say gives them standing>` | `<CLR-* or none>` | `<YYYY-MM-DD>` | `<upheld / declined / partial / TBD>` | `<role and person>` | `<what changed, where>` | `<YYYY-MM-DD>` | `<link or none>` |

### Column notes

| Column | Note |
|---|---|
| **ID** | `TD-<SERIAL>`. Takedowns are not an entity type in [../../standards/id_system.md](../../standards/id_system.md) and so have no `TYPE` code allocated. **This is a gap** — the local `TD-*` form here is provisional and must be either added to the ID grammar or replaced. Owner: Pipeline Engineer, with Rights & Clearances, before the first publication. |
| **Received** | The date it reached the studio, not the date someone read it. The SLA clock starts at the former. |
| **Contact route** | Which published address it came through. A request that arrived by a route the studio does not monitor is a finding about the route. |
| **Material** | Identify the asset, shot, or passage. "The episode" is rarely the actual object of the request. |
| **Basis asserted** | What the requester says gives them standing. Recorded as *asserted*, not as established — the studio does not adjudicate a claim by writing it down. |
| **Related clearance** | The `CLR-*` row the studio relied on, or `none`. A request against material with a clearance record is a different problem from one against material without, and the difference matters for the response and for the follow-up. |
| **Acknowledged** | Separate from the decision, and much sooner. Acknowledgement is not agreement. |
| **Decision / Decided by** | A named role and person. Core/02 §9 requires the studio to know in advance who decides; this column records that it did. |
| **Action taken** | Concretely what changed: asset replaced, sequence recut, credit corrected, episode restricted in a territory, master withdrawn. "Reviewed" is not an action. |
| **Public note** | Whether and where the change was disclosed. A silent edit to published material is a provenance failure as much as a courtesy failure — see [../media_provenance/README.md](../media_provenance/README.md). |

## Rules

- **Nothing is deleted from this table**, including requests that were declined and
  requests that turned out to be mistaken. The record of having been asked is itself
  the thing worth keeping.
- **A takedown that results in a change to published material triggers a re-publication
  of that production's provenance summary**, because the summary now describes a master
  that no longer exists. See [../media_provenance/README.md](../media_provenance/README.md).
- **A takedown that reveals a clearance error is fed back into
  [clearance_log.md](clearance_log.md)** as a status change on the affected row, with
  the takedown ID in the note. The clearance log is not left describing the world as it
  was believed to be.
- **Withdrawal by a contributor is honoured on the terms recorded in their consent
  scope**, which is in the clearance log under Interviews and testimony. If those terms
  are unclear, the answer is not a negotiation; it is that the consent was not
  adequately scoped, and that is a finding.

## Known gaps

| Gap | Consequence | Owner | When |
|---|---|---|---|
| No takedown procedure runbook | No stated SLA, no named decision-maker, no escalation path | Rights & Clearances | Before first publication |
| No ID type allocated for takedowns | `TD-*` here is provisional and does not validate | Pipeline Engineer | Before first publication |
| No published contact route | `takedown_contact` is `TBD` in the studio record | Studio, per its `studio.yaml` | Before first publication |

All three block publication, not delivery. A studio that can be reached but cannot
respond is in a worse position than one that has not published.
