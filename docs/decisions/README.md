---
title: Architecture decision records
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner, pipeline-engineer]
---

# Architecture decision records

One file per architectural decision: the situation that forced it, what was decided,
what it costs, what was rejected, and how we would know it was wrong.

## The index

| ADR | Title | Status | In one line |
|---|---|---|---|
| [0000](0000-template.md) | ADR template | template | Copy this; do not edit it in place. |
| [0001](0001-studio-not-show.md) | Build a studio, not a show | accepted (partially superseded by 0005) | Region is a production line, not the subject of the repository — so a second country is a command, not a fork. |
| [0002](0002-claims-as-records.md) | Facts live in claim records, not in scripts | accepted | Scripts carry `{{CLM-*}}` references; the fact, its confidence register, and its evidence live in a record CI can walk. |
| [0003](0003-prompt-cards.md) | Prompts are versioned records, not strings | accepted | A prompt is a YAML record with inheritance, evidence basis, and an append-only `runs` history — so it is reviewable *before* generation. |
| [0005](0005-platform-and-canon-packs.md) | Separate the platform from the editorial canon, via canon packs | accepted | Split `bible/` into core (universal) + pack (genre) + studio (brand); a studio declares one pack and inherits its gate set. |
| [0009](0009-licensing-posture.md) | Licensing posture — infrastructure vs productions | **proposed** | Open the engine and the packs, keep `studios/` proprietary — recommended, not yet decided. Blocks Phase 1. |

Numbers **0004, 0006, 0007, and 0008 are unused.** That is fine and is not a
bookkeeping error to be tidied up: numbers are allocated when a decision starts being
written and are never reclaimed if it is abandoned or folded into another ADR. A gap
costs nothing. Reusing a number costs everything, because every external
reference — a commit message, a PR comment, an evolution-log entry, a code
comment — silently points at a different decision than the one its author meant.

The same rule governs record IDs, for the same reason. See
[../../standards/id_system.md](../../standards/id_system.md).

## An ADR is immutable once accepted

**You never edit an accepted ADR. You supersede it.**

| To… | Do |
|---|---|
| Change a decision | Write a new ADR. Set `supersedes:` on the new one and `superseded_by:` on the old one. Leave the old text untouched. |
| Correct a typo or a broken link | Permitted. Nothing else. |
| Record that a decision turned out badly | New ADR of the reversing decision, plus an entry in [../architecture/evolution.md](../architecture/evolution.md) of kind `reversal`. |
| Add detail that was always true but unwritten | Also a new ADR. If it changes what a reader would do, it is a decision. |

What editing in place destroys is the only thing an ADR is for. The value is not the
current state of the architecture — the tree already tells you that. The value is the
frozen record of *what was known, feared, and rejected at the moment the choice was
made*. Editing 0001 to reflect what we learned in 0005 would erase the fact that the
first abstraction was one tier too shallow, which is the most useful thing 0001 now
teaches. `supersedes: partially 0001` on ADR 0005 is doing real work; a quietly
updated 0001 would be doing damage.

Status values: `proposed` (open, no decision yet — 0009), `accepted`, `superseded`,
`rejected` (written, decided against, kept because the reasoning is reusable),
`template`.

## Relationship to the evolution log

Both files exist. They are not redundant.

| | [docs/decisions/](.) | [docs/architecture/evolution.md](../architecture/evolution.md) |
|---|---|---|
| Unit | One decision | One structural change |
| Tense | Frozen at the date of decision | Rewritten forward as understanding changes — by appending, never editing |
| Answers | *What was decided, given what options?* | *How has the shape evolved, and what did each move teach?* |
| Contains | Options rejected, falsification condition | Trigger, cost, what it protects, what to watch for |
| Includes decisions later found wrong | Yes, unedited, marked superseded | Yes — that is largely the point |

An ADR is a decision at a point in time. The evolution log is the narrative across
them. ADR 0001 and ADR 0005 read as two confident and partly contradictory documents;
entries AE-001 and AE-006 read as one story in which the first diagnosis was right
and its abstraction was one tier too shallow. You need both: the ADRs so a future
reader can see what was actually weighed, the log so they can see what it cost to be
wrong.

Every ADR that changes structure should have a matching `AE-NNN` entry, and the
entry's `**ADR:**` field links back. Mechanical changes get an evolution entry with
`ADR: none — mechanical` and no ADR.

## Writing one

Copy [0000-template.md](0000-template.md) to `NNNN-kebab-title.md`. Two sections do
the load-bearing work and are the two people skip:

- **Consequences → Negative.** An ADR with no negative consequences is not an
  architectural decision; it is a preference. Name the cost that will tempt someone
  to abandon this later. ADR 0005 names four tiers reading as over-engineering while
  there is one studio — which is true, and saying so is what makes the document
  credible.
- **Validation.** Name a concrete observable signal that would show the decision was
  wrong: a metric, a pattern in the git history, a class of friction. Without one,
  the ADR can only be defended or attacked on taste. ADR 0002's signal — claim
  records appearing in git history *after* the scripts that reference them — is
  checkable by anyone with a clone.

An ADR is warranted when there is a constraint that makes the obvious answer wrong.
If there is no such constraint, write it in the relevant README instead.
</content>
</invoke>
