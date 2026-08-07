---
title: Labelling system — the reconstruction mark
status: template
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, pipeline-engineer]
---

# Labelling system

Design specification for the in-frame mark carried by every `reconstruction` and
`interpretive` shot.

Required by [pack 04 §7](../../../packs/documentary-history/04_visual_language.md)
(layer 1 of three) and by
[core/01 §3](../../../core/01_provenance_and_ai_disclosure.md) (disclosure level 1 of
four). Technical floors are fixed in
[standards/delivery_specs.md](../../../standards/delivery_specs.md) § Reconstruction
mark and § On-screen text.

Maturity: **NOT STARTED**. The constraints below are fixed and binding. Every visual
decision is `TBD — Visual Director`, and none may be taken before typeface selection
resolves ([README.md](README.md) §3).

## 1. The principle this is designed against

> **The mark is not an apology.**
> [pack 04 §7](../../../packs/documentary-history/04_visual_language.md) —
> *"Viewers who know what they are looking at trust the material they are told is
> real."*

The instinct is to make the mark small, faint, and brief, on the theory that it
interrupts the image. That instinct gets the economics exactly backwards. This studio
generates most of its imagery; if the audience cannot tell which shots are generated,
the honest shots earn nothing from being honest, and the archival material — the
expensive material, the material that took a rights negotiation and a scan fee — is
discounted to the same level as everything else. **The mark is what makes `archival`
mean something.**

Design it as a piece of the identity system that the studio is willing to be
recognised by, not as a compliance sticker. A viewer who has watched three episodes
should read the mark without consciously reading it, and should notice its absence.

Two consequences follow, and both are design constraints rather than sentiments:

- **It is never made harder to see in order to protect a shot.** If a composition
  cannot hold the mark, the composition changes.
- **It is never removed for a trailer, a thumbnail, a vertical cutdown, or a social
  clip.** Those are the contexts where the material travels furthest from its
  explanation, so they are the contexts where the mark matters most. See
  [thumbnail_system.md](thumbnail_system.md) for the still-image case.

## 2. What it says

| | |
|---|---|
| Wording, `reconstruction` class | `TBD — Visual Director + Cultural Advisor.` Baseline in the pack is `RECONSTRUCTION`. |
| Wording, `interpretive` class | `TBD.` The two classes are distinct under [pack 04 §5](../../../packs/documentary-history/04_visual_language.md) — one depicts, one evokes — and the decision to be made is whether the viewer is served by one mark or two. Record the reasoning; do not default to one mark because two is more work. |
| Case, tracking, wordmark treatment | `TBD — Visual Director` |
| Maximum character count | `TBD`, but it is a hard number and it is derived, not chosen: the longest **localised** variant must fit inside title safe at minimum size without wrapping, at the narrowest aspect the studio delivers. Set the budget from the longest variant, not the English one. |

Constraints on the wording itself:

- It states what the shot **is**, not how it was made. The tool belongs in the
  provenance manifest and the credits, not the frame.
- It is not hedged. "Artist's impression", "may not be accurate", and "for
  illustrative purposes" describe a disclaimer; the mark is a classification.
- It is not an AI-branding opportunity. The viewer is being told what they are
  looking at.

## 3. Placement

| | |
|---|---|
| Corner and margin | `TBD — Visual Director`, subject to the constraints below |
| Safe area | **Inside title safe (90%)**, always — [delivery_specs](../../../standards/delivery_specs.md) § Legal levels and safe areas. Not action safe. Title safe is the constraint because the mark is type, and type outside title safe is clipped by overscan on displays that still apply it. |
| Vertical and square crops | The mark must fall inside the **9:16 and 1:1 safe zones** marked in the storyboard ([core/03 §3](../../../core/03_distribution_and_formats.md)). A cutdown is a crop, not a re-generation and not a re-graphic; a mark that crops out has removed a disclosure from the version most likely to be seen out of context. |
| Consistency | One position, held for the whole series. The mark does not move to accommodate a shot. A mark that relocates reads as decoration; a mark in a fixed place reads as a system. |
| Collision with other graphics | Lower thirds, map labels, quotation cards, and the mark occupy declared, non-overlapping zones. Zone map `TBD — Visual Director`, and it is produced **before** the first lower third is designed, not after the first collision. |

The mark lives in its **own graphics layer** in the NLE project, separate from all
other on-screen text, per [pack 09 §6](../../../packs/documentary-history/09_localization.md).
This is a pipeline requirement: a localised or textless master must be a render, not
a rebuild. A mark burnt into the same layer as the titles makes the textless master
impossible and is caught only at delivery.

## 4. Size

