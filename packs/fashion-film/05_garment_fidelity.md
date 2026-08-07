---
doc: packs/fashion-film/05
title: Garment fidelity
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# 05 — Garment fidelity

## 1. The non-negotiable

> **The physical garment is ground truth. Every garment appearing in a deliverable
> exists as a physical object, has been captured as it physically is, and every
> generated frame showing it is verified against that capture.**

Fashion film is permitted more visual invention than any other genre on this platform.
The environment can be impossible, the light can be unmotivated, the body can move in
ways bodies do not. **The garment cannot.** Everything else in the frame is editorial;
the garment is the product, and a property shown that the garment does not have is a
false product claim wearing an editorial coat.

The line is drawn at the object, not at the image, because that is where the viewer's
expectation lands. Nobody buys the light.

## 2. Reference capture workflow

`reference_capture_workflow_established` is a line-opening condition
([pack.yaml](pack.yaml)). A line does not open without it, because retrofitting
reference capture after a collection has shipped to a shoot is impossible — the sample
has gone.

Capture happens **before** any generative work touches the garment, on the actual
sample that will appear or on the production unit it represents.

| Capture | What it fixes | Minimum |
|---|---|---|
| **Flat, front and back**, evenly lit, with a colour reference target in frame | Colour, proportion, seam and panel layout | Required for every garment |
| **On-form or on-body, front / three-quarter / back / profile** | Fit, silhouette, how the garment sits and hangs | Required for every garment |
| **Movement pass** — the garment walking, turning, and settling | **Drape.** The single property generative tools get wrong most often and most expensively | Required for any garment appearing in motion |
| **Detail macro** — closures, hardware, stitching, hem, lining, labels, trims | Finish. What a customer inspects on arrival | Required for every garment |
| **Texture macro** — weave, knit, pile, sheen, transparency, surface | Material read. Distinguishes the fabric from every other fabric of the same colour | Required for every garment |
| **Colour under two lighting conditions**, with the reference target in both | Metamerism. A garment that reads one colour in daylight and another under tungsten will produce a refund request, and the capture is what tells you which colour is the truthful one | Required for every garment |
| **Behaviour notes** — how it fastens, which way it wraps, whether it is reversible, how it creases | The things a generative model invents because nobody told it | Required |

**Recorded on the capture:** the sample identifier, size, colourway, the date, the
lighting setup, the colour target used, and who captured it. A capture without a colour
reference target is not a colour reference; it is a photograph.

**Where the physical sample does not yet exist** — pre-production collections, made-to-
order, or a piece still at the atelier — the garment does not appear in a deliverable.
There is no provisional path. The alternative is a generated garment presented as a
real one, which is prohibited at §3 and is the exact failure this pack is shaped
around.

## 3. What may and may not be generated

| Element | Generated? | Condition |
|---|---|---|
| **The garment itself** — its colour, texture, drape, cut, closure, finish, hardware, print, or trim | **No** | The garment is captured. This is the pack's non-negotiable |
| **A garment's colourway that was not produced** | **No** | Recolouring a captured garment into a colourway that does not exist is inventing a product |
| **Print and pattern placement** | **No** | Placement is a manufacturing fact. A repositioned print is a different garment |
| Environment, set, location, backdrop | Yes | Provenance recorded like any asset |
| Light, atmosphere, weather, particles | Yes | Must not alter how the garment's colour or texture reads — see §4 |
| Camera moves, transitions, motion design | Yes | — |
| Abstract and graphic elements, typography, titles | Yes | [08_editorial_visual_language.md](08_editorial_visual_language.md) |
| Non-garment props | Yes | Unless a real product is depicted, in which case the same rule applies to it |
| **The human body wearing the garment** | See [06_body_and_representation.md](06_body_and_representation.md) §3 | Studio-level decision, on-screen disclosure, never presented as a specific real model |
| Hair and makeup on a captured performer | Retouch only, within [06_body_and_representation.md](06_body_and_representation.md) §5 | Generative replacement is a body alteration, not a styling choice |
| Extending, retiming, or interpolating garment motion | **Constrained** | Permitted only where the result matches the movement pass at §2. Interpolation invents drape, and drape is the property being verified |
| Upscaling a garment shot | **Constrained** | Permitted only where it does not invent texture. Most upscalers invent texture; that is what they are for. Verify against the texture macro |
| Compositing a captured garment into a generated scene | Yes | Garment layer unaltered; grade must not shift its colour outside §4's tolerance |

