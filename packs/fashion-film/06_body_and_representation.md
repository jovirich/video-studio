---
doc: packs/fashion-film/06
title: Body and representation
status: active
version: 0.1.0
updated: 2026-08-07
owners: [cultural-advisor]
---

# 06 — Body and representation

## 1. Why this is a gate rather than a value

A generative model has a prior about what a body looks like. It is narrow, it is
specific, and it will be applied to every frame the studio does not actively
constrain. Nobody in the production chooses it; it arrives as the default and leaves
as the studio's editorial position, because that is what a body of published work is.

Two properties make this different from an ordinary craft concern:

- **The default is invisible from inside.** Each frame looks like a reasonable
  casting choice. The pattern is only visible across a campaign, by which point it is
  the campaign.
- **It cannot be fixed in the edit.** By picture lock the bodies are the bodies. This
  is why the `representation_review` gate runs at `04_prompts` as well as `08_review`
  ([gates.yaml](gates.yaml)) — before generation, not after, on the same reasoning as
  [documentary-history](../documentary-history/07_cultural_sensitivity.md) §2.

The gate carries `hold_authority`. Core defines what a hold is and requires that any
contributor may raise one, that it takes effect immediately, that only the designated
authority releases it in writing, and that the person who raised it is never penalised
([../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §6).
This pack designates the Cultural Advisor.

## 2. Representation range

`studio_must_decide: representation_range` — [pack.yaml](pack.yaml). Decided once, at
studio level, before the first line opens. `studio_ops` refuses greenlight while it is
unresolved.

> **Without a stated range, the model's default becomes the studio's editorial
> position by accident.**

That sentence is the whole argument. A studio that has not decided has still decided;
it has just done so without anyone signing it, and it will discover what it decided
when someone assembles the season's stills side by side.

**The studio states a range on each of these axes**, in its `brand/` or `style/`
folder and referenced from `studio.yaml`. Values are **TBD — the studio decides**,
because a pack cannot set a house casting policy without prescribing the one thing a
brand's identity actually consists of. What the pack fixes is that each axis is
answered, in writing, in checkable terms.

| Axis | What must be stated | What the default does if you do not |
|---|---|---|
| **Body size and shape** | The range shown, and the distribution across a campaign — not just the extremes reached once | Converges on a single narrow build |
| **Height and proportion** | Range shown; and a floor stating that proportions must be anatomically possible | Produces elongated, impossible proportions that read as aspirational and are not achievable by anyone |
| **Skin tone** | The range shown, and the commitment that it is *rendered correctly* across that range — see §4 | Converges toward a narrow band, and renders the rest badly |
| **Age** | The range shown, and a floor. Where garments are worn by anyone who could read as a minor, that is a separate decision with its own review | Converges on a narrow young band |
| **Hair texture and style** | The range shown | Converges, and renders textured hair poorly |
| **Visible disability, assistive devices, and body difference** | Whether shown, and if so how — as subject or as incidental presence | Absent entirely. Absence is a position |
| **Gender presentation** | The range shown, and how garments are assigned across it | Follows the model's prior, which is rigid |

**Rules on the range, whatever values the studio picks:**

- **It is a commitment across a body of work, not a checkbox per shoot.** One shoot
  cannot represent a range; a season can. The review therefore looks at the campaign,
  and the studio records the distribution it achieved as well as the one it intended.
- **It applies to generated and cast bodies identically.** A studio that casts broadly
  and generates narrowly has a narrow published position.
- **It applies to background and incidental figures**, which is where the default
  reasserts itself most reliably because nobody is reviewing the crowd.
- **A stated range is checkable; an aspiration is not.** "Inclusive casting" fails this
  section. "Sizes X to Y appear in every campaign, and at least Z of the principal
  looks" passes it, whatever X, Y, and Z are.
- **The range is published or it is internal — the studio decides, once.** Publishing
  it is a commitment; not publishing it is not an exemption from meeting it.

## 3. Synthetic human policy

`studio_must_decide: synthetic_human_policy` — [pack.yaml](pack.yaml). Decided once,
at studio level, recorded in `studio.yaml`, and applied uniformly.

> **Deciding this shot by shot in the edit is how it goes wrong.** A studio that has
> not decided will use a synthetic body the first time a schedule slips, and will
> discover it has a policy when someone asks what its policy is.

**The decision has four parts. All four are answered together.**

| Part | Options | Default pending a decision |
|---|---|---|
| **Whether at all**, in commercial fashion content | Never / editorial and non-commercial only / permitted with disclosure / permitted for specified roles only (background, obscured, non-garment-bearing) | **Never.** The safe default is that a body selling a physical garment is a real body |
| **On-screen disclosure**, where permitted | Persistent mark for the duration / a card at first appearance / both. **Metadata alone is not an option** | Persistent on-screen mark. [gates.yaml](gates.yaml) fixes `disclosure_mode: on-screen-when-synthetic-human` — the studio decides the form, not whether |
| **Wording and design of the mark** | TBD — the studio specifies, in its `brand/` folder, with the legibility and dwell floors from [08_editorial_visual_language.md](08_editorial_visual_language.md) | TBD |
| **Which roles** | Principal / secondary / background / hands and details / not garment-bearing | TBD — the studio decides, and states whether a synthetic figure may wear a garment at all |

**Why disclosure is on screen and not only in metadata.** A garment shown on a body is
a claim about how that garment fits a person. Where the body is synthetic, the viewer
is being shown a fit that no one has. Metadata does not reach the viewer; the frame
does. It is also, in a growing number of territories, an emerging disclosure
obligation — **the specific requirements are jurisdiction-specific, differ, and are
changing. This pack states no legal rule. Escalate** for every territory in the
distribution footprint, and record the ruling.

**Standing prohibitions, which the studio's decision cannot loosen:**

1. **No generated body is presented as a specific real model.** A synthetic figure
   that is recognisable as a named person is that person's likeness, and using it
   without their documented consent is prohibited by
   [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md)
   §2 item 2 — not by this pack, and therefore not waivable by this studio.
2. **No real model's likeness is generated beyond the scope of their contract.**
   Including in a colourway, a campaign, a territory, or a term the contract does not
   cover. See §6.
3. **No generated body is used to depict a size, shape, age, or skin tone the studio
   did not cast**, as a substitute for casting it. Synthesising the range at §2 rather
   than casting it is the failure mode this section most needs to name: it produces
   the appearance of a commitment while making it cheaper not to keep one, and it
   takes work from the people the commitment was about.
4. **No generated body is recognisable as a real person by accident.** Models
   reproduce faces from their training distribution unprompted. Checked at the
   representation review and at technical QC; a recognisable face is treated as an
   unconsented likeness, not as a coincidence.
5. **No generated minor.** No exception, no editorial rationale.

**A studio on more than one pack decides once.** The synthetic-human question in
[product-marketing](../product-marketing/06_product_depiction.md) §7 is the same
question with a different surface. Two different answers inside one organisation is a
policy nobody can state.

## 4. Skin-tone rendering across the full range shown

Stating a skin-tone range at §2 and rendering it badly is worse than not stating one,
because it publishes the commitment and then fails it in every frame.

This is the most common technical failure in the genre and it is not a casting problem;
it is a capture, generation, and grading problem, and it compounds at each stage.

| Stage | What goes wrong | What is required |
|---|---|---|
| **Lighting** | Setups designed for one skin tone underexpose or flatten others. Fill and contrast ratios are not neutral | Lighting is designed for the range in the frame, not adjusted after |
| **Capture** | Exposure metered for the lightest subject in a group | Exposure and white balance decisions recorded per setup, referenced to a target |
| **Generation** | Models render textured hair and deeper skin tones with less detail, more artefacting, and a persistent pull toward the prior. Both fail more at the edges of the range | Anchor references per subject; artefact checks specifically at the range's edges, where the tools are weakest |
| **Grade** | A show LUT built on one skin tone crushes shadow detail, shifts hue, or desaturates others. This is where a technically correct shoot becomes an incorrect deliverable | The show LUT is evaluated against **every** skin tone in the campaign before it is locked, not against a hero frame |
| **Delivery** | Codec, colour space, and platform re-encode compress shadow detail preferentially | Checked on every deliverable variant, not the master |

**The rule:** the studio states its skin-tone rendering intent explicitly, and the QC
pass checks it on **every shot with people in it**, at every stage above. This mirrors
[documentary-history](../documentary-history/04_visual_language.md) §4, which reaches
the same conclusion from a different genre — evidence that it is a platform-wide
rendering failure rather than a genre-specific one.

**A show LUT is not neutral.** A grade that flatters one tone and degrades another is
an editorial position on whose skin the work is designed around, and it is expressed in
every frame regardless of who was cast.

## 5. Retouching policy

`studio_must_decide: retouching_policy` — [pack.yaml](pack.yaml). Decided at studio
level, applied uniformly, recorded in `studio.yaml`.

The pack's structural position, which the studio's decision operates inside:

> **Any alteration of a real person's body is a post-process step, logged like every
> other alteration, and covered by that person's contract — or it does not happen.**

| Category | Typical position | Always required |
|---|---|---|
| **Technical correction** — dust, sensor noise, stray hair, wardrobe tape, a wrinkle in the backdrop | Ordinarily permitted | Logged as `post_process` |
| **Temporary and non-characteristic** — a blemish, a bruise, a scratch that will be gone next week | TBD — studio decides. Frequently permitted with the model's agreement | Logged; contract covers it |
| **Characteristic features** — scars, marks, freckles, moles, body hair, skin texture, teeth, tattoos, stretch marks | TBD — studio decides. **Removing what makes a person that person is a different act from removing dust**, and the model's own preference is the strongest input | Logged; **contract explicitly covers it**; model consulted |
| **Body shape** — slimming, lengthening, reshaping, resizing | TBD — studio decides. Where permitted, disclosed per studio policy | Logged; contract explicitly covers it; **and see the garment consequence below** |
| **Skin tone alteration** | **Prohibited.** Lightening or darkening a person's skin is not retouching | — |
| **Face replacement or identity alteration** | **Prohibited** without documented consent for that specific use — core §2 item 2 | — |
| **Generative replacement of any body part** | Treated as body-shape alteration at minimum, and as identity alteration where the part is identifying | Logged; contract explicitly covers it |

**The garment consequence, which is this section's real teeth.** Reshaping a body
inside a garment reshapes the garment. A digitally slimmed waist changes how the
garment sits, hangs, and fits — which makes it a false claim about the garment under
[05_garment_fidelity.md](05_garment_fidelity.md) §6, verified at a different gate by a
different owner. Body retouching and garment fidelity are the same problem seen from
two directions, and a studio that permits liberal body retouching should understand
that it has also loosened its garment accuracy, which it is not permitted to do.

**Disclosure of retouching** is a studio decision and is
**jurisdiction-specific in several territories** — some require disclosure of body
alteration in commercial imagery, with differing thresholds and wording. This pack
states no rule. **Escalate**, per territory in the distribution footprint.

**What is never a studio decision:** the log. Every alteration appears in the asset
manifest as a `post_process` step per
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §4.
An alteration that is not logged did not happen, as far as the gate is concerned.

## 6. Model contracts and AI processing

The `model_contract` record ([pack.yaml](pack.yaml)) exists because the standard scope
of a modelling agreement predates every capability in this pipeline.

> **A contract that does not mention AI processing does not permit it.** Silence is
> prohibition, not permission.

Every `model_contract` states:

```yaml
id: MDC-<SCOPE>-0008
type: model_contract
status: draft | review | locked | superseded | retracted
model: <person>
agency: <where applicable>
shoot: [<production ids>]
usage: { media: [...], territories: [...], term: <...>, exclusivity: <...> }
ai_processing:
  permitted: true | false
  retouching: [<categories from §5 this contract permits>]
  body_alteration: true | false
  generative_extension: true | false      # generating around, over, or from the capture
  face_or_identity: true | false
  training: true | false                  # may their images train a model? separate permission
  synthetic_generation: true | false      # may a likeness of them be generated at all?
  reuse_beyond_this_shoot: true | false
disclosure_agreed: <what the model has been told will appear on screen>
review_right: <whether they see and may object to processed images, and by when>
withdrawal: { permitted: <...>, mechanism: <...>, what_it_cannot_undo: <...> }
```

Six rules on that record:

1. **Display rights and training rights are different permissions.** Licensing an
   image for a campaign is not licensing it as training data. They are contracted
   separately or the second does not exist —
   [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §7.
2. **Generative extension is separately scoped.** Generating a background around a
   captured model, extending the frame, or continuing a movement all derive new
   imagery from their likeness.
3. **The model is told, in the same conversation as the contract**, what will be done.
   A model who learns at publication what was done to their image has not consented to
   it, whatever the paperwork said.
4. **Reuse beyond the shoot is scoped and dated.** A likeness reused in next season's
   campaign because the file was on the server is a breach, and it is the most common
   one.
5. **Withdrawal has a mechanism, or it is not a right.** What comes down, how fast,
   and what cannot be undone after release, stated up front.
6. **The `stakeholder_approval` gate checks contracts against the cut**
   ([gates.yaml](gates.yaml)) — every use in this specific version, including AI
   processing where applied. Not against the shoot as originally scoped.

Templates: [../../templates/legal/](../../templates/legal/).

## 7. Inheritance and enforcement

Adds to core; loosens nothing. §3 prohibitions 1 and 4 and §5's identity-alteration
row are
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md)
§2 item 2 applied, not restated in a weaker form; a studio's synthetic-human decision
operates strictly inside them. Rights and consent per
[../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §7.
Provenance and `post_process` logging per §4 of the disclosure document. Hold authority
per [../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §6.

| Standard | Gate | Mechanism |
|---|---|---|
| §2 | Greenlight | Studio cannot greenlight with `representation_range` unresolved; reviewed across the campaign, not the shoot |
| §3 | Greenlight | Studio cannot greenlight with `synthetic_human_policy` unresolved |
| §3 | `representation_review`, `technical_qc` | Synthetic-human flag on the prompt card ([pack.yaml](pack.yaml)); on-screen disclosure present where required |
| §4 | `representation_review`, `picture_audio_lock` | Skin-tone rendering checked on every shot with people, on the graded frame, on every variant |
| §5 | `technical_qc` | Every alteration present in the manifest as `post_process` |
| §5 body shape | `garment_verification` | Reshaped bodies reshape garments — [05_garment_fidelity.md](05_garment_fidelity.md) §6 |
| §6 | `stakeholder_approval` | Contracts cover every use in this cut, including AI processing |

Checklists: [../../ops/checklists/](../../ops/checklists/). Gate definitions: [gates.yaml](gates.yaml).
