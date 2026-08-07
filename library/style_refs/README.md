---
title: Style references
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, pipeline-engineer]
---

# Style references

Style anchors: the fixed image files that prompt cards point at to hold a consistent
look across hundreds of independent, memoryless generations.

**Maturity: DESIGNED.** Empty. No anchor has been created, and the
[20-shot continuity test](../../docs/status.md) that would show whether this mechanism
works at all is **NOT RUN**.

## This is the strongest continuity mechanism in the pipeline

A generative model has no memory between calls. Every shot in a sequence is generated
independently, and left to itself the look drifts — not dramatically, and not in any
single shot, but cumulatively across a sequence, which is exactly where it is least
visible while it is happening and most obvious once cut together.

Prose does not fix this. A style block written in words is re-interpreted on every
call, and two calls with identical wording do not produce the same interpretation. A
seed does not fix it either: a seed reproduces one generation, not a look.

A **fixed file** does fix it, because it is the same input every time. Every vendor's
style-reference mechanism differs in strength and syntax, but they share the property
that matters: an identical file yields a consistent bias. That is the mechanism, and
it is why this folder is more load-bearing than its size suggests.

## It only works if the files never silently change

**This is the entire condition, and it is trivially easy to break.**

Re-export an anchor at a different quality. Crop it slightly. Re-save it through a tool
that re-compresses. Upscale it. Replace it with "the better version". Each of those
produces a file that is visually indistinguishable from the original and is a different
input to the model — so every shot generated after the change carries a slightly
different bias from every shot generated before it, with nothing in the record marking
where the change happened.

The result is the failure this mechanism exists to prevent, made worse by being
invisible: a sequence that drifts, in a pipeline that believes it is anchored, with a
prompt card that still cites the same `STA-*` ID.

Therefore:

1. **Every anchor has a recorded SHA-256.** It is not metadata. It is the identity of
   the anchor, and the `STA-*` ID means *the file with this hash*.
2. **An anchor is immutable once referenced.** Not "should not be edited" — cannot be.
   Its ID keeps pointing at that byte sequence forever.
3. **A change is a new anchor with a new ID.** Not a new version of the old one.
   `STA-*` IDs are permanent and never reused, per
   [../../standards/id_system.md](../../standards/id_system.md).
4. **The old anchor is retained.** Shots generated against it must remain
   reproducible — the reproducibility guarantee in
   [../../README.md](../../README.md) § Platform guarantees depends on every input
   still existing.
5. **The hash is verified before generation, not after.** A mismatch is a hard stop.
   Discovering it afterwards means re-generating everything downstream of the change,
   and it means not knowing which shots those were.

**Verification maturity: NOT BUILT.** No code checks these hashes today. Until the
prompt renderer exists, the guarantee is a convention, and conventions do not survive a
deadline.

## Identifiers

`STA-<SCOPE>-<SERIAL>`, per
[../../standards/id_system.md](../../standards/id_system.md) — scope is a line's
two-letter code or `STUDIO`. Anchors here are cross-line and therefore `STA-STUDIO-*`;
a line's own anchors live with the line, in its style folder, and are line-scoped.

Prompt cards reference the ID, never the path
([../../standards/schemas/prompt_card.schema.json](../../standards/schemas/prompt_card.schema.json)).
A card citing a path is a card that breaks when the file moves and, worse, keeps
working when the file changes.

Anchors are also referenced from a line's `visual_identity.style_anchor_set`
([../../standards/schemas/production_line.schema.json](../../standards/schemas/production_line.schema.json)),
which is how a line declares which anchors define its look.

## Naming

```
STA-<SCOPE>-<SERIAL>_<slug>.<png|jpg>

STA-STUDIO-0001_example-slug.png
```

ID first, per
[../../standards/naming_conventions.md](../../standards/naming_conventions.md) §
Documents — IDs are uppercase, the slug is kebab-case and describes **what the anchor
establishes**, not what generated it. `grain-and-halation` is right;
`mj-v7-sref-2847` is wrong: the tool, the parameters, and the seed belong in the prompt
card and the manifest, where they are queryable.

**No `_vNN` on an anchor.** This is the one place in the repository where a version
suffix is wrong, and it is wrong for the reason above: a versioned filename invites the
belief that `_v02` replaces `_v01`, and anchors are never replaced. A different anchor
is a different ID.

## Licence requirement

An anchor is an image, and it is licensed like any other image.

- **Studio-authored or generated by the studio**: a row in
  [../../rights/permissions/clearance_log.md](../../rights/permissions/clearance_log.md)
  recording that, plus — if it was generated — a manifest entry with its tool, prompt
  card, and seed, and the vendor terms row it was made under
  ([../../rights/permissions/model_terms_register.md](../../rights/permissions/model_terms_register.md)).
  An anchor generated under terms that do not permit commercial use contaminates every
  shot made from it.
- **Licensed from a third party**: the grant must permit **use as an input to a
  generative process**. This is a genuinely unsettled question in most stock licences,
  which were not written with it in mind. Where the grant is silent, escalate rather
  than assume; a silence is not a permission.
- **Never** an anchor derived from a living artist's work, or from a specific cultural
  custodian's work, without agreement. Core/01 §2 prohibits generating in the style of
  either. An anchor is the most direct possible way to do exactly that, which makes
  this folder the place the prohibition is most likely to be breached by convenience.

Every anchor carries a `CLR-STUDIO-*` row before it is placed here.

## Manifest and storage

Anchor images are gitignored ([../../.gitignore](../../.gitignore)); the manifest is
not. Per anchor: `STA-*` ID, filename, **SHA-256**, pixel dimensions, format, what the
anchor establishes in one line, origin (authored, generated, licensed), clearance ID,
the generation record if generated, the date it was locked, and the IDs of any anchor
it supersedes.

The manifest is the register of anchors. A file in the object store with no manifest
row is not an anchor — it is a picture, and nothing may reference it.
