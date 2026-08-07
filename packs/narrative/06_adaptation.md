---
doc: packs/narrative/06
title: Adaptation and source texts
status: active
version: 0.1.0
updated: 2026-08-07
owners: [story-producer, cultural-advisor]
---

# 06 — Adaptation and source texts

An audience that holds a text reads every choice as a claim about it. Which variant
you filmed, which line you cut, whose face you gave a figure, and what you left
ambiguous are all received as assertions — not about the story, but about the
tradition. That is true whether or not the production intended any of it, and it is
true most sharply where the text is not literature to its audience but scripture,
lineage, or law.

The pack's response is not to be careful. Careful is not a mechanism. The response is
to make the production say what it is doing, in writing, before it starts, and to
publish that with the work.

## 1. Interpretive stance

`studio_must_decide: interpretive_stance` — [pack.yaml](pack.yaml). Declared before
the first script. Certified at `greenlight`. Published with the work.

The stance is a short written statement answering four questions. It is not a
disclaimer, it is not a legal notice, and it does not go in eight-point type at the
end of the credits. It is an editorial position the production is willing to defend.

| Question | What a real answer looks like |
|---|---|
| **Which tradition?** | The specific tradition, community, or literary lineage the work draws from — named at the level of specificity that its holders would use, not a regional generalisation. "African folklore" names nothing. Compare [documentary-history](../documentary-history/07_cultural_sensitivity.md) §6. |
| **Which variant text?** | The specific recension, edition, translation, or line of transmission worked from — by name, and by edition where editions differ. Where several are used, which is primary and how conflicts resolve ([05_story_bible.md](05_story_bible.md) §6). |
| **Whose reading?** | The interpretive lens. A tradition's own reading, a scholarly reading, a contemporary reading, a deliberately revisionist one. Whose it is, and where it comes from. An unstated lens is still a lens; it is just unaccountable. |
| **What is the production explicitly NOT claiming?** | The most important of the four. Not the definitive version. Not endorsed by the tradition's authorities unless it is and that is documented. Not a historical account of events. Not a ruling on a disputed reading. Named specifically enough to be useful. |

**Why this is a gate and not a preface.** A production that has not decided its stance
does not become neutral; it makes the choice implicitly, shot by shot, and then
discovers what it decided when the audience tells it. Declaring the stance in advance
also converts a class of criticism from "you got it wrong" into "we disagree with your
stated reading" — which is a conversation, and is the honest shape of the
disagreement.

**Recorded and published.** The stance is a required field on the production record
([pack.yaml](pack.yaml) `record_extensions.production.interpretive_stance`), and it
is published with the work — in the description, the credits, or an accompanying
note, per the studio's decision. **TBD — the studio decides the publication surface**
and records it in `studio.yaml`; it does not decide *whether* to publish, which is
fixed here.

