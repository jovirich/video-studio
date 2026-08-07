# Naming conventions

Enforced by `studio_ops validate --naming`. These exist so that sorting, globbing,
and cross-platform sync all behave, and so a filename tells you what a thing is
eighteen months later.

## Universal rules

1. **ASCII only in filenames.** Diacritics belong in the *content*, never the path.
   Sync tools, render farms, and NLEs mangle them differently on each platform.
2. **No spaces.** Underscore separates fields; hyphen separates words within a field.
3. **Lowercase**, except where an ID appears (IDs are uppercase) and except for the
   root whitelist files (`README.md`, `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`).
4. **Dates are `YYYY-MM-DD`.** Always. Never locale order.
5. **Versions are `vNN`**, zero-padded, never `_final`, `_final2`, `_FINAL_real`.
6. **Path length under 180 characters** from repo root — Windows still bites.

## Folders

| Pattern | Example |
|---|---|
| Studio-level | lowercase snake: `sources/`, `prompts/`, `templates/` |
| Ordered pipeline stages | `NN_name`: `02_script/`, `05_assets/` |
| Production line | `<iso2>-<name>`: `ng-nigeria`, `gh-ghana`, `et-ethiopia` |
| Episode | `S<NN>E<NN>_<slug>`: `S01E01_the-walls-of-x` |
| Records by ID | `<ID>_<slug>/`: `SRC-NG-0042_kano-chronicle/` |

The `NN_` prefixes on pipeline stages are load-bearing: they make the folder listing
itself a readable statement of the workflow order.

## Documents

```
<slug>.md                          general docs         beat_sheet.md
<ID>_<slug>.md                     record docs          CHR-NG-0007_example.md
<YYYY-MM-DD>_<slug>.md             dated artefacts      2026-08-07_advisory-ruling.md
_TEMPLATE_<slug>.md                templates            _TEMPLATE_source_record.md
```

Leading underscore on templates sorts them to the top of a listing and marks them as
not-real-content to both humans and the validator.

## Assets

```
<EPISODE>_<SEQ>_<SHOT>_<class>_<slug>_v<NN>.<ext>

S01E01_SEQ004_SHT0142_recon_walls-wide_v03.png
S01E01_SEQ004_SHT0142_recon_walls-wide_v03.mp4
S01E01_VO_narration_full_v07.wav
S01E01_SEQ002_MUS_bed-tension_v02.wav
```

| Field | Values |
|---|---|
| `class` | `recon`, `interp`, `arch`, `contemp`, `artefact`, `graphic`, `text`, `vo`, `mus`, `amb`, `sfx` |
| `slug` | kebab-case, ≤ 30 chars, describes content not tool |
| `v<NN>` | increments on every re-generation or re-render |

The slug describes **content**, never tool or settings. `walls-wide` is right;
`mj-v7-ar169-stylize250` is wrong — that information belongs in the prompt card and
the manifest, where it is queryable.

## Prompt cards

```
PC-<SCOPE>[-<EPISODE>]-<SERIAL>_<slug>.prompt.yaml

PC-NG-S01E01-0037_walls-establishing.prompt.yaml
PC-STUDIO-0009_generic-dust-motes.prompt.yaml
```

## Branches

```
studio/<area>-<slug>          studio/bible-music-policy
release/<episode>             release/s01e01
research/<episode>-<topic>    research/s01e01-fortifications
script/<episode>-<pass>       script/s01e01-draft-03
prompt/<episode>-<sequence>   prompt/s01e01-seq004
edit/<episode>-<version>      edit/s01e01-v05
fix/<slug>                    fix/manifest-validator-crash
```

## Prohibited patterns

The validator fails on any of these:

| Pattern | Why |
|---|---|
| Spaces in any path | Breaks shell pipelines and render farm queues |
| Non-ASCII in any path | Cross-platform normalisation differences |
| `final`, `FINAL`, `latest`, `new`, `old`, `copy`, `backup` in a name | Versions are numeric |
| `untitled`, `temp`, `test`, `asdf` | Committed accidents |
| A date in any format other than ISO | Ambiguity |
| An ID that does not match [id_system.md](id_system.md) | Breaks the reference graph |
| A file at repo root outside the whitelist | See [../CONTRIBUTING.md](../CONTRIBUTING.md) § File placement |
| `_TEMPLATE_` file with `status: locked` | A template was filled in place instead of copied |

That last one is the most common real mistake: someone opens the template, fills it
in, and saves over it. The validator catches it before the template is lost.
