---
title: Production budget template
status: active
version: 0.1.0
updated: 2026-08-07
owners: [showrunner]
---

# Production budget template

Copy this into the production's `00_brief/` folder and fill it before greenlight. It
is not optional at greenlight: `budget` is a field on the production record, and one
of its four values —
`consultation_fees_budgeted` — is a gate condition.

**Every figure below is `TBD`.** This is a platform template; it does not know your
currency, your region, your rates, or your scope, and a template that ships with
plausible numbers is a template whose numbers get shipped. Fill each line with an
amount and a stated basis, or with `TBD — <what is needed to resolve it>`.

## 1. What actually goes on the record

The production record carries four fields
([../standards/schemas/episode.schema.json](../standards/schemas/episode.schema.json)):

```yaml
budget:
  currency: TBD
  total: TBD
  generation_ceiling_usd: TBD
  consultation_fees_budgeted: TBD
```

Everything else in this document is working detail that rolls up into `total`.

> `TBD — the category breakdown below has no schema.` Whether it should get one, or
> stay a document, is a Platform Owner decision. Until it is made, the breakdown lives
> as markdown in the production folder and only the four fields above are machine
> readable.

## 2. The lines this kind of work forgets

Listed first, deliberately. An AI-assisted production budget assembled from
instinct will contain generation spend, an editor, and a composer, and will omit
every line in this section — because generative tooling makes the *visible* costs
collapse and leaves the human ones exactly where they were.
[../core/01_provenance_and_ai_disclosure.md](../core/01_provenance_and_ai_disclosure.md)
§7 states the position: generative tools change what the work costs; they do not
change who it belongs to.

| Line | Covers | Basis | Amount |
|---|---|---|---|
| Consultation and advisory fees | Advisors on the line's advisory register; community consultation; rulings and reviews; the advisor's review of material they informed, before it airs | Per advisor, per engagement, plus a retained rate for hold rulings during production | `TBD` |
| Community relationship costs | Providing the finished work to the community in a form they can access; travel to present it; translation of the material shown to them | Per community engaged | `TBD` |
| Translation | Narration translation, subtitles, quotation translation, orthography review; the translator is credited by name | Per language, per finished minute or per word | `TBD` |
| Language and pronunciation | IPA transcription of every proper noun; reference recordings from speakers of the language; the pronunciation check at audio lock, which is a named person, not a general responsibility | Per production, scaling with proper-noun count | `TBD` |
| Archive access and digitisation | Reading-room fees, reproduction fees, high-resolution scan fees, rush fees, and the separate charge many institutions levy for *permission* on top of the *copy* | Per institution, per item | `TBD` |
| Travel to archives and communities | The costs that decide whether a source gets consulted or cited from a catalogue entry | Per trip | `TBD` |
| Music licensing | Composition rights and recording rights are separate and both are payable; traditional recordings need the chain checked, which is billable work | Per cue, per territory, per term | `TBD` |
| Commissioned musicians | Where the score draws on a regional idiom, paying musicians from that tradition is both the right answer and the better-sounding one | Per session, per player | `TBD` |
| Voice licensing | Narration voice, including explicit coverage of synthetic reproduction where used. A synthetic voice is licensed from a consenting, compensated human, and the credit names them | Per production, per term, per territory | `TBD` |
| Contingency | See §5 | Percentage of subtotal, `TBD` | `TBD` |

Four of those lines — consultation, translation, archive fees, and music rights — are
the ones most often discovered *after* a greenlight, at which point the money to pay
them has already been committed to generation. That is the failure this section
exists to prevent.

## 3. Generation spend

| Line | Covers | Basis | Amount |
|---|---|---|---|
| Image generation | Stills, reconstruction and interpretive frames, matte extensions, upscales | Per attempt × attempts per shot × shots | `TBD` |
| Video generation | Motion for reconstruction and interpretive shots | Per second of output × attempts | `TBD` |
| Voice generation | Reference reads, narration where synthetic | Per minute | `TBD` |
| Music and SFX generation | Texture, drones, utility SFX, within the pack's music policy | Per cue | `TBD` |
| Restoration and upscale | Post-processing passes on generated and archival material | Per asset | `TBD` |
| Subscription and plan tiers | Vendor plan tiers held for **indemnity and commercial-use scope**, not for throughput. The tier that carries indemnity is frequently not the cheapest one that produces images | Per vendor, per month, per production | `TBD` |
| **Hard generation ceiling** | **The cap, not the budget** | See below | `TBD` |

### The ceiling is a cap, not a plan

`budget.generation_ceiling_usd` on the production record, and
`GENERATION_BUDGET_USD_PER_EPISODE` in [../.env.example](../.env.example), are the
same number: a hard per-production limit past which the generation adapters refuse to
run. The default in the environment template is `0`, with
`GENERATION_DRY_RUN=true`, so nothing generates until someone deliberately sets both.

Three things follow, and all three are routinely got wrong:

- **The ceiling is not the generation budget.** Budget the expected spend in the rows
  above; set the ceiling above it as the point at which something has gone wrong and
  the pipeline should stop rather than continue quietly.
- **Hitting the ceiling is a signal, not an obstacle.** A production at its ceiling
  before picture lock has a prompt problem or a brief problem, and raising the ceiling
  resolves neither. See [risk_register.md](risk_register.md) `RSK-PLAT-0003`.
- **The cap is currently enforced by nothing.** The adapters are stubs — **NOT
  BUILT**. Until they are wired, the ceiling is a number in a file and the real
  control is the vendor invoice.

## 4. The rest of the budget

| Category | Line | Basis | Amount |
|---|---|---|---|
| **People** | Research lead | Per production or per week | `TBD` |
| | Additional researchers | Per week | `TBD` |
| | Story producer / writer | Per production | `TBD` |
| | Visual director | Per production | `TBD` |
| | Editor | Per week | `TBD` |
| | Audio lead / mixer | Per production | `TBD` |
| | Composer | Per production, plus publishing position | `TBD` |
| | Rights and clearances | Per production or per clearance | `TBD` |
| | Pipeline engineer | Allocated across the slate, not per production | `TBD` |
| **Rights** | Archival stills and moving image | Per item, per territory, per term | `TBD` |
| | Museum and collection objects | Per object; photography rights are separate from object rights | `TBD` |
| | Manuscripts and documents | Per item, plus translation rights where translated | `TBD` |
| | Fonts | Licence tier covering broadcast/streaming and seat count | `TBD` |
| | LUTs, plugins, stock SFX | Licence permitting commercial redistribution in a finished film | `TBD` |
| **Production** | Interview and testimony capture | Per shoot day, per location | `TBD` |
| | Contemporary footage | Per shoot day | `TBD` |
| | Graphics and maps | Per graphic | `TBD` |
| **Delivery** | Captions and subtitles | Per language, per finished minute | `TBD` |
| | QC and packaging | Per deliverable variant | `TBD` |
| | Audio description | Only if in scope — decide before the shooting script, since it adds a script column and a stem | `TBD` |
| **Legal** | Contributor releases and consent | Per contributor | `TBD` |
| | Chain of title assembly | Per production | `TBD` |
| | Clearance advice, fair-dealing positions | Per opinion | `TBD` |
| **Infrastructure** | Asset store | Per TB, per month, across the slate | `TBD` |
| | Archive and preservation | Two copies, two locations, one offline, verified annually | `TBD` |

Detail on what each rights line must record is in
[../core/02_rights_and_licensing.md](../core/02_rights_and_licensing.md) §2. Delivery
specs that determine the QC and packaging line are in
[../standards/delivery_specs.md](../standards/delivery_specs.md).

## 5. Contingency

`TBD — Showrunner to set the percentage before the first greenlight.`

Set it against the cascade table in [workflow_states.md](workflow_states.md) §6
rather than against a general sense of caution, because that table is where the money
actually goes. A re-opened source lock costs the production; a re-opened audio lock
costs a re-mix. A contingency sized for re-mixes and spent on a re-script is a
contingency that ran out in month two.

A contingency of zero is a claim that no gate will be re-opened. No production has
ever made that claim truthfully.

## 6. Red flags at greenlight

The Showrunner signs the greenlight gate. These are the budget conditions that should
stop that signature.

| Condition | Why it stops the gate |
|---|---|
| `consultation_fees_budgeted: false` | **The named red flag.** The schema carries this as a boolean specifically so it cannot be omitted by silence. An advisor who is not paid is not an advisor; they are a favour being taken advantage of, and they will eventually and rightly stop answering. A production that has not budgeted consultation has decided to do the work without advisors and has not said so |
| Translation absent, but non-production-language material appears on screen | Either the budget is wrong or the plan is to strip diacritics and approximate the names, which the localisation policy prohibits and a regional audience detects immediately |
| Archive fees absent, but the research plan names institutions | The plan is to cite from catalogue entries rather than consult the material — a T3 chain presented as a T1 one |
| Generation ceiling set above the people subtotal | The production has decided, numerically, that images matter more than the people who make the work correct. That may be defensible; it should be defended out loud rather than arrived at |
| Contingency zero | See §5 |
| `total` present, category breakdown absent | A number nobody can defend line by line is a number that will be defended by cutting whichever line is easiest to cut, which is always consultation |

The greenlight checklist item that enforces this is in
[checklists/greenlight.md](checklists/greenlight.md).

## 7. Maturity

| Capability | Status |
|---|---|
| Budget category template | **DESIGNED** |
| `budget` block on the production record | **DESIGNED** — never validated against a real record |
| Generation ceiling enforcement in the adapters | **NOT BUILT** — the adapters are stubs |
| Spend reporting against the ceiling | **NOT BUILT** |

No production has been greenlit and no budget has been set. Ledger:
[../docs/status.md](../docs/status.md).
