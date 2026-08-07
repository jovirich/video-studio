# Standards

The Bible states the rules in prose. This folder states the mechanically checkable
subset in schema and spec, so that CI can enforce them without a human reading
every file.

**Rule of precedence:** where a schema and the Bible disagree, the Bible is correct
and the schema is a bug. File it as a `[pipeline]` issue.

## Contents

| File | Governs | Enforced by |
|---|---|---|
| [schemas/](schemas/) | The shape of every record type | `studio_ops validate --schemas` |
| [id_system.md](id_system.md) | Identifier grammar for every entity | `validate --naming` |
| [naming_conventions.md](naming_conventions.md) | File, folder, and asset names | `validate --naming` |
| [metadata_spec.md](metadata_spec.md) | Front matter and embedded media metadata | `validate --schemas` |
| [delivery_specs.md](delivery_specs.md) | Picture, audio, caption, and master specs | Technical QC gate |
| [prohibited_language.md](prohibited_language.md) | Words and patterns that fail review | `validate --canon` |
| [data_graphics.md](data_graphics.md) | Maps, charts, timelines | Picture lock |

## Schema index

| Schema | Applies to |
|---|---|
| `production_line.schema.json` | `productions/<line>/line.yaml` |
| `episode.schema.json` | `episodes/<code>/episode.yaml` |
| `source_record.schema.json` | `sources/registry/records/SRC-*.yaml` |
| `claim.schema.json` | `sources/registry/claims/CLM-*.yaml` |
| `character.schema.json` | `<line>/characters/profiles/CHR-*.md` front matter |
| `location.schema.json` | `<line>/locations/profiles/LOC-*.md` front matter |
| `timeline_event.schema.json` | `<line>/timeline/events/EVT-*.yaml` |
| `shot.schema.json` | `episodes/<code>/03_storyboard/shots/SHT-*.yaml` |
| `prompt_card.schema.json` | `**/*.prompt.yaml` |
| `asset_manifest.schema.json` | `episodes/<code>/manifest.yaml` |

All schemas are JSON Schema draft 2020-12. YAML files are parsed then validated
against them; there is no separate YAML schema language in use.

## Design principles for these schemas

1. **Required fields are required because omitting them causes real harm**, not
   because completeness is tidy. Every `required` entry should map to a failure mode
   someone can name.
2. **`TBD` is a legal value** in text fields during draft status, and is *illegal*
   once a record's `status` reaches `locked`. This is what lets scaffolding exist
   without inviting invented placeholders.
3. **No schema encodes a historical fact.** Enums cover process states, provenance
   classes, tiers, and registers — never periods, peoples, or places.
4. **Additive changes are minor; required-field changes are major** and ship with a
   migration in the same PR.
