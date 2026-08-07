---
title: Responsibility matrix
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner]
---

# Responsibility matrix

Who does the work, who is accountable for it, who has to be asked first, and who
finds out afterwards — across the eleven pipeline stages and the five concerns that
cut across all of them.

Role definitions are in [roles.md](roles.md). The lifecycle this matrix runs along is
in [workflow_states.md](workflow_states.md).

## 1. Legend

| | Means |
|---|---|
| **R** | Responsible — does the work |
| **A** | Accountable — **exactly one per row**. Owns the outcome and, where the row closes with a gate, signs it |
| **C** | Consulted — two-way, *before* the decision. A consultation that happens after the decision is an announcement |
| **I** | Informed — one-way, after |

Where a row closes with a gate, **A is the gate owner declared in the pack's
`gates.yaml`**. The two are the same fact recorded twice; if they ever disagree, the
`gates.yaml` wins, because that is the file `studio_ops` reads.

## 2. Pipeline stages

Columns are the nine signing and management roles. The worked gate set is
[documentary-history](../packs/documentary-history/gates.yaml) — the framework is
pack-neutral, the specific gates are not.

Abbreviations: SR `showrunner`, LL `line-lead`, RL `research-lead`,
SP `story-producer`, VD `visual-director`, AL `audio-lead`,
RC `rights-and-clearances`, CA `cultural-advisor`, PE `pipeline-engineer`.

| Stage / activity | SR | LL | RL | SP | VD | AL | RC | CA | PE | Closes with |
|---|---|---|---|---|---|---|---|---|---|---|
| `00_brief` | **A** | C | C | R | I | I | C | C | I | greenlight |
| `00_brief` — premise review | I | C | C | C | I | I | I | **A** | I | sensitivity 1 of 3 |
| `01_research` | I | C | **A** R | C | I | I | C | C | I | source lock |
| `02_script` | C | I | C | **A** R | C | I | I | C | I | script lock |
| `03_storyboard` | I | I | I | C | **A** R | I | I | C | C | — |
| `04_prompts` | I | I | C | C | **A** R | C | C | C | C | sensitivity 2 of 3 |
| `04_prompts` — prompt-set review | I | I | C | I | C | I | I | **A** | I | sensitivity 2 of 3 |
| `05_assets` | I | I | I | I | **A** | C | C | I | R | — |
| `06_edit` | C | I | I | C | **A** | C | I | C | R | picture lock |
| `07_audio_post` | I | I | C | I | C | **A** R | C | C | R | audio lock |
| `08_review` — fact-check | C | I | **A** R | C | C | C | I | I | C | fact-check |
| `08_review` — cut review | C | C | C | C | C | C | I | **A** | I | sensitivity 3 of 3 |
| `08_review` — clearances | C | I | C | I | C | C | **A** R | C | C | rights |
| `09_delivery` | I | I | I | I | C | C | C | I | **A** R | technical QC |
| `10_publish` | **A** | R | C | C | C | C | C | C | R | — |

Three things in that table are worth stating explicitly, because they are the ones
people get wrong:

**`08_review` is not a stage that happens after `06_edit`.** The numbering is a folder
layout, not a sequence. Fact-check is declared at `08_review` and **blocks picture
lock**, which is at `06_edit` — so the fact-check has to be complete before the cut
can lock. Sensitivity and rights overlap the same way. Read the `blocks:` graph in
`gates.yaml`, not the folder numbers. This is the single most common misreading of the
pipeline and it produces a schedule that is wrong by a whole review cycle.

**Sensitivity appears three times and is one gate.** Premise, prompt set, cut. The
Cultural Advisor is accountable at all three points and the gate is not signed until
the third clears. Running it once, at the end, is the failure mode the three-point
structure exists to prevent — once a striking image exists, the argument about whether
it should exist is much harder to win.

**`05_assets` and `03_storyboard` close with no gate.** They are blocked *into*
existence by script lock and blocked *out of* it by picture lock. Generation begins
only after script lock; a stage without a gate of its own is not an ungoverned stage.

## 3. Where the non-signing roles do the work

These four roles hold no signature ([roles.md](roles.md) §4) and do a large share of
the actual work.

| Role | Responsible for | Accountable role above them |
|---|---|---|
| `editor` | The assembly and cut at `06_edit`; NLE project structure; keeping on-screen text on separate layers so a textless master is a render, not a rebuild | `visual-director` |
| `composer` | The score and cue delivery at `07_audio_post`; cue sheet entries for original music | `audio-lead` |
| `translator` | Subtitles, translated narration, and quotation translation at `09_delivery`; recording whether a text was retranslated through an intermediate language | `audio-lead` for spoken material, `showrunner` for on-screen text |
| `advisor` | Subject-matter and community input at `00_brief`, `04_prompts`, and `08_review` | `cultural-advisor`, who converts advice into a written ruling |

