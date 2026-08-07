---
title: Documentation index
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner, pipeline-engineer]
---

# Documentation

Everything about *how this platform works and how to work on it*. Editorial rules
live in [`core/`](../core/) and [`packs/`](../packs/); this tree is engineering,
process, and orientation.

## Start here

| If you are… | Read |
|---|---|
| New to the repository | [onboarding/first_week.md](onboarding/first_week.md), then [glossary.md](glossary.md) |
| Trying to work out what actually runs | [status.md](status.md) — the capability ledger. Read it before trusting any other document's verbs. |
| Asking "why is it shaped like this?" | [architecture/README.md](architecture/README.md) |
| About to do a thing (open a line, ship a fix) | [workflows/README.md](workflows/README.md) |
| Handling something going wrong | [runbook/README.md](runbook/README.md) |
| Writing code against the toolkit | [api/README.md](api/README.md) |

## The tree

| Folder | Holds | Maturity of the material |
|---|---|---|
| [architecture/](architecture/) | The four-tier model, the `arch-2` structural contract, the evolution log, how to spin up new work, and the open weaknesses before episode one | DESIGNED |
| [decisions/](decisions/) | ADRs — one per architectural decision, immutable once accepted | DESIGNED |
| [runbook/](runbook/) | Operational procedures: asset storage, restricted records, takedowns, incidents, local environment | Mixed — see each file's header |
| [onboarding/](onboarding/) | First week, day by day, plus a day-one glossary subset | DESIGNED |
| [training/](training/) | Role-specific training material | NOT STARTED — structure only |
| [api/](api/) | `studio_ops` CLI and library reference, per-command maturity | Describes IMPLEMENTED and NOT BUILT surfaces, marked |
| [workflows/](workflows/) | End-to-end numbered procedures, with the manual equivalent for every NOT BUILT command | DESIGNED |
| [archive/](archive/) | Historical status artefacts — sprints, weeks, agent runs, misc | — |
| [status.md](status.md) | Per-capability ledger: DESIGNED / IMPLEMENTED / TESTED / NOT BUILT | Authoritative |
| [glossary.md](glossary.md) | Terms of art. Where a term has a general and a specific meaning, the specific one governs. | Authoritative |

## Two rules that govern everything in this folder

### 1. Never claim more maturity than exists

Four labels, and they are different claims rather than degrees of one:

| Label | Means | Evidence required |
|---|---|---|
| **DESIGNED** | The structure, schema, or standard exists on paper. No code runs. | The document exists and is internally consistent |
| **IMPLEMENTED** | Code exists and executes. Not proven at production scale. | The command runs and produces output |
| **TESTED** | Exercised against a real workload, with a recorded result someone else can review. | A test run, a report, a dated artefact |
| **NOT BUILT** | Specified, no code. An honest and useful state. | — |

A bare ✅ is banned. It reads as *working* when it usually means *specified*.
Currently **nothing in this repository is TESTED**; the implemented surface is the
`studio_ops` CLI skeleton and four validators. Full account:
[status.md](status.md), and [CONTRIBUTING.md](../CONTRIBUTING.md) § Never claim more
maturity than exists.

### 2. File-placement discipline

**Documentation lives in a semantic subfolder under `docs/`. Never at repository
root.**

The root whitelist is exactly: `README.md`, `ROADMAP.md`, `LICENSE`,
`CONTRIBUTING.md`, `CHANGELOG.md`, `pyproject.toml`, `requirements.txt`, `Makefile`,
`.gitignore`, `.gitattributes`, `.editorconfig`, `.env.example`, `.env`, and the
`.code-workspace` file. Root *directories* are fixed too — the list is
`ROOT_DIRS` in
[../automation/studio_ops/paths.py](../automation/studio_ops/paths.py).

This is enforced mechanically by `python -m studio_ops validate --root-hygiene`
(**IMPLEMENTED**), not by review discipline, because review discipline does not
survive a deadline. The validator names a destination rather than only refusing: a
stray `SPRINT_12_DELIVERY.md` at root is rejected with "Move it to
`docs/archive/sprints/`".

What it prevents is specific and familiar: a root that accumulates
`STATUS_FINAL.md`, `NOTES.md`, `SUMMARY_v2.md`, and `WEEK3.md` until the directory
listing no longer tells anyone what the project is, and until nobody can find the
one document that is still true. If you cannot decide which subfolder a document
belongs to, that is usually a sign the document is two documents.

New subfolders under `docs/` are fine and need no permission — they need a
`README.md` saying what belongs in them and a row in the table above.
</content>
