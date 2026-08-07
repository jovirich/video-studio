---
title: Brand — African History Studio
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, showrunner]
---

# Brand

The studio's identity system: how the work looks as a *studio*, as distinct from how
any one line looks on screen.

Maturity: **NOT STARTED**. Nothing in this folder has been designed. Every value is
`TBD`, and the reason is not that nobody has got to it — it is that the first
decision is blocked on a dependency described below, and starting anywhere else
produces work that has to be thrown away.

## 1. What lives here

| Document | Holds | Status |
|---|---|---|
| [brand_guide.md](brand_guide.md) | The identity system: logo, typography, colour, motion signature, title cards, lower thirds, end cards | **NOT STARTED** — structure only, all values `TBD` |
| [labelling_system.md](labelling_system.md) | Design spec for the reconstruction/interpretive on-screen mark required by [pack 04 §7](../../../packs/documentary-history/04_visual_language.md) and [core/01 §3](../../../core/01_provenance_and_ai_disclosure.md) | **NOT STARTED** — constraints fixed, design `TBD` |
| [thumbnail_system.md](thumbnail_system.md) | Thumbnail rules, including the honesty standard from [core/03 §4](../../../core/03_distribution_and_formats.md) | **NOT STARTED** — rules written, design `TBD` |

## 2. What does *not* live here

| Material | Where | Why |
|---|---|---|
| The look of the picture — palette, grade, lens set, light behaviour, texture | the line's `style/` folder, e.g. [lines/ng-nigeria/style/](../lines/ng-nigeria/style/README.md) | A single continental look would be a mistake. Each line defines its own. |
| Show LUTs, style anchor files, font binaries | [library/](../../../library/) | Shared, versioned, checksummed assets — not documents |
| Delivery-side numbers (safe areas, contrast floors, minimum text size) | [standards/delivery_specs.md](../../../standards/delivery_specs.md) | Machine-checked at technical QC. Brand may tighten them; it may not restate them and drift. |
| Whether a mark is required at all, and on which shots | [pack 04 §7](../../../packs/documentary-history/04_visual_language.md) | Genre canon. Brand designs the mark; the pack decides it exists. |

Brand is downstream of all four. It is a *rendering* of decisions made elsewhere, and
treating it as the place where those decisions get made is how a studio ends up with
an identity that its own delivery spec rejects.

## 3. The hard dependency — read this before opening a design file

> **Typeface selection is blocked on knowing every language and every diacritic the
> studio's lines will put on screen.**
> [pack 09 §2](../../../packs/documentary-history/09_localization.md) —
> *"This constrains typeface selection and must be settled before brand design
> begins."*

The rule that creates the block is short and absolute: diacritics and tone marks are
used **correctly and completely**, and stripping a mark because a font or a pipeline
cannot render it is not an available option — the font changes, or the pipeline
changes. A typeface must therefore cover the union of every mark used across every
language on the line's language register, in both the display and the text face, in
every weight the system uses, with correct mark positioning rather than a fallback
glyph substituted from a different family.

That requirement eliminates most typefaces, including most of the ones a designer
would shortlist on feel. It is also the cheapest constraint in the entire brand
system to satisfy *first* and the most expensive to satisfy *last*.

### What breaks if this is ignored

The failure is not "the type looks slightly wrong". It is:

- A combining mark renders as a fallback box, or lands on the wrong side of the
  glyph, or is silently dropped by the NLE's text engine — and it is caught at
  picture-lock text QC ([pack 09 §8](../../../packs/documentary-history/09_localization.md)),
  which is after every title card, lower third, map label, and end card has been
  built.
- The remedies at that point are: re-typeset the entire graphics package in a
  different face, or strip the marks. The second is prohibited. The first costs the
  whole graphics build.
- On a tonal language, a dropped or misplaced tone mark frequently produces a
  *different word*. It is a factual error on screen, correctable only by a re-render,
  and it is exactly the error that tells a regional audience nobody from the place was
  in the room.

### The order of work, and it is not negotiable

```
1. Line language register confirmed          lines/ng-nigeria/languages/README.md
   → which languages appear on screen                    Cultural Advisor
2. Orthography standard chosen per language              Cultural Advisor
   → which marks are actually used
3. Diacritic coverage requirement compiled               Visual Director
   → the union across all lines, as a character set
4. Typeface candidates tested against that set           Visual Director
   → rendering verified in the NLE, not in a specimen PDF
5. Licensing cleared for broadcast + delivery territories  Rights & Clearances
6. EVERYTHING ELSE IN BRAND DESIGN
```

Steps 1 and 2 are `unresolved` decisions in [studio.yaml](../studio.yaml)
(`production_language`, `orthography_standards`). Until they resolve, **nothing else
in brand design can start** — not the logo, not the colour system, not the title
cards. A logo drawn in a face the studio cannot use is not a head start.

Step 4 is a test, not a review. A specimen sheet proves a glyph exists in the font
file; it does not prove the studio's text engine composes it correctly at the sizes
and against the backgrounds the studio actually uses. The two are different claims,
and only the second matters.

## 4. Where brand may tighten, and where it may not

Brand may set values **stricter** than [delivery_specs](../../../standards/delivery_specs.md)
— a larger minimum size, a higher contrast floor, a tighter safe area. It may never
set a looser one, and a brand document that appears to is read as the delivery spec's
value, not the brand's.

Where a brand decision would require loosening a pack or core rule, the answer is a
different brand decision. There is no design problem in this studio whose solution is
an unlabelled reconstruction.

## 5. Before any of this is binding

The studio bible is **not ratified** ([bible/amendment_log.md](../bible/amendment_log.md)).
Nothing in this folder binds a designer until it is, and any work produced in the
interim is exploratory and marked as such.
