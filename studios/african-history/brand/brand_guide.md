---
title: Brand guide
status: template
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# Brand guide — African History Studio

The studio identity system.

Maturity: **NOT STARTED**. This document is a structure with no content. Every value
below is `TBD`, and that is the correct state: the identity cannot be designed before
typeface selection, and typeface selection cannot happen before the language and
orthography decisions resolve. See [README.md](README.md) §3 for the dependency and
the order of work.

> **Do not fill this document top to bottom.** §2 Typography is the entry point. A
> logo, a palette, or a title card designed before the typeface is known is
> exploratory work that will be redone, and the risk is that it will instead be
> defended.

## 0. How to fill this in

Each section carries the same four fields, and a section is not complete until all
four are answered:

| Field | Meaning |
|---|---|
| **Decision** | The value. |
| **Owner** | Who decides. A role, not a committee. |
| **Rationale** | Why this and not the obvious alternative. A rationale is what makes the decision defensible in eighteen months against someone who wants it changed for a single episode's convenience. |
| **Constraint check** | Which delivery-spec, localisation, and accessibility floors it was tested against, and how — measured, not judged. |

Amendments follow [bible/amendment_log.md](../bible/amendment_log.md); a brand
specification carrying a technical constraint additionally needs the Pipeline Engineer.

## 1. Logo and wordmark

| Item | Value |
|---|---|
| Studio wordmark | `TBD — Visual Director` |
| Symbol / monogram, if any | `TBD.` Decide whether one exists at all before drawing one. |
| Clear space | `TBD`, expressed in units derived from the mark itself, never in pixels |
| Minimum size | `TBD`, as a fraction of frame height for screen use and an absolute for print |
| Monochrome and single-colour versions | `TBD`. Required, not optional — the mark must survive a monochrome grade and a platform's own treatment. |
| Placement on masters | `TBD.` Inside title safe (90%), per [delivery_specs](../../../standards/delivery_specs.md). |
| Line lock-ups | `TBD.` How a line's identity ([lines/ng-nigeria/style/visual_identity.md](../lines/ng-nigeria/style/visual_identity.md)) sits alongside the studio mark, given that each line looks different by design. |
| Misuse | `TBD.` Enumerate what is prohibited — stretching, re-colouring, re-setting the wordmark in another face, placing it on an unlabelled reconstruction. |

Owner: Visual Director. Rationale, constraint check: `TBD`.

## 2. Typography — **start here, and only here**

**Blocked.** Nothing else in this document may be decided first. The dependency is
stated in full in [README.md](README.md) §3; the short version is that diacritics and
tone marks are used correctly and completely, stripping them is prohibited
([pack 09 §2](../../../packs/documentary-history/09_localization.md)), and that
requirement eliminates most typefaces before aesthetics are considered.

| Item | Value |
|---|---|
| Diacritic coverage requirement | `TBD — Cultural Advisor.` The union of every mark used by every language on every line's register, compiled as an explicit character set, not described in prose. Currently underivable: the register is a candidate list with nothing confirmed — [lines/ng-nigeria/languages/README.md](../lines/ng-nigeria/languages/README.md). |
| Display face | `TBD — Visual Director.` One. |
| Text face | `TBD — Visual Director.` One. |
| Weights and styles in the system | `TBD.` Coverage is verified in **every** weight used, not only the one the specimen showed. |
| Mark positioning verified | `TBD.` Rendered in the actual NLE and caption pipeline, at the actual sizes, over the actual footage. A specimen PDF proves the glyph exists; it does not prove the text engine composes it. |
| Right-to-left support | `TBD`, where any language on a register uses an RTL script ([pack 09 §8](../../../packs/documentary-history/09_localization.md)). Whether any does is `TBD — Cultural Advisor`. |
| Licensing | `TBD — Rights & Clearances.` Broadcast, streaming, and every delivery territory, plus embedding in a delivered caption or graphics file. Font binaries live in [library/fonts/](../../../library/fonts/), versioned with the licence recorded. |
| Fallback policy | There is no fallback. A missing glyph is a blocked delivery, not a substituted family. A silent fallback is how a wrong mark reaches air looking deliberate. |
| Type scale | `TBD.` Floor of 1/20 frame height for body text ([delivery_specs](../../../standards/delivery_specs.md) § On-screen text). |
| Caption typography | `TBD`, within the caption spec — 2 lines, 42 characters, ≤ 20 cps. Where a platform renders its own captions, the studio controls only the burnt-in case. |

