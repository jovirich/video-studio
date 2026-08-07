---
title: studio_ops CLI reference
status: active
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer]
---

# `studio_ops` CLI reference

The platform toolkit. Two equivalent invocations:

```bash
python -m studio_ops <command> [options]
studio <command> [options]          # console script from [project.scripts]
```

Prefer `python -m studio_ops` in documentation and scripts — it works without the
venv's `Scripts`/`bin` on `PATH`.

Setup: [../runbook/environment.md](../runbook/environment.md). Package design and
principles: [../../automation/README.md](../../automation/README.md).

## Maturity at a glance

| Command | Maturity | Notes |
|---|---|---|
| `--help`, CLI skeleton | **IMPLEMENTED** | Typer app; every documented command is registered, built or not |
| `validate --schemas` | **IMPLEMENTED** | YAML and markdown front matter against `standards/schemas/` |
| `validate --naming` | **IMPLEMENTED** | `standards/naming_conventions.md` |
| `validate --links` | **IMPLEMENTED** | Internal markdown links resolve |
| `validate --root-hygiene` | **IMPLEMENTED** | Root whitelist and permitted directories |
| `validate --sources` | **NOT BUILT** | Reports its own absence rather than passing silently |
| `validate --canon` | **NOT BUILT** | Blocked on `prohibited_patterns.json` |
| `validate --prompts` | **NOT BUILT** | Cheat-sheet staleness |
| `validate --packs` | **NOT BUILT** | Its stub still reports itself blocked on `pack.schema.json`, which now exists — a stale blocker message |
| `validate` *delivery gate* | **NOT BUILT** | In `ALL_GATES`; reachable only via `--all` — no `--delivery` flag exists |
| `new-studio` / `new-line` / `new-production` / `new-pack` / `new-record` | **NOT BUILT** | Templates exist; the copier does not |
| `report *` | **NOT BUILT** | No record graph to report on |
| `promptlib render` / `run` | **NOT BUILT** | The main practical payoff of the card structure; unproven |
| `pipeline conform` / `package` | **NOT BUILT** | The conform refusal is the mechanism behind the traceability guarantee |
| `status` | **NOT BUILT** | Use the hand-maintained [../status.md](../status.md) |
| Generation adapters | **NOT BUILT — deliberately** | Stubs behind a cost ceiling; wiring one is a separate budgeted decision |

**Nothing is TESTED.** The pytest suite (20 tests, passing) exercises fixture trees
with deliberate violations, which is the right thing to have and is not the same as
evidence from a real workload.

**A stub never passes silently.** Unbuilt commands print what they *will* do and what
they are blocked on, then exit non-zero. A command that appears to work and does
nothing is worse than a missing command.

---

## `validate`

```bash
python -m studio_ops validate [FLAGS] [--format table|json]
```

Runs repository gates. Gates are independent, so one run reports every failure rather
than stopping at the first.

| Flag | Gate | Checks | Maturity |
|---|---|---|---|
| `--all` | all nine | Every gate, built or not | — |
| `--schemas` | `schemas` | `.yaml`/`.yml` records and `.md` front matter routed to a schema by filename (`studio.yaml`, `line.yaml`, `production.yaml`, `episode.yaml`, `manifest.yaml`, `pack.yaml`, `*.prompt.yaml`) or by a `type` field | **IMPLEMENTED** |
| `--naming` | `naming` | Path length (180), spaces, non-ASCII, banned version markers (`final`, `latest`, `new`, `copy`, `backup`, `temp`, …), non-ISO dates, and a `_TEMPLATE_` file that was filled in place | **IMPLEMENTED** |
| `--links` | `links` | Every inline markdown link resolves. External schemes skipped; media paths (`05_assets/`, `masters/`, `renders/`, `stems/`) tolerated; absolute paths warned | **IMPLEMENTED** |
| `--root-hygiene` | `root-hygiene` | Root files against `ROOT_WHITELIST`, root directories against `ROOT_DIRS`, both in `paths.py`. Names a destination for a stray file | **IMPLEMENTED** |
| `--sources` | `sources` | *Will*: every `{{CLM-*}}` resolves; corroboration meets the register's requirement; independence asserted on every `established` claim | **NOT BUILT** — no records exist |
| `--canon` | `canon` | *Will*: prohibited patterns; unsourced superlatives and bare figures; `archival` class on a generated asset; missing reconstruction labels; one person signing two gates | **NOT BUILT** — `prohibited_patterns.json` never generated |
| `--prompts` | `prompts` | *Will*: vendor sheets older than 90 days; cards whose `terms_checked` is missing or expired | **NOT BUILT** |
| `--packs` | `packs` | *Will*: every declared gate has a checklist that exists; every document in `pack.yaml` exists; no pack rule loosens core | **NOT BUILT** — stub's stated blocker is stale |
| — | `delivery` | *Will*: resolution, frame rate, loudness, true peak, caption validity, stem completeness | **NOT BUILT** — needs ffprobe and a delivered package |
| `--format` | — | `table` (default) or `json` | **IMPLEMENTED** |