**The compositing rule is the workhorse of this pack.** It is what makes fashion film
compatible with heavy generative use at all: capture the garment, generate the world,
composite, verify. A pipeline built that way passes the `garment_verification` gate
routinely. A pipeline that generates the garment does not pass it at all.

## 4. Verification

The `garment_verification` gate ([gates.yaml](gates.yaml)) is owned by the Visual
Director and compares every frame in which a garment appears against that garment's
reference capture, on five properties.

| Property | Checked against | Failure looks like |
|---|---|---|
| **Colour** | The flat capture and the two-lighting capture, with the colour target | The garment is a different colour than the customer will receive. The most common and most expensive failure in the genre, and it is caused as often by grading as by generation — a show LUT applied over a garment shot is a colour alteration |
| **Texture** | The texture macro | Weave becomes knit, matte becomes sheen, a heavy fabric reads light. Generative upscaling and denoising both do this silently |
| **Drape** | The movement pass | Fabric behaves with the wrong weight — stiff cloth flows, heavy cloth floats. Invisible in a still, glaring in motion, and the property that most determines whether a customer feels misled |
| **Closure** | The detail macro | Buttons on the wrong side, an invented zip, a wrap crossing the wrong way, hardware that is not the hardware |
| **Finish** | The detail macro | Stitching, hems, linings, labels, and trims that differ from the object. The details a customer inspects first on arrival |

**Tolerances are studio decisions.** How much colour deviation is acceptable under
which delivery condition, and what measurement basis is used, is
**TBD — the studio decides**, recorded in `studio.yaml` and owned by the Visual
Director with the designer or brand owner. What this pack fixes is that a tolerance
exists, is numeric, is applied uniformly, and is not renegotiated at 2am on a delivery
day.

**The grade is inside the verification, not outside it.** Colour is verified on the
graded, delivered frame — not on the ungraded plate. A garment that was accurate before
the show LUT and is inaccurate after it is inaccurate. This is the single most common
way a production passes verification and still ships the wrong colour.

**Every deliverable variant is verified.** Different codecs, colour spaces, and
platform re-encodes move colour. A master that verifies and a vertical cutdown that
does not is a failure, and the cutdown is what most people will see.

## 5. The `garment` record

Declared in [pack.yaml](pack.yaml) `required_record_types`. ID grammar per
[../../standards/id_system.md](../../standards/id_system.md); this pack allocates
`GRM` at line scope. Records are never deleted — a garment cut from a collection keeps
its record so that assets referencing it can be found.

```yaml
id: GRM-<SCOPE>-0031
type: garment
status: draft | review | locked | superseded | retracted
collection: <collection>
season: <season>
name: <as it will be called in the deliverable and in the store>
sku_or_style_ref: <the identifier the business uses>
colourway: { name: <as named commercially>, reference: <colour reference and its basis> }
sizes_captured: [<sizes of the samples captured>]
materials: <composition as it will be published>       # a performance claim if published — see §6
reference_capture:
  flat: [<asset ids>]
  on_form: [<asset ids>]
  movement: [<asset ids>]
  detail_macro: [<asset ids>]
  texture_macro: [<asset ids>]
  colour_conditions: [{ condition: <...>, target: <colour target used>, asset: <asset id> }]
  captured_at: <iso8601>
  captured_by: <person>
  sample_identifier: <which physical unit>
behaviour_notes: >
  How it fastens, wraps, creases, and moves. What a generative tool would otherwise invent.
design_source: <DSR reference or `original`>            # 07_design_attribution.md
availability: { status: <in production | sample only | not produced>, territories: [...] }
tolerance_profile: <the studio's tolerance set applied to this garment>
verification: { gate: garment_verification, signed_by: <person>, signed_at: <iso8601> }
appears_in: [<asset and deliverable ids>]
```

