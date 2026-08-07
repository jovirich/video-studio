---
title: Clearance log
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [rights-and-clearances]
---

# Clearance log

The authoritative register of every third-party right the platform relies on.

> ## An item absent from this log is uncleared. By definition.
>
> There is no informal cleared state. There is no "we checked and it was fine". There
> is no verbal clearance, no clearance that lives in an email thread, and no clearance
> that lives in someone's memory. If it is not in this table with a `CLR-*` ID and a
> named human who checked it on a named date, the item is **uncleared**, and the rights
> gate ([../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md))
> treats it as such.
>
> This is deliberately absolute. A soft version of this rule produces a register that
> is 80% complete, which is worse than an empty one — an empty register makes nobody
> feel safe, and a partial register does.

Canon: [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md).
Nothing enters a locked cut without a record here: not a photograph, not a quotation
of any length, not a music cue, not a font in a title card, not a LUT, not a generated
asset from a tool whose terms have not been checked.

**Maturity: DESIGNED.** The register is empty and has never been used. No clearance
has been recorded, and `studio_ops report chain-of-title` — the command that reads
this table — is **NOT BUILT**.

## Identifiers

`CLR-<SCOPE>-<SERIAL>`, per [../../standards/id_system.md](../../standards/id_system.md).

| Part | Value |
|---|---|
| `CLR` | Fixed type code for a clearance record |
| `SCOPE` | The production line code in caps without the country prefix, or `STUDIO` for anything cross-line — which includes everything in [../../library/](../../library/) |
| `SERIAL` | Zero-padded 4 digits, allocated monotonically per (type, scope) by the toolkit |

Examples of the *shape*: `CLR-XX-0001` (line-scoped), `CLR-STUDIO-0001`
(cross-line). IDs are allocated by `studio_ops new-record --type clearance`, never by
hand — a hand-typed serial that collides silently corrupts the audit trail, and the
allocator refuses to run when it sees the gap-and-collision pattern that indicates
one. That command is **NOT BUILT**; until it exists, IDs are allocated by the Rights
& Clearances owner and recorded here in the same commit that allocates them.

An ID is permanent. A refused clearance keeps its ID; a superseded licence keeps its
ID and gains a successor row. Nothing is ever deleted from this table, because
"we used to have a licence for this" is exactly the fact a future dispute turns on.

## The register

**This table is empty.** The single row below is a template, marked as such, and
carries no real rights holder, no real fee, and no real terms.

| ID | Item | Category | Rights holder | Media | Territory | Term | Exclusivity | Fee | Credit wording (verbatim) | Restrictions | Status | Date checked | Checked by |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `CLR-XX-0000` | ⟨TEMPLATE ROW — DELETE ON FIRST REAL ENTRY⟩ `<what the item is, specifically enough to identify one file>` | `<one of the categories below>` | `TBD — who to ask` | `TBD — e.g. all media / online only` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD — copy the licensor's wording exactly, do not paraphrase` | `TBD — cropping / colouring / excerpting / duration cap` | `pending` | `TBD` | `TBD — role and person` |

### Column meanings

| Column | What goes in it, and what breaks without it |
|---|---|
| **ID** | `CLR-*`. Referenced from `manifest.yaml` as `acquisition.clearance_ref`. Without it the asset manifest cannot point at the clearance and the provenance chain has a hole. |
| **Item** | Identifies **one** thing. "Archive stills" is not an item; a specific image with a specific reference number is. A row covering a batch must name the batch's boundary precisely, or the batch grows quietly. |
| **Category** | From the table below. Determines which extra fields are mandatory. |
| **Rights holder** | The entity that can actually grant. Frequently not the entity that *offered* — see the traditional-material note below. |
| **Media** | What formats and channels the grant covers. A licence for "web" does not cover broadcast, and finding that out at delivery costs a re-licence at the licensor's leisure. |
| **Territory** | Where it may be shown. Checked against the intended distribution footprint **before** picture lock, not at delivery. |
| **Term** | How long. Record the expiry as a date, not a duration — "5 years" requires knowing the start, and the start is what gets lost. |
| **Exclusivity** | Whether anyone else may use the same material, and whether that matters. Usually it does not; where it does, it matters a lot. |
| **Fee** | What was paid, in what currency, and whether it was one-off or recurring. A recurring fee with no owner is how a licence lapses mid-season. |
| **Credit wording (verbatim)** | The licensor's exact required string. Paraphrasing a credit line is a breach of the licence, and it is the single most common one. Honoured in the credits **and** in the published credit list, per core/02 §3 — not one or the other. |
| **Restrictions** | Cropping, colouring, excerpting, minimum duration, maximum duration, no-modification, no-derogatory-use. **Many archive agreements restrict exactly the operations a modern edit performs by default** — reframing to 9:16, applying a show LUT, cutting a 4-second excerpt. Record them here or the edit will breach them without knowing. |
| **Status** | `cleared` / `pending` / `not-required` / `refused`. See below. |
| **Date checked** | ISO `YYYY-MM-DD`. When a human last verified this row against the actual agreement — not when the row was created. |
| **Checked by** | Role **and** person. The role so the record survives staff changes; the person so a question has an addressee. |