Owner: Visual Director, with Cultural Advisor on coverage and Rights & Clearances on
licensing. Rationale, constraint check: `TBD`.

## 3. Colour

| Item | Value |
|---|---|
| Studio brand palette | `TBD — Visual Director` |
| Relationship to a line's on-screen palette | `TBD.` These are different systems and must not be conflated: the studio palette is identity, the line palette is photography ([pack 04 §4](../../../packs/documentary-history/04_visual_language.md)). A brand colour that constrains a grade has escaped its layer. |
| Working and delivery space | Rec.709 / Gamma 2.4, per [delivery_specs](../../../standards/delivery_specs.md). Brand colour is specified inside legal range. |
| Contrast pairs | `TBD.` Every permitted foreground/background pair carries a **measured** ratio, ≥ 4.5:1 for text. Publish the table; do not leave it to a designer's eye at 2 a.m. |
| Colour-blind check | `TBD.` No information is carried by hue alone, anywhere in the system, including data graphics ([standards/data_graphics.md](../../../standards/data_graphics.md)). |
| Accent reservation | `TBD.` If an accent is reserved for a narrative function, state the function and hold it — an accent used for emphasis and for a category simultaneously teaches the viewer nothing. |

Owner: Visual Director. Rationale, constraint check: `TBD`.

## 4. Motion signature

| Item | Value |
|---|---|
| Logo animation | `TBD — Visual Director` |
| Duration | `TBD.` Short. It is seen every episode by an audience that has seen it before. |
| Easing and timing vocabulary | `TBD.` One vocabulary, reused across titles, lower thirds, and end cards, so motion reads as a system rather than as a set of presets. |
| Text entry and exit | `TBD.` Constraint: on-screen text is readable for at least 2× its reading time ([delivery_specs](../../../standards/delivery_specs.md)); animation time is not reading time. |
| Reduced-motion variant | `TBD.` Required. |
| Relationship to camera motion | Distinct from it. Graphics motion must not read as the shot moving — [pack 04 §2](../../../packs/documentary-history/04_visual_language.md) treats drifting motion on every shot as the signature tell of generated video, and a drifting graphic reinforces it. |
| Audio signature | `TBD — Audio Lead.` If one exists, it is a cue with a rights position like any other ([pack 05 §4](../../../packs/documentary-history/05_sound_and_score.md)). |

Owner: Visual Director, with Audio Lead. Rationale, constraint check: `TBD`.

## 5. Title cards

| Item | Value |
|---|---|
| Studio card | `TBD` |
| Series / line card | `TBD` |
| Episode title card | `TBD` |
| Position in the cut | `TBD — Story Producer`, consistent with the cold-open doctrine in [pack 03 §3](../../../packs/documentary-history/03_narrative_doctrine.md) |
| Safe area | Inside title safe (90%), and inside the 9:16 and 1:1 safe zones so a vertical cutdown is a crop ([core/03 §3](../../../core/03_distribution_and_formats.md)) |
| Layering | Every card on its own graphics layer, separate from picture, so the textless master is a render and a localised version is not a rebuild ([pack 09 §6](../../../packs/documentary-history/09_localization.md)) |
| Localised variants | `TBD.` Layout budget set by the **longest** variant, as with the reconstruction mark ([labelling_system.md](labelling_system.md) §10). |
| Interaction with the reconstruction mark | `TBD.` Declared, non-overlapping zones. If a title card sits over a labelled shot, the mark does not move and does not hide — the title moves. |

