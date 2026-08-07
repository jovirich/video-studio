---
doc: packs/product-marketing/06
title: Product depiction
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# 06 — Product depiction

[05_claim_substantiation.md](05_claim_substantiation.md) governs what the film
*says*. This governs what it *shows*, which is where the same failure arrives without
anyone writing it down.

## 1. The non-negotiable

> **Every depiction of the product's own interface is captured from the running
> product. It is never generated, and never rebuilt in a design tool and passed off
> as a capture.**

This is the pack's equivalent of documentary's prohibition on fabricated archival
material, and it rests on exactly the same clause:
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md)
§2 item 1 prohibits generating an artefact intended or likely to be taken for a
genuine one. A rendered UI is taken for a genuine one by every viewer, always. That
is what a UI shot is *for*.

Declared mechanically in [pack.yaml](pack.yaml):

```yaml
record_extensions:
  shot:
    prohibit_generated_for: [product_interface]
```

A shot classed `product_interface` with a generative provenance record fails
validation. There is no override flag, because the situations that produce the
temptation — the feature is not finished, the data looks bad, the loading state is
ugly — are precisely the situations where the rendered version would be a lie.

**Why this is stricter than it looks.** Not shipping is not the only failure. A
captured screen that has been retimed to hide latency, composited to remove an error
state, or recorded on an internal build with flags no customer can reach is also
showing something that does not exist. See §3.

## 2. Provenance classes for product material

Every shot carries a class, on the model of
[documentary-history](../documentary-history/04_visual_language.md) §5. It determines
what is permitted and which gate looks at it.

| Class | What it is | Generation | Treatment |
|---|---|---|---|
| `product_interface` | The running product, captured. Screen recording, device capture, screenshot in motion. | **Prohibited** | Build and date recorded on the shot. Any alteration logged per §3. |
| `product_physical` | The physical product, filmed or photographed. | **Prohibited** for the product itself | The unit filmed is identified. Colourways and finishes as they ship. |
| `product_mockup` | A representation of an interface that is not a capture. | Permitted under §4 | Labelled per §4. Never in a capability claim. |
| `context` | Environment, hands, desks, streets, weather, texture, the world the product sits in. | Permitted | Ordinary provenance record. No claim attaches. |
| `illustration` | Diagrams, abstractions, metaphor, motion graphics that explain rather than depict. | Permitted | Must not resemble the interface. See §4. |
| `graphic` | Charts, figures, comparison tables, statistics on screen. | Layout may be generated; **the numbers may not** | Every figure resolves to a `product_claim`. [../../standards/data_graphics.md](../../standards/data_graphics.md) applies. |
| `person` | Any human appearing as a customer, user, employee, or endorser. | See §6 and §7 | Release on file covering this use, including AI processing. |

Mixing `product_interface` and `product_mockup` inside a single continuous shot is
prohibited. A cut is required at the boundary — the same rule, for the same reason,
as documentary's prohibition on mixing archival and reconstruction in one shot.

## 3. Capture rules

A capture is evidence. It is treated like evidence.

**Recorded on every `product_interface` shot:**

| Field | Why |
|---|---|
| Build or release identifier | So the shot can be re-verified against what shipped |
| Capture date | Evidence has a shelf life ([05_claim_substantiation.md](05_claim_substantiation.md) §4) |
| Environment | Production, staging, or local. Staging and local captures need §3.2 |
| Account and entitlement | A capture from an internal account with every flag on shows a product nobody can buy |
| Data source | Real, seeded, or synthetic — see §3.1 |
| Alterations | Every one, per §3.3 |

### 3.1 The data in the screen

Real customer data never appears on screen. Not blurred, not scrolled past, not in a
notification that fires mid-capture. This is a privacy obligation, not an aesthetic
one, and it survives no deadline.

**Demonstration data is seeded deliberately** into a controlled account, and it is
plausible rather than flattering. Seeding an account with results the product does
not typically produce turns a capture into a performance claim
([05_claim_substantiation.md](05_claim_substantiation.md) §6) without anyone
noticing they made one — the numbers were on screen, so the film said them.

Names, faces, logos, and addresses in seeded data are fictional and are checked
against real entities before capture. A plausible invented company name that turns
out to exist is a problem someone else gets to have.

### 3.2 Unreleased and internal builds

