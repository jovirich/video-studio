---
doc: packs/narrative/08
title: Performance and voice
status: active
version: 0.1.0
updated: 2026-08-07
owners: [audio-lead]
---

# 08 — Performance and voice

## 1. Performance source

`studio_must_decide: performance_source` — [pack.yaml](pack.yaml). Decided at studio
level before the first line opens. Consent scope must cover it, and consent obtained
without stating the AI processing scope does not cover AI processing.

The studio declares, per character class, where the performance comes from:

| Source | What it means | What it requires |
|---|---|---|
| **Cast performer** | A person performs; the work uses their face, body, or voice as captured. | Ordinary talent agreement, **plus an explicit statement of what may be generated from, over, or around the performance**, what may be trained on, for what term, and in what territories. Silence is prohibition. |
| **Licensed synthetic voice** | A voice model licensed from a vendor, or built from a consenting voice donor. | The licence, checked for narrative and commercial use; the donor's documented consent; vendor terms recorded per [../../rights/permissions/](../../rights/permissions/) and re-checked before delivery ([../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §5). |
| **Both** | Cast performers for principals, synthetic for background, or a cast performance extended synthetically. | Everything above, plus a written boundary: which characters, which lines, and where the seam is. |

Recorded per character on `anchors.performance_source`
([05_story_bible.md](05_story_bible.md) §3), because a studio-level default that is
never checked per character is how an exception becomes the practice.

**Two rules that hold whatever is chosen:**

1. **A voice is a likeness.** Everything core says about synthesising a face applies
   to synthesising a voice, without reduction. A voice model built from a person's
   recordings is that person's likeness in another medium, and the fact that the
   output is not visually recognisable does not change what it is derived from.
