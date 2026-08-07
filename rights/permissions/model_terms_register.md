---
title: Model terms register
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [rights-and-clearances, pipeline-engineer]
---

# Model terms register

## ACTIVE VERIFICATION REQUIRED — OpenAI, EXP-001

The first vendor selected for a real run. **Nothing has been generated and nothing has
been spent**, because `studio_ops` refuses until the fields below are filled by a
person who has opened the current terms.

| Field | Value |
|---|---|
| Vendor | OpenAI |
| Model family | GPT Image 2 |
| Pinned snapshot | `gpt-image-2-2026-04-21` — **directed, not confirmed to resolve** |
| Floating alias | `gpt-image-2` — **refused by the adapter** for this run |
| Execution mode | `api` |
| Production | EXP-001, Phase A only |
| Terms URL | **TBD — not opened** |
| Terms effective date | **TBD** |
| Plan tier held | **TBD** |
| Output ownership provisions | **TBD — not read** |
| Commercial use permitted | **TBD — not read** |
| Broadcast / streaming use | **TBD — not read** |
| Indemnity, and at what tier | **TBD — not read** |
| Trains on inputs; can it be disabled | **TBD — not read** |
| Content restrictions relevant to this run | **TBD — not read** |
| Required attribution | **TBD — not read** |
| Price per image, current | **TBD — not read** |
| Date checked | **NOT CHECKED** |
| Checked by | — |

### Why every cell says TBD rather than a plausible answer

No process in this repository can read a vendor's terms page, and a remembered
summary of a terms document is not a verification — terms change, tiers differ, and
the studio's answer to *"were you permitted to use that?"* cannot be *"we believed
so."* The same reasoning that makes a language model tier T5 for research applies to
the studio's own commercial position.

The price cell is empty for a sharper reason: **a guessed price produces a ceiling
that bounds nothing while looking like a control.** The adapter refuses rather than
estimate.

### What unblocks generation

Four human acts, each mapping to a guard that is already live and tested:

| Act | Sets | Guard that lifts |
|---|---|---|
| Read the terms; fill this table | `OPENAI_TERMS_CHECKED` | `TermsNotVerifiedError` |
| Record the current per-image price | `OPENAI_IMAGE_PRICE_USD` | `PriceUnknownError` |
| Set a ceiling for the diagnostic phase | `budget_usd` | `BudgetExceededError` |
| Verify the request/response shape against live API docs | `WIRE_FORMAT_VERIFIED` | `AdapterNotBuiltError` |

Plus `GENERATION_DRY_RUN=false`, and `OPENAI_API_KEY`.

**Confirm the snapshot separately.** A snapshot ID that does not exist fails loudly and
harmlessly. A snapshot ID that silently resolves to the floating alias would defeat the
entire reason for pinning it, and the failure would be invisible until a mid-run model
update made the drift numbers meaningless.



Per-tool record of what each generative vendor's terms permit, at a stated date, at
the plan tier the studio actually holds.

