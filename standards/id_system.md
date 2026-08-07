# Identifier system

Every durable entity in the repository has an ID. IDs are permanent, never reused,
and never renumbered. A deleted record keeps its ID as a tombstone.

## Grammar

```
<TYPE>-<SCOPE>-<SERIAL>
<TYPE>-<SCOPE>-<EPISODE>-<SERIAL>     (episode-scoped types)
```

| Part | Rule |
|---|---|
| `TYPE` | Fixed three-letter code from the table below |
| `SCOPE` | Production line code in caps without the country prefix (`NG`, `GH`), or `STUDIO` for cross-line entities |
| `EPISODE` | `S01E01` form, for episode-scoped types only |
| `SERIAL` | Zero-padded, 4 digits, monotonically allocated per (TYPE, SCOPE) |

## Types

| Code | Entity | Scope | Example |
|---|---|---|---|
| `SRC` | Source record | line or studio | `SRC-NG-0042` |
| `CLM` | Claim | line | `CLM-NG-0117` |
| `CHR` | Character (person or collective actor) | line | `CHR-NG-0007` |
| `LOC` | Location | line | `LOC-NG-0031` |
| `ORG` | Organisation, polity, institution | line | `ORG-NG-0012` |
| `OBJ` | Object or artefact | line | `OBJ-NG-0005` |
| `EVT` | Timeline event | line | `EVT-NG-0088` |
| `QST` | Open question | line | `QST-NG-0023` |
| `FCK` | Fact-check report | episode | `FCK-NG-S01E01-0003` |
| `SHT` | Shot | episode | `SHT-NG-S01E01-0142` |
| `SEQ` | Sequence | episode | `SEQ-NG-S01E01-004` (3 digits) |
| `PC`  | Prompt card | episode or studio | `PC-NG-S01E01-0037`, `PC-STUDIO-0009` |
| `AST` | Asset | episode | `AST-NG-S01E01-0142` |
| `CUE` | Music cue | episode | `CUE-NG-S01E01-0011` |
| `CLR` | Clearance record | line or studio | `CLR-NG-0019` |
| `ADV` | Advisory ruling | line | `ADV-NG-0004` |
| `COR` | Correction | line | `COR-NG-0002` |
| `STA` | Style anchor | line or studio | `STA-NG-0006` |

## Allocation

IDs are allocated by the toolkit, never by hand:

```bash
python -m studio_ops new-record --type source --line ng-nigeria
python -m studio_ops new-record --type claim  --line ng-nigeria
```

The allocator reads the highest existing serial for the (type, scope) pair and takes
the next. It refuses to run if it finds a gap-and-collision pattern suggesting a
hand-edited ID, because silent ID reuse corrupts the audit trail irreversibly.

## Referencing

| Context | Form |
|---|---|
| In prose / script | `{{CLM-NG-0117}}` — double braces, stripped at render |
| In YAML | Bare string: `sources: [SRC-NG-0042, SRC-NG-0043]` |
| In a filename | Prefix: `SRC-NG-0042_kano-chronicle-scan.yaml` |
| In an asset filename | See [naming_conventions.md](naming_conventions.md) |

## Lifecycle states

Every record carries `status`:

| State | Meaning | `TBD` allowed? |
|---|---|---|
| `draft` | Being written | yes |
| `review` | Submitted to a gate | yes, but each must link an open question |
| `locked` | Signed off; changes require re-open | **no** |
| `superseded` | Replaced; `superseded_by` names the successor | frozen |
| `retracted` | Withdrawn; `retraction_reason` required | frozen |

Records are never deleted. `retracted` is how the studio remembers that it was wrong
about something, which is more valuable than a clean-looking registry.
