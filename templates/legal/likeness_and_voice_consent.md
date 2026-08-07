---
title: Likeness and voice consent — starting point, requires legal review
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [rights-and-clearances, audio-lead]
---

# Likeness and voice consent

> **STARTING POINT ONLY — NOT LEGAL ADVICE.** Must be reviewed by a qualified
> lawyer admitted in the relevant jurisdiction before use. Personality,
> publicity, image, and voice rights vary enormously between jurisdictions, and
> in several the enforceable position on synthetic reproduction is unsettled.
> See [README.md](README.md).

This instrument covers the use of a **living person's** likeness or voice,
including any **synthetic reproduction** of either.

> **It cannot be used for a historical figure.** Consent is impossible, so the
> question does not arise: synthesising a real or historical person's likeness or
> voice without documented consent or estate clearance is prohibited outright by
> [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2.
> There is no override flag and no review that permits it.

---

## Parties

| | |
|---|---|
| Studio | TBD — legal entity name and registered address |
| Person | TBD — name |
| Production(s) | TBD |
| Date | TBD |

## 1. What is being licensed

- [ ] **Likeness** — the person's appearance, in recorded footage or stills
- [ ] **Voice** — the person's voice, as recorded
- [ ] **Synthetic reproduction of voice** — a model trained on or conditioned by the
      person's recorded voice, producing speech the person did not perform
- [ ] **Synthetic reproduction of likeness** — a model producing images or motion of
      the person that were not captured
- [ ] TBD

Each box is a separate grant. Ticking the first two does **not** imply the second
two: performing for a camera and licensing a synthetic double of yourself are
different acts with different consequences, and a document that conflates them has
obtained agreement to something that was never explained.

## 2. Scope of synthetic reproduction

Complete only if a synthetic box above is ticked. Every field is a limit, and a
field left as "any" is a limit that does not exist.

| | |
|---|---|
| **Permitted uses** | TBD — specifically: narration for this production, and what else |
| **Prohibited uses** | TBD — at minimum: endorsement, political speech, anything the person would object to, any content presenting them as holding a view they do not hold |
| **Languages** | TBD — enumerate. A voice model trained on one language can be made to speak others, in an accent and register the person never agreed to and cannot check. |
| **Territories** | TBD |
| **Term** | TBD — a fixed period with an end date. Perpetuity on a synthetic voice is not a licence, it is a transfer. |
| **Sub-licensing** | TBD — normally none |
| **Approval** | TBD — whether the person approves each output, each production, or neither |
| **Disclosure** | Every use is disclosed as synthetic, in the credits and in the provenance record. Non-negotiable. |

## 3. No-training clause

The studio commits that recordings, images, and any derived model of the person
**will not**:

1. Be used to train, fine-tune, adapt, or evaluate any model beyond the specific
   model built for the permitted uses in §2.
2. Be provided to any third party for training, by any route, including as part of a
   dataset, a fine-tuning job, or a vendor's default retention.
3. Be retained by any vendor beyond the period necessary to produce the permitted
   output. TBD — name the vendors and state their retention terms, verified in the
   model terms register, on TBD — date.
4. Be used to produce output after the term in §2 ends. On expiry, TBD — the model
   and its training artefacts are deleted, and deletion is confirmed in writing.

TBD — a lawyer must assess whether a no-training term binds a downstream vendor the
studio does not contract with, and what the studio's remedy is if it does not. This
is the clause most likely to be unenforceable exactly where it matters most.

## 4. Custody of the model

| | |
|---|---|
| Who holds the trained model | TBD |
| Where it is stored | TBD |
| Who may run it | TBD — named individuals, not a role |
| Access log kept | TBD — yes / no; yes is strongly preferable |
| Deletion on expiry or withdrawal | TBD — within what period, confirmed in writing |

A voice model is a capability that outlives the production it was made for. Deciding
in advance who holds it and when it is destroyed is the difference between a licence
and an unbounded one.

## 5. Right of review

| | |
|---|---|
| Person reviews | TBD — every synthetic output / each production / a sample |
| Provided by | TBD — a stated period before publication |
| Response period | TBD |
| What review can change | TBD — rejection of any specific output, always |

For synthetic voice, review of **every** output before publication is the default
position and should only be relaxed for a good reason that is written down here.
The person cannot otherwise know what they are recorded as having said.

## 6. Right of withdrawal

The person may withdraw at any time, in writing, to TBD — contact.

| When | What the studio will do | What it cannot do |
|---|---|---|
| **At any time** | Stop generating new output immediately; delete the model and its training artefacts within TBD — period; confirm deletion in writing | — |
| **Before publication** | Remove all synthetic output from the production | — |
| **After publication** | Remove at the next version; annotate the published version; cease all further use | Recall copies already downloaded, mirrored, or re-uploaded |

TBD — whether any fee is repayable on withdrawal, and in what circumstances. Settle
this in advance; settling it during a withdrawal makes the withdrawal a negotiation,
which is the opposite of what the right is for.

## 7. Credit

| | |
|---|---|
| Credit form | TBD — named / anonymised / withheld, at the person's choice |
| Exact wording | TBD — as the person writes it, with correct diacritics |
| Synthetic use disclosed in credits | Yes — required, not optional |

## 8. Payment

| | |
|---|---|
| Fee | TBD |
| Basis | TBD — session, per production, per term, royalty |
| Further use | TBD — what triggers a further payment |
| Payment terms | TBD |

TBD — a lawyer should consider whether the fee structure is appropriate to a
synthetic licence, where the studio's marginal cost of further use is near zero and
the person's leverage after signature is near zero too.

## 9. Signatures

| | Person | Studio |
|---|---|---|
| Name | TBD | TBD |
| Signature | | |
| Date | TBD | TBD |

| | |
|---|---|
| Independent advice taken by the person | TBD — recommended, and recorded either way |
| Translation of this document provided | TBD |
| Clearance record | TBD — `CLR-XX-0000` |
