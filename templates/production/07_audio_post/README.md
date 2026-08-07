---
title: 07_audio_post — VO, score, mix, stems
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [audio-lead]
---

# 07_audio_post

Where the cut acquires its sound. Also where two claims get made that nobody
notices are claims: how a name is pronounced, and what a place sounded like.

## What goes here

| Path | What it is | In git? |
|---|---|---|
| `session/` | DAW session files | Yes |
| `mix_notes_v<NN>.md` | What changed in each mix pass | Yes |
| `loudness_report.md` | Measured integrated loudness, true peak, LRA | Yes |
| `cue_sheet_working.csv` | Working cue sheet; the delivered one lives in [../10_publish/](../10_publish/) | Yes |
| `stems/` | Rendered stems | **No** — gitignored; they are large and derivable |

## Before this stage starts

- **Picture lock is signed.** Mixing to a moving cut means mixing twice, and the
  second mix is done under a deadline.
- **The VO record sheet is complete** — every proper noun with IPA, a reference
  recording from a speaker of the language, and a named verifier
  ([../02_script/_TEMPLATE_vo_record_sheet.md](../02_script/_TEMPLATE_vo_record_sheet.md)).

## Two things here are editorial, not technical

**Pronunciation.** A mispronounced endonym is the most reliable signal available to
the people the material belongs to that nobody was consulted. It is also, uniquely,
a defect that no amount of post can fix cheaply — it is a re-record. The sheet exists
so the decision is made by a speaker of the language, in advance, rather than by
whoever is in the booth, from spelling, at speed.

**Ambience.** A sound bed asserts what a place sounded like. That is a
reconstruction, subject to the same evidence discipline as a reconstructed image,
and it is the one reconstruction that routinely ships without anyone having decided
it was one — because nobody thinks of a bed as a claim. Each bed's basis is recorded
on the shot record's `audio.ambience` field.

## Voice: the absolute limits

- **No synthesised voice of a real or historical person.** Not with a disclaimer,
  not as a "reference read" that survives into the mix, not for a figure long dead.
  For a historical person consent is impossible, so the question does not arise.
- A synthetic **narration** voice, where used at all, is licensed from a consenting
  living person under an instrument that forbids training and names languages,
  territories, and term.
  [../../legal/likeness_and_voice_consent.md](../../legal/likeness_and_voice_consent.md).
- Testimony is never re-voiced, re-timed to change meaning, or cleaned to the point
  of altering what was said. Repair noise, not content.

## Before this stage can be left

The **audio lock** gate is signed by the Audio Lead, certifying:

1. **Loudness and true peak meet spec** — measured and reported, not eyeballed on a
   meter. Targets in [../../../standards/delivery_specs.md](../../../standards/delivery_specs.md) § Audio.
2. **All stems rendered, including M&E**, full length, sample-accurate to the master,
   one file each. The M&E stem is what makes a dubbed version possible later;
   producing it after the fact means rebuilding the mix.
3. **Every proper noun pronounced per the VO record sheet**, verified by a speaker
   of the language.
4. **No synthesised voice of a real or historical person appears.**
5. **The cue sheet is complete** — every cue, its duration, its usage type, and its
   rights basis. An incomplete cue sheet blocks the rights gate, not this one, which
   means the problem surfaces one stage later than it was created.
