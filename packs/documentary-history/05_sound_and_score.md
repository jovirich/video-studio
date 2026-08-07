---
doc: bible/05
title: Sound and score
status: template
version: 0.1.0
owners: [audio-lead]
---

# 05 — Sound and score

Sound is where an AI-assisted documentary is most likely to be *quietly dishonest*,
because audiences interrogate images and absorb sound.

## 1. Narration voice

| | |
|---|---|
| Casting | `TBD per line.` The Nigeria line's position on accent, gender, and register is set in [../productions/ng-nigeria/languages/voice_policy.md](../../studios/african-history/lines/ng-nigeria/languages/voice_policy.md). |
| Human or synthetic | Both permitted. If synthetic, the voice is licensed from a consenting, compensated human whose agreement covers this use, and the credit names them. |
| Disclosure | Where narration is synthetic, the credits state it plainly. Not in six-point type. |
| Pace | 145–165 wpm. Slower for dense passages; the script marks them. |
| Pronunciation | Every proper noun in the VO record sheet carries an IPA transcription and a reference recording from a speaker of the language. This is non-negotiable and is the difference between a series the region respects and one it mocks. See [09_localization.md](09_localization.md) §4. |

## 2. Voices that are never synthesised

- Any identifiable real person, living or dead, without documented consent or estate
  clearance recorded in the clearance log.
- Any historical figure, in any circumstance. A voice actor may read a documented
  quotation, credited on screen as a reading. A synthesised "voice of" a historical
  person is a fabrication of evidence and is prohibited outright.
- Any interviewee. Testimony airs in the speaker's own voice, or is read by a
  credited actor with the speaker's agreement.

## 3. Interview and testimony audio

- Recorded to the spec in [../standards/delivery_specs.md](../../standards/delivery_specs.md) §Audio.
- Never re-timed, pitch-shifted, or "cleaned" in a way that changes meaning. Noise
  reduction and level correction only; anything further is logged on the asset.
- Edits within a testimony answer are marked visually (a cut, not a seamless
  splice). Removing a hesitation is fine; removing a qualification is not.
- The full unedited recording is retained per [02_evidence_and_sourcing.md](02_evidence_and_sourcing.md) §8.

## 4. Music policy

The hardest ethical question in the sound department, and it needs an explicit
answer before episode one.

| Category | Policy |
|---|---|
| **Original score** | Preferred. Composer credited and paid. Cue sheet maintained. |
| **Regional musicians, commissioned** | Strongly preferred where the score draws on regional idiom. Paying musicians from the tradition you are drawing on is both the right answer and the better-sounding one. |
| **Licensed recordings of traditional music** | Permitted with a licence *and* a check that the licensor actually held the right to grant it. Recordings of traditional performance are frequently licensed by parties with no relationship to the tradition. Record the chain in the clearance log. |
| **Library music** | Permitted for utility beds. Never for a sequence that carries cultural specificity. |
| **AI-generated music** | Permitted only as follows, and this is a hard boundary: `TBD — Showrunner + Cultural Advisor decision required before S01E01.` The default position pending that decision is: permitted for abstract, non-idiomatic texture and drones; **prohibited** for anything that imitates a specific regional musical tradition. Generating a pastiche of a living tradition to avoid paying its practitioners is the exact failure this studio should not commit. |
| **Sacred or ceremonial music** | Never used as underscore. Never generated. Its use in any form requires an advisory ruling. |

## 5. Ambience and sound design

- **Ambience is reconstruction and is held to the same standard as image.** A
  soundscape asserts what a place sounded like. Birds, insects, languages, animals,
  and industry are all period- and place-specific claims.
- Species and material accuracy is checked: the wrong birdsong is an anachronism
  that a local audience will hear instantly.
- Foley is built from real recordings where possible. Generated SFX are permitted
  and are logged like any generated asset.
- **Silence is a tool.** Not every frame needs a bed.

## 6. Archival audio

- Restoration is logged: what was done, by what process, to what original.
- Never re-synchronised to unrelated picture in a way that implies they belong
  together.
- Never pitch- or speed-corrected without a note, since early recordings' speeds are
  themselves contested.

## 7. Mix

| Target | Value |
|---|---|
| Integrated loudness | −14 LUFS for streaming/web delivery; −23 LUFS (EBU R128) for broadcast variants |
| True peak | ≤ −1.0 dBTP |
| Loudness range | 6–12 LU for documentary |
| Dialogue/VO seat | −18 to −12 LUFS short-term, consistently intelligible over the bed |
| Stems delivered | VO, dialogue/testimony, music, ambience, SFX, and an M&E (music + effects) pass for dubbing |

The M&E stem is mandatory from episode one. Retrofitting it later, when a
localisation deal appears, costs more than producing it correctly the first time.

## 8. Accessibility

- Captions on every deliverable, per [09_localization.md](09_localization.md) §5.
- Audio description track: `TBD` — decide before S01E01 whether it is in scope. If
  yes, the shooting script gains a description column and the mix gains a stem.
- Mix checked on a phone speaker as well as monitors. Most of the audience is on a
  phone speaker.

## 9. Sound QC checklist

Enforced at audio lock via [../ops/checklists/audio_lock.md](../../ops/checklists/audio_lock.md):

- [ ] Every proper noun pronounced per the VO record sheet
- [ ] No synthesised voice of a real or historical person
- [ ] Music clearances logged; no sacred material used as underscore
- [ ] Ambience checked for period and place accuracy
- [ ] Loudness targets met; true peak in spec
- [ ] All stems rendered, including M&E
- [ ] Generated audio assets present in the provenance manifest
