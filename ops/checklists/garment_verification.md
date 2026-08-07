---
title: Garment verification gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# Garment verification — checklist

| | |
|---|---|
| **Gate key** | `garment_verification` |
| **Owner** | `visual-director` |
| **Stage** | `08_review` |
| **Blocks** | `09_delivery` |
| **Packs** | fashion-film |
| **Completed copy** | `08_review/checklists/garment_verification.md` in the production folder |

**The physical garment is ground truth.** If a generated image shows a drape, a
texture, or a finish the actual garment does not have, that is a false product claim
wearing an editorial coat — and the person who discovers it is the customer, holding
the garment.

This gate is per garment, against a reference capture. It is not a general impression
of whether the film looks like the collection.

## What this signature certifies

> Every garment appearing in a deliverable exists physically and has a reference
> capture on file. Generated imagery has been compared against that reference for
> colour, texture, drape, closure, and finish. Nothing shown is a property the garment
> does not have.

## Checks

### Existence and reference

- [ ] Every garment appearing in any deliverable **exists physically**. Not a sample in production, not a pattern, not a render from the design file
- [ ] Every garment has a reference capture on file — photographed or filmed as it physically exists, at least once
- [ ] The reference capture is identified: which sample, which size, which colourway, captured on what date under what lighting
- [ ] The reference capture is in the asset store with a provenance record, like any other asset
- [ ] Where a garment appears in more than one colourway, each colourway has its own reference

### Per garment, per shot

Repeat for every garment in every shot it appears in.

- [ ] **Colour** matches the reference under the show LUT — checked against the capture, not against the lookbook, which is already a representation, and not against memory
- [ ] **Texture** matches: weave, pile, sheen, grain, and how the surface responds to light
- [ ] **Drape** matches: how the fabric falls, gathers, and moves. Generative models default to a generic fluid drape that most real fabrics do not have
- [ ] **Closure** matches: buttons, zips, hooks, ties — count, placement, and direction
- [ ] **Finish** matches: hems, seams, topstitching, hardware, linings where visible
- [ ] Proportions and fit match the garment on a body, not the garment as a silhouette
- [ ] Prints, motifs, and logos are correct — placement, scale, orientation, and repeat. A repeated print is where generative artefacts hide most reliably
- [ ] Nothing is shown that the garment does not have: no invented pocket, no added detail, no property the fabric does not possess

### The whole film

- [ ] The same garment reads as the same garment across every shot it appears in
- [ ] Styling — accessories, layering, hair, makeup — is consistent within a look
- [ ] No garment appears that is not on the list agreed at brief approval, or the addition is recorded
- [ ] No composite shows a garment in a state it cannot physically be in

### Attribution

- [ ] Any cultural textile, motif, or garment form drawn on is identified, attributed, and — where required — agreed with its custodians. This routes to [representation_review.md](representation_review.md); confirm it has been raised there rather than assuming it was

## Do not sign if

- **A garment does not physically exist.** No amount of design-file fidelity makes a
  generated garment a real one, and the film is a claim that it is.
- **The comparison was made against the lookbook.** The lookbook is another
  representation, produced under its own lighting and its own retouching. Compare
  against the capture.
- **A colour was matched by eye on an uncalibrated display**, or without the show LUT
  applied.
- **A drape or texture is "close enough".** Close enough is the distance between what
  the customer expected and what arrived.
- **A print repeat was not examined at full resolution.** Generative artefacts in a
  repeat are invisible at review scale and obvious in the delivered file.
- **A garment was added to the film after brief approval and its reference capture
  does not exist yet.**
- **You intend to also sign `picture_audio_lock` on this production.** Both are owned
  by `visual-director` — see [../roles.md](../roles.md) §5.1.

## Signature

| Field | Value |
|---|---|
| Role | `visual-director` |
| Person | |
| Date | |
| Garments verified | of |
| Reference captures on file | |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
