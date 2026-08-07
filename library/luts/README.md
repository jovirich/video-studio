---
title: LUTs
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# LUTs

Colour transforms: show LUTs, and the technical transforms that get material into and
out of the working space.

**Maturity: DESIGNED.** Empty. No LUT has been authored or licensed.

## What goes in here

| Kind | What it is |
|---|---|
| **Show LUT** | The look of one production line. Exactly one, versioned. |
| **Technical transform** | Log-to-display, colour-space conversion, camera or generator normalisation. Not a look. |
| **Utility** | Monitoring, viewing, and QC transforms used at the technical QC gate. |

Not here: a shot-specific grade, a sequence-specific correction, or anything that
exists to fix one asset. Those live in the production's grade project.

## One show LUT per line, versioned

**One.** Not one per season, not one per director, not one per sequence.

A production line is a coherent body of work, and its look is the thing an audience
recognises across episodes made months apart by different people. A second show LUT
means two looks, and nobody notices until the two episodes are watched back to back —
by which point both are delivered.

The LUT is versioned, never overwritten: `_v01`, `_v02`. A delivered production names
the exact version it was graded under, in the production record and in its grade
project. Overwriting a show LUT retroactively changes the look of every master that
referenced it and every shot still in progress against it, and it does so silently.
That is the single most expensive mistake available in this folder.

Versioning also means a look change is a *decision with a date* rather than a drift.
Bumping the version is cheap; explaining why episode four looks different is not.

## Shot grading works under the LUT, never around it

The order is fixed:

```
   source ──► technical transform ──► SHOT GRADE ──► SHOW LUT ──► display
                                      (balance, exposure,   (the look,
                                       continuity)           unmodified)
```

A shot is balanced **into** the show LUT. It is not corrected **after** it, and the
LUT is not disabled to make a difficult shot sit right.

Why this is a rule and not a preference:

- **A grade applied after the LUT is invisible to the LUT's own contrast handling**,
  so it fights the look rather than sitting inside it — and it fights it differently
  on every shot.
- **Disabling the LUT for one shot produces exactly one shot that is not in the show's
  colour space.** It will look correct in isolation, in the grading suite, on that
  monitor, and wrong in the cut.
- **The look becomes unreproducible.** If half the sequence is graded under the LUT
  and half around it, there is no version of the show LUT that renders the sequence
  consistently, and a future LUT revision cannot be applied at all.

If a shot cannot be balanced under the LUT, the shot is wrong or the LUT is wrong.
Both are fixable. A per-shot exception is not.

## Naming

```
<scope>_show_<slug>_v<NN>.cube          show LUT, scope is the line's id_scope or STUDIO
<scope>_tech_<from>-to-<to>_v<NN>.cube  technical transform
<scope>_qc_<slug>_v<NN>.cube            monitoring and QC
```

Lowercase, ASCII, no spaces, hyphens within a field and underscores between fields, per
[../../standards/naming_conventions.md](../../standards/naming_conventions.md). The
`v<NN>` is mandatory on every file, including the first one — an unversioned `_v01` is
what an unversioned file becomes the moment a second one exists.

The slug describes the look or the transform, never the tool or the settings.

## Licence requirement

A LUT is licensed material like any other, and the category in
[../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §2 is
explicit: **LUTs, plugins, and stock SFX require a licence permitting commercial
redistribution in a finished film.**

This is the specific trap for LUTs, because the transform is *baked into the delivered
image*. Unlike a plugin, which stays on the workstation, a LUT ships. Two questions
that a purchase page usually does not answer:

- Does the grant cover **redistribution of the output**, as opposed to use of the file?
- Does it cover **the number of workstations and render nodes** that will apply it?

Every LUT here — bought, bundled, free, or authored in-house — carries a row in
[../../rights/permissions/clearance_log.md](../../rights/permissions/clearance_log.md)
under category *LUTs, plugins, stock SFX*, with a `CLR-STUDIO-*` ID. A LUT authored by
the studio still gets a row: the row records that the studio owns it, which is the
fact a chain of title needs to state.

## Manifest and storage

`.cube` files are gitignored ([../../.gitignore](../../.gitignore)); the manifest is
not. The manifest records, per LUT: filename, version, SHA-256, clearance ID, the line
it belongs to, the working colour space it assumes, and the date it was locked.

The colour-space field is not optional. A LUT applied to material in a space it was not
built for produces a plausible-looking wrong image, which is the hardest class of error
to catch at QC.