**Changing it.** The stance may change during production. It is changed the way a
locked record is changed: by the Showrunner, in writing, with the reason recorded, and
with the `greenlight` and `sensitivity` gates re-opened per core's cascade
([../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §4).
Drifting away from the declared stance without changing it is the failure this
section exists to prevent.

## 2. Textual fidelity

Adaptation departs from its source. That is what adaptation is. The rule is not
fidelity; it is **that every departure is intentional and recorded**, certified at
`script_lock` ([gates.yaml](gates.yaml)).

| Category | Definition | Recorded as |
|---|---|---|
| **Rendered** | The source's content, in the work's own form. | Nothing — this is the baseline |
| **Compressed** | Events merged, characters combined, a sequence shortened. | A departure record. Composite characters are named as such where the audience could otherwise take them for a single figure in the source |
| **Expanded** | Material invented in a gap the source leaves. Dialogue, interiority, a scene the source summarises in a clause. | A departure record. This is where most of an adaptation's screen time lives |
| **Reordered** | Chronology changed for narrative reasons. | A departure record |
| **Omitted** | Present in the source, absent from the work. | A departure record, with the reason — omission is read as judgement, especially where the omitted material is contentious |
| **Contradicted** | The work asserts something the source does not, or asserts the opposite. | A departure record, plus the Showrunner's signature, plus the sensitivity gate where a living tradition holds the text |
| **Imported** | Material from outside the source tradition brought in. | A departure record naming what was imported from where. Silently importing a motif from a neighbouring tradition is a specific and well-earned source of offence |

**The departure record** attaches to the script and names: what the source has, what
the work does, the category above, the reason, and who decided. Recording it costs
minutes. Not recording it means the production cannot answer the one question its
audience will actually ask, which is *why did you change that?*

**Expansion is the honest word for invention.** A film that invents a childhood for a
figure the source introduces as an adult has invented a childhood. That is legitimate
and it is not fidelity; describing it as fidelity is what turns a defensible choice
into a broken promise.

## 3. Variant traditions

Living traditions are not single texts, and treating them as one is itself an
interpretive act — usually one that privileges whichever version was written down,
translated, or printed by whoever had a press.

- **Name the transmission, not just the text.** Who holds this version, where, and how
  it reaches the production — manuscript, print edition, translation, recorded
  performance, or a living transmitter who told it to a researcher. A translation is a
  reading, and it belongs in the stance at §1.
- **Divergence is content.** Where variants differ interestingly, the work may say so
  — in the piece, in accompanying material, or in the published stance. This is the
  narrative-fiction analogue of documentary's rule that uncertainty is engaging
  material rather than an embarrassment
  ([documentary-history](../documentary-history/03_narrative_doctrine.md) §5).
- **Do not launder a minority variant into the standard one**, and do not do the
  reverse. Adopting a variant because it suits the story is fine and is recorded as
  such under [05_story_bible.md](05_story_bible.md) §6; adopting it and presenting it
  as *the* tradition is not.
- **A synthesis exists in no tradition.** Where the work combines variants, that is
  declared at §1 under "what the production is not claiming".
- **Where the tradition has custodians, transmission is a relationship**, not a
  research method. Custodians are named, paid, credited, and given the work — the same
  standard as [documentary-history](../documentary-history/07_cultural_sensitivity.md) §5
  and §7, which this pack adopts unchanged rather than restating in a weaker form.

## 4. Obligations where the text is living scripture

Distinct from adaptation of a closed literary work, and treated separately because the
obligations are different in kind rather than in degree. A community that holds a text
as scripture is not an audience with a strong preference; the depiction bears on
practice, authority, and belonging.

**Standing requirements:**

1. **A named advisory relationship before the first script.** The line-opening
   condition `source_tradition_advisor_agreed` in [pack.yaml](pack.yaml) is not
   satisfied by having read widely. It requires a person or body, in that tradition,
   who has agreed to advise, on recorded terms including fee, credit, review rights,
   and the right to withdraw.
2. **The stance at §1 states the relationship honestly.** Advised by is not endorsed
   by. Consulted is not approved. Overstating the relationship is worse than not
   having one, because it borrows authority that was not given.
3. **Restricted material is not depicted without a ruling.** Material restricted by
   initiation, office, gender, age, or occasion is not depicted, and is not depicted
   merely because it circulates freely — wide availability is not consent. This pack
   adopts [documentary-history](../documentary-history/07_cultural_sensitivity.md) §3
   in full; a fiction framing does not weaken it, and in some traditions makes it
   worse.
4. **Depicting a figure the tradition holds sacred is a decision, not a casting
   choice.** Some traditions prohibit depiction outright; some restrict it by form;
   some are indifferent. The production does not guess. It asks, records the ruling,
   and abides by it. Where the tradition prohibits depiction and the production
   proceeds anyway, that is an editorial decision the Showrunner makes in writing,
   after a sensitivity ruling, disclosed in the stance — not a thing that happens
   because the script needed the character on screen.
5. **The community sees the work before release**, in a form they can access, as with
   [documentary-history](../documentary-history/07_cultural_sensitivity.md) §7.
6. **Rights, permissions, and the legal status of a text vary by jurisdiction** —
   whether the text is in the public domain, whether a particular translation or
   critical edition is separately protected, and whether any body holds enforceable
   rights over its use. This pack states no rule. **Escalate** to
   [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §3
   and to qualified advice for every territory in the distribution footprint.

## 5. When the sensitivity gate's hold authority applies

The `sensitivity` gate is owned by the Cultural Advisor and carries `hold_authority`
([gates.yaml](gates.yaml)). Core defines what a hold is and requires that any
contributor may raise one, that it takes effect immediately, that only the designated
authority releases it in writing, and that the person who raised it is never penalised
([../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §6).
This pack designates the Cultural Advisor as that authority and specifies the
categories.

**A hold may be raised on any of the following, by anyone, at any stage:**

| Category | Trigger |
|---|---|
| Sacred, restricted, or initiatory material | Any depiction, reference, or reconstruction of it — §4 item 3 |
| A figure the tradition holds sacred | Any depiction, any voicing, any invented dialogue attributed to them |
| Ritual, liturgical, or sacred speech and music | Any use, including as underscore |
| A variant resolution touching doctrine or authority | Where the choice between variants bears on a live question inside the tradition |
| Depiction of a real people, place, or community | Where the treatment could be read as degrading, defamatory, or as taking a side in a live dispute |
| An invented departure attributed to the tradition | Category `contradicted` or `imported` at §2, on material the tradition holds as scripture |
| Naming and language | Which name form a people, place, or figure is given — see [documentary-history](../documentary-history/09_localization.md) |
| Human remains, burial, and ancestor material | Any depiction |

**Three properties of the hold, which are not negotiable at studio level:**

1. **It applies before generation, not before publication.** The gate runs at
   `00_brief`, `02_script`, and `08_review` and blocks `05_assets`
   ([gates.yaml](gates.yaml)). Once a striking image exists, the argument about
   whether it should exist becomes much harder to win — this is
   [documentary-history](../documentary-history/07_cultural_sensitivity.md) §2's
   reasoning and it transfers exactly.
2. **The Showrunner cannot unilaterally release it.** Disagreement escalates to a
   written ruling involving the advisory contact for the tradition concerned. This is
   the one structural check on the Showrunner's editorial authority in this pack, and
   it exists because the cost of being wrong is borne by people outside the studio.
3. **A hold on a locked item re-opens the gates that locked it**, per core's cascade.

**What a hold is not:** a veto on adaptation, an objection to interpretation the
advisor disagrees with, or a route for a contributor to relitigate a creative
decision. The Cultural Advisor rules in writing, and the ruling states which category
above it rests on. A ruling that rests on no category is feedback — valuable, and not
a hold.

## 6. Inheritance and enforcement

Adds to core; loosens nothing. Inherits without modification
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2 —
no fabricated evidence, no unconsented likeness or voice including of historical
figures, no autonomous publication, and nothing generated presented as found material.
The last of those constrains adaptation directly: a fictional work may not present a
generated document, recording, or photograph as an authentic artefact of the tradition
it adapts, inside the fiction or outside it
([09_setting_fidelity.md](09_setting_fidelity.md) §5).

This pack replaces documentary's per-shot reconstruction mark with a single
production-level disclosure ([README.md](README.md)). That is a change of *mechanism*,
not of standard: the audience of a fiction is not at risk of mistaking the work for
evidence, so the per-shot mark protects nobody. The rule it implements — that
generated material is disclosed and never passed off as real — is unchanged.

| Standard | Gate | Mechanism |
|---|---|---|
| §1 | `greenlight` | Stance declared in writing on the production record; studio cannot greenlight without it |
| §1 | `technical_qc` | Stance published with the work on the studio's declared surface |
| §2 | `script_lock` | Every departure has a record with a category and a reason |
| §3, §4 | `sensitivity` | Advisory relationship agreed as a line-opening condition; rulings on file |
| §5 | `sensitivity` | Hold authority; blocks `05_assets` before generation, not after |