## 4. Cross-cutting concerns

These do not belong to a stage. They run the length of the production and, in the
first two cases, the length of the platform.

| Concern | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| **Canon change** — core, or a pack's doctrine | Proposer, whoever they are | `platform-owner` for core; `pack-owner` for a pack | `showrunner` of every studio on the affected pack; `cultural-advisor` where the change touches sensitivity | All contributors |
| **Schema change** — `standards/schemas/*` | `pipeline-engineer` | `platform-owner` | `research-lead` for record schemas, `rights-and-clearances` for clearance fields, every pack owner for gate fields | All contributors |
| **Rights** | `rights-and-clearances` | `rights-and-clearances` | `showrunner` on cost, `audio-lead` on music, `visual-director` on archival, `pipeline-engineer` on model terms | `line-lead`, `story-producer` |
| **Sensitivity** | Any contributor may raise a hold, without standing or seniority | `cultural-advisor` | `advisor` on the relevant tradition; `showrunner`; `line-lead` | All contributors |
| **Budget** | `line-lead` | `showrunner` | `pipeline-engineer` on generation spend, `rights-and-clearances` on licence and archive fees, `cultural-advisor` on consultation and advisory fees | `platform-owner` |

Four notes on that table, each of which is the reason a row is shaped the way it is:

- **Canon changes never ride along in a production PR.** A change to a pack or to
  core gets its own `studio/*` branch and its own review — see
  [../CONTRIBUTING.md](../CONTRIBUTING.md) § Branching. A rule amended under deadline
  pressure to unblock one episode is a rule amended for the worst possible reason.
- **Schema changes are accountable to the Platform Owner even though the Pipeline
  Engineer writes them**, because a schema field is a contract every existing record
  is already relying on. Adding a required field retroactively invalidates every
  record that predates it.
- **Rights has the same role Responsible and Accountable**, which is unusual and
  deliberate. There is no one to escalate a `pending` clearance to. It is not a risk
  to be weighed by a more senior person; it is a block
  ([../core/02_rights_and_licensing.md](../core/02_rights_and_licensing.md) §10).
- **Sensitivity is the only row where "Responsible" is *anyone*.** Any contributor
  may place a hold, it takes effect immediately, only the Cultural Advisor releases
  it in writing, and the person who raised it is never penalised
  ([../core/04_review_gate_framework.md](../core/04_review_gate_framework.md) §6). A
  hold that requires standing to raise is not a hold; it is a suggestion with extra
  steps.

## 5. One person, several roles

On a small team one person will hold several of these columns at once. That is
expected and explicitly permitted by
[../core/00_platform_charter.md](../core/00_platform_charter.md) §7.

**Except across gates on the same production.**
[../core/04_review_gate_framework.md](../core/04_review_gate_framework.md) §5
prohibits it, and it is not a stylistic preference — it is the mechanism the entire
matrix above rests on. The most common review failure is not incompetence, it is
proximity: the person who made the thing cannot see it. Two gates signed by the same
person are one gate wearing two hats, and the production record will not say so.

What that means in practice:

| Combination | Permitted? |
|---|---|
| One person is Showrunner **and** Line Lead **and** Story Producer | Yes. One gate between them on a documentary-history production — script lock, which the Story Producer signs; greenlight would then need someone else |
| One person is Research Lead **and** Editor | Yes. The Editor signs nothing |
| One person is Visual Director **and** Audio Lead on the same episode | **No.** Two gates: picture lock and audio lock |
| One person is Showrunner **and** signs greenlight, then also signs picture lock because the Visual Director left | **No.** Re-assign the role, or bring in an outside signatory |
| One person is Pipeline Engineer on every production in the studio | Yes, and normal. Technical QC is one gate per production |

`studio_ops validate --canon` is specified to flag a repeated `person` value across a
production's signatures. It is **NOT BUILT** — see
[../docs/status.md](../docs/status.md) — so until it exists this is enforced by
whoever reviews the production record, which is exactly the kind of enforcement that
does not survive a deadline.

Being flagged is a staffing signal, not a paperwork problem. The honest responses are
to bring in outside signatories, adopt a pack with a smaller gate set, or not produce
yet. The structural consequences of doing none of those are in
[risk_register.md](risk_register.md) `RSK-PLAT-0001`, and the unresolved conflict
between §5 and the packs' own gate sets is in [roles.md](roles.md) §5.1.