| | |
|---|---|
| Type size | `TBD — Visual Director`, expressed as a **fraction of frame height**, never in points or pixels. A pixel value is meaningless across a UHD master, a 1080p web render, and a vertical cutdown. |
| Floor | Not smaller than **1/20 of frame height** for the cap height of the wording — the on-screen body-text minimum in [delivery_specs](../../../standards/delivery_specs.md) § On-screen text. The mark is not exempt from that floor on the grounds of being unobtrusive; if it is below the floor it is not a disclosure. |
| Practical test | See §6. The floor is a necessary condition, not a sufficient one. |
| Ceiling | `TBD.` There is one, and it is set by the point at which the mark competes with the shot for the viewer's attention rather than classifying it. Record where it was set and why. |

## 5. Contrast

| | |
|---|---|
| Floor, against the shot behind it | **≥ 3:1, measured** — [delivery_specs](../../../standards/delivery_specs.md) § Reconstruction mark |
| Studio target | `TBD — Visual Director.` Recommend matching the general on-screen-text floor of **≥ 4.5:1** rather than the mark-specific 3:1. Brand may tighten a delivery floor and may never loosen one ([README.md](README.md) §4). |
| Measurement | Computed against the **actual luminance under the mark across the whole duration of the shot**, not against an average frame and not by eye. Generated footage drifts in luminance across a clip; a mark measured on frame one can fall below floor by frame ninety. |
| Backing treatment | `TBD — Visual Director.` A scrim, plate, shadow, or outline is permitted and is often the only way to hold the floor over a moving image. Whatever is chosen is part of the mark and travels with it — the mark is never rendered without its backing on the theory that this shot is dark enough. |
| Colour dependence | The mark must survive being read without colour. Its legibility comes from luminance contrast, so that it holds on a monochrome grade, in a colour-blind viewer's perception, and after platform re-encoding. |
| Verification | A named QC step at picture lock, per shot with a label, recorded — not a spot check. |

## 6. Legibility at 360p

The mark is checked at **360p**, and it is checked as a *render*, not as a preview
scaled in a viewer.

The 360p requirement is not conservatism about old hardware. It is the condition under
which most of this material will actually be seen: a phone, over a poor connection, at
the bitrate the platform decided to serve. A disclosure that only functions on a
grading monitor has been designed for the wrong audience — and specifically for an
audience outside the region the work depicts, which is the failure
[bible/00_charter.md](../bible/00_charter.md) §3 names as disqualifying regardless of
viewing figures.

The check, `TBD` in its exact procedure but fixed in shape:

- [ ] Render at 360p through the actual delivery encoder, at the actual bitrate
- [ ] Read the mark at arm's length on a phone-sized display
- [ ] Read it over the **worst-case** shot in the episode — highest motion, highest
      texture, lowest contrast under the mark — not a representative one
- [ ] Read the longest **localised** variant, not the shortest
- [ ] Confirm no compression artefact closes a counter or destroys a diacritic

Hairlines, tight tracking at small sizes, and fine serifs fail this test first. That
is a constraint on typeface selection, and it is one more reason the typeface is
chosen before anything else is drawn.

## 7. Behaviour with captions

Captions are mandatory on every deliverable
([pack 09 §5](../../../packs/documentary-history/09_localization.md)) and default to
bottom centre, repositioning to avoid on-screen text
([delivery_specs](../../../standards/delivery_specs.md) § Captions and subtitles).

The binding rule: **the mark is never obscured by a caption, and the caption is never
obscured by the mark.**

- The mark's zone is declared as a caption-exclusion region in the caption authoring
  spec, so repositioning is automatic rather than per-cue handwork.
- Placing the mark in a bottom corner therefore commits the studio to a caption
  reposition on every labelled shot, in every language, in every caption format —
  including the ones the studio does not control the rendering of. Placement `TBD`,
  but this is the trade-off, and it is decided knowingly.
- **Platform-rendered captions and burnt-in subtitles are different problems.** The
  studio controls the position of burnt-in subtitles; it does not control where a
  platform's caption renderer puts a cue, or how large a viewer has set it. The mark
  is placed so that it survives a caption the studio did not position.
- Where a shot carries both a caption and a subtitle for non-production-language
  speech, the mark yields nothing. The other elements move.

## 8. Persistence