`appears_in` and `availability` together answer the question that arrives when a
colourway is dropped or a piece is never produced: **which assets have to come down?**
Assembling that from memory across a season of cutdowns is the avoidable emergency the
field runs annually.

## 6. Where an editorial image becomes a false product claim

Editorial licence is real and this pack protects it. The boundary is not "is the image
stylised" — it is **what would a reasonable viewer take away about the object they
might buy?**

| Image | Position |
|---|---|
| The garment in an impossible landscape, under impossible light, in an impossible colour *grade applied to the whole frame* | **Editorial.** The world is obviously invented; the garment reads as itself |
| The same, where the grade has pushed the garment outside the colour tolerance | **False claim.** The viewer will read the garment's colour as the garment's colour |
| A dramatic wind machine making a fabric move more than it would | **Editorial**, if the fabric could move that way. **False claim**, if it could not — that is a drape assertion |
| A garment shown fastened in a way it does not fasten | **False claim** |
| Extreme motion blur, obscured detail, silhouette, shadow | **Editorial.** Showing less is always safe. Showing *different* is not |
| A garment digitally slimmed, lengthened, or reshaped on the body | **False claim about fit**, and a body alteration under [06_body_and_representation.md](06_body_and_representation.md) §5 |
| A print scaled up "for the frame" | **False claim.** Scale is a property of the garment |
| A material property stated on screen — waterproof, thermal, recycled content, durability | **Out of this pack entirely.** These are performance claims and need [product-marketing](../product-marketing/05_claim_substantiation.md)'s substantiation gate, including its §10 legal-review categories. Sustainability and material-composition claims are regulated in several territories and the rules differ and are changing — **escalate** |

**Three tests, applied at the gate in order:**

1. **The arrival test.** If the viewer received this garment tomorrow, would the image
   have set an expectation the object does not meet? Colour, texture, drape, closure,
   finish.
2. **The obscurity test.** Editorial may show *less* of a garment than exists — dark,
   blurred, cropped, in silhouette. It may not show something *other* than what
   exists. Suppression is free; substitution is not.
3. **The provenance test**, which is core's:
   [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §8 —
   *if a viewer learned exactly how this shot was made, would they feel informed or
   deceived?*

## 7. Inheritance and enforcement

Adds to core; loosens nothing. §3's prohibition on generating the garment is
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md)
§2 item 1 applied to this genre's evidentiary object: a generated garment presented as
a real one is a fabricated artefact of exactly the kind that clause prohibits, and it
is this pack's counterpart to documentary's fabricated archival photograph and
[product-marketing](../product-marketing/06_product_depiction.md) §1's rendered
interface. Provenance on every asset, rights cleared **including music and fonts**, and
captions on every deliverable are inherited unchanged
([README.md](README.md) § Constraints inherited from core).

| Standard | Gate | Mechanism |
|---|---|---|
| §2 | Line opening | `reference_capture_workflow_established`; a line does not open without it |
| §2, §5 | `garment_verification` | Every garment in a deliverable has a locked record with a complete reference capture |
| §3 | `picture_audio_lock` | No garment asset carries generative provenance; [pack.yaml](pack.yaml) requires `reference_capture` on any prompt card touching a garment |
| §4 | `garment_verification` | Five-property comparison on the graded frame, on every deliverable variant |
| §6 | `stakeholder_approval` | Designer signs that the depiction represents the object |
| §6 material claims | Escalation | Routed to [product-marketing](../product-marketing/05_claim_substantiation.md) §10 or out of scope |

Checklists: [../../ops/checklists/](../../ops/checklists/). Gate definitions: [gates.yaml](gates.yaml).