No flag at all prints the available gates and exits 1. `--all` is what CI is meant to
run; today CI runs the six gates named in the workflow file, two of which do not exist.

### Exit codes

| Code | Meaning |
|---|---|
| `0` | Clean — every requested gate ran and found nothing |
| `1` | Findings — at least one `ERROR`-severity finding |
| `2` | A requested gate is **NOT BUILT** |

**Why 2 is distinguished from 0.** A green build that ran four of nine gates must not
look like a green build that ran nine. Collapsing them would mean that implementing a
gate could *worsen* the reported state, and that adding a gate to `ALL_GATES` is
invisible until someone reads the log — which is the exact false-confidence failure the
NOT BUILT convention exists to prevent. Keeping them separate lets CI treat "we did not
check" as its own condition, distinct from both "we checked and it is fine" and "we
checked and it is broken".

> **Known defect: exit code 2 is currently unreachable.** `validate/not_built.py`
> records its NOT BUILT status as a `Finding` with `Severity.ERROR`, and
> `RunReport.exit_code()` tests `error_count` before `not_built`. So
> `validate --sources` exits `1`. Do not depend on `2` until this is fixed —
> [../architecture/refinements_before_episode_one.md](../architecture/refinements_before_episode_one.md)
> item 4.

Warnings never affect the exit code. They require acknowledgement; they do not block a
merge.

### Output — table

A per-gate summary (gate, state, files checked, errors, warnings) followed by the first
50 findings per gate with severity, location, message, and hint. Truncation is stated
explicitly; the full set is always available in JSON.

### Output — JSON

From `result.py`. Stable enough to script against.

```json
{
  "errors": 1,
  "warnings": 0,
  "not_built": ["sources", "canon"],
  "gates": [
    {
      "gate": "links",
      "state": "IMPLEMENTED",
      "files_checked": 259,
      "errors": 1,
      "warnings": 0,
      "findings": [
        {
          "gate": "links",
          "severity": "error",
          "message": "broken internal link: ../../../templates/legal/interview_consent.md",
          "path": "packs/documentary-history/methodology/oral_history_protocol.md",
          "line": 31,
          "rule": "dead-link",
          "hint": "Resolves to templates/legal/interview_consent.md, which does not exist."
        }
      ]
    }
  ]
}
```

| Field | Type | Notes |
|---|---|---|
| `errors`, `warnings` | int | Totals across all gates in the run |
| `not_built` | list[str] | Gate names that reported `NOT_BUILT` |
| `gates[].gate` | str | Gate name |
| `gates[].state` | `"IMPLEMENTED"` \| `"NOT_BUILT"` | The **validator's** maturity, distinct from what it found. This is the field to read when deciding whether a green result means anything. |
| `gates[].files_checked` | int | 0 for a NOT BUILT gate |
| `gates[].errors`, `.warnings` | int | Counts for this gate |
| `gates[].findings[]` | list | Every finding, not truncated |
| `findings[].severity` | `"error"` \| `"warning"` \| `"info"` | `error` blocks a merge; `warning` requires acknowledgement |
| `findings[].path` | str \| null | Repo-relative **POSIX** path, stable across platforms. Falls back to an absolute path if the path cannot be made relative — on Windows that means a drive-letter casing mismatch; see the environment runbook. |
| `findings[].line` | int \| null | Where the gate tracks line numbers (`links` does; `naming` and `root-hygiene` do not) |
| `findings[].rule` | str \| null | Stable rule id — `dead-link`, `no-spaces`, `ascii-only`, `iso-dates`, `numeric-versions`, `path-length`, `root-whitelist`, `root-dirs`, `template-not-filled`, `not-built`, `schema:<file>` |
| `findings[].hint` | str \| null | What to do about it |

