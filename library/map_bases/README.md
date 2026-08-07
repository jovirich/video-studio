---
title: Map bases
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, research-lead]
---

# Map bases

Base cartography that map graphics are built on: coastlines, hydrography, terrain,
graticules, and the neutral ground layers that a production's own annotation sits over.

Referenced from [../../standards/data_graphics.md](../../standards/data_graphics.md)
§ Maps, which is the standard these files serve.

**Maturity: DESIGNED.** Empty. No base map has been sourced or licensed.

## What goes in here

The **ground**, not the argument. A base map carries physical geography and a stated
projection. Everything a production adds on top — borders, territories, routes,
extents, labels, dates — is that production's claim, lives with that production, and is
sourced like any other claim.

The split matters because it is where map graphics go wrong. A base map that arrives
with borders already drawn has made an assertion the studio did not make, did not
source, and cannot defend, and it will be reused a dozen times before anyone notices
that nobody chose it. Prefer bases without political boundaries. Where a base carries
them, the manifest says so explicitly and the production either removes them or owns
them as a claim.

## Projection is recorded per base map

**Mandatory, per item, in the manifest.** Not per folder, not per project.

`data_graphics.md` requires the projection to be stated on the map or in the credit.
That is impossible to comply with if the file itself does not record which projection
it is in, and it is not recoverable by inspection — a rendered raster looks like a map
whichever projection produced it.

Two failures follow from an unrecorded projection:

- **Silent mixing.** Two bases in different projections, used in two sequences of the
  same production, present two different pictures of relative size and distance without
  anything on screen indicating that the ground changed.
- **Unregistrable overlays.** An annotation layer built for one projection placed over
  a base in another is wrong by an amount that varies across the frame — small enough
  near the centre to look right, large enough at the edges to be false.

Different projections make different political arguments about relative size. That is
`data_graphics.md`'s point, and it is why the projection is a recorded property of the
asset rather than a rendering detail.

Also recorded per item, for the same reason: the **datum or coordinate reference
system**, the **extent** the base covers, the **source date or vintage** of the
underlying data, and whether the base includes **political boundaries**.

## Licences vary per item

Cartographic data comes from many kinds of provider under many kinds of grant, and
**there is no folder-level licence**. Each base map is cleared on its own terms, with
its own row.

What varies, and what the row must therefore capture:

| Varies | What to record |
|---|---|
| Whether derivative works are permitted | Every use here is a derivative — the production annotates the base. |
| Attribution wording | Frequently prescribed to the word, and frequently required *on the map itself* rather than only in credits. A credit that must appear in-frame is a design constraint, not a paperwork item. |
| Share-alike obligations | Core/02 §3: `SA` variants have viral implications for the finished work. **Escalate before use.** A share-alike base map under a finished film is a decision about the film's licence. |
| Non-commercial restrictions | Core/02 §3: `NC` variants are incompatible with monetised distribution. |
| Redistribution of the data versus the rendered image | Often different grants. The studio distributes a rendered image; check that specifically. |
| Territory and term | As any other asset. |

Every base carries a row in
[../../rights/permissions/clearance_log.md](../../rights/permissions/clearance_log.md)
with a `CLR-STUDIO-*` ID. Where the base derives from a public dataset, the row records
the **exact licence variant** — not "open" — and the jurisdiction basis if the claim is
public domain. Core/02 §3: public-domain status is jurisdiction-specific, and a
production distributed globally faces the most restrictive relevant jurisdiction.

## Naming

```
map_<extent>_<projection>_<theme>_v<NN>.<tif|svg|geojson>

map_continent-africa_equal-area_coastline_v01.svg
map_world_equirectangular_terrain_v02.tif
```

Lowercase, ASCII, hyphens within a field, underscores between fields, per
[../../standards/naming_conventions.md](../../standards/naming_conventions.md). The
projection goes in the filename as well as the manifest — it is the property most often
needed at the moment someone is choosing a file, and a manifest lookup is one step more
than people take.

Vector preferred over raster wherever the source allows it: a raster base cannot be
re-projected, re-scaled for a 9:16 cutdown, or re-styled to sit under a different show
LUT without visible loss.

## Manifest and storage

`.tif` bases are gitignored ([../../.gitignore](../../.gitignore)); the manifest is not.
Per base: filename, SHA-256, **projection**, datum/CRS, extent, source and source date,
whether political boundaries are present, clearance ID, licence variant, attribution
wording, and whether that attribution must appear in-frame.

That last field exists because it is the one that changes a design after it is approved.
