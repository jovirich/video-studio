---
doc: bible/10
title: Distribution and formats
status: template
version: 0.1.0
owners: [showrunner, pipeline-engineer]
---

# 10 — Distribution and formats

> **Fill state.** Platform choices are `TBD — Showrunner`. The format discipline
> below applies whatever is chosen, and the technical numbers are in
> [../standards/delivery_specs.md](../standards/delivery_specs.md), which is the
> authoritative machine-checked version.

## 1. Product tiers

| Tier | Runtime | Purpose |
|---|---|---|
| **Feature** | 60–90 min | Season capstone or standalone. `TBD if in scope.` |
| **Episode** | 22–45 min | The core unit. Target runtime `TBD` — pick one and hold it; variable runtimes hurt both scheduling and audience habit. |
| **Short** | 6–12 min | Single-question pieces. Uses the same evidence chain and the same gates. |
| **Vertical cutdown** | 30–90 s | Derived from a locked episode only. Never original claims. |
| **Trailer** | 60–120 s | Derived from locked material only. |

**Cutdowns are derived, never original.** A short-form piece that makes a claim not
present in a gated episode has bypassed the entire review system. If a short deserves
to exist on its own, it goes through the gates on its own.

## 2. Masters

Deliver and archive:

| Master | Spec |
|---|---|
| Archival master | UHD 3840×2160, ProRes 422 HQ or better, 24p, Rec.709, full mix + all stems, no burnt-in text |
| Textless master | Same, without on-screen text, for localisation |
| Web master | H.264/H.265 UHD and 1080p, −14 LUFS |
| Caption files | SRT + VTT, per language |
| Stems | VO, testimony, music, ambience, SFX, M&E |
| Provenance manifest | `manifest.yaml` for the episode |
| Chain of title | Assembled per [08_rights_and_licensing.md](08_rights_and_licensing.md) §8 |

Masters live in the asset store, not in git. Path convention in
[../docs/runbook/asset_storage.md](../docs/runbook/asset_storage.md).

## 3. Aspect ratios

- 16:9 is primary. All framing decisions are made in 16:9.
- Every shot is composed with a **9:16 and 1:1 safe zone** marked in the storyboard
  so vertical cutdowns are a crop, not a re-generation. Generating a second vertical
  version of a shot doubles cost and guarantees continuity drift.
- The storyboard template carries the safe-area overlay.

## 4. Titles, thumbnails, descriptions

- Titles state the subject honestly. Curiosity gaps are permitted; misdirection is
  not. A title implying a claim the episode does not make is an accuracy failure
  under [01_editorial_standards.md](01_editorial_standards.md) §1.
- Thumbnails follow the system in [../brand/thumbnail_system.md](../brand/thumbnail_system.md).
  **A thumbnail using generated imagery carries the same honesty standard as the
  episode** — it may not depict something the episode shows to be false, and it may
  not be presented as a photograph.
- Descriptions carry: the question, the sources summary link, the AI-use statement,
  the correction notice if any, and the credits link.
- Chapters generated from the beat sheet by `studio_ops report chapters`.

## 5. The published evidence layer

Each episode publishes, alongside the video:
- a **sources page** (bibliography from the claim chain),
- a **provenance summary** (which shots were generated, with what),
- a **corrections log** (empty at launch, append-only after).

This is generated, not written by hand, from records that already exist. It costs
almost nothing and is the studio's primary differentiator against the large volume of
unsourced history content the audience will otherwise compare it to.

## 6. Versioning and re-cuts

- Published episodes are versioned `v1`, `v2`, … A re-cut that changes a claim
  increments the version, updates the corrections log, and states the change in the
  description.
- Silent replacement of a published file is prohibited.
- The superseded master is retained.

## 7. Platform variants

`TBD.` For each platform, record: max runtime, aspect requirements, caption format,
loudness target, monetisation restrictions relevant to the subject matter (historical
violence and colonial content are routinely demonetised or age-gated — plan for it
rather than being surprised), and whether Content Credentials survive upload.

## 8. Archive and preservation

- Everything required to rebuild an episode — project files, source media,
  manifests, prompt cards, LUTs, fonts — is archived together per episode.
- Two copies, two locations, one offline. Verified annually.
- A README in each archive package explaining how to rebuild, written for someone who
  was not there.
