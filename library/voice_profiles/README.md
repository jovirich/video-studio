---
title: Voice profiles
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [audio-lead, rights-and-clearances]
---

# Voice profiles

Licensed synthetic voice profiles available for narration and reference reads across
the platform.

**Maturity: DESIGNED.** Empty. No voice has been licensed.

## A licensed voice is a consenting, compensated human

This folder holds configuration. What it *represents* is a person who agreed, in
writing, on stated terms, for a stated fee, that their voice may be reproduced
synthetically.

That is the whole content of this README, and everything below is a consequence of it.

Core/01 §1 permits generated narration only from a licensed, consenting voice, and
core/01 §2 prohibits absolutely the synthesis of a real person's likeness or voice
without documented consent or estate clearance — **including historical figures, for
whom no consent is possible**. A voice profile whose consent cannot be produced on
demand is not a library asset; it is a liability sitting in a folder that makes it easy
to use.

Consequences that are easy to state and easy to skip:

- **No profile is added before the agreement is signed.** Not for a test, not for a
  pitch, not "temporarily". A profile present in the library is a profile that will be
  used.
- **No cloning of a voice from recorded material** the studio happens to hold. Holding
  a recording is not consent to synthesise the speaker, and an interview release almost
  never contemplates it. Core/02 §7 requires the voice licence to cover synthetic
  reproduction **explicitly**.
- **Never a real or historical person's voice.** Core/01 §1, Voice row: never a real or
  historical person. This is not a rights question that a sufficiently well-drafted
  agreement resolves; it is a prohibition.
- **Withdrawal is honoured.** If the agreement grants withdrawal, its terms bind the
  library and every production using the profile. That is a scheduling and re-record
  risk, and it belongs in the risk register rather than being discovered.

## The consent scope lives in the clearance log

Not here. Here is the pointer.

Every profile carries a row in
[../../rights/permissions/clearance_log.md](../../rights/permissions/clearance_log.md)
with a `CLR-STUDIO-*` ID, under category *Interviews and testimony* for the consent
instrument and *Talent and crew* for the licence, and that row is where the scope is
recorded. The library manifest holds the ID and nothing else about the agreement,
because a scope duplicated in two places diverges, and the copy people read is the one
that is easier to reach.

What the clearance row must answer, at minimum:

| Question | Why |
|---|---|
| **Who** — the named person | A voice profile with no named human behind it is unusable, whatever the vendor says. |
| **What use** — narration, reference reads, character performance, promotional | Promotional and in-programme use are commonly separately consented. |
| **What content** — any subject-matter limits the person set | People consent to a project, not to a voice bank. A limit stated in conversation and not recorded is a limit that will be crossed. |
| **Territory, term, and expiry date** | As any licence. Record the expiry, not the duration. |
| **Withdrawal terms** | What happens to material already delivered, and what happens to material in production. |
| **Fee, and whether it is per-use or per-term** | Per-use fees with no owner are how a licence quietly lapses. |
| **Whether the vendor may train on the input** | The vendor's own terms also apply — see [../../rights/permissions/model_terms_register.md](../../rights/permissions/model_terms_register.md) Q5. Two agreements govern one voice, and they must be compatible. |
| **Credit wording** | Verbatim. The person is credited by name unless they asked not to be. |

Two agreements govern every profile here: the **person's** licence and the **vendor's**
terms. Either can prohibit a use the other permits. The narrower one governs.

## Disclosure

Synthetic narration is disclosed. Core/01 §3 requires the credits statement to name
every generative tool used by category, and requires that where a tool substitutes for
a craft role — VO explicitly among them — the studio says so rather than leaving the
absence unexplained. A licensed synthetic voice is not a loophole in that; it is a
case of it.

## Naming

```
voice_<person-slug>_<language>_<register>_v<NN>.yaml

voice_a-person_en_narration_v01.yaml
```

Lowercase, ASCII, hyphens within a field, underscores between fields, per
[../../standards/naming_conventions.md](../../standards/naming_conventions.md). The
person slug is the licensed person's own name as they wish to be credited, slugified —
not a nickname, not the vendor's internal voice ID, and not a character name. The file
should make it obvious that a specific human is behind it.

Language uses the code recorded in the line's language entry; where a voice is licensed
in more than one language, that is more than one profile, because the consent and the
performance are separately given.

## Manifest and storage

Profile configuration is YAML and is **not** gitignored — `library/**/*.yaml` is
re-included in [../../.gitignore](../../.gitignore). Any voice model artefacts or
sample audio the vendor produces are, and stay in the object store.

Per profile: the person's name as credited, clearance ID, vendor, vendor's voice
identifier, plan tier the profile depends on, languages, expiry date, withdrawal terms
reference, and the date the consent scope was last verified.

That last date is checked at every delivery alongside the model terms register. A
consent that was adequate at greenlight and a distribution footprint that grew after it
is the exact shape of the problem this folder exists to prevent.
