---
chain: map_and_graphic
version: 1.0.0
status: active
updated: 2026-08-07
owners: [visual-director, research-lead]
---

# Chain — maps and data graphics

Graphics assert. A map asserts a border; a chart asserts a quantity; a timeline
asserts a sequence and usually implies a cause. They carry claim IDs like narration.

Standard: [../../standards/data_graphics.md](../../standards/data_graphics.md).

## Why generation plays a small role here

A generated map is an unusable map. Models produce plausible-looking cartography with
invented coastlines, fictional labels, and borders drawn from nothing. Graphics are
**constructed from data**, not prompted.

Generation's legitimate role is texture and surround — a parchment ground, a stylised
frame — never the information layer.

## Steps

| # | Step | Tool | Notes |
|---|---|---|---|
| 1 | Establish the claim | human | What does this graphic assert? Claim ID required before design begins. |
| 2 | Gather data | human | Coordinates, elevation, historical hydrography, quantities, dates — each with its source |
| 3 | Choose projection | human | Stated on the graphic. Projections make arguments about relative size. |
| 4 | Base layer | [after-effects](../post/after-effects/) / GIS / [blender](../scene3d/blender/) | Real elevation and hydrography data. Base map licences in [library/map_bases](../../library/map_bases/). |
| 5 | Information layer | [after-effects](../post/after-effects/) / [recraft](../image/recraft/) | Zones not hard borders; uncertainty visible; period names primary |
| 6 | *(optional)* Texture | image model | Ground, frame, atmosphere. Never labels or geometry. |
| 7 | Animate | [after-effects](../post/after-effects/) | Each animated stage asserts a date and needs its own claim ID |
| 8 | Review | research-lead | Sources present, projection stated, uncertainty encoded, names match entity records |

## Rules that catch most failures

- **Historical polities are zones, not outlines.** Gradient or hatched. A hard line
  only where a documented boundary is being depicted, carrying its source.
- **Modern borders are never drawn over pre-colonial periods** without an on-screen
  note that they are a modern overlay for orientation.
- **Period place names primary**, modern name once for orientation.
- **Animating expansion asserts dates for every stage.** Either every stage has a
  claim ID, or the animation becomes a single "greatest documented extent" frame.
- **No truncated bar axes.** Line charts may truncate with the baseline labelled.
- **Attested / estimated / modelled** encoded visually and keyed. Most pre-modern
  quantities are modelled.
- **Names checked mechanically against entity records**, not by eye.

## Vector where possible

[recraft](../image/recraft/) and native vector tools produce editable output, which
keeps textless masters and localised versions cheap. A baked raster map has to be
rebuilt for every language.

## Provenance

Provenance class `graphic`. The shot record carries the claim IDs. Sources appear on
the graphic or in a credit within the same sequence. Data files are archived with the
production so the graphic can be rebuilt or corrected.
