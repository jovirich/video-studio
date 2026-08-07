---
doc: bible/08
title: Rights and licensing
status: active
version: 0.1.0
owners: [rights-and-clearances]
---

# 08 — Rights and licensing

## 1. The rule

**Nothing enters a locked cut without a clearance record.** Not a photograph, not a
quotation of any length, not a music cue, not a font in a title card, not a LUT, not
a generated asset from a tool whose terms have not been checked.

The clearance log is [../sources/permissions/clearance_log.md](../rights/permissions/clearance_log.md).
An item absent from it is uncleared by definition.

## 2. Categories

| Category | What must be recorded |
|---|---|
| **Archival still/moving image** | Rights holder, licence scope (media, territory, term, exclusivity), fee, credit wording required, restrictions on cropping/colouring/excerpting |
| **Museum and collection objects** | Institution, object accession number, photography rights (separate from object rights), credit line as specified by the institution |
| **Manuscripts and documents** | Custodian, reproduction permission, translation rights if translated |
| **Interviews and testimony** | Signed consent form, scope, withdrawal terms, anonymity requirements |
| **Music** | Composition rights and recording rights are separate — record both. Cue sheet entry. Territory and term. |
| **Traditional music and performance** | Add: who granted it, and on what basis they held the right to. Frequently the licensor is not the tradition's custodian. |
| **Fonts** | Licence tier covering broadcast/streaming use and the number of seats |
| **LUTs, plugins, stock SFX** | Licence permitting commercial redistribution in a finished film |
| **Generated assets** | The vendor's terms at the date of generation — see §5 |
| **Third-party code** | Licence compatibility for anything vendored into `automation/` |

## 3. Public domain and open licences

- Public domain status is **jurisdiction-specific**, and a documentary distributed
  globally faces the most restrictive relevant jurisdiction. Record the basis and
  the jurisdiction.
- A digitised public-domain work may carry a separate claim in the *scan* in some
  jurisdictions. Record the digitiser's position.
- Creative Commons: record the exact variant. `NC` variants are incompatible with
  monetised distribution. `SA` variants have viral implications for the finished
  work — escalate before use.
- Attribution requirements are honoured in the credits *and* in the episode's
  published credit list, not one or the other.

## 4. Fair dealing / fair use

Available in some jurisdictions for criticism, review, quotation, and news
reporting, with different scope in each. The studio's position:

- Fair dealing is a **considered position taken with advice**, never an assumption
  made because a licence was unaffordable.
- Any reliance is recorded in the clearance log with a written rationale addressing
  purpose, amount used, and market effect.
- Reliance is not used for the *primary* visual material of a sequence.

## 5. Generated asset rights

Recorded in [../sources/permissions/model_terms_register.md](../rights/permissions/model_terms_register.md),
per tool, with the date checked and the plan tier held. The register tracks:

- Does the licence permit **commercial** use of outputs?
- Does it permit use in a **broadcast/streaming** production specifically?
- Who **owns** the output, and can the studio claim any exclusivity?
- Is there **indemnity** against third-party IP claims, and at what plan tier?
- Does the vendor **train on inputs**, and can that be disabled?
- Are there **content restrictions** relevant to documentary (violence, real people,
  historical figures)?
- What **attribution** does the vendor require?

Re-checked before every delivery, because vendor terms change without notice and a
delivered master is not easily recalled.

## 6. Music cue sheet

Maintained per episode at `10_publish/cue_sheet.csv` from episode one, even if the
score is entirely original. Retrofitting a cue sheet for a distributor at short
notice is a well-known and entirely avoidable emergency.

## 7. Talent and crew

- Contributor releases for every on-screen participant.
- Voice licence for narration, explicitly covering synthetic reproduction if used.
- Composer agreement stating whether the studio holds the master and the publishing.
- Crew agreements assigning work product to the studio, with moral-rights
  acknowledgement per jurisdiction.

## 8. Chain of title

Maintained per episode: a single document evidencing that the studio holds
everything required to distribute. Assembled at delivery by
`studio_ops report chain-of-title --episode <code>` from the clearance log, and *(NOT BUILT)*
reviewed by Rights & Clearances. Distributors will ask for it; assembling it from
memory at that point is how deliveries slip.

## 9. Territory and takedown

- Record any territorial restriction on any asset, and check it against the intended
  distribution footprint before lock.
- Maintain a takedown procedure: how a rights holder or community reaches the
  studio, the response SLA, and who decides. Documented in
  [../docs/runbook/takedown_procedure.md](../docs/runbook/takedown_procedure.md).

## 10. The rights gate

Runs at picture lock and again at delivery. Checklist:
[../ops/checklists/rights_gate.md](../ops/checklists/rights_gate.md).
An episode cannot be delivered with any asset in `pending` clearance state. There is
no provisional delivery.
