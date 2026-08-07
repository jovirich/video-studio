# Canon pack — `<code>`

> Template. Copy with `studio_ops new-pack --code <code> --title "<title>"`.
> Do not fill this file in place.

## What this pack is for

`TBD` — one paragraph. The kind of video work this governs.

## The problem this pack is shaped around

`TBD` — every good pack exists because a genre has a characteristic way of going
wrong. Name it. If you cannot name a failure mode this pack prevents, you probably
do not need a new pack; you need a studio bible addendum under an existing one.

## Documents

`TBD` — list only the canon documents this genre actually needs. Three is a
legitimate number. Do not copy another pack's document list out of symmetry.

Numbers 00, 01, 02, 03, and 04 are reserved by [core](../../core) and are never
used by a pack.

| # | Document | Governs |
|---|---|---|
| 05 | | |

## Gates

`TBD` — declared in [gates.yaml](gates.yaml).

Start from the question **"what would we regret not having checked?"**, not from
another pack's list. Then check the result against these:

- Does every gate have exactly one accountable role?
- Does every gate have a written checklist?
- Does every gate block something? A non-blocking gate is feedback.
- Is technical QC present? Core requires it in every pack.
- Can the production actually be staffed with distinct signatories?

## What this pack deliberately does not cover

`TBD` — as important as what it does. A reader needs to know when to reach for a
different pack rather than request an exemption from this one.

## Constraints inherited from core

This pack may not loosen any of these. Listed so an author does not waste time
drafting around them:

- No fabricated evidence, and nothing generated may be presented as found material
- No unconsented likeness or voice synthesis
- No autonomous publication — a human signs every gate
- Every asset carries a provenance record
- Nothing ships with a rights status of `pending`
- Captions on every deliverable

Full text: [core/01](../../core/01_provenance_and_ai_disclosure.md) §2.

## Checklist before this pack goes active

- [ ] `pack.yaml` complete
- [ ] `gates.yaml` complete; every gate has a checklist file that exists
- [ ] Every canon document written, or explicitly declared out of scope
- [ ] `studio_ops validate --pack <code>` passes
- [ ] Pack Owner named
- [ ] Reviewed against core for any accidental loosening
