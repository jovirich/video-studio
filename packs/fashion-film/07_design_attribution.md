---
doc: packs/fashion-film/07
title: Design attribution
status: active
version: 0.1.0
updated: 2026-08-07
owners: [cultural-advisor]
---

# 07 — Design attribution

Fashion draws on traditions. That is not a problem to be solved; it is how the field
has always worked, and the traditions themselves are the product of the same
borrowing. What generates justified anger is not the borrowing — it is borrowing that
does not say where it came from, and borrowing from people who were not asked, paid, or
credited while the result is sold.

A generative model makes both failures effortless. Asked for a motif, a weave, or a
garment form, it will produce one, competently, without knowing what it is, whose it
is, whether it is restricted, or what it means. The production then has an image with
no origin — which is not neutral, because the origin still exists and someone will
recognise it.

## 1. Attribution standard

`studio_must_decide: attribution_standard` — [pack.yaml](pack.yaml). Decided at studio
level before the first line opens, recorded in `studio.yaml`.

> **Every design element drawn from an identifiable source outside the studio's own
> work is recorded as a `design_source` before it enters a prompt or a sample, and is
> credited and compensated according to a standard the studio set in advance.**

The studio decides the *standard*. The pack fixes that a standard exists, is written
down, and is applied uniformly — because deciding attribution case by case means
deciding it under deadline, in favour of the deadline, every time.

**The studio states, on each of these, before its first production:**

| Question | What must be answered | Default pending a decision |
|---|---|---|
| **What triggers a `design_source` record?** | The threshold at which a reference becomes a source. See §2 for the pack's floor | The floor at §2 |
| **Where does credit appear?** | On-screen credit, end card, published campaign notes, product page, or several. A credit only the studio can see is not a credit | On screen and in published campaign material |
| **How is credit worded?** | Named community, region, tradition, and — where individuals are involved — named people. **"Inspired by traditional craft" credits nobody** | Named at the level of specificity the source's own holders use |
| **What is compensation, and on what basis?** | Fee, royalty, commission, or a defined arrangement. Named per category | TBD — the studio decides. A standard with no compensation term is a credit policy, not an attribution standard, and should say so plainly rather than imply otherwise |
| **Who decides whether a source needs agreement rather than attribution?** | See §4 | The Cultural Advisor, who holds `hold_authority` at the `representation_review` gate ([gates.yaml](gates.yaml)) |
| **What happens when the source cannot be identified?** | The element is not used, or is used only after a ruling | The element is not used. See §3 |

**Three rules the pack fixes regardless of the studio's standard:**

1. **Attribution precedes generation.** The `design_source` record exists before the
   prompt card that draws on it, and before the sample is made — not before delivery.
   Once the campaign exists, attribution becomes a negotiation conducted from a
   position where the studio has already taken the thing.
2. **Specificity is the whole content of a credit.** A tradition belongs to particular
   people in a particular place. "African print", "tribal pattern", "ethnic motif",
   and "traditional weave" name nothing, flatten everything, and are the exact
   colonial-era category-inheritance that
   [documentary-history](../documentary-history/07_cultural_sensitivity.md) §6 refuses.
   The prohibited-language list at
   [../../standards/prohibited_language.md](../../standards/prohibited_language.md)
   applies to campaign copy as much as to narration.
3. **Attribution is not a substitute for agreement.** Some sources require permission,
   and crediting without it is taking with a footnote. §4 draws the line.

## 2. What requires a `design_source` record

The pack's floor. A studio may set a lower threshold, never a higher one.