Owner: Visual Director. Rationale, constraint check: `TBD`.

## 6. Lower thirds

| Item | Value |
|---|---|
| Contributor identification | `TBD.` Fields: name, and the **standing** on which they speak. "An elder from the village" is not standing ([oral history protocol §3](../../../packs/documentary-history/methodology/oral_history_protocol.md)); a lower third that flattens standing into a generic label discards the thing that makes the testimony evidence. |
| Anonymised variant | `TBD.` Required — [pack 01 §7](../../../packs/documentary-history/01_editorial_standards.md) provides for contributors whose safety depends on anonymity, and the graphics system must have a treatment ready rather than improvised. |
| Source and credit strips | `TBD.` Archival credits, institution credits for `artefact` shots, translation credits ([pack 04 §5](../../../packs/documentary-history/04_visual_language.md)). |
| Quotation treatment | `TBD.` Original-language text alongside translation where practical, translator named ([pack 09 §7](../../../packs/documentary-history/09_localization.md)). The layout must accommodate two scripts at once. |
| Duration | `TBD`, floor of 2× reading time, measured on the **longest** localised variant |
| Zone | `TBD.` Declared and non-overlapping with the reconstruction mark and the caption region ([labelling_system.md](labelling_system.md) §3, §7). |
| Name forms | Rendered exactly as the entity record holds them, checked mechanically rather than by eye ([pack 09 §8](../../../packs/documentary-history/09_localization.md)). |

Owner: Visual Director. Rationale, constraint check: `TBD`.

## 7. End cards

| Item | Value |
|---|---|
| Credit roll structure | `TBD.` Must accommodate the named credits the studio commits to: scholars, translators, language consultants, knowledge holders, composer, performers ([core/01 §7](../../../core/01_provenance_and_ai_disclosure.md), [bible/00_charter.md](../bible/00_charter.md) §7). |
| AI-use statement | `TBD` in design; **mandatory** in content, naming every generative tool by category ([core/01 §3](../../../core/01_provenance_and_ai_disclosure.md)). Not in six-point type — where narration is synthetic, the credit states it plainly ([pack 05 §1](../../../packs/documentary-history/05_sound_and_score.md)). |
| Sources and provenance pointer | `TBD.` The published evidence layer — sources page, provenance summary, correction log — is a differentiator and the end card is where a viewer is told it exists ([core/03 §5](../../../core/03_distribution_and_formats.md)). |
| Correction address | `TBD — Showrunner`, and it is on screen. See [bible/corrections.md](../bible/corrections.md) §2. |
| Advisory credits | `TBD.` Advisors are credited by name, per their agreed terms and their right to be credited or not ([pack 07 §5](../../../packs/documentary-history/07_cultural_sensitivity.md)). |
| Roll speed | `TBD.` Legible at 360p, like everything else. A credit nobody can read is not a credit, and this studio's credits are a commitment rather than a formality. |
| Localised variants | `TBD` |

Owner: Visual Director, with Showrunner on the commitments the card makes.
Rationale, constraint check: `TBD`.

## 8. What this document does not contain

- The **look of the picture**. That is the line's, in
  [lines/ng-nigeria/style/visual_identity.md](../lines/ng-nigeria/style/visual_identity.md).
- The **reconstruction mark**, which is large enough and load-bearing enough to have
  its own spec: [labelling_system.md](labelling_system.md).
- **Thumbnails**: [thumbnail_system.md](thumbnail_system.md).
- **Delivery numbers**. Those are [standards/delivery_specs.md](../../../standards/delivery_specs.md),
  which is machine-checked. This document may tighten them and may never restate them
  — a restated number is a number that will disagree with the spec eventually, and the
  disagreement will be discovered at technical QC on a delivery day.
