---
title: Narration voice policy — Nigeria line
status: template
version: 0.1.0
updated: 2026-08-07
owners: [audio-lead, cultural-advisor]
---

# Narration voice policy

Who speaks this line, how, and how the audience is told.

Referenced from
[05_sound_and_score.md §1](../../../../../packs/documentary-history/05_sound_and_score.md).
Registered as `narration_voice_policy`, `unresolved`, in
[studio.yaml](../../../studio.yaml).

Maturity: **NOT STARTED**. Every decision below is `TBD — Audio Lead + Cultural
Advisor`. The workflows are fixed; the choices are not made.

> Sound is where an AI-assisted documentary is most likely to be *quietly dishonest*,
> because audiences interrogate images and absorb sound.
> — [pack 05](../../../../../packs/documentary-history/05_sound_and_score.md)

## 1. Casting

| Decision | Value |
|---|---|
| Narrator | `TBD — Audio Lead + Cultural Advisor` |
| Single narrator or ensemble | `TBD` |
| Continuity across the line | `TBD.` Whether the voice is fixed for the line, per season, or per production. Decide once — a narrator who changes without a reason reads as a production problem to the audience, because it usually is one. |
| Quotation reads | `TBD.` A voice actor may read a documented quotation, credited on screen as a reading. Distinct from narration, and audibly distinct. |
| Testimony | Never re-voiced. Testimony airs in the speaker's own voice, or is read by a credited actor **with the speaker's agreement** ([pack 05 §2](../../../../../packs/documentary-history/05_sound_and_score.md)). |

The constraint that outranks every casting preference is
[bible/00_charter.md](../../../bible/00_charter.md) §3: **the work must be legible and
non-condescending to an audience from the region it depicts.** A narrator whose
delivery treats the region as exotic to the listener has failed that test before the
first claim is made, regardless of how the voice tests elsewhere.

## 2. Accent

`TBD — Cultural Advisor + Audio Lead`, and the decision is recorded with its reasoning
rather than defaulted into. Whatever is chosen, three things are recorded:

- **What was chosen and why**, in terms of the audience relationship the charter
  defines — not in terms of what is easiest to cast or what is assumed to travel.
- **What the choice signals**, honestly. An accent is a claim about who is telling this
  history and to whom. There is no neutral option; a choice made without stating the
  signal has still made the signal.
- **What it does not license.** No accent choice permits a proper noun to be
  mispronounced. §5 applies to every narrator without exception.

## 3. Register and pace

| | |
|---|---|
| Reading age and assumed prior knowledge | `TBD — Showrunner`, via [bible/00_charter.md](../../../bible/00_charter.md) §3 (`audience`, unresolved). This policy cannot be finalised before it. |
| Tone | `TBD.` Constraint: the certainty registers in [pack 01 §2](../../../../../packs/documentary-history/01_editorial_standards.md) are *performed* as well as written. A narrator who delivers `probable` with the authority of `established` has overclaimed with a vocal choice, and no reviewer of the script will catch it. |
| Pace | 145–165 wpm, slower on dense passages, which the script marks ([pack 05 §1](../../../../../packs/documentary-history/05_sound_and_score.md)) |
| Handling "we do not know" | `TBD.` Delivered plainly, not apologetically. Uncertainty is content ([pack 03 §5](../../../../../packs/documentary-history/03_narrative_doctrine.md)), and a narrator who sounds embarrassed by it teaches the audience to hear it as a failure. |

## 4. Human or licensed-synthetic

Both are permitted by the pack. This line has not chosen: `TBD — Audio Lead +
Cultural Advisor`.

**If synthetic**, all of the following hold and none is optional:

- The voice is licensed from a **consenting, compensated human** whose agreement covers
  this use — documentary, this subject matter, these territories, this duration.
- **The human is credited by name.** A synthetic voice is not a way of not crediting
  anyone.
- The licence is recorded in the clearance log and re-checked before every delivery,
  alongside the vendor's terms ([core/01 §5](../../../../../core/01_provenance_and_ai_disclosure.md)).
- Every generated narration asset carries a provenance record in the production
  manifest like any other generated asset.

