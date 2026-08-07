# Pull Request

## What this changes

<!-- One paragraph. What is different after this merges? -->

## Area

- [ ] `bible/` — editorial canon (requires Showrunner + Cultural Advisor review)
- [ ] `standards/` — schemas or specs (requires Pipeline Engineer review; may be breaking)
- [ ] `research/` or `sources/` — evidence layer (requires Research Lead review)
- [ ] `prompts/` — prompt library (requires Visual Director or Audio Lead review)
- [ ] `productions/<line>/` — line-level material
- [ ] `episodes/<code>/` — episode work
- [ ] `automation/` — tooling
- [ ] `docs/`, `ops/`, `brand/`, `library/` — supporting

## Evidence checklist

Tick only what genuinely applies. An unticked box is information, not a failure.

- [ ] Every new factual statement carries a claim ID that resolves in `sources/registry/`.
- [ ] No placeholder fact was invented to fill a template. Unknowns are marked
      `TBD — needs research` and have an entry in `research/open_questions/`.
- [ ] Every new source record names its archive, custodian, and access condition.
- [ ] Any third-party media added is logged in `sources/permissions/clearance_log.md`.

## Generation checklist

- [ ] Every generated asset has a prompt card and a provenance entry in the episode manifest.
- [ ] No AI-generated image is presented as archival footage anywhere in this change.
- [ ] No real person's likeness or voice is synthesised without a clearance reference.
- [ ] Model terms for each tool used were checked against
      `sources/permissions/model_terms_register.md`.

## Sensitivity

- [ ] This change touches material flagged sensitive in `bible/07_cultural_sensitivity.md`.
      → If ticked, name the advisor consulted: ______________________
- [ ] This change involves conflict, violence, human remains, sacred practice, or
      living communities' claims. → If ticked, link the advisory ruling: ____________

## Gates

<!-- Delete rows that do not apply. Gates are defined in ops/workflow_states.md -->

| Gate | Owner | Status |
|---|---|---|
| Fact-check | Research Lead | ⬜ not required / ⬜ pending / ⬜ signed |
| Sensitivity | Cultural Advisor | ⬜ not required / ⬜ pending / ⬜ signed |
| Rights | Rights & Clearances | ⬜ not required / ⬜ pending / ⬜ signed |
| Script lock | Story Producer | ⬜ not required / ⬜ pending / ⬜ signed |
| Picture lock | Visual Director | ⬜ not required / ⬜ pending / ⬜ signed |
| Technical QC | Pipeline Engineer | ⬜ not required / ⬜ pending / ⬜ signed |

## Linked issues

Closes #
Related canon change (`studio/*` PR):

## Reviewer notes

<!-- What should the reviewer look at hardest? Where are you least confident? -->