### Status values

| Value | Meaning | Permits delivery? |
|---|---|---|
| `cleared` | A written grant exists, its scope covers the intended use, and a named human has read it. | Yes |
| `pending` | Requested, negotiating, awaiting countersignature, or awaiting a re-check. | **No** |
| `not-required` | A considered position that no clearance is needed — public domain in every relevant jurisdiction, studio-owned, or a fair-dealing reliance. **Requires a written rationale**, not a shrug. See core/02 §3 and §4. | Yes |
| `refused` | Asked and declined. The row stays forever, so nobody asks again in year three and nobody uses it by accident. | **No** |

**No production may be delivered with any asset in `pending`.** Core/02 §10 states it
without qualification: an episode cannot be delivered with any asset in `pending`
clearance state, and there is no provisional delivery. The rights gate runs twice — at
picture lock and again at delivery — precisely because things move back into `pending`
between the two, and the second run is the one that catches it. A `pending` row at
delivery is not a paperwork problem to resolve later; it is a blocked delivery.

`not-required` is the value that requires the most discipline. It is a *decision*, and
it carries a rationale in the Restrictions column or a linked note. A `not-required`
with no stated basis is functionally an uncleared item wearing a green label.

## Categories

From [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §2.
Each row's category determines what the row must additionally record.

| Category | What the row must record beyond the standard columns |
|---|---|
| **Archival still / moving image** | Rights holder, full licence scope, fee, required credit wording, and the restrictions on cropping, colouring, and excerpting. These four are the ones that get missed. |
| **Museum and collection objects** | The institution, the object's accession number, and **photography rights separately from object rights** — they are frequently held by different parties, and a licence to the object is not a licence to the photograph of it. Credit line exactly as the institution specifies. |
| **Manuscripts and documents** | Custodian, reproduction permission, and translation rights separately if the material is translated. A translation is a new work with its own rights holder. |
| **Interviews and testimony** | Signed consent form (path to it), the scope consented to, withdrawal terms, and any anonymity requirement. Anonymity is a technical constraint on the edit and the metadata, not just an editorial one. |
| **Music** | **Composition rights and recording rights are separate — record both.** One row per right, or one row that names both holders explicitly. Plus territory, term, and the cue sheet entry (`10_publish/cue_sheet.csv`, maintained from episode one). |
| **Traditional music and performance** | Everything under Music, **plus who granted it and on what basis they held the right to grant it.** Frequently the licensor is not the tradition's custodian. A row here that cannot answer the "on what basis" question is not cleared, whatever the paperwork says. |
| **Fonts** | Licence tier covering **broadcast/streaming** use specifically, and the **number of seats**. See [../../library/fonts/README.md](../../library/fonts/README.md) — the diacritic constraint eliminates most typefaces before the licence question is even reached. |
| **LUTs, plugins, stock SFX** | A licence permitting commercial redistribution **inside a finished film**. "Royalty free" describes a payment model, not a grant, and does not answer this. |
| **Generated assets** | The vendor's terms **at the date of generation**, by reference to a dated row in [model_terms_register.md](model_terms_register.md). Terms change; what matters is what they were when the asset was made and what they are at delivery. |
| **Third-party code** | Licence compatibility for anything vendored into `automation/`. Copyleft in a delivered toolchain is a decision, not an accident. |
| **Talent and crew** | Contributor releases, voice licence (explicitly covering synthetic reproduction if used), composer agreement stating who holds master and publishing, crew agreements assigning work product. Core/02 §7. |

## Related registers

- [model_terms_register.md](model_terms_register.md) — generative vendor terms, per
  tool. A generated asset's row here points at a dated row there.
- [chain_of_title.md](chain_of_title.md) — the per-production assembly of all of the
  above, for a distributor.
- [takedown_log.md](takedown_log.md) — what happened after publication.

## Maintaining this register

- One row per grant, not per use. An item used in four episodes has one row and four
  manifest references.
- Re-check dates matter more than creation dates. A row checked in 2026 and relied on
  in 2028 has not been checked.
- Never widen a scope from memory. If the row says "online only" and the production
  needs broadcast, the answer is a new grant, not an edited cell.
- The row is not the agreement. Store the signed document and reference it; this table
  is an index over the agreements, not a substitute for them.
