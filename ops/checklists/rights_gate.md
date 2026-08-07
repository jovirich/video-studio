---
title: Rights gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [rights-and-clearances]
---

# Rights — checklist

| | |
|---|---|
| **Gate key** | `rights` |
| **Owner** | `rights-and-clearances` |
| **Stage** | `08_review`, then again at `09_delivery` |
| **Blocks** | `09_delivery` |
| **Packs** | Declared as a standalone gate by documentary-history. The other three packs fold the same certification into `technical_qc`; the checks below still apply to them |
| **Completed copy** | `08_review/checklists/rights_gate.md`, re-signed at `09_delivery` |

The governing rule is one sentence:
[../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §1 —
**nothing enters a locked cut without a clearance record.** Not a photograph, not a
quotation of any length, not a music cue, not a font in a title card, not a LUT, not
a generated asset from a tool whose terms have not been checked. An item absent from
the clearance log is uncleared by definition.

## What this signature certifies

> Every asset in the manifest has a rights status other than `pending`; model terms
> were re-checked at delivery; the cue sheet is complete; and chain of title
> assembles.

## Why it runs twice

Once at `08_review`, when the cut stops changing and the asset list is finally
knowable. Once at `09_delivery`, because vendor terms change without notice and a
delivered master is not easily recalled. The second pass is not a formality — it is
the pass that catches
[../risk_register.md](../risk_register.md) `RSK-PLAT-0002`.

## Checks

### Every asset

- [ ] Every asset in the manifest appears in the clearance log
- [ ] No asset has a rights status of `pending`
- [ ] Territorial restrictions on every asset checked against the intended distribution footprint
- [ ] Any asset whose licence expires before the intended term is either re-licensed or replaced

### By category — [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §2

- [ ] **Archival still and moving image**: rights holder, licence scope (media, territory, term, exclusivity), fee, required credit wording, and restrictions on cropping, colouring, and excerpting — all recorded, and the restrictions actually honoured in the cut
- [ ] **Museum and collection objects**: institution, accession number, photography rights recorded **separately** from object rights, credit line exactly as the institution specifies
- [ ] **Manuscripts and documents**: custodian, reproduction permission, translation rights where translated
- [ ] **Interviews and testimony**: signed consent form, scope, withdrawal terms, anonymity requirements — and the anonymity requirements reflected in the credits and the caption file
- [ ] **Music**: composition rights **and** recording rights recorded separately, per cue, with territory and term
- [ ] **Traditional music and performance**: who granted the licence, and on what basis they held the right to grant it. The licensor is frequently not the tradition's custodian
- [ ] **Fonts**: licence tier covers broadcast/streaming use and the number of seats actually used
- [ ] **LUTs, plugins, stock SFX**: licence permits commercial redistribution inside a finished film
- [ ] **Generated assets**: the vendor's terms **at the date of generation**, per tool
- [ ] **Third-party code** vendored into the pipeline: licence compatibility checked

### Generated-asset terms

For every vendor used on this production, the model terms register answers, with a
date checked and the plan tier held:

- [ ] Commercial use of outputs permitted
- [ ] Broadcast/streaming use permitted specifically
- [ ] Output ownership established, and any exclusivity the studio can claim
- [ ] Indemnity against third-party IP claims, and at which plan tier — confirm the studio holds that tier
- [ ] Training on inputs: whether it happens and whether it was disabled
- [ ] Content restrictions relevant to this production
- [ ] Attribution the vendor requires, and where it appears in the credits
- [ ] `terms_checked` date is **not earlier than the delivery date** for the delivery pass

### Public domain, open licences, fair dealing

- [ ] Public domain status recorded with its **jurisdiction** and basis. A globally distributed work faces the most restrictive relevant jurisdiction
- [ ] For digitised public-domain works, the digitiser's position on the scan recorded
- [ ] Creative Commons variants recorded exactly. `NC` variants are incompatible with monetised distribution; `SA` variants have viral implications for the finished work
- [ ] Attribution requirements honoured in the credits **and** in the published credit list
- [ ] Any fair-dealing reliance recorded with a written rationale addressing purpose, amount used, and market effect — and is not carrying the primary visual material of a sequence

### Talent, crew, and title

- [ ] Contributor release for every on-screen participant
- [ ] Voice licence for narration, explicitly covering synthetic reproduction where used
- [ ] Composer agreement states whether the studio holds master and publishing
- [ ] Crew agreements assign work product, with moral-rights acknowledgement per jurisdiction
- [ ] Consent records state AI processing scope — consent obtained without it does not cover this platform's use
- [ ] Cue sheet complete, including entirely original score
- [ ] Chain of title assembles end to end with no gap
- [ ] Takedown procedure and response path current

## Do not sign if

- **Anything is `pending`.** Not "expected Friday", not "verbally agreed". There is
  no provisional delivery and no partial rights sign-off.
- **A licence exists but its scope was not read against the actual use.** A licence
  for one territory and a distribution plan for three is an uncleared asset with
  paperwork attached.
- **A traditional-music licence has no answer to "on what basis did the licensor hold
  this right?"** This is the single most common clearance that looks complete and is
  not.
- **A model terms entry predates the delivery date** at the delivery pass. Re-check
  it; do not carry the earlier check forward.
- **You are being asked to weigh the risk.** An uncleared asset is a block, not a risk
  to be balanced against the schedule. If that pressure is being applied, record it in
  the note field and mark the gate `blocked`.
- **You signed another gate on this production.**

## Signature

| Field | Value |
|---|---|
| Role | `rights-and-clearances` |
| Pass | `08_review` / `09_delivery` |
| Person | |
| Date | |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
