---
title: Fonts
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, cultural-advisor]
---

# Fonts

Typefaces used in titles, lower thirds, captions, maps, charts, and every other frame
of text the platform puts on screen.

**Maturity: DESIGNED.** Empty. No typeface has been selected or licensed.

## The constraint that eliminates most typefaces

**Full diacritic coverage for every language any line uses.**

This is first because it decides the outcome. Licence and taste are real constraints;
this one is a filter, and it removes most candidates before either of the others is
reached.

A production line declares its on-screen languages in its `line.yaml`
([../../standards/schemas/production_line.schema.json](../../standards/schemas/production_line.schema.json)),
and that schema already says why: *"Font selection depends on the union of their
diacritic coverage."* The union, not the intersection. A typeface that handles four of
a line's five languages handles none of them, because the fifth one appears in the same
lower third as the other four and cannot be set in a fallback without the fallback
being visible.

What "full coverage" means in practice, and why the usual shortcuts fail:

- **Every mark, in every position, at every weight and optical size the design uses.**
  A face whose bold weight lacks a mark the regular weight has will silently fall back
  mid-word.
- **Stacked and combining marks composed correctly**, not merely present in the
  character set. A mark that exists but collides with the ascender, or sits at the
  wrong height over a capital, is a coverage failure that a glyph-count check passes.
- **Tone marks where a line's languages are tonal.** `production_line.schema.json`
  carries a `tonal` flag per language for exactly this reason.
- **Rendering under the actual pipeline**, not in a design tool. The NLE, the caption
  burner, the graphics renderer, and the platform's own subtitle renderer each compose
  marks differently, and each is a place coverage breaks.
- **Fallback is not coverage.** A fallback font in a title card is a different typeface
  appearing mid-sentence. It will be noticed by exactly the audience the line most
  needs to be careful with.

The test is not "does the font support the language" as claimed by a specimen page. It
is: set the longest real string the line will use, in every weight, render it through
the delivery pipeline, and look at it. That test is **NOT RUN** — no line has declared
its languages beyond `TBD`, so no typeface can be selected yet. This blocks brand
design and every graphic, and it is a known blocker, not an oversight.

Getting this wrong is not a typographic embarrassment. Setting a language's own words
without its marks, in a production about that language's speakers, is an editorial
failure with a typographic cause.

## Licence requirement

Category *Fonts* in
[../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §2. Two
things must be recorded, and both are commonly wrong:

**1. A tier covering broadcast and streaming use specifically.** A desktop licence
covers making artwork. It does not necessarily cover embedding the rendered result in
a distributed film, and broadcast/OTT is frequently a separate, separately-priced grant.
This is the same distinction the model terms register draws between "commercial use"
and "broadcast/streaming use specifically" — asked separately, or it does not get asked.

**2. The seat count.** Every workstation, every render node, every machine an editor,
designer, or contractor opens the file on. Seat counts are exceeded by accident, in the
ordinary course of a freelancer joining for two weeks, and the overage is discovered at
audit rather than at install.

Also record, because they bite later: whether the licence permits **embedding** in a
delivered file, whether it permits **modification** (a designer adding a missing mark
is a modification and is frequently prohibited), and whether it is **perpetual or
subscription** — a subscription face that lapses affects every master still in
production and, depending on the grant, every master already delivered.

Every typeface here carries a row in
[../../rights/permissions/clearance_log.md](../../rights/permissions/clearance_log.md)
with a `CLR-STUDIO-*` ID, including open-licence faces. An open licence is still a
licence with terms, and "it was free" answers none of the questions above.

## Naming

```
<foundry-or-project>_<family>_<style>_v<NN>.<otf|ttf|woff2>
```

Lowercase, ASCII, hyphens within a field, underscores between fields, per
[../../standards/naming_conventions.md](../../standards/naming_conventions.md). Keep
the family and style as the foundry names them — renaming a style to something tidier
breaks the match between the file, the licence, and the design document.

Variable fonts: one file per family, with the axes recorded in the manifest rather than
in the filename.

## Manifest and storage

Font binaries are gitignored ([../../.gitignore](../../.gitignore)); the manifest is
not. Per family, the manifest records: family, styles held, file SHA-256s, clearance ID,
licence tier, **seat count granted and seats in use**, embedding permission,
modification permission, expiry if any, and the **coverage evidence** — which languages
were tested, through which renderer, on what date, by whom.

The coverage evidence is the point of the manifest entry. Without it, "we checked" is a
memory, and the next person to add a language has no way to know what was checked
before.