**Never synthesised, in any circumstance** — the absolute list from
[pack 05 §2](../../../../../packs/documentary-history/05_sound_and_score.md), repeated
here because this is the document an Audio Lead reads under deadline:

1. Any identifiable real person, living or dead, without documented consent or estate
   clearance in the clearance log.
2. **Any historical figure, in any circumstance.** A synthesised "voice of" a
   historical person is a fabrication of evidence and is prohibited outright. A voice
   actor reading a documented quotation, credited on screen as a reading, is the
   permitted alternative and is a different thing.
3. Any interviewee.

## 5. Disclosure

Where narration is synthetic, the credits state it **plainly. Not in six-point type.**

That phrasing is the pack's and is deliberate. Disclosure that technically exists and
practically cannot be read is the failure this studio's whole disclosure architecture
is built against — four required levels, of which the credits statement is one
([core/01 §3](../../../../../core/01_provenance_and_ai_disclosure.md)), and none of
which substitutes for another.

| Where | What it says | State |
|---|---|---|
| Credits | That narration is synthetic, naming the licensed voice and the tool by category | `TBD` |
| Published provenance summary | The same, machine-generated from the manifest | `TBD` |
| End card | `TBD — Visual Director`, per [brand_guide.md](../../../brand/brand_guide.md) §7 |

The governing test, applied to this decision as to every generative one: *if a viewer
learned exactly how this was made, would they feel informed or deceived?*

## 6. Pronunciation workflow

**Mandatory. No exceptions.** The workflow is
[pack 09 §4](../../../../../packs/documentary-history/09_localization.md); what is
`TBD` here is only *who* performs each step for this line.

```
1. Every proper noun in the script is extracted into the VO record sheet
   (02_script/vo_record_sheet.md), mechanically —
   `studio_ops report pronunciation --production <code>`   [NOT BUILT]

2. Each entry gets an IPA transcription
   and a reference recording from a SPEAKER OF THE LANGUAGE,
   stored in the asset store against the entity record

3. The narrator receives both before the session — not at it

4. At audio lock, pronunciation is checked against the reference recordings
   by a NAMED PERSON WHO SPEAKS THE LANGUAGE
```

| Step | Owner | State |
|---|---|---|
| Extraction | Pipeline Engineer — the tool is **NOT BUILT**, so this is currently manual and therefore currently unreliable | — |
| IPA transcription | `TBD — Cultural Advisor` to name a qualified transcriber per language | not engaged |
| Reference recordings | `TBD` — speaker per language, paid and credited | none exist |
| Verification at audio lock | `TBD` — **a named person on the gate**, per language, not a general responsibility | not named |

Step 4 is the one that decays first. "Someone will check the pronunciation" is not a
gate; a gate has a named owner, a written checklist, a recorded signature, and it
blocks ([core/04 §1](../../../../../core/04_review_gate_framework.md)). Where a
language on the register is tonal, this check is a **factual** check: a tone error
frequently produces a different word, and it is the error a regional audience hears
instantly and does not forgive, because it is heard — correctly — as evidence that
nobody from the place was in the room.

The languages this applies to are the confirmed entries in
[README.md](README.md), which currently number zero.

## 7. Recording and delivery

| | |
|---|---|
| Capture spec | [standards/delivery_specs.md](../../../../../standards/delivery_specs.md) § Audio. Noise floor ≤ −60 dBFS on narration. |
| VO seat in the mix | −18 to −12 LUFS short-term, consistently intelligible over the bed |
| Stems | `vo` delivered separately, always, plus the M&E pass — mandatory from the first production, because retrofitting it when a localisation deal appears costs more than producing it correctly the first time |
| Pickups and re-records | Logged against the script version, so a claim change after audio lock cascades correctly through the gates |

## 8. Blocked on

- `audience` and `production_language` — `unresolved` in [studio.yaml](../../../studio.yaml)
- The language register — [README.md](README.md), no entry confirmed
- An advisory contact — [../advisory/README.md](../advisory/README.md), **NOT STARTED**;
  without one there is nobody with standing to name a pronunciation verifier or to rule
  on the accent decision

This policy is not written by the Audio Lead alone. It is co-owned, and the second
signature is the one that is currently missing.