| Element | Record required |
|---|---|
| A textile identified with a specific people, region, or community — its weave, dye method, structure, or characteristic pattern | **Yes** |
| A motif, symbol, or pattern with meaning inside a tradition | **Yes** |
| A garment form or silhouette identified with a specific culture | **Yes** |
| A craft technique — a specific embroidery, resist-dye, beadwork, or construction method | **Yes** |
| Work by a named artisan, collaborator, or workshop | **Yes**, always |
| Work by a named living designer or artist outside the studio | **Yes** — and see §4; core prohibits generating in the style of a living artist or cultural custodian without agreement |
| Regalia, ceremonial dress, or garments restricted by office, initiation, gender, age, or occasion | **Yes**, and §4 applies — this is not an attribution question |
| Religious or sacred dress and symbols | **Yes**, and §4 applies |
| A historical period reference from a closed tradition with no living custodians | **Yes**, at reduced obligation — credited, not agreed |
| Generic construction — a set-in sleeve, a French seam, a shirt collar | No |
| The studio's own archive | No, beyond ordinary internal versioning |

**The generative-tool clause.** A model asked for "a traditional pattern" will produce
something derived from a real tradition it did not name. The output has a source; the
production simply does not know what it is. Two consequences:

- **A prompt that does not name a source produces an element with an unrecorded
  source, which is not permitted.** If the studio wants a tradition's motif, it names
  the tradition, records the `design_source`, and meets whatever §4 requires. If it
  does not want one, the prompt must actively exclude the space rather than leave it
  unspecified — an unspecified prompt is filled from the model's prior, and its prior
  is somebody's heritage.
- **Recognition is the test, not intent.** "The model made it up" is not a defence
  available to anyone who recognises what it made up.

## 3. When the source cannot be identified

The output looks like something, nobody can say what, and the deadline is Thursday.

**The default is that the element is not used.** This is the same discipline as
[documentary-history](../documentary-history/02_evidence_and_sourcing.md) §9 — when
the research runs out, change the claim down, do not fill the gap — and it is easier
here, because fashion has an option documentary lacks: **design something else.**

Before discarding, in order:

1. **Ask someone who would know.** The advisory relationship exists for this.
2. **Ask the design team what they were looking at.** Unrecorded references are
   usually recoverable within a day of the moodboard being made and not after.
3. **If it is identified, record it and meet §1 and §4.**
4. **If it is not identified, it is not used.** Recording "source unknown" is not a
   `design_source` record; it is a note that the studio proceeded anyway.

## 4. When agreement is required rather than attribution

Attribution says where something came from. Agreement means the people it came from
said yes. They are different obligations and the second is not discharged by the first.

**Agreement is required, not merely attribution, where:**

