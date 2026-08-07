# Core canon

Rules that hold for **every** production this platform makes, regardless of genre,
studio, or subject. A history documentary, a brand film, a narrative short, and a
technical explainer are all bound by these and by nothing else at platform level.

The test for whether something belongs here: *would this rule still be right for a
production with no historical claims in it at all?* If not, it belongs in a
[canon pack](../packs), not in core.

## Documents

| # | Document | Governs |
|---|---|---|
| 00 | [Platform charter](00_platform_charter.md) | What the platform is, the tier model, what core does and does not decide |
| 01 | [Provenance and AI disclosure](01_provenance_and_ai_disclosure.md) | What may be generated, how it is labelled, what is prohibited outright |
| 02 | [Rights and licensing](02_rights_and_licensing.md) | Clearance, model terms, chain of title, attribution |
| 03 | [Distribution and formats](03_distribution_and_formats.md) | Masters, aspect ratios, versioning, archive |
| 04 | [Review gate framework](04_review_gate_framework.md) | How gates work. *Which* gates a production has comes from its pack. |
| 05 | [Amendment log](05_amendment_log.md) | Every change to core or to any pack |

Terminology for the whole platform is in [../docs/glossary.md](../docs/glossary.md).

## What core deliberately does not decide

These vary by genre and are therefore a pack's business, never core's:

- Whether factual claims require source records, and to what standard
- Narrative structure and voice
- Visual and sonic language
- Cultural sensitivity procedure and advisory authority
- Language, naming, and localisation policy
- Which review gates exist, and who owns them

A brand film has no fact-check gate. A history documentary cannot ship without one.
Core does not pretend otherwise — it defines what a gate *is* and lets the pack say
which ones apply.

## Precedence

```
core  >  pack  >  studio bible  >  line addendum  >  production
```

A lower layer may **add** constraints and may **tighten** an upper layer's rule. It
may never loosen one. A pack that wanted to permit something core prohibits would
have to amend core, with core's signatures — which is the point.

Where a lower layer needs an exemption, it is recorded in
[05_amendment_log.md](05_amendment_log.md) with a rationale, or it does not exist.

## Enforcement

- **By people** — the gate framework in [04_review_gate_framework.md](04_review_gate_framework.md).
- **By machine** — [../standards/](../standards) encodes the checkable subset;
  `studio_ops validate --canon` fails a build on prohibited patterns.
- **By structure** — a production cannot exist outside a line, a line outside a
  studio, or a studio without a declared pack. The scaffolder will not create one.

## Amending core

Highest bar on the platform. Requires the Platform Owner plus the responsible role
for the section, plus **an impact statement naming every studio affected**. A core
change lands on every production in flight.

Procedure in [05_amendment_log.md](05_amendment_log.md).
