# Quarantine — candidates that must not be ingested

Nothing in this folder may be ingested, referenced from a continuity record, or used
as a reference image. It is kept rather than deleted because *why* a candidate failed
is evidence, and because two of these failures changed the design.

## `PC-NG-EXP001-0001_c01` … `_c04` — not four candidates

They are **627×627**. No image surface generates at that size. It is exactly half of
1254×1254, the size of the composite grids produced earlier in the run: these four
files are the four cells of **one** 2×2 grid, cropped apart and renamed.

That matters more than the naming. Four cells of one generation share a single
sampling event, so they are not four independent draws — treating them as four
candidates would have overstated the evidence for whatever they agreed on by a factor
of four.

They also carry the **superseded** eyebrow scar. All four place it on the same wrong
side, which is consistent with the earlier finding and takes lateral-feature accuracy
to roughly 1 in 12.

## `PC-NG-EXP001-0002_BROKEN-CARD_c01` — the card was wrong, not the render

Generated from card v0.1.0, which asked for a cheek birthmark, forbade a cheek
birthmark in its negatives, and checked for a nose-bridge one. The surface complied
exactly with the prompt it was given. **This is not evidence about the vendor** and
must not be scored as such.

Fixed in card v0.2.0. `validate --prompts` now fails that class of card before a
render, rather than after.

## The defect all of this exposed

Every one of these files named a prompt-card id in its filename, and **nothing bound
it to a card *version***. Both A's and B's cards were rewritten (lateral → midline)
while sitting at `version: 0.1.0`, so a file made before the rewrite was
indistinguishable from one made after it. That is how a stale candidate came within
one step of being ingested as a canonical anchor.

Two changes followed:

1. The cards that changed materially are now at `0.2.0`.
2. Incoming filenames carry the card version:
   `EXP001_ANCHOR_<card-id>_v<card-version>_c<NN>.png`

The version in the filename is an operator's assertion, not proof. It is checkable by
a human against the card, which the previous scheme was not.
