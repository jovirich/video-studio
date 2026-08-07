---
title: Chain of title — per-production template
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [rights-and-clearances]
---

# Chain of title

The single document evidencing that the studio holds everything required to distribute
one production. Assembled at delivery; requested by distributors.

Canon: [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §8.

**Maturity: DESIGNED.** This is a template. No chain of title has been assembled,
because no production exists. `studio_ops report chain-of-title --episode <code>` —
the command that would build one from [clearance_log.md](clearance_log.md) — is
**NOT BUILT**.

## What this is for

A distributor, broadcaster, platform, festival, or insurer will ask the studio to
demonstrate, in one document, that it can grant what it is purporting to grant. That
request arrives late, with a deadline, and it is not negotiable. Core/02 §8 puts it
plainly: assembling it from memory at that point is how deliveries slip.

Two properties make this document work:

1. **It is derived, not written.** Every line is a projection of a row in the clearance
   log, the manifest, or a signed agreement on disk. Nothing is asserted here that is
   not recorded there. A chain of title with facts of its own is a second source of
   truth, and the second one is always the one that is wrong.
2. **It is assembled at delivery, not before.** Rights move. A chain assembled at
   picture lock is a draft; the one that ships is built from the state of the register
   on the delivery date and is dated accordingly.

## How to use this template

Copy it into the production's delivery folder as
`09_delivery/chain_of_title.md`, fill every field, and have Rights & Clearances review
and sign it. Do not fill this file in place — see
[../../standards/naming_conventions.md](../../standards/naming_conventions.md)
§ Prohibited patterns.

A field that cannot be filled is written `TBD — <what is needed, who provides it, by
when>`. A `TBD` remaining at delivery is a blocked delivery, not a footnote.

---

## TEMPLATE — copy below this line

```markdown
---
title: Chain of title — <PRODUCTION CODE>
status: draft
version: 0.1.0
updated: <YYYY-MM-DD>
owners: [rights-and-clearances]
---

# Chain of title — <PRODUCTION TITLE> (<PRODUCTION CODE>)

Assembled: <YYYY-MM-DD>
Assembled by: <role> / <person>
Reviewed and signed: <role> / <person> / <YYYY-MM-DD>
State of the clearance log as at: <YYYY-MM-DD>, commit <git sha>

## 1. The production

| Field | Value |
|---|---|
| Studio | `<studio code>` |
| Line | `<line code>` |
| Production code | `<code>` |
| Title as delivered | `<title>` |
| Duration | `<TC>` |
| Delivery date | `<YYYY-MM-DD>` |
| Canon pack and version | `<pack>` `<version>` |

## 2. Underlying work

What the production is based on, and the studio's right to base it on that.

| Item | Nature | Holder | Basis on which the studio may use it | Clearance ID |
|---|---|---|---|---|
| `<TBD>` | `<original / adaptation / commissioned>` | `<TBD>` | `<agreement, assignment, or public domain with jurisdiction stated>` | `<CLR-*>` |

State explicitly if the work is wholly original to the studio. "Nothing underlies this"
is an answer, and it needs to be written down rather than inferred from an empty table.

## 3. Assignments of work product

Every contributor whose output is in the delivered master, and the instrument by which
the studio holds it.

| Contributor role | Agreement type | Signed | Assigns | Moral rights addressed | Reference |
|---|---|---|---|---|---|
| `<crew role>` | `<employment / contractor / commission>` | `<YYYY-MM-DD>` | `<what>` | `<yes / no / n-a — per the agreement>` | `<path>` |

Moral rights treatment varies by jurisdiction. Record what the agreement says; do not
state what the law requires.

## 4. On-screen and voice contributors

| Contributor | Release on file | Scope consented to | Withdrawal terms | Anonymity constraints | Clearance ID |
|---|---|---|---|---|---|
| `<TBD>` | `<YYYY-MM-DD>` | `<TBD>` | `<TBD>` | `<TBD>` | `<CLR-*>` |

Where a synthetic voice is used, the licence must explicitly cover synthetic
reproduction — core/02 §7. Record which clause does so.

## 5. Third-party material in the delivered master

Generated from the clearance log, filtered to assets present in the frozen manifest.
One row per clearance record, not per use.

| Clearance ID | Item | Category | Holder | Media | Territory | Term (expiry) | Credit wording | Restrictions | Status |
|---|---|---|---|---|---|---|---|---|---|
| `<CLR-*>` | `<TBD>` | `<TBD>` | `<TBD>` | `<TBD>` | `<TBD>` | `<YYYY-MM-DD>` | `<verbatim>` | `<TBD>` | `cleared` |

**Every row reads `cleared`, `not-required`, or the delivery does not go.** Core/02 §10.

## 6. Music

| Cue | Composition rights | Recording rights | Territory | Term | Cue sheet row | Clearance ID |
|---|---|---|---|---|---|---|
| `<CUE-*>` | `<holder>` | `<holder>` | `<TBD>` | `<TBD>` | `<row ref>` | `<CLR-*>` |

Composition and recording are separate rights and are listed separately here even when
one party holds both. Cue sheet: `10_publish/cue_sheet.csv`.

## 7. Generated material

| Vendor | Modality | Plan tier at generation | Terms checked (generation) | Terms checked (delivery) | Register row |
|---|---|---|---|---|---|
| `<vendor>` | `<modality>` | `<tier>` | `<YYYY-MM-DD>` | `<YYYY-MM-DD>` | `rights/permissions/model_terms_register.md` |

Both dates are required. The first evidences what the terms permitted when the asset
was made; the second evidences that they still permit it now. See that register's
"Why it is re-checked before every delivery".

## 8. Territory and distribution footprint

| Field | Value |
|---|---|
| Intended distribution footprint | `<TBD>` |
| Narrowest territory across all rows in §5 and §6 | `<TBD>` |
| Conflicts | `<none / list>` |

The second row is the binding constraint on the first. A single asset licensed for one
territory caps the whole master unless it is replaced.

## 9. Positions taken rather than licences held

Anything in §5 with status `not-required`, and the written rationale for it. Public
domain claims name the jurisdiction and the basis; fair-dealing reliance addresses
purpose, amount used, and market effect, and states who advised. Core/02 §3 and §4.

| Clearance ID | Position | Basis | Jurisdiction(s) considered | Advised by | Date |
|---|---|---|---|---|---|
| `<CLR-*>` | `<public domain / fair dealing / studio-owned>` | `<TBD>` | `<TBD>` | `<TBD>` | `<YYYY-MM-DD>` |

## 10. Encumbrances, exclusions, and known gaps

Anything a distributor would rather hear now than discover later: expiring terms,
narrow territories, restrictions that constrain re-versioning, assets that would need
replacing for a broadcast cut.

| Item | Nature of the encumbrance | Expires | Consequence if ignored | Owner |
|---|---|---|---|---|
| `<TBD>` | `<TBD>` | `<YYYY-MM-DD>` | `<TBD>` | `<role>` |

An empty §10 is a claim, and it is the claim most likely to be wrong. Write "none
identified as at <date>, by <person>" rather than leaving it blank.

## 11. Attestation

> As at `<YYYY-MM-DD>`, every asset in the frozen manifest for `<code>` has a
> clearance record with status `cleared` or `not-required`; no record is `pending` or
> `refused`; every required credit is carried verbatim in the credits and in the
> published credit list; and the encumbrances in §10 are the ones known to the studio.

| Role | Person | Date |
|---|---|---|
| Rights & Clearances | `<person>` | `<YYYY-MM-DD>` |
| Showrunner | `<person>` | `<YYYY-MM-DD>` |

No person signs both lines — `core/04_review_gate_framework.md` §5.
```

---

## What breaks without this document

- **Delivery slips.** The distributor's request has a deadline; reconstructing consent
  scopes and credit strings from email under that deadline is the failure core/02 §8
  names.
- **A credit is paraphrased.** The verbatim strings live in the clearance log and are
  carried here unchanged. Retyping them at credit-roll time is where they drift.
- **The narrowest territory is never computed.** Nobody looks across all licences at
  once until this table forces it, and by then the distribution decision is made.
- **`not-required` goes unexamined.** §9 is the section that makes a position visible
  as a position. Without it, a fair-dealing reliance and a signed licence look the same
  in a list.
