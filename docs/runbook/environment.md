---
title: Local environment
status: active
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer]
---

# Local environment

**Maturity: IMPLEMENTED.** Everything in this runbook runs today. It is the only
runbook in this folder of which that is true.

## Requirements

| | |
|---|---|
| Python | **3.11 or later** (`requires-python = ">=3.11"`). The code uses `X \| Y` union syntax and `frozenset[str]` generics throughout. |
| Git | Any recent version |
| `make` | Optional. Windows usually lacks it; every target has a VS Code task equivalent, and every target is a one-line command you can run directly. |

No API key is required. No network is required. See § Offline by design.

## Setup

```bash
git clone <remote> video-studio
cd video-studio

python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux

pip install -e ".[dev]"
```

`-e` (editable) matters: `studio_ops` lives in `automation/`, which is declared as the
package root in `pyproject.toml` (`package-dir = { "" = "automation" }`). A
non-editable install gives you a stale copy and edits to the validators will appear to
do nothing.

`.venv/` is a permitted root directory and is gitignored. Do not create the venv
elsewhere and do not name it anything else — `validate --root-hygiene` rejects
unexpected root directories, and the ignore lists in `paths.py` know about `.venv`,
not about `env` or `venv311`.

Verify:

```bash
python -m studio_ops --help
```

Two invocations exist and are equivalent: `python -m studio_ops <cmd>` and the
`studio` console script installed by `[project.scripts]`. Prefer `python -m studio_ops`
in documentation and scripts — it works without the venv's `bin`/`Scripts` on `PATH`,
which is one less thing to be wrong.

## Running the validators

```bash
# What is actually implemented
python -m studio_ops validate --schemas --naming --links --root-hygiene

# Everything, including the gates that report their own absence
python -m studio_ops validate --all

# Machine-readable
python -m studio_ops validate --all --format json
```

Exit codes, as designed:

| Code | Means |
|---|---|
| `0` | Clean |
| `1` | Findings |
| `2` | A requested gate is NOT BUILT |

`2` is distinguished from `0` deliberately: a green build that ran four of nine gates
must not look like a green build that ran nine.

> **Known defect.** Exit code `2` is currently unreachable. NOT BUILT gates record
> their status as an `ERROR`-severity finding, and `RunReport.exit_code()` tests the
> error count first, so `validate --sources` exits `1`. Do not write scripts that rely
> on `2` until this is fixed —
> [../architecture/refinements_before_episode_one.md](../architecture/refinements_before_episode_one.md)
> item 4.

Findings print as a per-gate summary table followed by the first 50 findings per gate.
The full set is always in `--format json`.

The repository does not currently validate clean: `--links` reports errors for files
that were specified and never written — at the time of writing, record and legal
templates referenced from the pack methodology documents. That is the link gate working
correctly. Before you assume you broke something, check whether your finding names a
file you touched.

## Running the tests

```bash
pytest                                       # config comes from pyproject.toml
pytest --cov=studio_ops --cov-report=term-missing
pytest automation/tests/test_validators.py -k naming -v
```

`testpaths = ["automation/tests"]` and `pythonpath = ["automation"]` are set in
`pyproject.toml`, so `pytest` from the repository root does the right thing with no
arguments. Tests build fixture trees containing deliberate violations and assert that
each rule fires — a validator that runs cleanly on an empty repository has proved
nothing.

The rest of what CI runs:

```bash
ruff check automation
ruff format --check automation
mypy automation/studio_ops
```

`mypy` runs with `disallow_untyped_defs = true`. New functions need annotations,
including `-> None`.

## The Windows path-casing trap

**Always use a canonical uppercase drive letter: `C:\dev\...`, never `c:\dev\...`.**

Windows filesystems are case-insensitive but case-*preserving*, and Python is neither.
`Path.resolve()` returns whatever casing the process was handed, so a shell started in
`c:\dev\Video Production` and one started in `C:\dev\Video Production` produce
different strings for the same directory. The consequences are quiet:

| Symptom | Cause |
|---|---|
| `rel(path, root)` returns an absolute path instead of a repo-relative one | `Path.relative_to()` raises `ValueError` on a case mismatch; `result.py` catches it and falls back to the full path. Findings suddenly print `C:\dev\...\file.md` instead of `docs/file.md`. |
| `find_repo_root()` walks past the root | It compares resolved paths |
| A path appears twice in a diff of validator output | Two casings of one file |
| `git status` shows a file as both deleted and added | A directory was created with different casing |

None of these fail loudly. They produce output that looks *slightly* wrong, which is
worse.

Practical rules:

- Type the drive letter uppercase, every time, in shells, in IDE workspace files, and
  in `STUDIO_ROOT`.
- Never create a second path to the same tree — no `subst`, no junction, no
  network-drive alias to your own working copy.
- Never rename a file by case alone (`Readme.md` → `README.md`) in one commit. Git on
  Windows will not see it. Rename via an intermediate name, in two commits.
- Set `core.ignorecase` to its default (`true` on Windows). Overriding it produces
  duplicate index entries.
- Line endings are handled by `.gitattributes`; do not set `core.autocrlf` by hand.

The naming validator will catch spaces and non-ASCII in your paths. It cannot catch
casing, because from inside the process both casings are the same file.

## Offline by design

**No validator touches the network.** Not to resolve a schema `$ref`, not to check a
link, not to reach a vendor. This is a stated design principle in
[`automation/README.md`](../../automation/README.md), and it is enforced structurally:
`config.py` is deliberately thin, schema `$ref`s resolve through an in-memory
`referencing.Registry` built from `standards/schemas/`, and `links.py` skips anything
matching `http://`, `https://`, `mailto:`, `tel:`, or `#`.

Three things this buys:

1. **CI never fails because a vendor is down.** A red build always means the repository
   is wrong, which is the only way a red build stays meaningful.
2. **A validation result is reproducible.** The same tree gives the same findings today
   and in three years, when several of those vendors no longer exist.
3. **You can validate on a plane, in an archive with no wifi, or on a machine holding
   restricted material that must not touch a network at all.** That last one is not
   hypothetical — see [restricted_records.md](restricted_records.md).

The cost is accepted deliberately: external links are never checked, so a dead
`https://` URL in a vendor sheet will not be caught here. That is a periodic manual
sweep, not a gate.

`.env` is likewise not required. It is read if present (`python-dotenv`), and its
absence is not an error. Copy [`.env.example`](../../.env.example) to `.env` only when
you need the asset store or an adapter — neither of which exists yet. `.env` is
gitignored and the CI secret scan rejects it if it is ever tracked.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `No module named studio_ops` | Venv not activated, or installed non-editable | Activate; `pip install -e ".[dev]"` |
| `jsonschema is not installed` from the schemas gate | Installed without `[dev]`, or a partial install | `pip install -e ".[dev]"` |
| Findings show absolute Windows paths | Drive-letter casing | See § the casing trap |
| `validate` reports "No gate selected" and exits 1 | No flag given | Pass `--all` or a specific gate flag |
| Validators walk something they should not | A directory not in `IGNORE_DIRS` | Add it to `IGNORE_DIRS` in `paths.py` — the one place the folder contract lives |
| `make: command not found` | Windows | Use the VS Code task, or run the command from the Makefile directly. Note that several Makefile targets name commands that do not exist; see refinements item 15. |
| Repo root resolves somewhere unexpected | `find_repo_root()` looks for the co-presence of `core/` and `packs/`, then `.git/` | Run from inside the tree, or set `STUDIO_ROOT` |
</content>
