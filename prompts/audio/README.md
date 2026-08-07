---
title: Audio generation
status: active
version: 0.1.0
updated: 2026-08-07
owners: [audio-lead]
---

# Audio generation

Voice, music, and sound effects. The area where generative tooling is most likely to
be **quietly dishonest**, because audiences interrogate images and absorb sound.

## Platform prohibitions

Binding on every studio, from [core/01 §2](../../core/01_provenance_and_ai_disclosure.md):

- **No synthesised voice of a real person** — living or dead — without documented
  consent or estate clearance.
- **No synthesised voice of a historical figure, ever.** A voice actor may read a
  documented quotation, credited on screen as a reading. A "voice of" a historical
  person is fabricated evidence.
- **No synthesised interviewee.** Testimony airs in the speaker's own voice, or is
  read by a credited actor with the speaker's agreement.
- **No voice cloned from a recording whose consent did not cover it.** Interview
  consent forms must state this explicitly or they do not permit it.

## Vendors

| Vendor | For | Notes |
|---|---|---|
| [elevenlabs](elevenlabs/) | Narration, voice cloning, dubbing | Strong multilingual; pronunciation dictionaries |
| [resemble](resemble/) | Voice cloning, real-time | Consent-oriented tooling |
| [murf](murf/) | Stock narration voices | Utility work, temp tracks |
| [suno](suno/) | Music generation | See music policy caution below |
| [udio](udio/) | Music generation | As above |
| [adobe-podcast](adobe-podcast/) | Speech enhancement, restoration | Processing, not generation |

## Voice

### The licensed-voice model

Where narration is synthetic, the voice is licensed from a **consenting, compensated
human** whose agreement covers this specific use, and the credits name them. This is
not a formality — it is the difference between a tool and an uncompensated
substitution.

### Pronunciation is mandatory, not optional

Every proper noun goes through the VO record sheet with an IPA transcription and a
reference recording from a speaker of the language. Never trust a model's default
pronunciation of a name.

For tonal languages this is a factual matter: wrong tone frequently produces a
different word. It is checked at audio lock by someone who speaks the language.

### Direction, not description

Voice prompts are direction. Pace, emphasis, emotional register, where to breathe,
where to slow. Not "read this in a documentary voice".

### Consistency across a season

Lock: voice ID, model version, stability and similarity settings, and the
pronunciation lexicon. Record all of them on the card. A model update mid-season will
change the voice audibly, which is why the version is recorded.

## Music

The hardest ethical question in the audio department. Each pack sets its own policy;
[documentary-history](../../packs/documentary-history/05_sound_and_score.md) §4 is
the strictest and worth reading whatever pack you are under.

The recurring hazard: **generating a pastiche of a living musical tradition to avoid
paying its practitioners.** Commissioning musicians from the tradition you are
drawing on is both the right answer and the better-sounding one.

Where AI music is used:
- Abstract texture, drones, and beds — generally acceptable.
- Anything imitating a specific regional or cultural idiom — requires an explicit
  studio-level decision, and is prohibited outright under the documentary-history pack.
- Sacred or ceremonial music — never generated, in any pack.

Every cue, generated or not, goes on the cue sheet from production one.

## Ambience and SFX

**Ambience is a claim.** A soundscape asserts what a place sounded like — species,
languages, animals, industry, weather. In a documentary context it is reconstruction
and is held to the same standard as image. In any context, wrong birdsong is an error
a local audience hears instantly.

Foley from real recordings where possible. Generated SFX are permitted and logged
like any generated asset.

**Silence is a tool.** Not every frame needs a bed.

## QC

- [ ] No synthesised voice of a real or historical person
- [ ] Voice licence covers this use; contributor credited
- [ ] Every proper noun matches the VO record sheet, verified by a speaker
- [ ] Model version and settings recorded — a model update changes the voice
- [ ] Music cleared; nothing sacred used as underscore
- [ ] Ambience checked for period and place accuracy
- [ ] All generated audio present in the provenance manifest
- [ ] Loudness and true-peak targets met; M&E stem rendered