2. **The performer is credited and paid.** A cast performer whose captured performance
   is extended, retimed, relit, or otherwise processed generatively is still the
   performer of every frame that derives from them, and is credited as such. Where a
   generative tool substitutes for a craft role, the studio states so in the credits
   rather than leaving the absence unexplained
   ([../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §7).

### 1.1 What core prohibits, and why it bites harder here

> **Synthesising a real person's likeness or voice without documented consent or
> estate clearance — including historical figures, for whom no consent is possible.**
> — [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2 item 2

Authors adopting this pack routinely expect that prohibition to be a documentary rule.
It is not; it is core, and core binds every studio. It reaches further into narrative
work than into documentary, because narrative is the genre that *wants* to put real
people on screen.

**The rule, applied:**

> A narrative film about a historical figure may depict them **via a cast performer**.
> It may not **synthesise their actual face or voice**.

That distinction is the whole of it, and it is sharper than it first sounds:

| Doing this | Position |
|---|---|
| Casting a performer who resembles the figure, and filming them | **Permitted.** This is how the medium has always worked. The performer's own likeness rights are contracted normally. |
| Generating an environment, costume, or crowd around that captured performance | **Permitted.** Provenance recorded; the performance itself unaltered in identity. |
| Building a character reference or trained adapter from photographs of the historical figure | **Prohibited.** This is synthesising their likeness. The mechanism at [07_visual_continuity.md](07_visual_continuity.md) §2 does not launder it. |
| Generating a face that is a recognisable reconstruction of the figure's actual face | **Prohibited**, whether the input was photographs, portraits, or a description. The test is what the output is recognisable as, not what went in. |
| Training a voice model on recordings of the figure, or cloning their voice from archive | **Prohibited.** No consent is possible from the dead, and this pack does not treat impossibility as permission. |
| A cast performer *interpreting* the figure's voice — accent, cadence, manner | **Permitted.** That is acting. |
| Generating a face "inspired by" the figure but not recognisable as them | **Permitted**, and the boundary is judged by the Cultural Advisor at the sensitivity gate, not by the person who made it. |
| Any of the above for a **living** person | **Prohibited without their documented consent**, and fictionalised depiction of real living people is outside this pack entirely — [README.md](README.md). Escalate. |

**Why no exception exists for the dead.** The prohibition is absolute in core, with no
override flag, and the reason is that consent is the mechanism — not harm. A dead
person cannot consent, cannot correct the record, and cannot decline. Estates may hold
enforceable rights in some jurisdictions and not others, and that is a separate
question from this one: **estate clearance is necessary where it applies and is never
sufficient on its own**, because the clause requires documented consent *or* estate
clearance and the studio's own standard is the higher of the two. Where an estate
exists and grants clearance, the studio may proceed; where no estate exists, the
absence is not a permission. Jurisdictional post-mortem personality rights differ
sharply and change — **escalate**, per
[../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §3.

**Why it bites harder than expected in practice:** the tooling makes the prohibited
thing easier than the permitted thing. Casting, contracting, and filming a performer
is days of work; generating a recognisable face is a prompt. Every incentive in the
production points at the prohibited path, which is exactly why the rule is core's and
not the studio's to weigh.

## 2. Directing a performance the tool will process

Where captured performance passes through generative processing, the capture is
planned for it or the processing eats it.

- **Capture more than the shot needs.** Latitude in framing, angle, and duration is
  the cheapest insurance against a boundary artefact discovered in the conform.
- **Protect the eyes and the mouth.** Identity and intention live there, and they are
  the first things a generative pass degrades. Where a process is known to soften
  them, the shot is designed so the moment that carries the scene is not the moment
  under the heaviest processing.
- **Stillness survives; micro-motion does not.** Small continuous movement — breath,
  weight shifts, hair — is where temporal instability shows. A held performance
  processes cleanly; a restless one flickers.
- **The performer is told what will happen to the performance**, in the same
  conversation as the contract. This is a consent requirement, not a courtesy: a
  performer who learns at premiere what was done to their face has not consented to
  it, whatever the paperwork said.

## 3. Voice and dialogue

- **Casting a synthetic voice is casting.** It is decided at the character record,
  auditioned, and locked before recording. Swapping a voice model mid-production is a
  continuity break of the same kind as swapping a face, and audiences detect it faster.
- **A synthetic voice has a fixed configuration.** Model, version, settings, and seed
  where applicable are recorded on the character and on every asset. Vendor updates
  change voices without notice; an unrecorded configuration cannot be reproduced when
  a pickup line is needed in month nine.
- **Pickups and ADR are planned as a certainty.** With cast performers, a recall
  window is contracted up front. With synthetic voices, the configuration record is
  the recall window, and it is worth more than a re-audition.
- **Performance direction is not a prompt parameter.** Intention, subtext, and the
  reason a line lands are decided by a person and then implemented, whichever source
  is used. A synthetic voice will produce a fluent reading of a line nobody has
  decided the meaning of, and fluency is what makes that failure hard to hear.
- **Language, accent, and name pronunciation** are decided deliberately and recorded on
  the character record. Where the work uses a real language or a real people's names,
  [documentary-history](../documentary-history/09_localization.md)'s discipline
  applies: the name form used on screen is a choice, it is recorded, and it is a
  sensitivity category under [06_adaptation.md](06_adaptation.md) §5. Synthetic voices
  mispronounce unfamiliar names confidently and consistently, which is worse than
  mispronouncing them variably, because it sounds authoritative.
- **Sacred, liturgical, and ritual speech** is not generated and not used as texture.
  [06_adaptation.md](06_adaptation.md) §5 and
  [documentary-history](../documentary-history/07_cultural_sensitivity.md) §3, adopted
  unchanged.

## 4. Crowds, background, and non-speaking figures

- Generated background figures are permitted, with provenance recorded.
- **A generated background figure may not be recognisable as a real person.** The
  practical failure: models reproduce recognisable faces from their training
  distribution without being asked. Crowd shots are checked for it at the sensitivity
  and technical QC gates, and a recognisable face in a crowd is treated as an
  unconsented likeness, not as a coincidence.
- **A recurring background figure is a recurring character**, and picks up an anchor
  set the second time they appear ([07_visual_continuity.md](07_visual_continuity.md) §3).
- Crowd audio built from synthetic voices is unrestricted, provided no individual line
  is intelligible as a real person's voice.

## 5. Provenance and disclosure

Every performance asset carries the provenance record required by
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §4,
plus, for this pack:

```yaml
performance_source: cast | synthetic | hybrid
performer: <person, or `n/a`>
performer_consent: <contract or release reference>       # required when performance_source != synthetic
ai_processing_scope: <what the consent permits>          # required whenever any generative pass is applied
voice_model: { vendor: <vendor>, model: <model>, version: <version>, settings: <...> }
likeness_subject: <person id, or `original character`>
likeness_clearance: <clearance reference>                # required when likeness_subject is a real person
```

`ai_processing_scope` is the field that makes the consent enforceable rather than
decorative. It states what was permitted, so that a processing pass beyond it is a
detectable violation rather than a judgement call at delivery.

**Disclosure** is production-level in this pack, not per shot
([README.md](README.md)): the credits and description name the generative tools used
by category, including voice. The audience is not at risk of mistaking a fiction for
evidence, so a per-shot mark protects nobody; the standard is unchanged, only the
mechanism. Where a synthetic voice performs a character the audience would otherwise
take for a named human performer, the credits say so — an unexplained absence in a
cast list is its own kind of misleading.

## 6. Inheritance and enforcement

Adds to core; loosens nothing. §1.1 is core's §2 item 2 applied, not restated in a
weaker form, and this pack cannot grant an exception to it — a pack that wanted one
would have to amend core, with core's signatures and an impact statement naming every
studio affected ([../../core/05_amendment_log.md](../../core/05_amendment_log.md)).
Rights and consent per
[../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §7.
Templates: [../../templates/legal/](../../templates/legal/).

| Standard | Gate | Mechanism |
|---|---|---|
| §1 | Greenlight | Studio cannot greenlight with `performance_source` unresolved |
| §1.1 | `sensitivity` | Any real-person likeness or voice requires clearance on file; hold authority applies |
| §1.1 | `technical_qc` | `likeness_clearance` present wherever `likeness_subject` is a real person |
| §3 | `continuity_lock` | Voice configuration recorded before generation |
| §4 | `sensitivity`, `technical_qc` | Crowd faces checked for recognisable real people |
| §5 | `technical_qc` | `performer_consent` and `ai_processing_scope` present on every processed performance asset |
| §5 | `technical_qc` | Production-level AI disclosure present in credits and description |
