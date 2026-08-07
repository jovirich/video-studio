# Canon pack — product-marketing

For **video about a product, service, or company you control**: launch films, feature
explainers, onboarding and how-to, case studies, app demos, campaign cutdowns.

Suitable for studios like `giftinz` or `mytenant` — a product line's own video output.

## The problem this pack is shaped around

Marketing video fails in a different direction from documentary. The risk is not
inventing history; it is **claiming something about the product that is not true, or
not true yet.**

That failure has teeth documentary's does not: a false product claim is a regulatory
and contractual exposure, not only a credibility one. And the specific hazard of
generative tooling here is that it makes it trivially easy to show a UI, a result, or
a use case that **does not exist** — a screen that was rendered rather than captured,
a metric that was invented to fill a slot in the edit.

So this pack inverts documentary's emphasis:

- **Product claims are gated, everything else is not.** No source registry for the
  atmosphere shots. A hard gate on anything asserting what the product does.
- **Any depiction of the product's interface must be captured, not generated.**
  A rendered UI is the marketing equivalent of a fabricated archival photograph.
- **A client/stakeholder approval gate exists**, which documentary deliberately lacks.
- **Roadmap language is controlled.** "Coming soon" is a commitment someone has to
  keep.

## Documents

| # | Document | Governs |
|---|---|---|
| 05 | [Claim substantiation](05_claim_substantiation.md) | What may be asserted about the product, and what evidence backs it |
| 06 | [Product depiction](06_product_depiction.md) | UI capture rules, mockups, results, testimonials |
| 07 | [Brand and message discipline](07_brand_and_message.md) | Voice, positioning, competitor references, disclaimers |
| 08 | [Narrative patterns](08_narrative_patterns.md) | Structures that work for launch, explainer, case study, demo |

00–04 are [core's](../../core/). This pack is intentionally small — most of what
marketing video needs is already in core (provenance, rights, delivery,
accessibility), and adding ceremony beyond that slows a team down without protecting
anything.

## Gates — five, not nine

| Gate | Owner | Certifies |
|---|---|---|
| Brief approval | Showrunner | Audience, message, and success measure are agreed |
| Claim substantiation | Rights & Clearances | Every product claim is substantiated and evidenced |
| Stakeholder approval | Showrunner | Product/legal/brand owners have signed the cut |
| Picture + audio lock | Visual Director | The cut is final and specs are met |
| Technical QC | Pipeline Engineer | Provenance, rights, captions, package — core's universal gate |

Full definitions: [gates.yaml](gates.yaml).

## What this pack deliberately does not cover

- **Third-party or competitor products.** Comparative advertising carries
  jurisdiction-specific rules this pack does not contain. Escalate.
- **Regulated categories** — financial products, health claims, children's
  advertising. These need legal review beyond a checklist.
- **Historical or factual content about the world.** If a product video makes claims
  about history, economics, or society, those claims need
  [documentary-history](../documentary-history/)'s evidence chain, not this pack's.
- **Paid media compliance** — platform ad policies, disclosure of sponsorship.
  Handled at distribution, not here.

## Constraints inherited from core

Unchanged and not loosenable: no fabricated evidence, no unconsented likeness or
voice, provenance on every asset, nothing ships `pending` on rights, captions on
every deliverable, a human signs every gate.

Note what that means in practice here: **a generated "customer" testimonial is
prohibited.** Synthesising a person who appears to endorse the product is
fabricated evidence under core §2, whatever the marketing convention.

## Adopting

```yaml
# studios/giftinz/studio.yaml
pack: product-marketing
pack_version: "0.1.0"
```
