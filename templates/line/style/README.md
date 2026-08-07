---
title: style — visual identity and style anchors
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# style

The line's look, defined once so that productions inherit it instead of each
inventing one.

```
style/
├── visual_identity.md   the look, and the reasoning behind it
├── lens_set.md          the defined lens language
├── palette.md           colour, and how it carries meaning
└── anchors/             STA-XX-0000_<slug>.md — fixed reference images
```

Template: [../../records/_TEMPLATE_style_anchor.md](../../records/_TEMPLATE_style_anchor.md).
Referenced from [../line.yaml](../line.yaml) under `visual_identity`, and inherited by
every prompt card through its `inheritance` block
([../../production/04_prompts/_TEMPLATE_card.prompt.yaml](../../production/04_prompts/_TEMPLATE_card.prompt.yaml)).

## Why style anchors exist

A generative model has no memory between runs. Asked twice for the same person, it
produces two people; asked across a season, it produces a different person per
episode, each internally plausible.

A **style anchor** is a fixed reference image, recorded with an ID, that every card
depicting that entity or look feeds back in. It is the mechanism by which a face, a
building, a textile, or a grade stays the same across shots, sequences, productions,
and seasons.

Without anchors, continuity is maintained by whoever is generating that week
remembering what last month looked like. That works for about six weeks.

## Why the lens set is defined at the line

Prompt cards draw their camera language from the line's defined lens set, not from
each tool's defaults. A production whose lens language is whatever each vendor
prefers has no lens language — and the tell is legible to an audience that could not
name what they are seeing.

The same argument applies to the palette and the LUT: they are inherited, and any
deviation is an **override with a stated reason** on the card. An override without a
reason fails review, because unexplained overrides accumulate — each defensible on
its own — until the look has drifted with no single decision having caused it.

## Camera movement

Every non-static movement carries a stated motivation on the shot record.
**Unmotivated drift is the signature tell of generated video.** Each individual
instance looks fine; thirty in a row read as a screensaver. Requiring the motivation
is what forces the question to be asked at all.

## The look is answerable to evidence too

Texture, materials, light, and palette are not purely aesthetic choices in
reconstruction work — they assert what a place and a period looked like. A grade that
makes everything sepia asserts a past that was brown, and it is a claim nobody wrote
down. Where the line's look departs from what the evidence supports, the departure is
recorded here as a stated stylisation rather than left to read as documentary.
