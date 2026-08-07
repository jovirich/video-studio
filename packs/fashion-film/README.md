# Canon pack — fashion-film

For **fashion, beauty, and lifestyle film**: lookbooks, campaign films, runway
coverage, editorial motion, product-in-context, designer profiles.

## The problem this pack is shaped around

Fashion film's characteristic failure is not factual — it is **representational and
attributive**.

Four specific hazards, all of which generative tooling makes worse:

1. **The synthetic model question.** A generated human body used to sell a physical
   garment is a claim about how that garment fits a real person. It is also, in
   several jurisdictions, an emerging disclosure obligation. This pack requires an
   explicit studio-level decision and an on-screen disclosure — it does not let the
   choice be made shot by shot in the edit.
2. **Body representation.** Generative models carry strong, narrow priors about
   bodies. Left unmanaged they will produce a single body type, a narrow skin-tone
   range, and impossible proportions, and the output will look like a deliberate
   editorial position because it is one.
3. **Design attribution and appropriation.** Fashion draws on traditions.
   Reproducing a cultural textile, motif, or garment form without attribution or
   agreement is the field's most reliable source of justified anger, and a model will
   generate one on request without knowing what it is.
4. **The garment must be real.** If a generated image shows a drape, a texture, or a
   finish the actual garment does not have, that is a false product claim wearing an
   editorial coat.

## Documents

| # | Document | Governs |
|---|---|---|
| 05 | [Garment fidelity](05_garment_fidelity.md) | The physical garment is the ground truth; what may and may not be generated |
| 06 | [Body and representation](06_body_and_representation.md) | Model casting, synthetic bodies, range, retouching limits |
| 07 | [Design attribution](07_design_attribution.md) | Cultural sources, collaborating artisans, credit and agreement |
| 08 | [Editorial visual language](08_editorial_visual_language.md) | Look, movement, styling coherence, campaign systems |

00–04 are [core's](../../core/).

## Gates — six

| Gate | Owner | Certifies |
|---|---|---|
| Brief approval | Showrunner | Collection, message, and season are agreed |
| Garment verification | Visual Director | Every garment shown exists and is depicted accurately |
| Representation review | Cultural Advisor | Casting range, body treatment, and attribution clear |
| Stakeholder approval | Showrunner | Designer and brand have signed this cut |
| Picture + audio lock | Visual Director | The cut is final; specs met |
| Technical QC | Pipeline Engineer | Core's universal gate |

Full definitions: [gates.yaml](gates.yaml).

## Non-negotiables in this pack

- **The garment is ground truth.** Every garment appearing in a deliverable is
  photographed or filmed as it physically exists, at least once, and generated
  imagery is checked against that reference. Colour, texture, drape, closure, and
  finish must match.
- **Synthetic humans are disclosed on screen**, not only in metadata, where they
  appear in commercial fashion content. This is a studio-level decision made once,
  recorded in `studio.yaml`, and applied uniformly.
- **No generated body is presented as a specific real model**, and no real model's
  likeness is generated beyond the scope of their contract. Model contracts must
  explicitly cover AI processing and generation, or they do not cover it.
- **Retouching that changes body shape** is logged as a post-process step like any
  other alteration, and is subject to whatever the studio's disclosure policy states.

## What this pack deliberately does not cover

- **Product claims about performance** — waterproofing, durability, material
  composition. Those need [product-marketing](../product-marketing/)'s substantiation
  gate.
- **Historical costume documentary.** Use [documentary-history](../documentary-history/).
- **Sponsored and influencer content**, which carries its own disclosure regime.

## Constraints inherited from core

Unchanged: no unconsented likeness, provenance on every asset, rights cleared —
**including the music, which fashion film routinely gets wrong** — captions, human
gates.

## Adopting

```yaml
# studios/<code>/studio.yaml
pack: fashion-film
pack_version: "0.1.0"
```
