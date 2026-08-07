---
title: Shared library
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, pipeline-engineer]
---

# Shared library

Platform-level assets that more than one studio, line, or production legitimately
uses: colour, type, sound, cartography, graphics, voice, and the style anchors that
hold visual continuity together.

**Maturity: DESIGNED.** Every folder below is empty. Nothing has been licensed,
nothing has been placed, and no manifest has been written.

## What belongs here

Three tests, all of which must pass:

1. **Shared** — more than one line or studio could reasonably use it. A single-use
   asset is not library material even if it is beautiful.
2. **Cross-studio safe** — it carries no editorial position, no subject matter, and no
   brand. Per [../CONTRIBUTING.md](../CONTRIBUTING.md), a platform-level file must
   never name a studio or its subject.
3. **Licensed for the platform, not for one project** — the grant covers the studios
   that will use it, at the seat count they will need, for the distribution they
   intend. A licence bought for one production and reused here is a breach waiting for
   an audit.

## What does not belong here

| Not here | Where instead |
|---|---|
| A studio's brand typography, logo, or motion signature | `studios/<code>/brand/` |
| A line's palette, lens set, or visual identity document | `studios/<code>/lines/<line>/style/` |
| Reference imagery for one sequence or one shot | that production's folder |
| Anything naming a region, a period, a people, or a subject | a line, not the platform |
| Generated output | the asset store, referenced by the production's manifest |
| Anything used once | the production that used it |

Show LUTs are the deliberate exception, explained in [luts/README.md](luts/README.md):
the *file* sits here because the grading pipeline needs one canonical location for it
and because two lines under one studio must not resolve the same LUT name to different
bytes — while the *decision* it encodes belongs to a line, which owns and versions it.
Getting that split wrong in either direction produces either a line whose look drifts
between productions, or a platform folder full of one studio's taste.

## Every item carries a licence record

**No exceptions, no categories that are obviously fine.** Every item in every folder
below has a row in
[../rights/permissions/clearance_log.md](../rights/permissions/clearance_log.md) with
a `CLR-STUDIO-*` ID, before it is placed here — not after, and not at delivery.

This is where a shared library goes wrong, and it goes wrong quietly. A LUT is
downloaded for a test, survives into a delivered grade, and nobody ever asked whether
its licence permits redistribution inside a finished film. A font is licensed for one
seat and ends up on four machines and a render node. A music bed marked "royalty free"
turns out to describe a payment model rather than a grant. Each of those is invisible
until a distributor asks, at which point the answer has to be reconstructed from
memory by someone who was not there.

The clearance-log rule that makes this work is the one in
[../core/02_rights_and_licensing.md](../core/02_rights_and_licensing.md) §1: an item
absent from the log is uncleared **by definition**. There is no informal cleared
state, and "it came with the software" is not one.

`CLR-STUDIO-*` scope, not a line scope — library items are cross-line by construction,
and scoping them to the line that happened to buy them is how the second studio ends
up unable to find the licence.

## Binaries are gitignored; manifests are not

[../.gitignore](../.gitignore) excludes the media itself — `*.cube`, `*.otf`, `*.ttf`,
`*.woff2`, everything under `music_beds/` and `sfx/` and `style_refs/`, `*.tif` map
bases — and then re-includes `README.md`, `.gitkeep`, and `*.yaml` beneath
`library/`.

That split is intentional and it is the same split as the rest of the platform: git
holds the *record*, the object store holds the *bytes*. What it means in practice:

- **The manifest is the source of truth about what exists.** A file present on someone's
  disk but absent from a manifest is not in the library; it is on someone's disk.
- **A clone of this repository is enough to know what the library contains**, what each
  item is licensed for, and what its checksum should be — without transferring
  gigabytes.
- **Checksums are how the two halves are kept honest.** This matters most for
  [style_refs/](style_refs/), where a silently changed file breaks continuity across
  every shot that referenced it.
- **Never commit a binary here.** The gitignore will usually stop you; when it does
  not, the reviewer should.

## Folders

| Folder | Holds | The constraint that actually decides selection |
|---|---|---|
| [luts/](luts/) | Show LUTs and technical transforms | One show LUT per production line, versioned. Shot grading works *under* it. |
| [fonts/](fonts/) | Typefaces for titles, captions, and graphics | **Full diacritic coverage for every language any line uses.** This eliminates most typefaces before licence or taste is considered. |
| [music_beds/](music_beds/) | Licensed underscore and texture | The licence must permit inclusion in a distributed finished film. |
| [sfx/](sfx/) | Effects, foley, and ambience | As music beds. "Royalty free" does not answer the question. |
| [map_bases/](map_bases/) | Base cartography for map graphics | Projection is recorded per base map. Licences vary per item. |
| [graphics_kit/](graphics_kit/) | Lower thirds, cards, frames, chart furniture | Must be neutral enough to carry any studio's brand on top of it. |
| [voice_profiles/](voice_profiles/) | Licensed synthetic voice profiles | A licensed voice is a consenting, compensated human. Consent scope lives in the clearance log. |
| [style_refs/](style_refs/) | Fixed, checksummed style anchors referenced by `STA-*` | The files must never silently change. That is the entire mechanism. |

## Naming

Per [../standards/naming_conventions.md](../standards/naming_conventions.md):
ASCII only, no spaces, lowercase, hyphens within a field and underscores between
fields, versions as `_vNN`. Each folder's README states the pattern for its own asset
type; where they differ from the general rule they say why.

## Adding an item

1. Establish the licence **first**. Read the grant, not the marketing page.
2. Open a clearance row and take a `CLR-STUDIO-*` ID.
3. Place the binary in the object store; record it in the folder's manifest with its
   SHA-256 and its clearance ID.
4. Commit the manifest. Do not commit the binary.
5. For [style_refs/](style_refs/), the checksum is load-bearing rather than
   administrative — see that folder's README before adding anything.

Steps 1 and 2 are in that order deliberately. An item placed first and cleared later is
an item that is in use before anyone knows whether it may be.
