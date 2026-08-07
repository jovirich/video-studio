# Prompt library

Platform-level. Every studio and every canon pack uses this library; nothing here
names a studio or a subject.

## The central idea

**A prompt is a record, not a string.**

A prompt kept as text in a doc is unversioned, unreviewable, unattributable, and
non-inheritable. For a platform whose defining guarantee is provenance, that is
disqualifying. So every generation is specified by a **prompt card** — a YAML record
validated against
[prompt_card.schema.json](../standards/schemas/prompt_card.schema.json) — and the
vendor string is *rendered* from it, never hand-written.

```
   line style block  ──┐
   sequence style    ──┼──►  PROMPT CARD  ──► render ──► vendor-specific string
   style anchors     ──┘      (the record)                 (disposable output)
                                   │
                                   ├──► sensitivity review, before generation
                                   ├──► evidence basis, if it depicts reconstruction
                                   └──► runs[]: seed, outcome, cost, what was learned
```

Rationale: [ADR 0003](../docs/decisions/0003-prompt-cards.md).

## Layout

```
prompts/
├── _framework/      how to write a card; parameters; negatives; seeds; evaluation
├── chains/          multi-tool recipes (still → upscale → motion → grade)
├── image/           midjourney flux stable-diffusion ideogram firefly imagen
│                    dall-e recraft leonardo
├── video/           runway kling veo sora luma pika hailuo wan seedance higgsfield
├── audio/           elevenlabs suno udio resemble adobe-podcast murf
├── text/            claude gpt gemini llama perplexity
├── scene3d/         blender houdini gaussian-splatting tripo meshy unreal
├── restoration/     topaz magnific krea adobe
├── performance/     hedra heygen synclabs runway-act
└── post/            resolve premiere after-effects descript capcut
```

Each modality folder has a README covering the craft that is common across its
vendors and a comparison table. Each vendor folder has a cheat sheet: what it is good
at, what it fails at, its parameters, and its terms-check status.

## Rules

1. **Cards are versioned, never overwritten.** Bump the version; record what changed
   and why. The point is a library that improves, not one that accumulates.
2. **Style is inherited, not retyped.** A card takes its `style_block` from its
   sequence, which takes it from its line. Every override carries a stated reason.
3. **`runs[]` is append-only, and the `notes` field is the valuable part.** "Why it
   worked or did not" is the only thing that compounds across a season. A card with
   an empty runs history is paperwork.
4. **Terms before tokens.** A vendor's `terms_checked` date must be current in
   [rights/permissions/model_terms_register.md](../rights/permissions/model_terms_register.md)
   before a card targeting it is generated from. A tool whose licence does not permit
   commercial use does not enter the pipeline, however good it is.
5. **No card generates without its provenance destination.** The manifest entry is
   created by the same run that creates the asset. There is no path that produces an
   untracked file.
6. **`raw_override` is a last resort and is measured.** Every use marks a place the
   abstraction did not fit. A rising override rate means the structure is wrong, not
   that the users are.

## Prohibited, at platform level

No card, in any modality, for any studio, may:

- generate material intended or likely to be taken for genuine archival evidence,
- synthesise a real person's likeness or voice without a clearance reference,
- imitate a living artist or a named cultural custodian's work without agreement,
- run autonomously into a published deliverable.

Full text: [core/01 §2](../core/01_provenance_and_ai_disclosure.md). A canon pack may
add prohibitions; none may remove these.

## Writing a card

```bash
# NOT BUILT — these commands do not exist yet. See docs/status.md.
python -m studio_ops new-prompt --line <line> --shot SHT-XX-S01E01-0042 \
  --modality image --vendor midjourney
```

Then read [_framework/prompt_anatomy.md](_framework/prompt_anatomy.md). The single
most consequential field is `period_markers` — concrete material detail is what
prevents a model's strong prior toward generic, placeless output.

## Rendering and running

```bash
# NOT BUILT — these commands do not exist yet. See docs/status.md.
python -m studio_ops promptlib render --card PC-NG-S01E01-0037
python -m studio_ops promptlib render --card PC-NG-S01E01-0037 --vendor flux
python -m studio_ops promptlib run    --card PC-NG-S01E01-0037 --dry-run
```

`render` targets a different vendor from the same card — that portability is the
main practical payoff of the structure. `run` is gated by
`GENERATION_BUDGET_USD_PER_EPISODE` and defaults to `--dry-run`.

## Maintaining the library

Vendors change models, parameters, and terms frequently — often without notice.
Cheat sheets carry a `checked` date. A sheet older than 90 days is flagged by
`studio_ops validate --prompts` as stale. Stale is a warning, not a failure; silently *(NOT BUILT)*
wrong is the thing to avoid.
