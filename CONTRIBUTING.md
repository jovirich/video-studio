# Contributing

## Who does what

See [ops/roles.md](ops/roles.md) for the full role definitions and
[ops/raci.md](ops/raci.md) for the responsibility matrix. Short version:

| Role | Owns | Can sign off on |
|---|---|---|
| Showrunner | Slate, episode greenlight, final cut | Everything |
| Research Lead | Source records, claim IDs, open questions | Fact-check gate |
| Story Producer | Briefs, outlines, beat sheets, narration | Script lock |
| Visual Director | Visual language, prompt cards, look consistency | Picture lock |
| Audio Lead | VO, score, mix, loudness | Audio lock |
| Rights & Clearances | Permissions, licences, archival use | Rights gate |
| Cultural Advisor | Sensitivity, language, representation | Sensitivity gate |
| Pipeline Engineer | `studio_ops`, schemas, CI, provenance ledger | Technical QC |

No person signs two gates on the same episode. That is the point of having gates.

## Branching

```
main                     protected; only merges from release/*
release/s01e01           episode integration branch
  ├── research/s01e01-<topic>
  ├── script/s01e01-<pass>
  ├── prompt/s01e01-<sequence>
  ├── edit/s01e01-<version>
  └── fix/<short-description>
studio/<area>            changes to studio-level infrastructure (bible, schemas,
                         prompts, automation) — never on an episode branch
```

A change to studio-level canon **never** rides along in an episode PR. If your
episode work exposes a problem in the Bible or the schemas, open a separate
`studio/*` PR and link it. Canon changes get their own review.

## Pull request gates

Every PR runs [.github/workflows/validate.yml](.github/workflows/validate.yml):

1. `studio_ops validate schemas` — front matter and YAML/JSON records match
   [standards/schemas/](standards/schemas).
2. `studio_ops validate naming` — file and asset names match
   [standards/naming_conventions.md](standards/naming_conventions.md).
3. `studio_ops validate links` — no dead internal links, no orphan records.
4. `studio_ops validate sources` — every claim ID referenced in a script exists in
   [sources/registry/](templates/records) and is at the required tier.
5. `studio_ops validate canon` — no prohibited pattern (unsourced assertion,
   unlabelled synthetic archival, missing provenance on a generated asset).
6. `ruff` + `mypy` + `pytest` for anything under [automation/](automation).

A red gate is a blocked merge. There is no override flag; if a gate is wrong, fix
the gate in a `studio/*` PR.

## Writing rules for contributors

- **Never invent a fact to fill a template.** Leave `TBD — needs research` and open
  an entry in [research/open_questions/](templates/records). A plausible
  placeholder that survives to air is the single most likely way this project
  embarrasses itself.
- **Never paste a date, name, or figure into a script without a claim ID.** The
  validator will catch it, but catch it yourself first.
- **Never commit generated media to git.** Media goes to the asset store; git holds
  the manifest. See [docs/runbook/asset_storage.md](docs/runbook/asset_storage.md).
- **Prompt changes are versioned, not overwritten.** Bump the prompt card version
  and record what changed and why. See [prompts/README.md](prompts/README.md).

## Never claim more maturity than exists

Documentation distinguishes three states, and they are different claims — not degrees
of the same one:

| Label | Means | Evidence required |
|---|---|---|
| **DESIGNED** | Structure, schema, or spec exists on paper. No code runs. | The document exists and is internally consistent |
| **IMPLEMENTED** | Code exists and executes. Not proven at production scale. | The command runs |
| **TESTED** | Exercised against a real workload, with a recorded, reviewable result. | A test run, a report, a dated artefact |
| **NOT BUILT** | Specified, no code. Honest and useful. | — |

**A bare ✅ or "complete" is prohibited.** It reads as *working* when it usually means
*specified*, and that gap is how a schedule built on scaffolding slips.

Rules:

- Every capability claim in a README, roadmap, or status table carries one of these
  labels.
- The ledger at [docs/status.md](docs/status.md) is updated in the **same commit**
  that changes a capability's maturity — it is not a separate chore.
- Promotion names the evidence. "It seems to work" promotes nothing.
- Use the same three words in commit messages and in conversation. "Built" and
  "finished" are ambiguous; these are not.

The gap that matters most is **IMPLEMENTED → TESTED**. A validator that runs cleanly
on an empty repository has proved almost nothing.

## Commit messages

```
<area>(<scope>): <imperative summary>

area  = bible | standards | research | sources | prompts | templates |
        line | episode | automation | ops | docs | brand | library
scope = ng-nigeria, s01e01, schemas, midjourney, ...
```

Example: `episode(s01e01): add beat sheet skeleton and open-question links`

## File placement

Documentation goes in a semantic subfolder under [docs/](docs) — never at repo
root. The root whitelist is: `README.md`, `ROADMAP.md`, `LICENSE`,
`CONTRIBUTING.md`, `CHANGELOG.md`, `pyproject.toml`, `requirements.txt`, `Makefile`,
`.gitignore`, `.gitattributes`, `.editorconfig`, `.env.example`, and the
`.code-workspace` file. Anything else at root will be rejected in review, and
`studio_ops validate --root-hygiene` fails the build.

## Which layer does your change belong to?

The most common review correction. Use this test:

| Ask | If yes |
|---|---|
| Would this rule still be right for a production with **no historical claims at all**? | [core/](core) |
| Is it right for a whole **genre** of work? | [packs/](packs) |
| Is it right for **one studio's** brand and mission? | `studios/<code>/bible/` |
| Is it about **one region or strand**? | `studios/<code>/lines/<line>/` |
| Is it about **one piece**? | that production's folder |

Precedence is `core > pack > studio > line > production`. A lower layer may add
constraints and tighten upper ones. It may never loosen one. If you need an
exemption, amend the layer that owns the rule — with that layer's signatures.

Platform-level files must never name a studio or its subject matter. If you find
yourself writing "for instance, in Nigeria…" in `core/`, `standards/`, or `prompts/`,
the change belongs a layer down.