| Situation | Why |
|---|---|
| The source is **restricted** within its tradition — by initiation, office, gender, age, lineage, or occasion | Wide availability is not consent. This is [documentary-history](../documentary-history/07_cultural_sensitivity.md) §3, adopted unchanged; a commercial framing makes it worse, not lighter |
| The element is **sacred, ceremonial, or religious** | As above |
| The source is a **living artisan, workshop, community enterprise, or named custodian** | Core prohibits generating in the style of a living artist or a specific cultural custodian's work without agreement — [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2 item 7. Not waivable by this pack or this studio |
| The tradition is **held collectively** and has a body that speaks for it | The right to grant belongs to the holders, and frequently the person offering it is not the holder |
| The element carries **legal protection** — geographical indication, collective mark, registered design, or a protected traditional-knowledge regime | **Jurisdiction-specific, differs by territory, and changes. This pack states no rule — escalate**, per [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §3, for every territory in the distribution footprint |
| The studio intends **commercial production**, not editorial reference | The obligation scales with what is being sold |

**Where agreement is required and not obtained, the element does not appear.** Not with
a credit, not with a disclaimer, not "as homage". The `representation_review` gate
carries hold authority precisely for this, and the Showrunner cannot unilaterally
release it — the cost of being wrong is borne by people outside the studio.

**Agreement is a relationship, not a clearance.** Adopting
[documentary-history](../documentary-history/07_cultural_sensitivity.md) §5 and §7
unchanged: approach through recognised channels; state plainly what the material will
be used for, where it will be shown, and for how long; consent for a campaign is not
consent for a training set; provide the finished work to the community in a form they
can access; where they ask that something not be shown, the default is to comply.

## 5. Collaborating artisans

Where people made the thing, the obligations are concrete and are not satisfied by a
paragraph about heritage.

- **Named.** In the credits, in campaign material, and on the `design_source` record.
  Individuals by name where they consent to be named; the workshop or cooperative
  where they prefer that.
- **Paid.** For the work, at a rate agreed before it starts, and separately from any
  fee paid to an intermediary. An artisan who is not paid is not a collaborator;
  they are a favour being taken advantage of, and they will rightly stop answering —
  [documentary-history](../documentary-history/07_cultural_sensitivity.md) §5 reaches
  the same conclusion about advisors, for the same reason.
- **Told what the work is for**, including the territories and the term.
- **Asked about AI processing specifically.** Whether their work may be photographed
  for reference, generated from, trained on, or reproduced generatively are four
  separate permissions, and none is implied by a commission to make a garment.
- **Given the finished work.**
- **Credited in the same register as everyone else.** A film that names its director
  and its stylist by name and its makers as "local artisans" has stated a hierarchy.

## 6. The `design_source` record

Declared in [pack.yaml](pack.yaml) `required_record_types`. ID grammar per
[../../standards/id_system.md](../../standards/id_system.md); this pack allocates
`DSR` at line scope. Records are never deleted — a withdrawn agreement is recorded as
`retracted` with the reason, which is how the studio remembers what it stopped using
and why.

```yaml
id: DSR-<SCOPE>-0004
type: design_source
status: draft | review | locked | superseded | retracted
element: What was drawn on, described precisely enough to be recognised.
kind: textile | motif | garment_form | technique | artisan_work | designer_work | period_reference
origin:
  people_or_community: <named at the specificity its holders use>
  region: <...>
  tradition: <...>
  named_individuals: [<artisans, custodians, designers>]
identified_by: <who established this, and how>
restricted: true | false | unknown        # unknown blocks use until resolved — §3
obligation: attribution | agreement       # §4
agreement:
  required: true | false
  granted_by: <person or body, and the basis on which they hold the right to grant>
  scope: { media: [...], territories: [...], term: <...>, commercial: true|false, ai_processing: <...> }
  reference: <agreement document>
  advisory_ruling: <ADV reference>
compensation: { basis: <...>, agreed_with: <...>, reference: <...> }
credit:
  wording: <exact words as they will appear>
  surfaces: [<on-screen, end card, campaign notes, product page>]
used_in: [<garment ids, asset ids, prompt card ids>]
community_received_work: true | false
retraction_reason: <required when retracted>
```

Two fields carry disproportionate weight:

- **`granted_by` … the basis on which they hold the right to grant.** The recurring
  failure in this field, across genres, is that the person who granted permission was
  not the person entitled to grant it. Recording the basis makes that checkable
  instead of assumed — the same requirement
  [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §2
  places on traditional music.
- **`used_in`.** When an agreement expires or is withdrawn, this is what tells you
  which garments, campaigns, and cutdowns are affected. Without it, withdrawal cannot
  be executed, and a withdrawal that cannot be executed is not a right.

## 7. Inheritance and enforcement

Adds to core; loosens nothing. §4's requirement of agreement for living artisans and
custodians is
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md)
§2 item 7 applied, and is not waivable at studio level. Rights per
[../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md).
Hold authority per
[../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §6.
Where this document adopts
[documentary-history](../documentary-history/07_cultural_sensitivity.md), it adopts it
as written — a rule quoted at reduced strength is a loosened rule.

| Standard | Gate | Mechanism |
|---|---|---|
| §1 | Greenlight | Studio cannot greenlight with `attribution_standard` unresolved |
| §2 | `representation_review` | Every qualifying element has a locked `design_source` before generation |
| §3 | `representation_review` | `restricted: unknown` blocks use; hold authority applies |
| §4 | `representation_review` | Agreement on file with `granted_by` basis; Showrunner cannot release the hold |
| §5 | `stakeholder_approval` | Artisan credit and compensation recorded before delivery |
| §6 | `technical_qc` | Credit wording present on the declared surfaces in the delivered package |

Checklists: [../../ops/checklists/](../../ops/checklists/). Gate definitions: [gates.yaml](gates.yaml).