`rule` is the field to filter on. Messages are for humans and will be reworded;
`rule` values are contract.

---

## Scaffolding — all NOT BUILT

Each prints what it will do and what it is blocked on, then exits non-zero.

| Command | Options | Will do | Blocked on |
|---|---|---|---|
| `new-studio` | `--code --title --pack` | Copy `templates/studio/` to `studios/<code>/`, write `studio.yaml` with the declared pack, seed the decision register from the pack's `studio_must_decide` list | `templates/studio/` scaffolding and `pack.schema.json` |
| `new-line` | `--studio --code --title` | Copy `templates/line/` with `line_status: candidate` and all opening conditions false | `templates/line/` scaffolding |
| `new-production` | `--line --season --number --slug` | Copy `templates/production/`, build the gate block from the studio's pack `gates.yaml`, allocate the production ID | `templates/production/` scaffolding and `gates.yaml` parsing |
| `new-pack` | `--code --title` | Copy `packs/_TEMPLATE_pack/` to `packs/<code>/` | **Nothing** — the cheapest scaffolder to build first |
| `new-record` | `--type --line` | Allocate the next serial for (type, scope), **refuse on a gap-and-collision pattern suggesting a hand-edited ID**, write the record from its template | The ID allocator |

`new-record` is the one that matters. Its own stub says so: hand-allocated IDs collide,
and a collided ID silently corrupts the reference graph — records reference each other
by ID string, not by path, and `validate --sources` (which would detect it) is also NOT
BUILT. Manual workarounds are in [../workflows/open_a_line.md](../workflows/open_a_line.md)
step 7.

Manual equivalents for each: [../workflows/](../workflows/).

## Command groups — all NOT BUILT

| Group | Will provide |
|---|---|
| `report` | `bibliography`, `shotlist`, `open-questions`, `source-coverage`, `dependents`, `pronunciation`, `chapters`, `provenance`, `chain-of-title` |
| `promptlib` | `render` a card to a vendor string; `run` it against an adapter under the production's cost ceiling |
| `pipeline` | `ingest`, `manifest`, `conform`, `package`. The conform step refuses any timeline clip without a manifest entry — that refusal is the mechanism behind the platform's traceability guarantee |

Invoking a group with no subcommand prints its NOT BUILT notice. Blocked on, in each
case, the same thing: no records, no assets, no proven asset-store round trip.

## `status`

```bash
python -m studio_ops status [--studio <code>] [--line <code>]
```

**NOT BUILT.** Will walk studios, lines, and productions and report stage, gate
signatures, unresolved decisions, and counts. Blocked on having control records to
walk. Use [../status.md](../status.md), which is hand-maintained and honest.

---

## Adding a validator

Five steps, from [../../automation/README.md](../../automation/README.md). All five, or
the gate is not added.

1. **Module in `validate/`**, exposing `run(cfg) -> GateReport`. Take paths from
   `paths.iter_files()` so `IGNORE_DIRS` is respected; return `Finding` objects; do not
   print. Touch the network never.
2. **Register it in `validate/__init__.py`** — move the name from `UNBUILT` to the
   `IMPLEMENTED` dict. `ALL_GATES` is derived, so `--all` picks it up automatically.
3. **Add a CLI flag in `cli.py`** — a parameter on `validate()` plus a row in the
   flag/name tuple list.
4. **Fixture tree with deliberate violations, plus a test asserting each is caught** —
   and a clean-input test asserting silence. This is the step that makes the gate mean
   anything; a validator that runs cleanly on an empty repository has proved nothing.
5. **Update the maturity table in `automation/README.md` *and*
   [../status.md](../status.md) in the same commit**, and the table at the top of this
   file. A status change is not a separate chore.

Three conventions worth following because the existing gates do:

- **Give every finding a stable `rule` string.** It is what CI and humans filter on.
- **Write a hint that names the fix**, not the problem. `root_hygiene` suggests a
  destination directory rather than only refusing, which turns a rejection into an
  action.
- **State the gate's own maturity in the module docstring**, and be honest about what a
  clean run does *not* prove. `schemas.py` does this well: a clean run there proves the
  schemas parse, not that they are right.
</content>
