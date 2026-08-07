---
doc: core/04
title: Review gate framework
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner]
---

# 04 — Review gate framework

Core defines what a gate **is**. A canon pack defines **which** gates a production
has, who owns them, and what their checklists contain.

This split is the point: a brand film has no fact-check gate and should not be
forced to fake one; a historical documentary cannot ship without one and must not be
able to skip it.

## 1. What a gate is

A gate is a named point in the pipeline at which a **specific human** certifies a
**specific claim** against a **written checklist**, and records a signature.

Four properties, all required:

| Property | Meaning |
|---|---|
| **Named owner** | A role, not a committee. Someone is accountable. |
| **Written checklist** | Fixed in advance. Not "does this feel right?" |
| **Recorded signature** | Role, person, date. Stored on the production record. |
| **Blocking** | Downstream stages cannot proceed. Not advisory. |

A review that lacks any of these is feedback, which is valuable and is not a gate.

## 2. Gate states

| State | Meaning |
|---|---|
| `not-required` | This pack does not include this gate, or it does not apply to this production. Requires a reason. |
| `pending` | Not yet submitted |
| `in-review` | With the owner |
| `signed` | Certified. Signature recorded. |
| `blocked` | Failed, or held. Named blockers recorded. |

`signed` is the only state that permits downstream work.

## 3. Declaring a gate set

A pack declares its gates in `gates.yaml`:

```yaml
gates:
  - key: fact_check
    title: Fact-check
    owner: research-lead
    blocks: [picture_lock, delivery]
    checklist: checklists/fact_check.md
    required: true
    certifies: >
      Every claim referenced in the locked script resolves to a claim record at the
      required tier, with independence checked.
```

`studio_ops` reads this to build the production record's `gates` block. A production
cannot be created without a pack, and therefore never has an undefined gate set.

## 4. Re-opening a signed gate

Sometimes necessary; always recorded.

1. Anyone may request a re-open with a stated reason.
2. The gate owner decides.
3. On re-open the gate returns to `pending`, the prior signature is **retained in
   history**, and every downstream gate that was signed on the basis of it returns
   to `pending` too.

That cascade is the mechanism that makes late changes visible rather than quiet. A
change to a locked script after picture lock is not a small edit; the framework
makes it feel like what it is.

## 5. Separation of duties

**No person signs two gates on the same production.**

This is core, not a pack's choice, and it is the single constraint most likely to be
quietly abandoned on a small team. It exists because the most common review failure
is not incompetence but proximity — the person who made the thing cannot see it.

`studio_ops validate --canon` flags a repeated name across a production's
signatures. Being flagged is a staffing signal, not a paperwork problem.

## 6. Holds

A **hold** is distinct from a failed gate. A hold is raised by any contributor
against a specific item — an asset, a shot, a sequence, a record — and freezes work
on it until a designated authority rules in writing.

Core requires that:
- any contributor may raise one, without needing standing or seniority,
- the hold takes effect immediately,
- it is released only by the authority the pack designates, in writing,
- the person who raised it is not penalised, ever.

Which authority, and for what categories, is the pack's decision. The
documentary-history pack assigns it to the Cultural Advisor and makes it the one
thing the Showrunner cannot unilaterally override.

## 7. Evidence of a gate

A signed gate leaves three artefacts:

1. The signature on the production record (`episode.yaml` / `production.yaml`).
2. The completed checklist, committed at the path the gate declares.
3. A git commit — so the state of the material at signing time is recoverable.

A signature without a committed checklist is not a signed gate, and the validator
treats it as `pending`.

## 8. The universal gate

Every pack, whatever its genre, includes **technical QC** at delivery. Core requires
it because it is where the platform's own guarantees are verified: provenance
complete, labels applied, rights cleared, specs met, captions present.

Everything else is negotiable by genre. That one is not.
