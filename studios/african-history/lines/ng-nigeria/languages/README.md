---
title: Language register — Nigeria line
status: template
version: 0.1.0
updated: 2026-08-07
owners: [cultural-advisor, showrunner]
---

# Language register

Which languages appear on screen in this line, in what orthography, rendered how.

Maturity: **NOT STARTED**. The entries below are **candidates for confirmation**, not
decisions. Nothing in this register has been confirmed by a Cultural Advisor, because
this line has no advisory contact ([../advisory/README.md](../advisory/README.md)).

> Language is where a series about a region either earns local trust in the first
> thirty seconds or loses it permanently. Mispronounced names and imposed exonyms are
> read — correctly — as evidence that nobody from the place was in the room.
> — [pack 09](../../../../../packs/documentary-history/09_localization.md)

## 1. What this register is, and what it is not

It is an **administrative record of a production decision**: what will appear on
screen, in text and in speech, and in what form. It is not a description of the
region's languages, and it must never become one. A statement about a language — its
tone system, its orthographic history, its script, its distribution, how many people
speak it — is a research finding, carries a source record and a claim ID like anything
else, and does not belong in this file.

That distinction is why the entries below are almost entirely `TBD`. The studio can
say *"we may put this language on screen"* without research. It cannot say anything
*about* the language without it.

## 2. Candidate entries — none confirmed

Held in [../line.yaml](../line.yaml) under `languages`. Reproduced here for
readability; the YAML is authoritative.

| Candidate | ISO 639-3 | Script | Orthography standard | Tonal | Style guide |
|---|---|---|---|---|---|
| English | `TBD` | `TBD` | `TBD` | `TBD` | not written |
| Hausa | `TBD` | `TBD` | `TBD` | `TBD` | not written |
| Igbo | `TBD` | `TBD` | `TBD` | `TBD` | not written |
| Yoruba | `TBD` | `TBD` | `TBD` | `TBD` | not written |
| Nigerian Pidgin | `TBD` | `TBD` | `TBD` | `TBD` | not written |

Every cell is `TBD — Cultural Advisor`, and so is the **list itself**.

Read the table as a question, not an answer: *are these the languages this line puts
on screen, and are they the right set?* The Cultural Advisor confirms, removes, and
adds. The Showrunner separately sets the production language
(`production_language`, `unresolved` in [studio.yaml](../../../studio.yaml)); the
pack's working assumption for this line is narration in one language with substantial
regional-language content in testimony, quotation, and naming, and a working assumption
is not a decision.

The `Tonal` column is deliberately unfilled and is deliberately absent from
[line.yaml](../line.yaml) rather than set to a placeholder. The schema would accept a
boolean; recording one without research would be recording a finding this studio has
not made. It matters concretely: where a language is tonal, a tone error in narration
frequently produces a different word, and
[pack 09 §4](../../../../../packs/documentary-history/09_localization.md) treats that
as a factual error rather than a pronunciation slip.

### What confirming an entry requires

Per language, before the row is anything but a candidate:

- [ ] Cultural Advisor with relevant standing confirms the language belongs on the
      register, and in what role — narration, testimony, quotation, naming, on-screen
      text, captions
- [ ] The **orthography standard** is chosen and the choice is *justified in writing*.
      There is usually more than one standard, the choice is political, and an
      unexplained choice will be read as a position whether or not one was intended
      ([pack 09 §2](../../../../../packs/documentary-history/09_localization.md))
- [ ] The exact **diacritic and combining-mark inventory** the chosen orthography uses,
      written out as characters — not described in prose
- [ ] Whether the language is tonal, and how tone is marked in the chosen orthography
- [ ] Capitalisation, hyphenation, and plural conventions for names
- [ ] A named speaker who will verify pronunciation at audio lock
      ([voice_policy.md](voice_policy.md))
- [ ] A style guide written at `languages/<slug>.md`

## 3. Encoding and rendering

Fixed, not `TBD`, and inherited rather than decided here:

| | |
|---|---|
| Encoding | UTF-8 throughout, normalisation form **NFC**, verified at delivery |
| Filenames | ASCII only, always. Diacritics belong in the content; platforms and sync tools normalise paths differently and corrupt them silently ([standards/naming_conventions.md](../../../../../standards/naming_conventions.md)) |
| Stripping marks | **Prohibited.** If a font or a pipeline cannot carry a mark, the font or the pipeline changes ([pack 09 §2](../../../../../packs/documentary-history/09_localization.md)) |
| Text QC | Enforced at picture lock: marks present and correctly positioned, no mojibake, no fallback boxes, no dropped combining marks, font covers every character, names match entity records **checked mechanically rather than by eye** ([pack 09 §8](../../../../../packs/documentary-history/09_localization.md)) |

## 4. Why this register blocks brand design

**The union of diacritic coverage across the confirmed languages is the character set
a typeface must support. That set cannot be compiled until this register is confirmed,
and the typeface cannot be chosen until the set exists.**

The chain is short and it runs one way only:

```
this register confirmed
      │   which languages, and in what role
      ▼
orthography standard chosen per language        Cultural Advisor
      │   which marks are actually used
      ▼
diacritic coverage requirement compiled          Visual Director
      │   the union, as an explicit character set
      ▼
typeface tested against it and licensed          Visual Director + Rights
      │
      ▼
EVERYTHING ELSE IN BRAND DESIGN                  brand/README.md §3
```

Nothing in [brand/](../../../brand/README.md) can start ahead of this — not the logo,
not the colour system, not the title cards, not the lower thirds, not the
reconstruction mark. A face chosen on feel and found later to lack a mark leaves two
options: re-typeset every graphic already produced, or strip the mark. The second is
prohibited, so it is the first, and it arrives at picture lock.

Adding a language to this register **after** the typeface is selected re-opens the
selection. That is not a reason to keep the register short; it is a reason to confirm
it properly once, early, with the advisor in the room.

## 5. Naming policy

The rules are the pack's
([09 §3](../../../../../packs/documentary-history/09_localization.md)) and are not
restated. What this line owns is the **application**: every decision about which name
form appears on screen is recorded on the entity record, with its reason, and applied
mechanically from there
([../characters/README.md](../characters/README.md),
[../locations/README.md](../locations/README.md)).

Two applications that will recur in this line and are decided once rather than per
production:

- **Ethnonyms are checked against how the group names itself.** Several widely used
  forms in the literature are external impositions, and inheriting one because the
  sources use it reproduces the imposition while citing it.
- **Titles and honorifics are rendered accurately, not translated into approximate
  European equivalents.** A title is not "king" because that is the nearest English
  word; the translation imports a whole theory of the office.

Where a form is contested, both are given and the dispute is named. It is never
resolved silently by editorial preference, and "we picked the one our audience knows"
is editorial preference.

## 6. Documents in this folder

| Document | Holds | State |
|---|---|---|
| This file | The register, its confirmation requirements, and the brand dependency | candidates only |
| [voice_policy.md](voice_policy.md) | Narration voice: casting, accent, register, human vs licensed-synthetic, disclosure, pronunciation workflow | **NOT STARTED** |
| `<slug>.md` per language | Per-language style guide — orthography, marks, capitalisation, name conventions | none written |
