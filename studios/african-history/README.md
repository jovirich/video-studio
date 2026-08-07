# African History Studio

Documentary about the histories of the African continent and its diasporas,
organised into production lines by region.

**Nigeria is line 01.** The line structure exists so that a second and third line —
another country, another region, a diaspora strand — open without disturbing the
first and without renegotiating anything at studio level.

| | |
|---|---|
| Canon pack | [`documentary-history`](../../packs/documentary-history) v0.1.0 |
| Status | `opening` — not yet cleared to greenlight |
| Lines | [`ng-nigeria`](lines/ng-nigeria) (01) |
| Platform | [video-studio](../../README.md) |

## Contents

| Path | Holds |
|---|---|
| [studio.yaml](studio.yaml) | Pack declaration, governance, decision register |
| [bible/00_charter.md](bible/00_charter.md) | Mission, scope, audience, independence, standing commitments |
| [bible/amendment_log.md](bible/amendment_log.md) | Changes to this studio's canon |
| [bible/corrections.md](bible/corrections.md) | Public, append-only correction log |
| [brand/](brand) | Identity, title cards, thumbnails, the reconstruction label |
| [lines/](lines) | Production lines |

## What this studio is bound by

In precedence order — a lower layer may tighten, never loosen:

1. [Platform core](../../core) — provenance, AI disclosure, rights, delivery, gates
2. [documentary-history pack](../../packs/documentary-history) — evidence, narrative,
   visual, sound, sensitivity, localisation
3. This studio's [bible](bible) — mission, scope, and any tightenings
4. A line's addendum — region-specific rules
5. A production's own record

## Before the first greenlight

Tracked in [studio.yaml](studio.yaml) under `decisions`. `studio_ops` refuses to
greenlight while any is `unresolved`:

- [ ] Mission, audience, and success conditions written into the charter
- [ ] AI-generated music policy decided
- [ ] Production language and orthography standards decided
- [ ] Visual identity defined for the Nigeria line
- [ ] Narration voice policy decided
- [ ] Advisory board contracted and registered
- [ ] Archive landscape surveyed
- [ ] Typefaces selected with full diacritic coverage for every line language

The last one blocks all brand design and is routinely discovered too late.

## Opening a second line

```bash
python -m studio_ops new-line --studio african-history --code gh-ghana --title "Ghana"
```

A line does not open until its three conditions are met — a named research lead with
domain competence, an agreed advisory contact, and a surveyed archive landscape. The
schema enforces this: `line_status: open` fails validation while any is false.

Candidate lines and the reasoning for their ordering belong in
[lines/README.md](lines/README.md).