Permitted only where the studio's roadmap policy
([05_claim_substantiation.md](05_claim_substantiation.md) §5) permits showing
unreleased functionality at all, and then:

- the shot carries the qualifier that policy requires, for its full duration;
- the build is recorded, and the claim record carries `strength: roadmap`;
- **the functionality is real and running.** A capture of a prototype that fakes its
  own backend is a mockup, is classed `product_mockup`, and is labelled as one. The
  distinction is whether the thing on screen actually did what it appears to do.

### 3.3 What may be done to a capture

| Alteration | Permitted | Condition |
|---|---|---|
| Crop, scale, reframe | Yes | Not to hide adjacent state that contradicts the claim |
| Speed change | Yes | **Only with a visible indication**, where the change is material to a performance claim. Silently cutting a nine-second load to one second is a fabricated performance figure |
| Cursor smoothing, click highlights, keystroke overlays | Yes | Presentational |
| Colour grade consistent with the show LUT | Yes | Must not alter interface colours that carry meaning (error red, status states) |
| Compositing the capture into a device frame or environment | Yes | The capture itself unmodified |
| Removing an error, empty, or loading state | **No** | This is the alteration that changes what the product is |
| Replacing text, labels, or values in the interface | **No** | Re-capture with the right data instead |
| Generative fill, upscale that invents detail, frame interpolation across UI text | **No** | Invents interface that was never rendered |
| Compositing a real interface into a generated scene | Yes | The interface is unaltered; the scene is classed `context` and provenance-recorded |

