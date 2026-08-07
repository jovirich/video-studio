---
title: Thumbnail system
status: template
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, showrunner]
---

# Thumbnail system

Rules for the still image that represents a production wherever it is listed.

Referenced from [core/03 §4](../../../core/03_distribution_and_formats.md). The
honesty standard below is core's and is not negotiable at this layer; everything else
is studio brand and is `TBD — Visual Director`.

Maturity: **NOT STARTED**. No thumbnail exists, because no production exists. The
rules are written now because a thumbnail is produced under launch-day pressure, by
whoever is available, at the moment when the argument for cutting a corner is
strongest and the person who would object is in a mix.

## 1. The honesty standard

> **A thumbnail using generated imagery carries the same honesty standard as the
> production.** It may not depict something the production shows to be false, and it
> may not be presented as a photograph.
> — [core/03 §4](../../../core/03_distribution_and_formats.md)

This is the whole of the section that matters. Three things follow from it, and each
closes a specific loophole that will otherwise be found:

1. **A thumbnail is not marketing collateral operating under different rules.** It is
   the first factual assertion the production makes, it is seen by everyone including
   the people who never watch, and it is the only frame most of the audience will ever
   see. If the frame is not defensible, the production is not defensible.

2. **A thumbnail may not assert what the production declines to assert.** If a
   sequence is cut because the evidence would only carry it at `probable`, a thumbnail
   cannot depict it as though it were settled. If a detail is deliberately framed out
   of a reconstruction because it is unattested
   ([pack 04 §6](../../../packs/documentary-history/04_visual_language.md) — *"if the
   roof form is unattested, frame below the roofline"*), it does not reappear in the
   key art because the key art needed a silhouette. The evidence chain does not stop
   at the edge of the video file.

3. **It may not be presented as a photograph.** Generated imagery may be used and is
   expected to be. What is prohibited is presentation that invites a viewer to read it
   as a found photograph or as archival material — a photographic grain treatment on a
   reconstruction, a false border or mount, an aged-print treatment, a caption or title
   overlay implying a date and place of capture, or a crop that mimics a known archival
   format. See the standing prohibition in
   [core/01 §2](../../../core/01_provenance_and_ai_disclosure.md) against generating
   material likely to be taken for a genuine historical item; a thumbnail is a
   distribution of exactly that material at maximum reach.

| Provenance class of the source frame | Permitted in a thumbnail |
|---|---|
| `archival`, `artefact`, `contemporary` | Yes, with the same rights clearance and the same credit obligations as in the production. A thumbnail is a use. |
| `reconstruction`, `interpretive` | Yes, subject to §2 |
| A generated frame that is not in the production | **No.** A thumbnail is derived from the production, like any other cutdown ([core/03 §1](../../../core/03_distribution_and_formats.md)). Generating a frame purely for the thumbnail routes an image to the audience around every gate the production passed. |
| Anything under an advisory hold | **No**, and the hold applies to the thumbnail by default. Consent for a documentary is not consent for a thumbnail ([pack 07 §7](../../../packs/documentary-history/07_cultural_sensitivity.md)). |

## 2. Labelling a thumbnail

The in-frame reconstruction mark ([labelling_system.md](labelling_system.md)) is
designed for moving image inside a player the studio controls. A thumbnail is a still,
displayed at a size the studio does not control, in a grid the studio does not
control, often cropped.

`TBD — Visual Director`, but the decision is constrained and it is **not** "omit the
mark":

- The mark, or a still-image equivalent of it, is carried on any thumbnail whose
  primary image is `reconstruction` or `interpretive`.
- It is subject to the same floors as the in-frame mark — contrast measured, inside
  the crop that survives at the smallest listing size, legible at that size.
- If the mark cannot be held legibly at the platform's smallest rendering, the
  conclusion is that **that frame is not a usable thumbnail**, not that the mark is
  dropped. This will occasionally cost the studio its best-looking option, which is
  the point at which the rule is doing work.

## 3. Legibility at small size

A thumbnail is designed at its **smallest** displayed size and checked at its largest,
never the reverse. Design at full resolution and the result is a wide shot with six
elements that resolves, in a listing, to a grey rectangle.

| | |
|---|---|
| Design size | `TBD — Visual Director.` Set it from the actual smallest rendering on the platforms in scope, and re-set it when the platform set changes. |
| Subject scale | One subject, large. `TBD` as a minimum fraction of frame. |
| Depth cues | A thumbnail reads by silhouette and value structure, not by detail. Test in greyscale; if it fails in greyscale it fails on a phone in daylight. |
| Contrast floor | `TBD — Visual Director`, not below the on-screen text floor of **4.5:1** for any text element ([delivery_specs](../../../standards/delivery_specs.md) § On-screen text). |
| Compression | Checked after the platform's re-encode, not before. Platforms re-encode aggressively and fine texture is the first thing lost. |

## 4. Text on a thumbnail

| | |
|---|---|
| Maximum words | `TBD — Visual Director.` Set a hard number and hold it. Every unenforced limit here becomes six words in a smaller size. |
| Maximum lines | `TBD`, and it is small. |
| Minimum size | `TBD`, expressed as a fraction of thumbnail height, tested at the smallest listing size. |
| Typeface | The studio's, once it exists. Full diacritic coverage required — a thumbnail carrying a stripped mark is the same prohibited failure as a title card carrying one ([pack 09 §2](../../../packs/documentary-history/09_localization.md)). |
| Relationship to the title | The text does not contradict, exaggerate, or extend the title. Two different claims in the listing is a claim the production never made. |
| Prohibited | Fabricated quotation marks around words nobody said; invented "leaked"/"declassified"/"banned" framing; numerals implying a precision the claim record does not carry; arrows and circles pointing at nothing the production discusses. |

## 5. Faces

Faces carry attention, and they are also where the studio's own rules bite hardest.

- **A named historical individual is not depicted in a thumbnail** on a generated
  likeness. Synthesising a real person's likeness without consent — impossible for a
  historical figure — is a standing prohibition
  ([core/01 §2](../../../core/01_provenance_and_ai_disclosure.md)), and a thumbnail is
  its most public possible use.
- **Unnamed and crowd figures** follow the reconstruction craft rules
  ([pack 04 §6](../../../packs/documentary-history/04_visual_language.md)) and remain
  unnamed. A face used to represent a specific person by implication — by title, by
  caption, by adjacency — is the same violation with an extra step.
- **A living person** requires consent for this use specifically
  ([pack 07 §3](../../../packs/documentary-history/07_cultural_sensitivity.md)). An
  interviewee's consent to appear in a production is not consent to be the
  thumbnail; that is a distinct scope and it is asked for distinctly.
- **Identifiable victims of documented violence** are never used, in any treatment, at
  any size ([core/01 §2](../../../core/01_provenance_and_ai_disclosure.md)).
- **Expression** is an editorial choice, not a click device. A reaction face
  manufactured for a thumbnail asserts an emotional register the production does not
  support, and on historical subjects it usually asserts something about a people.
  Pan-regional pastiche is the model's default and will be produced unless the review
  actively prevents it ([pack 07 §6](../../../packs/documentary-history/07_cultural_sensitivity.md)).
- **Skin-tone rendering** is checked here exactly as it is checked on every shot with
  people ([pack 04 §4](../../../packs/documentary-history/04_visual_language.md)). A
  thumbnail is frequently graded separately for punch, and that is precisely where the
  show LUT's discipline gets abandoned. The line's rendering intent applies —
  [lines/ng-nigeria/style/visual_identity.md](../lines/ng-nigeria/style/visual_identity.md).

## 6. Series recognisability

A viewer should identify the studio, and the line, from a thumbnail in a grid before
reading a word.

| | |
|---|---|
| Fixed elements | `TBD — Visual Director.` Candidates: a consistent mark position, a fixed type treatment, a fixed compositional zone, a line-level colour signature. Choose few and hold them absolutely. |
| Line differentiation | `TBD.` Each line has its own look ([lines/ng-nigeria/style/visual_identity.md](../lines/ng-nigeria/style/visual_identity.md)); the thumbnail system must let a line be visually distinct while remaining recognisably this studio. A single continental look would be a mistake, and a thumbnail grid is where that mistake is most visible. |
| What recognisability buys | It is the only defence against the studio's material being compared, in a grid, against unsourced history content that is optimising for the same click. The studio cannot win that comparison on clickability; it can win it on being identifiable and then being right. |
| Consistency vs. freshness | Consistency wins. A system that is revised per episode is not a system. Revisions are versioned and dated in [brand_guide.md](brand_guide.md). |

## 7. A/B testing discipline

Testing thumbnails is permitted. Testing is a measurement of attention, and it is
never an override of §1.

1. **Every variant passes the same review before it enters a test.** A variant is not
   "just a test" — it is published, to a real segment of the audience, and if it is
   not defensible it must not be shown to anyone.
2. **A variant that wins on an accuracy violation is discarded, and the violation is
   recorded.** The temptation runs in one direction: the misleading variant usually
   wins, because misdirection is effective. That is the reason for the rule, not an
   argument against it.
3. **What is being optimised is stated in advance.** Click-through alone selects for
   overclaiming. Pair it with a retention or completion measure, or accept that the
   test will reliably select the least honest image.
4. **Tests are logged** — variants, dates, segments, result, decision — so that a
   later question about what a viewer saw has an answer. A viewer who reports being
   misled by a thumbnail that is no longer live is owed a straight response, and
   [bible/corrections.md](../bible/corrections.md) applies: a thumbnail that misled is
   a correctable error and it is corrected in public.
5. **A thumbnail change on a published production is a change to published material.**
   Silent replacement is prohibited by
   [core/03 §6](../../../core/03_distribution_and_formats.md) for masters; the same
   logic applies here, and a swap made because the first choice misled is logged as a
   correction, not as an optimisation.

## 8. Misdirection

Prohibited outright, at this layer and above. Curiosity gaps are permitted; a
curiosity gap invites a question the production answers. Misdirection implies an
answer the production does not give.

The test, applied to the pair of title and thumbnail together:

> **Would a viewer who watched the whole production feel that the thumbnail described
> it?**

If the honest answer is no, it does not ship, regardless of how it tests. Specific
prohibited moves, none of them hypothetical:

- Depicting an event, object, structure, or scale that the production does not
  establish, or that it establishes as contested or false.
- Implying a discovery, a secret, a suppression, or a reversal that the production
  does not make.
- Using a real archival image in a way that implies a different time, place, or people
  — a **misleading true statement**, and the failure mode
  [pack 01 §1](../../../packs/documentary-history/01_editorial_standards.md) names as
  the one that kills documentaries.
- Composite treatments that read as a single photograph.
- Implying a claim the title does not make, so that the pair asserts something neither
  does alone.

A title implying a claim the production does not make is already an accuracy failure
under [pack 01 §1](../../../packs/documentary-history/01_editorial_standards.md). The
thumbnail is held to that standard, and title and thumbnail are reviewed **together**,
because the misdirection is usually in the combination.

## 9. Review and delivery

| | |
|---|---|
| Gate | Picture lock for the image; the honesty test at fact-check alongside the description and on-screen text |
| Owner | Visual Director, with the Showrunner signing the title/thumbnail pair |
| Advisory | Required where the image touches any category in [pack 07 §2](../../../packs/documentary-history/07_cultural_sensitivity.md). An advisory hold on a thumbnail blocks publication, not just the image. |
| Provenance | Every thumbnail is an asset with a manifest entry, a prompt card if generated, and a rights status. It ships in `artwork/` in the delivery package ([delivery_specs](../../../standards/delivery_specs.md) § Delivery package). |
| Specs | `TBD — Visual Director + Pipeline Engineer.` Dimensions, colour space, file size ceilings and safe-crop margins per platform, once the platform set is decided (`runtime_and_platforms`, `unresolved` in [studio.yaml](../studio.yaml)). |
