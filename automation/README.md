---
title: studio_ops
status: active
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer]
---

# `studio_ops`

The platform toolkit: scaffolding, validation, reporting, prompt rendering, and
pipeline stubs.

## Maturity — read this first

Per [docs/status.md](../docs/status.md). Commands shown elsewhere in this repository
are the **specification**; this table is what actually runs.

| Command | Maturity | Note |
|---|---|---|
| `studio_ops --help`, CLI skeleton | **IMPLEMENTED** | |
| `validate --root-hygiene` | **IMPLEMENTED** | Whitelist enforced against the real tree |
| `validate --naming` | **IMPLEMENTED** | Prohibited patterns from `standards/naming_conventions.md` |
| `validate --links` | **IMPLEMENTED** | Internal markdown links resolved |
| `validate --schemas` | **IMPLEMENTED** | YAML/front matter against `standards/schemas/` |
| `modes` — list backends by execution mode | **IMPLEMENTED** | |
| `prepare-job` — assemble an interactive work order | **IMPLEMENTED** | Offline; no adapter runs |
| `ingest` — fulfil a job | **NOT BUILT** | Thin join between two built pieces |
| `validate --sources` | **NOT BUILT** | Reports its own absence rather than passing silently |
| `validate --canon` | **NOT BUILT** | As above |
| `validate --prompts` | **NOT BUILT** | Cheat-sheet staleness |
| `new-studio` / `new-line` / `new-production` / `new-pack` / `new-record` | **NOT BUILT** | Scaffold templates exist; the copier does not |
| `report *` | **NOT BUILT** | |
| `promptlib render` / `run` | **NOT BUILT** | |
| `pipeline conform` / `package` | **NOT BUILT** | The conform refusal is the mechanism behind traceability. It does not exist. |
| Generation adapters | **NOT BUILT — deliberately** | Stubs with a cost ceiling. Wiring one is a separate, budgeted decision. |

**A stub never passes silently.** Unbuilt validators exit non-zero with
`NOT BUILT — this gate does not exist yet`. A validator that returns "OK" because it
does nothing is worse than no validator, because it manufactures false confidence.

## Execution modes

A backend declares how it gets from a request to bytes. This is an implementation
detail **behind** `Adapter`, not a tier: a production asks for an image and never
learns which mode produced it. Swapping mode changes one config value and no record.

| Mode | Phases | Needs | Guards |
|---|---|---|---|
| `local` | one | nothing external | dry-run |
| `interactive` | **two** | an operator and a surface | dry-run, ceiling at fulfilment |
| `api` | one | verified terms, credentials, a ceiling | dry-run, ceiling, post-flight overrun |

The distinction that matters is **synchrony, not cost**. `local` and `api` return
bytes from `generate()`. `interactive` cannot — the generating happens out of band —
so it prepares a job and raises `AwaitingFulfilmentError`. It never fabricates a
result for work that has not happened, which would defeat every provenance guarantee
in the package.

Interactive mode is deliberately **vendor-agnostic**. A job can be fulfilled from a
chat client, an image tool, a colleague's workstation, or a vendor console, and the
ingest path is identical. It asserts nothing about whether any particular assistant,
subscription, or editor exposes a generation API — it exists precisely because some
do not.

## Design

```
studio_ops/
├── cli.py            Typer app; every command is registered here
├── config.py         Environment and repo-root resolution
├── paths.py          The folder contract, in one place
├── frontmatter.py    YAML front matter read/write
├── result.py         Finding / Report types shared by all validators
├── validate/         One module per gate
├── scaffold/         Template copiers (NOT BUILT)
├── report/           Derived views (NOT BUILT)
├── promptlib/        Card -> vendor string (NOT BUILT)
├── pipeline/         Manifest, conform, package (NOT BUILT)
└── adapters/         Vendor interfaces (deliberate stubs)
```

Three principles:

1. **Validation is offline.** No validator touches the network, so CI never depends
   on a vendor being up and a validation result is reproducible.
2. **The folder contract lives in `paths.py` alone.** Every other module asks it.
   Moving a directory is one edit.
3. **Findings are data.** Validators return `Finding` objects; rendering is separate.
   The same run can print a table, emit JSON, or annotate a PR.

## Usage

```bash
pip install -e ".[dev]"

python -m studio_ops validate --all
python -m studio_ops validate --naming --links
python -m studio_ops validate --all --format json
```

Exit codes: `0` clean, `1` findings, `2` a requested gate is NOT BUILT.

Distinguishing `1` from `2` matters — a green build that ran three of six gates
should not look like a green build that ran six.

## Testing

```bash
pytest
```

Tests cover the implemented validators against fixture trees containing deliberate
violations. That is what moves a row from IMPLEMENTED toward TESTED — a validator
that runs cleanly on an empty repository has proved nothing.

## Adding a validator

1. Module in `validate/`, exposing `run(ctx) -> list[Finding]`.
2. Register in `validate/__init__.py`.
3. Add a CLI flag in `cli.py`.
4. Fixture tree with deliberate violations, plus a test asserting each is caught.
5. Update the maturity table above **and** [docs/status.md](../docs/status.md) in the
   same commit.
