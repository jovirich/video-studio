---
doc: packs/product-marketing/07
title: Brand and message discipline
status: template
version: 0.1.0
updated: 2026-08-07
owners: [showrunner]
---

# 07 — Brand and message discipline

> **Fill state.** The *rules* below are pack canon. The *system* — faces, palette,
> logo behaviour, motion signature — is `TBD` per studio and is specified in that
> studio's `brand/` folder. A pack that shipped a house style would be prescribing
> the one thing a brand cannot inherit.

## 1. Brand system

`studio_must_decide: brand_system` — [pack.yaml](pack.yaml). A studio cannot
greenlight its first production until this section is answered in its own
`brand/` folder and referenced from `studio.yaml`.

Marketing video is produced in volume, in parallel, under deadline, by people who
did not all attend the same conversation. Coherence therefore cannot come from taste;
it has to come from a specified system that a prompt card, an editor, and a freelancer
can each inherit without asking. The mechanism is the same three-layer inheritance
that [documentary-history](../documentary-history/04_visual_language.md) §1 uses for
look: a written system, versioned anchors, and prompt inheritance from
[../../prompts/README.md](../../prompts/README.md).

What the studio specifies, before its first brief:

| Element | Must state | What breaks without it |
|---|---|---|
| **Typography** | Display face, text face, UI face if different; weights in use; licence tier covering broadcast and streaming and the number of seats; **full diacritic and script coverage for every language the studio ships in** | Font licensing is the most common late-stage delivery failure in this genre, and coverage gaps are discovered at localisation, after the design is locked. Choose before designing — coverage eliminates most faces. |
| **Colour** | Primary, secondary, one accent reserved for a named function (usually the call to action); the exact values; the working and delivery colour spaces per [../../standards/delivery_specs.md](../../standards/delivery_specs.md) | An accent used decoratively stops meaning anything, and the call to action stops being findable. |
| **Contrast and legibility** | Minimum contrast ratio for text over image, minimum type size at the smallest delivery format, safe areas per platform | Core guarantees accessibility ([../../core/00_platform_charter.md](../../core/00_platform_charter.md) §5 item 6). Text that is legible on a grading monitor and not on a phone fails it. |
| **Logo** | Clear space, minimum size, permitted lockups and backgrounds, what is prohibited (stretching, recolouring, effects), whether animation is permitted and which | Every prohibition here exists because someone did it. |
| **Motion signature** | Timing curves, transition vocabulary, the two or three moves that are the studio's, entrance and exit behaviour for type and UI | Motion is the fastest-read brand cue and the least often specified. Without it, generated and edited material drift apart within one campaign. |
| **Sonic signature** | Whether there is an audio mnemonic; music direction; whether generated music is permitted and for what | Rights on music are cleared or the piece does not ship ([../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §2). |
| **Interface presentation** | How captured UI is framed: device frames, browser chrome, scale, background treatment | Inconsistency here reads as several different products. |
| **Style anchors** | A fixed, versioned set of reference frames per piece type, in [../../library/style_refs/](../../library/style_refs/), referenced by ID from every prompt card | "Match the brand" is not a specification a generative tool can act on. A checksummed file is. |

**Each element is a file, not a habit.** The rule this section actually enforces:
anything on that table which exists only in someone's head is undefined, and the gate
treats undefined as unmet.

## 2. Voice

The studio's voice is `TBD` and specified in its `brand/` folder. What the pack
requires of any voice it specifies:

- **A stated person and tense**, applied consistently. Second person ("you can…")
  and third ("teams can…") make different promises about who is being addressed.
- **A stated relationship to the product's own interface copy.** A film that speaks
  differently from the product it depicts feels like a film about a different product.
- **Named prohibitions, not just aspirations.** "Confident, human, clear" describes
  nothing. A prohibited-language list does work:
  [../../standards/prohibited_language.md](../../standards/prohibited_language.md)
  holds the platform-wide list; a studio adds its own.
- **Superlatives are claims.** "The fastest", "the only", "the first", "the best" are
  factual assertions and are validated as such under
  [05_claim_substantiation.md](05_claim_substantiation.md) §2. This is the single
  most common route by which a brand voice decision becomes a substantiation problem:
  nobody thinks of a tagline as a claim.
- **Intensifiers are load-bearing.** "Instantly", "effortlessly", "seamlessly",
  "automatically" each assert something measurable about how the product behaves.
  Treat them as performance claims or cut them.

## 3. Positioning and message discipline

The `brief_approval` gate ([gates.yaml](gates.yaml)) certifies that the piece has one
job stated in one sentence. This section is what that sentence is held against.

| Requirement | Rule |
|---|---|
| **One core message per piece** | Recorded on the production record — [pack.yaml](pack.yaml) requires `core_message`, `audience`, `call_to_action`, `success_measure`. A piece with three messages communicates none; the second and third are a different piece. |
| **The audience is a person, not a segment** | "Operations leads at companies migrating off spreadsheets" is workable. "SMBs" is not, and produces a film addressed to nobody. |
| **The call to action is single and achievable** | One action, available to the audience the piece names, on the platforms it will run on. |
| **The success measure is agreed before production** | Otherwise the piece is judged after the fact against whatever it happened to achieve, and nothing is learned. |
| **Positioning is inherited, not invented per piece** | Positioning belongs to the studio and lives in `brand/`. A film that repositions the product mid-campaign is a decision requiring the product owner, not an edit. |

**The message is not a claim, and the boundary is thin.** "Built for teams who move
fast" is positioning. "Cuts your release cycle in half" is a claim. The brief gate
routes anything on the wrong side of that line to
[05_claim_substantiation.md](05_claim_substantiation.md) before the script is written,
because discovering it at the substantiation gate means re-cutting.

## 4. Competitor and third-party references

**This pack does not contain a rule for comparative advertising, and does not try to.**

What may be said about a named competitor, what must be substantiated and to what
standard, whether their mark may be shown, how the comparison must be constructed,
and what the remedy is when it is wrong are **jurisdiction-specific**, differ
materially between territories, and change. A pack-level rule here would be
confidently wrong in most of the distribution footprint.

**Escalate.** Specifically:

| Situation | Route |
|---|---|
| Naming a competitor | Legal reviewer named under [05_claim_substantiation.md](05_claim_substantiation.md) §3, for **every territory in the footprint**, before scripting |
| Showing a competitor's mark, product, or interface | As above, plus rights review — depicting is separate from naming |
| An unnamed but identifiable competitor | As above. Identifiable is the same as named for most purposes, and sometimes worse |
| "The old way", generic incumbents, a category rather than a company | Still a comparison claim under [05_claim_substantiation.md](05_claim_substantiation.md) §8; evidence still required |
| A partner's or integration's mark | Permission to name, permission to depict, and permission to imply endorsement are three separate permissions. Record all three or use none |
| A customer's mark in a case study | [06_product_depiction.md](06_product_depiction.md) §6 |

Two rules the pack does state, because they hold everywhere:

1. **Never depict a competitor's product using generated imagery.** The interface
   prohibition at [06_product_depiction.md](06_product_depiction.md) §1 applies with
   more force to somebody else's product than to your own — you are fabricating
   evidence about a third party who will notice.
2. **Never show a competitor's product performing worse than it does.** Degrading a
   comparison by configuration, version, or capture conditions is fabricated evidence
   under [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2 item 1,
   whatever the local comparative-advertising rules permit.

## 5. Disclaimers and on-screen qualifiers

A disclaimer is a repair for a claim the film has already made. It works only if the
audience can actually read it.

| Requirement | Rule |
|---|---|
| **Proximity** | The qualifier appears with the claim it qualifies, not in an end card. A viewer who sees the claim and not the qualifier has been told the unqualified claim. |
| **Legibility** | Same minimum contrast and type size as any other on-screen text (§1). A qualifier set below the studio's own legibility floor is decorative. |
| **Dwell** | On screen long enough to read at the reading speed the studio specifies. TBD — the studio sets a words-per-second floor and applies it uniformly. |
| **Survives the cutdown** | Qualifiers are checked on **every deliverable variant**, not the master. A qualifier that fits in 16:9 and is cropped out of 9:16 has silently removed itself from the version most people will see. This is the most common real failure of this section. |
| **Survives mute** | Where a qualifier exists only in voiceover, it does not exist. Autoplay is muted on most surfaces. |
| **Not a substitute** | A disclaimer does not rescue an unsubstantiated claim. If the claim needs a paragraph to be true, the claim is wrong; change the claim. |
| **Captioned** | Core requires captions on every deliverable. Spoken qualifiers appear in them. |

Legally mandated disclaimer content — what must be said, in what words, at what size —
is **jurisdiction- and category-specific**. This pack states the craft floor above and
nothing about the legal one. **Escalate** to the legal reviewer for the categories at
[05_claim_substantiation.md](05_claim_substantiation.md) §10.

## 6. Asset versioning

Brand assets change, and a marketing library outlives the version of the brand it was
made under. Without versioning, the studio finds out which pieces are stale by seeing
one of them.

- **Every brand asset is versioned numerically and immutably.** `_v01`, `_v02`, per
  [../../standards/naming_conventions.md](../../standards/naming_conventions.md).
  Words like `final`, `new`, and `latest` are refused by
  `studio_ops validate --naming`, which is the point.
- **A production records the asset versions it used**, on the production record. This
  is what makes "which pieces are running the old logo?" a query rather than a review
  session.
- **`brand_assets_current` is a line-opening condition** ([pack.yaml](pack.yaml)).
  A line does not open against a brand system nobody has checked this quarter.
- **A brand change does not silently invalidate delivered work.** When a version
  supersedes another, the superseding record lists what is affected and the studio
  decides, explicitly, per asset: re-cut, retire, or leave. Deciding nothing means
  leaving, and leaving should be a decision someone made.
- **Derived variants inherit their master's version.** A cutdown carries the version
  of the master it came from; re-mastering a cutdown against new brand without
  re-mastering its siblings is how a campaign ends up in two brands at once.
- **Claim expiry and asset versioning are the same mechanism.** The `used_in` field on
  a `product_claim` ([05_claim_substantiation.md](05_claim_substantiation.md) §9) and
  the asset version list answer the same question — *what do we have to touch?* Keep
  them in one place per line, or they will disagree.

## 7. Inheritance and enforcement

Adds to core; loosens nothing. Inherits without modification: accessibility and
legibility guarantees ([../../core/00_platform_charter.md](../../core/00_platform_charter.md) §5),
the prohibitions at
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2 —
which §4 rule 2 above tightens rather than restates — font, music, and asset clearance
([../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §2),
and delivery specification ([../../core/03_distribution_and_formats.md](../../core/03_distribution_and_formats.md)).

| Standard | Gate | Mechanism |
|---|---|---|
| §1 | Greenlight | Studio cannot greenlight with `brand_system` unresolved |
| §2, §3 | `brief_approval` | One message, one audience, one call to action, one success measure on the production record |
| §2 superlatives | `claim_substantiation` | Superlatives resolve to `product_claim` records |
| §4 | `stakeholder_approval` | Legal ruling on file for any third-party reference |
| §5 | `picture_audio_lock` | Qualifiers checked on every deliverable variant, not the master |
| §6 | `technical_qc` | Asset versions recorded; `validate --naming` refuses non-numeric version markers |

Checklists: [../../ops/checklists/](../../ops/checklists/). Gate definitions: [gates.yaml](gates.yaml).
