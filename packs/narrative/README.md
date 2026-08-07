# Canon pack — narrative

For **story-driven work where the depiction is the point**: original fiction,
adaptation, scripture-based and mythological narrative, dramatised anthology,
animated storytelling.

Suitable for studios like a biblical narrative line, a folklore series, or an
original fiction anthology.

## The problem this pack is shaped around

Documentary's failure is inventing history. Narrative's is the opposite: **it is
supposed to invent, so nothing internal stops it drifting into incoherence,
disrespect, or a claim it never meant to make.**

Three specific hazards:

1. **Continuity collapse.** Generative tools have no memory. Across 300 shots a
   character's face, a location's geography, and a world's rules will drift unless
   something external holds them. Documentary handles this with entity records; here
   it is the whole job.
2. **The adaptation boundary.** Work drawn from scripture, epic, or living
   tradition is *interpretation*, and audiences who hold that text will read every
   choice as a claim about it. The pack requires the interpretive stance to be
   declared up front rather than discovered in the comments.
3. **Accidental factual assertion.** A narrative piece set in a real time and place
   makes implicit claims about it. Where the setting is real, this pack borrows
   documentary's evidence chain for the setting alone — not for the plot.

## Documents

| # | Document | Governs |
|---|---|---|
| 05 | [Story bible framework](05_story_bible.md) | World rules, character canon, continuity ledger |
| 06 | [Adaptation and source texts](06_adaptation.md) | Interpretive stance, textual fidelity, variant traditions, respect obligations |
| 07 | [Visual continuity](07_visual_continuity.md) | Character anchors, location anchors, drift detection, shot-to-shot coherence |
| 08 | [Performance and voice](08_performance_and_voice.md) | Casting, synthetic performance limits, direction |
| 09 | [Setting fidelity](09_setting_fidelity.md) | When a real time and place is depicted, what must be evidenced |

00–04 are [core's](../../core/).

## Gates — seven

| Gate | Owner | Certifies |
|---|---|---|
| Greenlight | Showrunner | The story is worth telling and the interpretive stance is declared |
| Story bible lock | Story Producer | World rules and character canon are fixed |
| Script lock | Story Producer | The script is final |
| Sensitivity | Cultural Advisor | The treatment of the source tradition and its communities clears |
| Continuity lock | Visual Director | Anchors exist for every recurring character and location |
| Picture + audio lock | Visual Director | The cut is final; no continuity break survives |
| Technical QC | Pipeline Engineer | Core's universal gate |

Full definitions: [gates.yaml](gates.yaml).

## The labelling question

Documentary labels generated imagery because the audience might otherwise take it for
evidence. **Narrative has no such risk within the work** — the audience knows it is
watching a story.

So this pack replaces per-shot reconstruction marks with a **single production-level
disclosure** in the credits and description naming the generative tools used. Core's
requirement that generated material never be *presented as* found material still
applies: a narrative piece may not include a fake newsreel, a fabricated document, or
a synthetic archival photograph presented as real, even inside a fiction.

That last point is the boundary that matters, and it is easy to cross by accident in
a "found footage" framing.

## What this pack deliberately does not cover

- **Factual documentary.** If the work asserts what actually happened, it needs
  [documentary-history](../documentary-history/).
- **Depiction of real living people** in fictionalised form. That is a legal and
  ethical question beyond a checklist. Escalate.
- **Interactive or branching narrative.**

## Constraints inherited from core

Unchanged: no fabricated evidence presented as real, no unconsented likeness or
voice — **including of historical figures** — provenance on every asset, rights
cleared, captions, human gates.

The likeness rule bites harder here than authors expect. A narrative film about a
historical figure may depict them via a cast performer; it may not synthesise their
actual face or voice.

## Adopting

```yaml
# studios/<code>/studio.yaml
pack: narrative
pack_version: "0.1.0"
```
