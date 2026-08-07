---
title: Style — Nigeria line
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# Style

The look of this line: what the picture is, how it behaves, and what a prompt card
inherits.

Maturity: **NOT STARTED**. No palette, no lens set, no LUT, no style anchors, no
motifs. Registered as `visual_identity`, `unresolved`, in
[studio.yaml](../../../studio.yaml).

## 1. Why the look is defined here and not at studio level

> A single continental look would be a mistake; Nigeria's line defines its own.
> — [pack 04](../../../../../packs/documentary-history/04_visual_language.md)

The pack sets the *rules* — camera grammar, light behaviour, provenance classes,
skin-tone discipline, the QC checklist. It does not set the *look*, and it explicitly
pushes the look down to the line.

The reason is the failure mode the studio is most likely to commit and least likely to
notice. Generative models default hard to pan-African pastiche and will produce it
unless the prompt and the review actively prevent it
([pack 07 §6](../../../../../packs/documentary-history/07_cultural_sensitivity.md)).
A studio-level look would not merely permit that default — it would *codify* it,
turning a model artefact into house style, and every subsequent line would inherit an
aesthetic that asserts a continental sameness no evidence supports.

"African" is not a culture. Nor is a country. A line's look is specific to the
material the line covers, and a second line opens with its own, not with this one's.

## 2. Documents

| Document | Holds | State |
|---|---|---|
| [visual_identity.md](visual_identity.md) | Palette, lens set, grade and show LUT, light behaviour, texture, skin-tone rendering intent, style anchor set | **NOT STARTED** — every value `TBD — Visual Director` |
| [motifs.md](motifs.md) | The register of recurring visual and narrative motifs, so they are deliberate rather than accidental | empty |

## 3. How this folder is used downstream

The look is not documentation. It is an **input to generation**, and it is consumed
mechanically:

```
style/visual_identity.md        the line's style block, written so a prompt can inherit it
        │
        ▼
sequence style block            per sequence type, inheriting from the line
        │
        ▼
prompt card  PC-NG-<code>-NNNN  inherits the sequence block; an override must say why
        │
        ▼
generated asset                 recorded in the manifest with its card, seed, parameters
```

Two things follow, and both are the reason this folder blocks work rather than
describing it:

- **A prompt card cannot be written before the line's style block exists**, because it
  has nothing to inherit. Every prompt card in this line is blocked on
  [visual_identity.md](visual_identity.md).
- **The style block is written in language a prompt can use.** "Warm and evocative" is
  a mood board. A style block states palette, lens, stop, light source and direction,
  texture, and grade in terms that survive being pasted into a generator by someone
  who was not in the conversation.

**Style anchors** ([library/style_refs/](../../../../../library/style_refs/)) are the
second mechanism and are not a substitute for the first: a fixed, versioned set of
reference images per sequence type, referenced by `STA-NG-*` ID from every prompt card.
Specific files with checksums — not "a vibe".

## 4. The consistency problem this exists to solve

Generative tools have no continuity. Two prompts written by the same person a week
apart produce two different worlds, and left unmanaged an AI-assisted documentary looks
like a mood board: beautiful shot to shot, incoherent across a cut
([pack 04 §1](../../../../../packs/documentary-history/04_visual_language.md)).

The three mechanisms, in order of authority, are the look bible, the style anchors,
and prompt inheritance. All three live or point here. None of them exists yet.

## 5. Relationship to brand

Different layers, and conflating them breaks both:

| | [style/](visual_identity.md) — the line | [brand/](../../../brand/README.md) — the studio |
|---|---|---|
| Governs | Photography: what the picture looks like | Identity: type, logo, cards, marks, thumbnails |
| Varies | Per line, by design | Constant across lines |
| Owner | Visual Director, per line | Visual Director, studio-wide |
| Blocked on | The archive landscape survey and advisory coverage — see [visual_identity.md](visual_identity.md) §1 | Typeface selection, which is blocked on the language register ([brand/README.md](../../../brand/README.md) §3) |

A brand colour that constrains a grade has escaped its layer. A line palette that
appears in a title card has escaped in the other direction.

## 6. Blocked on

Everything in this folder is downstream of research that has not happened. The line
has no research lead, no advisory contact, and no archive landscape survey
([../README.md](../README.md) §2). A look designed before the material is known is a
look the material will have to be made to fit — which is the mechanism by which an
evidence-led production quietly becomes an illustrated aesthetic.