Every permitted alteration is logged as a `post_process` step in the asset manifest,
per [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §4.
An alteration that is not in the manifest did not happen, as far as the gate is
concerned, and the gate will find it.

## 4. Mockups, concepts, and illustration

Mockups are legitimate. Pretending they are captures is not.

**Permitted uses of `product_mockup`:**

- Concept and vision work explicitly framed as such — a film about where the product
  is going, not what it does.
- Abstracted or stylised interface that no viewer would read as a screenshot:
  simplified geometry, non-literal typography, deliberately unreal.
- Recruiting, culture, and brand films where no capability is asserted.

**Required label.** Wherever a mockup could be read as the product, it carries an
on-screen qualifier for the duration of the shot. Exact wording is
**TBD — the studio decides**, recorded in `studio.yaml` alongside its roadmap policy
under [05_claim_substantiation.md](05_claim_substantiation.md) §5, and applied
uniformly. Deciding it per-piece produces a set of assets that qualify inconsistently,
which reads as though the qualified ones were the exceptions.

**The resemblance line.** Illustration and motion graphics that *explain* the product
are unrestricted. The moment they start to resemble the actual interface — real
control affordances, real layout, real-looking data — they become a mockup and pick
up the label. The test at the gate: **shown this frame with no context, would a
viewer believe it is a screenshot?** If yes, it is a mockup or it is a capture. There
is no third thing.

**Prohibited outright:** a mockup of functionality that does not exist and is not
planned, in a piece that also contains real captures. The mixture is what deceives;
the viewer calibrates on the real material and extends that trust to the rest.

## 5. Showing results and outcomes

A results shot — the dashboard after, the inbox at zero, the graph going up — is the
most persuasive thing in a marketing film and the easiest place to make a claim
nobody wrote.

- **A depicted result is a claim about typical experience** unless the film says
  otherwise. Record it as a `product_claim` of kind `outcome`, with the population it
  is typical of.
- **An atypical result is labelled.** Where the studio shows a best case, it says so
  in frame. What the qualifier says is TBD — the studio decides, with legal review
  where the category falls under [05_claim_substantiation.md](05_claim_substantiation.md) §10.
- **Before/after requires the same conditions.** Same account, same data, same
  hardware, same period. A before shot captured on a deliberately degraded setup is
  fabricated evidence.
- **Time compression is disclosed** where the elapsed time is part of what is being
  shown. A montage of a month's work in eight seconds is obviously a montage; a
  "watch it finish" shot that has been cut is not obviously anything.
- **No generated result.** If the dashboard cannot be made to show the outcome using
  real or honestly seeded data, the shot does not exist. This follows from §1 and is
  worth stating separately because the result shot is where teams reach for a design
  tool at 2am.

## 6. Customer stories

Case studies are this pack's most valuable format and its highest-consent-risk one.

**Requirements, all of them:**

1. **The customer is real and is a customer.** Named, identifiable, currently using
   the product, and willing to be associated with it.
2. **The words are theirs.** A customer may be interviewed, edited for length, and
   asked good questions. They may not be scripted into a claim they did not make, and
   an edit may not assemble a sentence they did not say. Editing to change meaning is
   the misleading-true-statement failure and it is a consent breach as well as an
   editorial one.
3. **A release covering this use, before the shoot.** Scope, media, territories,
   duration, right of review, right of withdrawal — and **whether AI processing of
   their footage, image, or voice is permitted, and to what extent**. Per
   [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §7 and
   [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2 item 2,
   a release that does not state the AI processing scope does not cover AI processing.
   Templates: [../../templates/legal/](../../templates/legal/).
4. **Their employer's permission where they speak for it**, and their premises,
   logos, and staff cleared separately. Permission to be filmed is not permission to
   use a mark.
5. **Any performance figure they state is still a `product_claim`.** "It cut our
   processing time by half" is an outcome claim with an `E-CUS` evidence type, and it
   is attributed to them on screen rather than restated as a general fact.
6. **Withdrawal has a mechanism.** What happens to assets in market when a customer
   withdraws, and how fast, is recorded on the release. Withdrawal that cannot be
   executed is not a right.

**Anonymised customers** are permitted where the customer requires it. The release
still exists, the identity is held outside the repository, and the film does not
imply a larger or different customer than the real one.

## 7. Generated testimonials — prohibited

**A person who appears to be a customer, user, or endorser, and who does not exist,
may not appear in this studio's output. In any form.**

This is not a rule this pack invents. It is
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md)
§2 items 1 and 2 applied without modification: a synthetic endorser is a fabricated
evidentiary artefact, and where it borrows from a real person it is an unconsented
likeness as well. A pack may add constraints and tighten core; it may never loosen
one ([../../core/00_platform_charter.md](../../core/00_platform_charter.md) §6). The
marketing convention that treats a synthetic spokesperson as a production efficiency
does not survive contact with core, and the studio does not get to adopt it by
declaring it stylised.

Covered by the prohibition:

- A generated human delivering a testimonial, review, or endorsement.
- A generated human presented as "a user" in a scenario that implies real experience.
- A real actor delivering an invented testimonial as though it were their own
  experience.
- A voice clone of a real customer reading approved copy they did not say.
- Generated social proof: fabricated reviews, ratings, comment threads, follower
  counts, or user counts shown on screen.

Permitted, and clearly distinct:

- **A disclosed actor in a disclosed scenario.** A performer portraying a fictional
  user in a piece the viewer plainly reads as dramatised, making no claim to be a
  real customer. Ordinary talent contract; performance provenance recorded.
- **A generated human in a non-endorsing role** — a figure in a crowd, a hand, an
  abstract or illustrated character — where the studio's provenance disclosure covers
  it and the figure asserts nothing about the product. Note that
  [fashion-film](../fashion-film/06_body_and_representation.md) §3 requires a
  studio-level decision before any synthetic human is used commercially; a studio on
  this pack running both kinds of work should make the same decision once rather than
  per pack.
- **Real employees as themselves**, with releases.

**The test**, which is core's test narrowed to this genre: *if a viewer learned
exactly how this person was made, would they feel informed or deceived?* For a
testimonial the answer is always "deceived", because the entire persuasive force of a
testimonial is the belief that someone real said it.

## 8. Inheritance and enforcement

Inherits unmodified from core: provenance on every asset and generated material
labelled ([../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §3–4),
clearance on everything ([../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md)),
human signature at every gate
([../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md)).
Adds the interface-capture prohibition, the class table at §2, and the alteration log
at §3.3. Loosens nothing.

| Standard | Gate | Mechanism |
|---|---|---|
| §1, §2 | `picture_audio_lock` | Every `product_interface` shot has a capture record and no generative provenance |
| §3.3 | `technical_qc` | Alterations present in the manifest |
| §4 | `picture_audio_lock` | Mockup label applied per studio policy |
| §5, §6 | `claim_substantiation` | Result and outcome claims resolve to records |
| §6 | `stakeholder_approval` | Customer release on file covering this cut and its AI processing |
| §7 | `technical_qc` | No `person` asset with generative provenance in an endorsing role |

Checklists: [../../ops/checklists/](../../ops/checklists/). Gate definitions: [gates.yaml](gates.yaml).
