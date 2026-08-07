---
title: TBD — studio bible amendment log
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [showrunner]
---

# Amendment log

> Skeleton. Copied to `studios/<code>/bible/amendment_log.md`. It starts empty,
> and an empty log is the correct state for a new studio — not a gap to be filled.

Every change to this studio's bible, with what changed, why, who signed it, and what
it invalidates.

## Why an amendment log rather than git history

Git records **what** changed. This log records **why**, and — the part git cannot
supply — **what the change invalidates**.

A studio's canon is referenced by records that were written under the previous
version. When a rule changes, the question "which existing records now fail it, and
are they grandfathered or re-opened?" has an answer, and it needs to be written down
at the moment the change is made. Reconstructing it a year later from a diff is
possible in principle and does not happen in practice.

## Rules

1. **Canon changes never ride along in a production's pull request.** They go on a
   `studio/*` branch and get their own review.
   [../../../CONTRIBUTING.md](../../../CONTRIBUTING.md) § Branching.
2. **An amendment names what it invalidates.** "No existing records affected" is a
   valid entry and asserts that someone checked.
3. **A tightening applies going forward; existing signed work is grandfathered
   unless the entry says otherwise.** Say which, explicitly — the default is
   whichever one nobody wrote down, and that is how a signed gate quietly becomes
   unsigned.
4. **A loosening of core or the pack is not an amendment this log can carry.**
   Precedence is `core > pack > studio > line > production`. If the studio needs
   relief from an upper layer, that layer is amended, with its signatures.
5. **Entries are append-only.** A corrected entry gets a new entry, not an edit.

## Entries

| Date | Version | Document | Change | Reason | Invalidates | Signed |
|---|---|---|---|---|---|---|
| TBD — ISO | TBD — the bible version after the change | TBD — e.g. `00_charter.md §7` | TBD — what the rule now says | TBD — what prompted it: a finding, a ruling, a near miss | TBD — records, gates, or productions affected, or `none, checked` | TBD — role and person |

## Pending amendments

Proposed, not yet signed. Kept here rather than in a message thread so that a change
under discussion is visible to anyone reading the rule it would change.

| Proposed | Document | Proposed change | Raised by | Status |
|---|---|---|---|---|
| TBD — ISO date | TBD | TBD | TBD | TBD — under discussion / rejected, with reason / signed on `<date>` |

A rejected proposal stays on this table with its reason. The same proposal arrives
again about every eighteen months, and the recorded reason is what stops the second
discussion being the first one over again.
