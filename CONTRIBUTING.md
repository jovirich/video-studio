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
   [standards/schemas/](standards/schemas/).
2. `studio_ops validate naming` — file and asset names match
   [standards/naming_conventions.md](standards/naming_conventions.md).
3. `studio_ops validate links` — no dead internal links, no orphan records.
4. `studio_ops validate sources` — every claim ID referenced in a script exists in
   [sources/registry/](sources/registry/) and is at the required tier.
5. `studio_ops validate canon` — no prohibited pattern (unsourced assertion,
   unlabelled synthetic archival, missing provenance on a generated asset).
6. `ruff` + `mypy` + `pytest` for anything under [automation/](automation/).

A red gate is a blocked merge. There is no override flag; if a gate is wrong, fix
the gate in a `studio/*` PR.

## Writing rules for contributors

- **Never invent a fact to fill a template.** Leave `TBD — needs research` and open
  an entry in [research/open_questions/](research/open_questions/). A plausible
  placeholder that survives to air is the single most likely way this project
  embarrasses itself.
- **Never paste a date, name, or figure into a script without a claim ID.** The
  validator will catch it, but catch it yourself first.
- **Never commit generated media to git.** Media goes to the asset store; git holds
  the manifest. See [docs/runbook/asset_storage.md](docs/runbook/asset_storage.md).
- **Prompt changes are versioned, not overwritten.** Bump the prompt card version
  and record what changed and why. See [prompts/README.md](prompts/README.md).

## Commit messages

```
<area>(<scope>): <imperative summary>

area  = bible | standards | research | sources | prompts | templates |
        line | episode | automation | ops | docs | brand | library
scope = ng-nigeria, s01e01, schemas, midjourney, ...
```

Example: `episode(s01e01): add beat sheet skeleton and open-question links`

## File placement

Documentation goes in a semantic subfolder under [docs/](docs/) — never at repo
root. The root whitelist is: `README.md`, `LICENSE`, `CONTRIBUTING.md`,
`CHANGELOG.md`, `pyproject.toml`, `requirements.txt`, `Makefile`, `.gitignore`,
`.gitattributes`, `.editorconfig`, `.env.example`, and the `.code-workspace` file.
Anything else at root will be rejected in review.
