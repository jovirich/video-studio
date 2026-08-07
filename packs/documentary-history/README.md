# Canon pack — documentary-history

For **historical documentary made with heavy generative assistance**: work whose
factual claims are answerable to evidence, whose imagery is largely reconstructed
because no archival footage exists, and whose subject matter frequently belongs to
living communities.

Adopted by: [African History Studio](../../studios/african-history).

## The problem this pack is shaped around

A documentary made with generative tools has one specific failure mode: **the imagery
is cheap and the truth is expensive.** Left unmanaged, output volume outruns
verification and the show quietly becomes fiction with a serious voiceover.

Everything in this pack is aimed at making that failure structurally hard:

- Facts live in **claim records**, not in scripts. A script references a claim ID;
  it does not assert on its own authority.
- Prompts are **reviewable before generation**, because once a striking image exists
  the argument about whether it should exist is much harder to win.
- **Uncertainty is a first-class recordable state**, so nobody is tempted to fill a
  gap with something plausible.
- The **advisory hold** is the one authority the Showrunner cannot override.

## Documents

| # | Document | Governs |
|---|---|---|
| 01 | [Editorial standards](01_editorial_standards.md) | Accuracy, certainty registers, attribution, corrections |
| 02 | [Evidence and sourcing](02_evidence_and_sourcing.md) | Claims, source tiers, corroboration, the claim ID chain |
| 03 | [Narrative doctrine](03_narrative_doctrine.md) | Structure, voice, uncertainty as content, reconstruction |
| 04 | [Visual language](04_visual_language.md) | Look, camera grammar, provenance classes, generated-image QC |
| 05 | [Sound and score](05_sound_and_score.md) | VO, music policy, ambience as reconstruction, mix |
| 07 | [Cultural sensitivity](07_cultural_sensitivity.md) | Sacred material, representation, advisory authority |
| 09 | [Localization](09_localization.md) | Language, orthography, naming, pronunciation, captions |

Numbering has gaps because 00, 06, 08, and 10 are core's
([charter](../../core/00_platform_charter.md),
[provenance and AI disclosure](../../core/01_provenance_and_ai_disclosure.md),
[rights](../../core/02_rights_and_licensing.md),
[distribution](../../core/03_distribution_and_formats.md)). The gaps are kept so the
numbers stay stable if a document moves between layers.

## Working method

| Path | What it holds |
|---|---|
| [methodology/](methodology) | Research protocol, bias register, oral history protocol, AI-in-research rules |
| [sourcing/](sourcing) | How the source and claim registry works |
| [`ops/checklists/`](../../ops/checklists) | The gate checklists. They live at platform level, not in this pack: `technical_qc` and `rights` are required by core in *every* pack, and four copies would diverge quietly, leaving no single body to verify a platform guarantee against. |
| [gates.yaml](gates.yaml) | The nine-gate set |

Registers of actual records — sources, claims, questions, entities — live at the
**line** level, because they are line-scoped. This folder holds only method.

## The nine gates

| Gate | Owner | Certifies |
|---|---|---|
| Greenlight | Showrunner | The question is worth asking and is within advisory coverage |
| Source lock | Research Lead | The research pack is complete and independence-checked |
| Script lock | Story Producer | The script is final and every fact carries a claim ID |
| Fact-check | Research Lead | Every claim resolves at its required tier |
| Sensitivity | Cultural Advisor | Premise, prompts, and cut clear cultural review |
| Rights | Rights & Clearances | Nothing is `pending` |
| Picture lock | Visual Director | The cut is final; anachronism and label checks pass |
| Audio lock | Audio Lead | Mix, pronunciation, and stems are correct |
| Technical QC | Pipeline Engineer | Specs met, provenance complete, package assembled |

Full definitions in [gates.yaml](gates.yaml). Framework in
[core/04](../../core/04_review_gate_framework.md).

## What this pack deliberately does not cover

- **Fiction and dramatisation as a primary mode.** Reconstruction here is always
  subordinate to evidence. A pack for narrative work would invert that.
- **Contemporary journalism.** Right-of-reply, live subjects, and legal risk around
  ongoing events need rules this pack does not contain.
- **Client approval workflows.** No commissioning-client gate exists.

If a production needs any of those, it needs a different pack — not an exemption
from this one.

## Adopting this pack

```yaml
# studios/<code>/studio.yaml
pack: documentary-history
pack_version: "0.1.0"
```

Then satisfy the line-opening conditions in
[07_cultural_sensitivity.md](07_cultural_sensitivity.md) §5 before greenlighting
anything.
