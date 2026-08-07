---
title: Graphics kit
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# Graphics kit

The reusable furniture of on-screen graphics: lower thirds, title and card layouts,
frames and mattes, chart and timeline components, caption and label plates, transition
elements.

**Maturity: DESIGNED.** Empty. Nothing has been designed or licensed.

## What goes in here

**Structure, not identity.** A kit item defines where a thing sits, how it is spaced,
how it animates, and what it does at 9:16 as well as 16:9. A studio's brand — its
colours, its typeface, its logo, its motion signature — is applied *to* the kit, from
`studios/<code>/brand/`, and is never baked into it.

The test: could a second studio with a completely different look use this file without
editing it? If not, it is a brand asset in the wrong folder, and it will be copied and
diverged rather than reused.

| Belongs here | Belongs to a studio or line |
|---|---|
| A lower-third layout, its safe margins, its in and out | The colours and typeface it renders in |
| A chart component honouring [../../standards/data_graphics.md](../../standards/data_graphics.md) | The palette that encodes the categories |
| A disclosure card layout for the in-frame generative mark | The wording, which core and the pack set |
| A timeline component with its uncertainty rendering | The events on it, which are claims |
| Caption and label plates sized for the delivery specs | The language and orthography |

## What the kit must satisfy

Kit items are shared, so their constraints are the union of every studio's:

- **Accessibility.** Contrast and legibility are checked at the technical QC gate for
  every deliverable — [../../README.md](../../README.md) § Platform guarantees. A kit
  component that only meets contrast against one brand's background has moved the
  problem rather than solved it. Record the contrast assumptions.
- **Reframing.** Cutdowns are crops ([../../docs/status.md](../../docs/status.md)). A
  component whose 16:9 layout does not survive a 9:16 crop makes every cutdown a
  redesign. Safe areas are recorded per component, not assumed.
- **Diacritics.** Text plates must accommodate stacked marks without clipping, at every
  weight — see [../fonts/README.md](../fonts/README.md). A lower third whose height was
  set by unaccented Latin will clip the first accented character it meets, and it will
  meet one.
- **Data-graphics discipline.** Chart, map, and timeline components carry the
  requirements in [../../standards/data_graphics.md](../../standards/data_graphics.md)
  in their structure: a place for the projection statement, a place for the source
  credit, a rendering for uncertainty. A component with nowhere to put a source credit
  produces graphics without source credits.
- **Localisation headroom.** A plate sized to fit one language's string length will
  break on a longer one. Record the character budget it was designed to.

## Licence requirement

Every element in a kit file is licensed material, and a kit is usually an assembly of
several: typefaces, icon sets, textures, template projects, plugins the project depends
on, and any purchased motion-graphics package it was built from.

**Each of those is cleared separately**, and the kit's manifest entry lists them all.
A kit item cleared as a single line — "in-house" — hides the icon set that came from a
download and the plugin the render depends on.

- Purchased template packages: the grant must permit **use in a distributed finished
  film** and, where the studio is producing for a third party, **use in client work**.
  Many template licences distinguish the two.
- Icon and texture sets: attribution wording, and whether attribution is required
  on screen.
- Plugin dependencies: a plugin needed to *render* the kit is a dependency of every
  production that uses it, and the licence must cover every render node.
- Studio-authored components: still get a row, recording that the studio owns them —
  the fact a chain of title needs to state.

All rows go in
[../../rights/permissions/clearance_log.md](../../rights/permissions/clearance_log.md)
with `CLR-STUDIO-*` IDs, under the category matching each element.

## Naming

```
gfx_<component>_<variant>_v<NN>.<ext>

gfx_lower-third_two-line_v01.aep
gfx_card_disclosure_v02.svg
gfx_chart_bar-horizontal_v01.svg
```

Lowercase, ASCII, hyphens within a field, underscores between fields, per
[../../standards/naming_conventions.md](../../standards/naming_conventions.md). The
component name describes **function**, never appearance — `gfx_card_disclosure` stays
correct through a redesign; `gfx_card_gold-serif` does not.

Prefer resolution-independent formats. A raster component is a component that will be
rebuilt for the first delivery spec it does not fit.

## Manifest and storage

Project files and binaries are gitignored ([../../.gitignore](../../.gitignore));
the manifest is not. Per component: filename, SHA-256, the tool and version it was
authored in, its dependencies (fonts, plugins, icon sets, each with a clearance ID),
safe-area and contrast assumptions, character budget, the aspect ratios it has been
proved in, and the date it was last opened successfully.

That last field is not bureaucratic. A motion-graphics project is only as durable as
the application version that opens it, and a kit nobody has opened in two years is a
kit of unknown state.
