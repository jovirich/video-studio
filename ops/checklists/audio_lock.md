---
title: Audio lock gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [audio-lead]
---

# Audio lock — checklist

| | |
|---|---|
| **Gate key** | `audio_lock` |
| **Owner** | `audio-lead` |
| **Stage** | `07_audio_post` |
| **Blocks** | `09_delivery` |
| **Blocked by** | `picture_lock` |
| **Packs** | documentary-history. The other three packs combine this with picture in [picture_audio_lock.md](picture_audio_lock.md) |
| **Completed copy** | `07_audio_post/checklists/audio_lock.md` in the production folder |

Sound is where AI-assisted work is most likely to be quietly dishonest, because
audiences interrogate images and absorb sound. A soundscape asserts what a place
sounded like; the wrong birdsong is an anachronism a local audience hears instantly
and an outside audience never questions.

The core list below is
[../../packs/documentary-history/05_sound_and_score.md](../../packs/documentary-history/05_sound_and_score.md)
§9, which names this gate as the place it is enforced.

## What this signature certifies

> Loudness and true-peak targets met, all stems rendered including M&E, every proper
> noun pronounced per the VO record sheet and verified by a speaker of the language,
> no synthesised voice of a real or historical person.

## Checks

### The §9 list

- [ ] Every proper noun pronounced per the VO record sheet
- [ ] No synthesised voice of a real or historical person
- [ ] Music clearances logged; no sacred material used as underscore
- [ ] Ambience checked for period and place accuracy
- [ ] Loudness targets met; true peak in spec
- [ ] All stems rendered, including M&E
- [ ] Generated audio assets present in the provenance manifest

### Pronunciation — the check that decides regional trust

- [ ] Every proper noun in the script appears in the VO record sheet
- [ ] Each entry carries an **IPA transcription** and a **reference recording from a speaker of the language**
- [ ] The narrator received both before the session
- [ ] Pronunciation verified against the reference recordings **by a named person who speaks the language**. This is a named person on this gate, not a general responsibility
- [ ] Tone is correct in tonal languages. A word mispronounced by tone is frequently a different word — treat it as a factual error, because it is one

### Voice

- [ ] No identifiable real person's voice is synthesised without documented consent or estate clearance in the clearance log
- [ ] **No historical figure's voice is synthesised, in any circumstance.** A voice actor may read a documented quotation, credited on screen as a reading. A synthesised "voice of" is a fabrication of evidence and is prohibited outright
- [ ] No interviewee's voice is synthesised. Testimony airs in the speaker's own voice or is read by a credited actor with the speaker's agreement
- [ ] Where narration is synthetic, the voice is licensed from a consenting, compensated human, the credit names them, and the credits state the narration is synthetic — plainly, not in six-point type

### Testimony and archival audio

- [ ] No testimony re-timed, pitch-shifted, or "cleaned" in a way that changes meaning. Noise reduction and level correction only; anything further is logged on the asset
- [ ] Edits within a testimony answer are marked visually — a cut, not a seamless splice
- [ ] Hesitations may be removed; qualifications may not
- [ ] Archival audio restoration logged: what was done, by what process, to what original
- [ ] No archival audio re-synchronised to unrelated picture in a way implying they belong together
- [ ] No pitch or speed correction on early recordings without a note, since their original speeds are themselves contested

### Music

- [ ] Cue sheet complete, including entirely original score
- [ ] Composition rights and recording rights recorded separately for every licensed cue
- [ ] For licensed recordings of traditional music, the chain is recorded: who granted it and on what basis they held the right
- [ ] No library music under a sequence carrying cultural specificity
- [ ] **No sacred or ceremonial music as underscore, in any form, generated or recorded**
- [ ] Generated music complies with the pack's music policy and does not imitate a specific regional musical tradition
- [ ] Commissioned musicians paid and credited

### Ambience and sound design

- [ ] Ambience treated as reconstruction and held to the same standard as image: birds, insects, languages, animals, and industry are period- and place-specific claims
- [ ] Species and material accuracy checked
- [ ] Generated SFX logged in the manifest like any other generated asset
- [ ] Silence used where it belongs. Not every frame needs a bed

### Mix and delivery

- [ ] Integrated loudness on target per variant: −14 LUFS streaming, −23 LUFS ±0.5 broadcast
- [ ] True peak ≤ −1.0 dBTP
- [ ] Loudness range 6–12 LU
- [ ] Dialogue/VO seated at −18 to −12 LUFS short-term and consistently intelligible over the bed
- [ ] Noise floor ≤ −60 dBFS on narration
- [ ] All six stems rendered at full length, sample-accurate, one file each: `vo`, `testimony`, `music`, `ambience`, `sfx`, `me`
- [ ] **The M&E stem exists and has been checked by playing it.** It is mandatory from the first production; retrofitting it when a localisation deal appears costs more than producing it correctly now
- [ ] Mix checked on a phone speaker as well as monitors. Most of the audience is on a phone speaker
- [ ] Audio conformed to the locked picture, not to an earlier cut

## Do not sign if

- **Pronunciation was verified by someone who does not speak the language.** Checking
  a recording against another recording is not verification; it is comparison. This is
  the check that decides whether a series the region respects or one it mocks.
- **The M&E stem was rendered but never played.** An M&E with narration bleeding
  through is discovered by the dubbing house, at the worst possible moment, and the
  fix is a full re-mix.
- **Any voice in the cut is synthesised from a real or historical person.** There is
  no version of this that is acceptable, and no clearance that makes a historical
  figure's synthesised voice permissible.
- **A music cue is in the mix and not in the cue sheet.** Retrofitting a cue sheet
  for a distributor at short notice is a well-known and entirely avoidable emergency.
- **Ambience was designed for atmosphere without being checked as a claim.**
- **Loudness was checked on the mix bus and not on the rendered deliverable.**
- **You signed another gate on this production.**

## Signature

| Field | Value |
|---|---|
| Role | `audio-lead` |
| Person | |
| Date | |
| Pronunciation verified by | *name and language* |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