Canon: [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §5
and [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §5.

**Maturity: DESIGNED.** This register is **empty of terms**, deliberately and
permanently until a human fills it in.

## Why this register contains no terms

It would be trivial to write down what each vendor's licence appears to say. It would
also be the most dangerous document in this repository.

Vendor terms change without notice, are versioned by plan tier, differ between the
consumer and enterprise agreement for the same product, and are frequently amended in
ways that do not generate an email. A statement here that "vendor X permits commercial
broadcast use" would be read as verified fact by everyone downstream, would survive
long after it stopped being true, and would be relied on at the exact moment it
mattered — the delivery of a master that cannot be recalled.

An empty register is honest and produces the correct behaviour: nobody generates until
someone checks. A stale register produces confident, wrong behaviour. So this file
states **no vendor's terms**, quotes **no vendor's licence**, and links to **no
vendor's terms URL that has not been verified by a human** — a URL asserted from
memory is a claim like any other.

The register's value is not the answers. It is the seven questions, the dates, and the
names.

## Why it is re-checked before every delivery

Core/02 §5: *"Re-checked before every delivery, because vendor terms change without
notice and a delivered master is not easily recalled."*

The check is not "have the terms changed since we started?" It is "what do the terms
say **today**, at **our** plan tier, for the assets **in this master**?" Three things
move independently between greenlight and delivery:

1. **The vendor's terms**, which can change mid-production.
2. **The studio's plan tier**, which can be downgraded by an expiring card as easily
   as it was upgraded by a decision. Indemnity in particular is commonly tier-gated,
   and losing the tier loses the indemnity retroactively for nothing already made.
3. **The intended distribution**, which broadens. A licence adequate for online
   release is not automatically adequate for broadcast, and the distribution decision
   is usually made after the assets exist.

A generated asset's row in [clearance_log.md](clearance_log.md) points at a **dated**
row here. What matters at a dispute is what the terms were on the date of generation
*and* what they were at delivery. One date is not enough.

## The seven questions

Every entry answers all seven. They are core/02 §5, unaltered:

| # | Question | Why it is on the list |
|---|---|---|
| **Q1** | Does the licence permit **commercial** use of outputs? | The gate question. A tool whose terms do not permit commercial use does not enter the pipeline, however good it is. |
| **Q2** | Does it permit use in a **broadcast/streaming** production specifically? | Distinct from Q1 and routinely missed. "Commercial use" in a vendor's marketing copy often means the output may be sold; it does not always address distribution through a broadcaster or platform, which some terms carve out. Ask it separately or it does not get asked. |
| **Q3** | Who **owns** the output, and can the studio claim any **exclusivity**? | Ownership and exclusivity are different questions with different answers. Non-exclusive output is usually acceptable; discovering it is non-exclusive after building a brand identity on it is not. |
| **Q4** | Is there **indemnity** against third-party IP claims, and **at what plan tier**? | The tier clause is the whole question. Indemnity is the single most common tier-gated term, and the studio's actual tier is the only one that counts. |
| **Q5** | Does the vendor **train on inputs**, and can that be **disabled**? | Determines whether the tool may touch unpublished archival scans, interview recordings, or restricted material at all — see core/01 §6, which prohibits sending such material to an endpoint without a no-training position. |
| **Q6** | Are there **content restrictions** relevant to the genre? | Depiction of real people, historical figures, violence, minors, and religious material are all commonly restricted, and the restrictions bite hardest on exactly the subject matter a factual production needs. What is "relevant to the genre" is the canon pack's call, not this register's. |
| **Q7** | What **attribution** does the vendor require? | An unmet attribution requirement is a licence breach that is invisible until someone looks at the credits. Record the exact required wording, as in the clearance log. |

## The register

One row per vendor folder under [../../prompts/](../../prompts/). Every field reads
`TBD — not yet checked`, which means precisely that: **no human has read this vendor's
terms**. It does not mean "probably fine", and it does not mean "low risk".

Two columns need a note before you fill them:

- **Plan tier held** — the tier the studio *actually pays for right now*, not the tier
  whose terms were read. If they differ, the row is wrong in the direction that hurts.
- **Terms link** — the URL of the agreement the answers were read from, recorded at
  check time. Left `TBD` here because asserting a vendor's terms URL without opening it
  is the same error as asserting the terms themselves.

Answers are short and literal: `yes`, `no`, `yes — <tier>`, `no — <what is excluded>`,
or `TBD`. A cell containing a hedge is an unchecked cell.

**49 vendors carry a prompt cheat sheet. 49 rows below. 0 have been checked.** That
count is the worklist, and it is the honest measure of how far this register is from
doing its job. Regenerate the rows whenever a vendor folder is added or removed — the
list is derived from `prompts/*/`, so a vendor with a cheat sheet and no row here is a
tool someone can reach for without a rights record existing.

### Audio — voice, music, and speech processing

| Vendor | Plan tier held | Q1 commercial | Q2 broadcast/streaming | Q3 ownership / exclusivity | Q4 indemnity + tier | Q5 training on inputs / can disable | Q6 content restrictions | Q7 attribution | Date checked | Checked by | Terms link |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [adobe-podcast](../../prompts/audio/adobe-podcast/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [elevenlabs](../../prompts/audio/elevenlabs/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [murf](../../prompts/audio/murf/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [resemble](../../prompts/audio/resemble/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [suno](../../prompts/audio/suno/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [udio](../../prompts/audio/udio/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |

### Image

| Vendor | Plan tier held | Q1 commercial | Q2 broadcast/streaming | Q3 ownership / exclusivity | Q4 indemnity + tier | Q5 training on inputs / can disable | Q6 content restrictions | Q7 attribution | Date checked | Checked by | Terms link |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [dall-e](../../prompts/image/dall-e/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [firefly](../../prompts/image/firefly/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [flux](../../prompts/image/flux/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [ideogram](../../prompts/image/ideogram/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [imagen](../../prompts/image/imagen/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [leonardo](../../prompts/image/leonardo/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [midjourney](../../prompts/image/midjourney/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [recraft](../../prompts/image/recraft/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [stable-diffusion](../../prompts/image/stable-diffusion/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |

### Performance — lip-sync, avatar, and motion transfer

| Vendor | Plan tier held | Q1 commercial | Q2 broadcast/streaming | Q3 ownership / exclusivity | Q4 indemnity + tier | Q5 training on inputs / can disable | Q6 content restrictions | Q7 attribution | Date checked | Checked by | Terms link |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [hedra](../../prompts/performance/hedra/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [heygen](../../prompts/performance/heygen/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [runway-act](../../prompts/performance/runway-act/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [synclabs](../../prompts/performance/synclabs/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |

### Post — editorial, effects, and transcription

| Vendor | Plan tier held | Q1 commercial | Q2 broadcast/streaming | Q3 ownership / exclusivity | Q4 indemnity + tier | Q5 training on inputs / can disable | Q6 content restrictions | Q7 attribution | Date checked | Checked by | Terms link |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [after-effects](../../prompts/post/after-effects/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [capcut](../../prompts/post/capcut/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [descript](../../prompts/post/descript/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [premiere](../../prompts/post/premiere/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [resolve](../../prompts/post/resolve/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |

### Restoration and upscaling

| Vendor | Plan tier held | Q1 commercial | Q2 broadcast/streaming | Q3 ownership / exclusivity | Q4 indemnity + tier | Q5 training on inputs / can disable | Q6 content restrictions | Q7 attribution | Date checked | Checked by | Terms link |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [adobe](../../prompts/restoration/adobe/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [krea](../../prompts/restoration/krea/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [magnific](../../prompts/restoration/magnific/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [topaz](../../prompts/restoration/topaz/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |

### Scene and 3D

| Vendor | Plan tier held | Q1 commercial | Q2 broadcast/streaming | Q3 ownership / exclusivity | Q4 indemnity + tier | Q5 training on inputs / can disable | Q6 content restrictions | Q7 attribution | Date checked | Checked by | Terms link |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [blender](../../prompts/scene3d/blender/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [gaussian-splatting](../../prompts/scene3d/gaussian-splatting/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [houdini](../../prompts/scene3d/houdini/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [meshy](../../prompts/scene3d/meshy/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [tripo](../../prompts/scene3d/tripo/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [unreal](../../prompts/scene3d/unreal/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |

### Text

| Vendor | Plan tier held | Q1 commercial | Q2 broadcast/streaming | Q3 ownership / exclusivity | Q4 indemnity + tier | Q5 training on inputs / can disable | Q6 content restrictions | Q7 attribution | Date checked | Checked by | Terms link |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [claude](../../prompts/text/claude/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [gemini](../../prompts/text/gemini/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [gpt](../../prompts/text/gpt/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [llama](../../prompts/text/llama/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [perplexity](../../prompts/text/perplexity/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |

### Video

| Vendor | Plan tier held | Q1 commercial | Q2 broadcast/streaming | Q3 ownership / exclusivity | Q4 indemnity + tier | Q5 training on inputs / can disable | Q6 content restrictions | Q7 attribution | Date checked | Checked by | Terms link |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [hailuo](../../prompts/video/hailuo/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [higgsfield](../../prompts/video/higgsfield/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [kling](../../prompts/video/kling/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [luma](../../prompts/video/luma/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [pika](../../prompts/video/pika/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [runway](../../prompts/video/runway/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [seedance](../../prompts/video/seedance/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [sora](../../prompts/video/sora/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [veo](../../prompts/video/veo/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |
| [wan](../../prompts/video/wan/) | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked | TBD — not yet checked |

## Hard rule — no generation from an unchecked tool

> **A prompt card whose `tool.terms_checked` is absent, or older than the studio's
> re-check interval, must not be generated from.**

`tool.terms_checked` is a field on every prompt card
([../../standards/schemas/prompt_card.schema.json](../../standards/schemas/prompt_card.schema.json)).
It is an ISO date, and it points at the **date of the row in this register** for that
vendor — not at the day someone glanced at a pricing page.

| Condition | Consequence |
|---|---|
| `terms_checked` absent | The card does not render. No generation. |
| `terms_checked` older than the studio's re-check interval | The card does not render. The register row is re-checked first. |
| Vendor has no row in this register at all | The vendor is not in the pipeline. Adding one is a Rights & Clearances decision, not a generation-time convenience. |
| Row exists, `Q1` or `Q2` is `no` | The tool does not enter the pipeline. Core/02 §5. |

The re-check interval is a **studio** decision — it belongs in `studio.yaml`, is
sourced from the pack's `studio_must_decide` set if the pack cares, and is `TBD` for
every studio today. Until a studio sets one, the interval that applies is core's
floor: **before every delivery**, which is the one core/02 §5 states unconditionally.

**Enforcement maturity: NOT BUILT.** No code reads `terms_checked` today. The prompt
renderer that would refuse the card is **NOT BUILT**
([../../docs/status.md](../../docs/status.md)). Until it exists this rule is enforced
by the rights gate and by the person at the keyboard, which is exactly the weak
position the renderer is meant to fix.

## Filling a row

1. Open the agreement that applies to the tier the studio holds. Not a summary page,
   not a FAQ, not a blog post about the change.
2. Answer all seven questions, in the vendor's terms rather than your own.
3. Record the date, your role and name, and the URL you read.
4. Where a question has no clear answer in the document, write
   `TBD — <what would resolve it and who asks>`. An unanswerable question is a finding,
   not a blank.
5. If the answer to Q1 or Q2 is `no`, say so plainly and remove the vendor from the
   pipeline. Do not soften it — a soft `no` here is how a tool stays in use.

## What this register does not do

- It does not interpret the terms. A summary answer is a pointer to the clause, not a
  substitute for it.
- It does not constitute legal advice, and nothing in it should be read as a statement
  about any jurisdiction's law.
- It does not clear the *asset*. The asset is cleared in
  [clearance_log.md](clearance_log.md), which references the dated row here. Two
  registers, two purposes: this one is about the tool, that one is about the thing.
