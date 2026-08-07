---
doc: bible/09
title: Localization, language, and naming
status: active
version: 0.1.0
owners: [showrunner, cultural-advisor, audio-lead]
---

# 09 — Localization, language, and naming

Language is where a series about a region either earns local trust in the first
thirty seconds or loses it permanently. Mispronounced names and imposed exonyms are
read — correctly — as evidence that nobody from the place was in the room.

## 1. Production language

Primary production language: `TBD — Showrunner.` For the Nigeria line the working
assumption is English narration with substantial Nigerian-language content in
testimony, quotation, and naming; the line's position is set in
[../productions/ng-nigeria/languages/README.md](../productions/ng-nigeria/languages/README.md).

## 2. Orthography

Every language used gets an entry in the line's `languages/` folder stating:

- The **orthography standard** adopted (there is usually more than one, and the
  choice is political — record why).
- **Diacritics and tone marks are used correctly and completely.** Stripping
  diacritics because a font or a pipeline cannot handle them is not acceptable;
  change the font or the pipeline. This constrains typeface selection
  ([04_visual_language.md](04_visual_language.md) §9) and must be settled before
  brand design begins.
- Encoding: UTF-8 throughout, normalisation form NFC, verified at delivery.
- Capitalisation, hyphenation, and plural conventions for names in that language.

## 3. Naming policy

For every person, people, place, and polity:

| Question | Rule |
|---|---|
| Which name form on screen? | The form used by the people concerned, unless a documented reason overrides. Recorded on the entity record with the reason. |
| Exonyms and colonial names | Not used as the primary form. May be given once, parenthetically, for viewer orientation — clearly marked as the colonial or external name. |
| Historical vs modern place names | The period-appropriate name is primary; the modern name is given once for orientation. Never silently substituted. |
| Contested names | Both forms given, with the dispute named. Never resolved silently by editorial preference. |
| Ethnonyms | Checked against how the group names itself. Several widely used names in the literature are external impositions. |
| Honorifics and titles | Rendered accurately, not translated into approximate European equivalents. A title is not a "king" because that is the nearest English word. |

## 4. Pronunciation

Mandatory workflow, no exceptions:

1. Every proper noun in a script is extracted into the **VO record sheet**
   (`02_script/vo_record_sheet.md`) automatically by
   `studio_ops report pronunciation --episode <code>`.
2. Each entry gets an **IPA transcription** and a **reference recording** from a
   speaker of the language, stored in the asset store against the entity record.
3. The narrator receives both before the session.
4. Pronunciation is checked at audio lock against the reference recordings by
   someone who speaks the language. This is a named person on the gate, not a
   general responsibility.

A tonal language mispronounced by tone is not a small error — it frequently produces
a different word. Treat it as a factual error, because it is one.

## 5. Captions and subtitles

- **Captions in the production language on every deliverable.** Not auto-generated
  and shipped; auto-generated and *corrected*, against the script and the VO record
  sheet.
- Non-production-language speech is subtitled, with the language named on first
  appearance.
- Subtitle style: max 2 lines, 42 characters per line, 1–7 second duration,
  reading speed ≤ 20 cps. Spec in [../standards/delivery_specs.md](../standards/delivery_specs.md).
- Formats: SRT and VTT minimum; TTML where the platform requires styled captions.
- Translated subtitles are produced by a human translator or human-reviewed; machine
  drafts are permitted as a first pass and are always reviewed. The translator is
  credited.

## 6. Dubs and localised versions

- The M&E stem is produced from episode one ([05_sound_and_score.md](05_sound_and_score.md) §7),
  which is what makes a dub possible later at reasonable cost.
- On-screen text (titles, lower thirds, map labels, the reconstruction mark) is kept
  in separate graphics layers so a localised version does not require a re-render of
  the picture. This is a pipeline requirement, not a nice-to-have — enforce it in the
  edit project structure.
- A dub does not change a claim. Translated narration goes through the same
  fact-check reference chain; `studio_ops validate --sources` runs on translations too.

## 7. Quotation and translation

- Original-language quotation appears on screen alongside the translation where
  practical.
- The translator is named. A translation is an interpretive act and is credited as
  one.
- Where a translation is contested or a term is untranslatable, say so rather than
  choosing quietly.
- Retranslating from an intermediate language is recorded as such on the claim; it
  materially weakens the evidentiary chain.

## 8. Text rendering QC

Enforced at picture lock:

- [ ] All diacritics and tone marks present and correctly positioned
- [ ] No mojibake, no fallback-glyph boxes, no dropped combining marks
- [ ] Font covers every character used in every language on screen
- [ ] Right-to-left text (where applicable, e.g. Ajami script) renders correctly
- [ ] Caption files validate and match the locked audio
- [ ] Names match the entity records exactly — checked mechanically, not by eye
