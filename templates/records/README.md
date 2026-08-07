---
title: Record templates
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [research-lead, pipeline-engineer]
---

# Record templates

One template per record type. Copied by `studio_ops new-record --type <type> --line <line>`
(**NOT BUILT** — [../../docs/status.md](../../docs/status.md)).

| Template | Type | ID form | Schema | Lives at |
|---|---|---|---|---|
| [_TEMPLATE_source_record.md](_TEMPLATE_source_record.md) | `source` | `SRC-XX-0000` | [source_record](../../standards/schemas/source_record.schema.json) | `<line>/sources/records/` |
| [_TEMPLATE_claim.md](_TEMPLATE_claim.md) | `claim` | `CLM-XX-0000` | [claim](../../standards/schemas/claim.schema.json) | `<line>/sources/claims/` |
| [_TEMPLATE_character.md](_TEMPLATE_character.md) | `character` | `CHR-XX-0000` | [character](../../standards/schemas/character.schema.json) | `<line>/characters/profiles/` |
| [_TEMPLATE_location.md](_TEMPLATE_location.md) | `location` | `LOC-XX-0000` | [location](../../standards/schemas/location.schema.json) | `<line>/locations/profiles/` |
| [_TEMPLATE_timeline_event.md](_TEMPLATE_timeline_event.md) | `timeline_event` | `EVT-XX-0000` | [timeline_event](../../standards/schemas/timeline_event.schema.json) | `<line>/timeline/events/` |
| [_TEMPLATE_open_question.md](_TEMPLATE_open_question.md) | `open_question` | `QST-XX-0000` | — | `<line>/research/open_questions/` |
| [_TEMPLATE_research_brief.md](_TEMPLATE_research_brief.md) | — | dated | — | `<line>/research/briefs/` |
| [_TEMPLATE_fact_check.md](_TEMPLATE_fact_check.md) | `fact_check` | `FCK-XX-S00E00-0000` | — | `<line>/research/fact_checks/` |
| [_TEMPLATE_advisory_ruling.md](_TEMPLATE_advisory_ruling.md) | `advisory_ruling` | `ADV-XX-0000` | — | `<line>/advisory/rulings/` |
| [_TEMPLATE_correction.md](_TEMPLATE_correction.md) | `correction` | `COR-XX-0000` | — | alongside the line's corrections log |
| [_TEMPLATE_style_anchor.md](_TEMPLATE_style_anchor.md) | `style_anchor` | `STA-XX-0000` | — | `<line>/style/anchors/` |

Shot and prompt card records are production-scoped and live with the production
skeleton: [../production/03_storyboard/](../production/03_storyboard/) and
[../production/04_prompts/](../production/04_prompts/).

## Five types have no schema yet

`open_question`, `fact_check`, `advisory_ruling`, `correction`, and `style_anchor`
have IDs in [../../standards/id_system.md](../../standards/id_system.md) and no file
in [../../standards/schemas/](../../standards/schemas/). Their front matter here
follows the minimum in [../../standards/metadata_spec.md](../../standards/metadata_spec.md)
plus the fields the ID system and the gates actually need — a convention held by
these templates and not enforced by anything.

That is a real gap, not a stylistic choice: `studio_ops validate --schemas` routes on
the `type` field, so records of these five types pass validation by being invisible
to it. When a schema is written for one, reconcile it with the template in the same
commit.

## IDs are allocated, never typed

IDs are permanent, never reused, never renumbered. A deleted record keeps its ID as a
tombstone. The allocator takes the next serial for the (type, scope) pair and refuses
to run on a gap-and-collision pattern suggesting a hand-edited ID.

Hand-allocating is the failure worth being afraid of, because it fails *quietly*: a
collided ID does not break a reference, it re-points it at the wrong record, and
nothing in the graph reports an error.

## Dates are quoted in front matter

`updated: "2026-08-07"`, not `updated: 2026-08-07`.

Unquoted, YAML resolves an ISO date to a date object, and every schema types these
fields as strings — so an unquoted date fails validation with a message that reads
like a schema bug. The example in
[../../standards/metadata_spec.md](../../standards/metadata_spec.md) is unquoted;
these templates quote, and the discrepancy is worth resolving in one direction or the
other.

## The `TBD` convention

Every substantive field reads `TBD — <what is needed to resolve it>`. The trailing
clause is not decoration: `TBD` alone says something is missing, while
`TBD — needs the repository's shelfmark for the folio` says what to go and do.

- Legal at `status: draft` and `status: review`.
- Illegal at `status: locked`. Locking is what forces the decision.
- A `TBD` in a `review`-status record must link an open question.

A few fields cannot carry the clause because their schema pattern-matches them —
`pack` on a studio record accepts the bare literal `TBD` only, and ID fields must
match their pattern, so they carry obvious placeholders (`XX`, `S00E00`, `0000`)
instead. Where that happens, the explanation sits in a comment beside the field.
