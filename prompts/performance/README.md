---
title: Performance and likeness
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, cultural-advisor]
---

# Performance and likeness

Lip sync, face animation, and performance transfer. The modality with the strictest
platform-level constraints, because it is the one that manufactures a person saying
something.

## Platform prohibitions

From [core/01 §2](../../core/01_provenance_and_ai_disclosure.md), binding on every
studio and not loosenable by any pack:

1. **No synthesis of a real person's likeness or voice without documented consent or
   estate clearance.**
2. **No synthesis of a historical figure, in any circumstance.** No consent is
   possible, and a synthesised historical performance is fabricated evidence.
3. **No alteration of archival footage of a real person.** Re-syncing an archival
   speaker's lips to different words alters a record.
4. **No generated testimonial or endorsement.** A synthetic person appearing to
   testify or endorse is fabricated evidence, whatever the genre convention.

These are not editorial preferences. They are the boundary between using a tool and
manufacturing evidence.

## What is permitted

| Use | Requirement |
|---|---|
| A consenting presenter, dubbed into other languages | Consent explicitly covers synthetic reproduction **and each target language** |
| A licensed narration voice | Contract covers this use; contributor credited |
| A cast performer playing a role in narrative work | Standard performer agreement plus AI processing scope |
| Performance transfer from a driving performer to a fictional character | Driving performer credited and compensated |
| Lip sync for a consented interviewee's dubbed version | Consent covers dubbing |

Note the pattern: **there is always a consenting, compensated human at the origin.**
Where there is not, the use is prohibited.

## Consent scope

A general appearance release does not cover this. Consent must state, explicitly:

- that synthetic reproduction of likeness and/or voice may occur,
- which languages and territories,
- for how long, and whether it survives the production,
- that the material will **not** be used to train a model or create a reusable voice
  or avatar beyond this scope,
- how to withdraw, and honestly what withdrawal can and cannot undo after release.

Template: [../../templates/legal/likeness_and_voice_consent.md](../../templates/legal/likeness_and_voice_consent.md).

Consent obtained without the AI clause is not consent for these tools. This is the
most common gap in existing contributor releases, and retrofitting it after the fact
is often impossible.

## Vendors

| Vendor | For |
|---|---|
| [hedra](hedra/) | Character performance from a still plus audio |
| [heygen](heygen/) | Presenter avatars and multilingual dubbing |
| [synclabs](synclabs/) | Lip sync to a new audio track |
| [runway-act](runway-act/) | Performance transfer from a driving video |

## Documentary-specific note

Under [documentary-history](../../packs/documentary-history/), this modality is
almost entirely unavailable, and that is correct. The desire to have a historical
figure speak is strong, and satisfying it fabricates the single most persuasive kind
of false evidence there is.

The permitted alternative: a voice actor reads a **documented** quotation, credited
on screen as a reading, with the source of the words named. That is honest, it is
often more affecting, and it is defensible.

## Disclosure

Any performance-synthesis use is disclosed in the credits, naming the tool and the
consenting contributor, and carries the pack's applicable on-screen labelling. There
is no tier of use small enough to skip this.