| Rule | Value |
|---|---|
| Duration | **The full duration of the labelled shot** — [delivery_specs](../../../standards/delivery_specs.md) § Reconstruction mark. Not a few seconds at the head. |
| Fade in / out | `TBD — Visual Director.` If used, the fade is inside the shot's own boundaries and the mark reaches full opacity well before the shot's midpoint. |
| Across a cut | Re-evaluated per shot from the shot record's `provenance_class`. The mark is a property of the shot, not of the sequence. |
| Sequences of labelled shots | `TBD.` If the mark persists unbroken across consecutive labelled shots, define the rule precisely, because the ambiguous case — a labelled shot, a two-second `archival` insert, a labelled shot — is where a viewer is most likely to be misled and is exactly the case a general rule must resolve. |
| Mixed classes in one shot | Cannot arise. [pack 04 §5](../../../packs/documentary-history/04_visual_language.md) prohibits mixing `archival` and `reconstruction` inside a single continuous shot and requires a cut at the boundary. That prohibition exists so that "is this shot labelled?" is always answerable. |
| Unlabelled classes | `archival`, `contemporary`, `artefact`, `graphic`, and `text_on_screen` carry no mark. The absence of the mark is itself an assertion — that the studio is telling the viewer this material is real — and it is only worth anything if the mark's application is exhaustive. |
| Application | Driven mechanically from the shot record's `provenance_class` and checked at picture lock. Never applied by hand shot by shot, because hand application fails silently on exactly the shots someone was in a hurry with. |

## 9. First-use explainer card

Layer 2 of the pack's three-layer disclosure: a full card at the first
`reconstruction` or `interpretive` shot in **each** production.

| | |
|---|---|
| Trigger | First labelled shot of the production. Once per production, not once per season — a viewer's first episode may be any episode. |
| Duration | `TBD`, floor of **2× the reading time of its text** ([delivery_specs](../../../standards/delivery_specs.md) § On-screen text), measured at the reading speed the audience definition in [bible/00_charter.md](../bible/00_charter.md) §3 sets. That definition is `TBD — Showrunner`, so this duration cannot be finalised before it. |
| Copy | `TBD — Story Producer + Visual Director.` It must say what the mark means, what the studio does generate, and what it does not. It is written to be read once, at speed, by someone who has not thought about provenance before. |
| Tone | Plain. Not defensive, not promotional, not a lecture about the technology. |
| Placement in the cut | Before or on the first labelled shot — never after it. A card that explains a mark the viewer has already seen twice has failed at its only job. |
| Localisation | Same treatment as the mark: separate graphics layer, full variant set, no exceptions. |
| Relationship to the credits statement | The card is not a substitute for the credits statement or the published provenance summary (layers 2 and 3 of [core/01 §3](../../../core/01_provenance_and_ai_disclosure.md)). All four disclosure levels are required; none stands in for another. |

## 10. Localised variants

The mark reads in the language on screen. A disclosure the viewer cannot read is not a
disclosure.

| | |
|---|---|
| Variant set | `TBD — Cultural Advisor.` One variant per language in the line's register — [lines/ng-nigeria/languages/README.md](../lines/ng-nigeria/languages/README.md), currently a candidate list with every entry unconfirmed. |
| Wording per variant | `TBD — Cultural Advisor.` Translated by a named human translator and reviewed by a speaker, per [pack 09 §5](../../../packs/documentary-history/09_localization.md). The term is doing precise work — "reconstruction" is a technical claim about evidence, not a synonym for "picture" — and an approximate translation quietly changes what the studio is asserting. |
| Diacritic handling | Every mark rendered correctly and completely. Stripping is prohibited ([pack 09 §2](../../../packs/documentary-history/09_localization.md)). This is the constraint that feeds typeface selection, and the mark is the worst case for it: small type, over moving image, at 360p, after compression. |
| Layout budget | The zone is sized for the **longest** variant, not the English one, and re-checked whenever a language is added to a line's register. A variant that forces a smaller size or a wrap has broken §4 and §6. |
| Which variant on a given deliverable | Follows the on-screen language of that deliverable, not the studio's working language. Set in the line's language register. |
| Adding a line | A new line with a new language re-opens this section. The layout budget is re-derived, not assumed to still hold. |

## 11. What is checked, where

| Check | Gate | Owner |
|---|---|---|
| Mark applied to every shot whose `provenance_class` requires it | Picture lock | Visual Director |
| Contrast measured, per labelled shot, over full duration | Picture lock | Visual Director |
| 360p legibility on the worst-case shot, longest variant | Picture lock | Visual Director |
| Inside title safe, and inside the 9:16 and 1:1 safe zones | Picture lock | Visual Director |
| Caption-exclusion zone honoured in every caption file and language | Technical QC | Pipeline Engineer |
| Mark on its own graphics layer; textless master renders clean | Technical QC | Pipeline Engineer |
| Explainer card present, before the first labelled shot | Picture lock | Visual Director |
| Diacritics correct and complete in every variant | Picture lock | Cultural Advisor |

`studio_ops validate --canon` enforces the mechanically checkable subset — a generated
asset with `label_applied: false`, or an `archival` class on an asset with generation
provenance. It is **NOT BUILT**
([docs/status.md](../../../docs/status.md)). Until it is, every row above is a human
check on a written checklist, and the checklists live in
[ops/checklists/](../../../ops/checklists/) and are themselves **NOT BUILT**.

State that honestly in any schedule that assumes this is automated. It is not.
