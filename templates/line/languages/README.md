---
title: languages — orthography, diacritics, pronunciation
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [cultural-advisor, translator]
---

# languages

One entry per language appearing on screen in this line. Listed on
[../line.yaml](../line.yaml) and described in detail here.

```
languages/
└── <language-slug>.md   orthography standard, diacritic inventory, tone,
                         font requirements, style decisions
```

Governed by the pack's localisation document:
[../../../packs/documentary-history/09_localization.md](../../../packs/documentary-history/09_localization.md).

## What each entry records

| | |
|---|---|
| Orthography standard | Which one, and **who decided**. Several standards usually exist and choosing between them is an editorial act, not a technical one. |
| Diacritic inventory | Every mark used. This is what font selection is checked against. |
| Tone | Whether the language is tonal, and how tone is marked. It changes what an IPA transcription must contain to be usable. |
| Capitalisation, hyphenation, plurals | The decisions that otherwise get made differently by each writer |
| Naming conventions | Endonym vs exonym policy, honorifics, regnal forms |
| Reference speakers | Who verifies pronunciation, and their standing |

## Why fonts are decided at the line, once

Font selection depends on the **union of the diacritic coverage of every language on
the line**. A typeface that renders one language's marks correctly and drops another's
is discovered at the grade, and the fix is a re-render of every title in every
production on the line.

Check it once, here, against the actual inventory — not against a specimen sheet, and
not by looking at a sample in a design tool that silently substitutes a fallback
glyph. The fallback is exactly what makes the problem invisible until it is expensive.

## Diacritics in content, never in paths

Correct in the content — a name rendered without its marks is a different name.
Absent from filenames, because platforms normalise them differently and sync tools
corrupt them silently.
[../../../standards/naming_conventions.md](../../../standards/naming_conventions.md).

Captions are UTF-8, NFC normalised, no BOM.
[../../../standards/delivery_specs.md](../../../standards/delivery_specs.md).

## Translation

Every translation used on screen is credited to its translator, including
translations of quotations, and the edition translated from is recorded. An
uncredited translation presents an editorial act as a transcription.

Machine translation is a **draft**. It is reviewed and corrected by a named human
before it reaches a caption, a title, or a quotation, and that human is credited.
[../../legal/translator_agreement.md](../../legal/translator_agreement.md).
