---
title: Archive
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner]
---

# Archive

Where historical status artefacts go once they stop being current.

This folder exists for one reason: **so that documents whose truth expired do not
accumulate at repository root.** Its contents are, by definition, not authoritative.

## The folders

| Folder | Holds | Typical name |
|---|---|---|
| `sprints/` | Per-sprint plans, delivery notes, retrospectives | `2026-08-07_sprint-12_retro.md` |
| `weeks/` | Weekly status, standup summaries, week-in-review notes | `2026-08-07_week-31_status.md` |
| `agents/` | Output from automated or agent-assisted runs: generated reports, batch summaries, run logs worth keeping | `2026-08-07_link-audit_run.md` |
| `misc/` | Everything else that was true once — one-off summaries, analyses, notes, migration write-ups | `2026-08-07_arch2-migration-notes.md` |

Filenames start with an ISO date (`YYYY-MM-DD`) because the only useful sort order for
an archive is chronological, and because `naming` rejects locale-ordered dates —
`07-08-2026` and `08-07-2026` are indistinguishable, which is precisely the problem.

## The rule

> **Historical status artefacts go here, not at repository root.**

The root whitelist is exactly thirteen files plus the `.code-workspace`, and
`python -m studio_ops validate --root-hygiene` (**IMPLEMENTED**) fails the build on
anything else. It suggests a destination rather than only refusing:
`SPRINT_12_DELIVERY.md` at root is rejected with "Move it to `docs/archive/sprints/`",
and `WEEK3_NOTES.md` with `docs/archive/weeks/`. The suggestion map lives in
`validate/root_hygiene.py`.

The rule is enforced mechanically rather than by review, because review discipline does
not survive a deadline. Left alone, a repository root becomes `STATUS.md`,
`STATUS_FINAL.md`, `NOTES.md`, `SUMMARY_v2.md`, `WEEK3.md`, and `TODO_old.md` — at
which point the directory listing no longer says what the project is, and nobody can
tell which of six documents is still true.

## Archive rather than delete

Deleting is tempting and is usually the wrong call. An archived sprint retro tells you
what the team believed at the time, which is what makes a later post-mortem possible;
git history technically has it, but nobody excavates git history for something they do
not know exists.

Archive when: a status document's date has passed, a plan has been superseded, a
one-off analysis has been acted on, or an agent run has produced output worth keeping
but not worth maintaining.

Delete only when: it is a duplicate, it contains material that should never have been
committed (see [../runbook/restricted_records.md](../runbook/restricted_records.md) —
and note that deletion does not remove it from history), or it is generated output that
can be regenerated exactly.

## What does not belong here

| Not this | Where it goes |
|---|---|
| The current capability ledger | [../status.md](../status.md) — living, updated in the same commit as any maturity change |
| Superseded architectural decisions | [../decisions/](../decisions/) — an ADR is never archived. It stays in place, marked `superseded_by`, because its whole value is being the frozen record. |
| Reversed or revised architecture | [../architecture/evolution.md](../architecture/evolution.md) — append a new entry; never move or edit an old one |
| Retracted claims, sources, or records | They stay in their registry with `status: retracted` and a reason. IDs are permanent tombstones. |
| Released changes | [../../CHANGELOG.md](../../CHANGELOG.md) |
| Media of any kind | The asset store — [../runbook/asset_storage.md](../runbook/asset_storage.md) |

The distinction that matters: **archive holds documents whose truth expired. It never
holds records.** A record that is no longer true is marked, not moved — that is what
makes the audit trail continuous, and moving one would break every reference to it.
</content>
