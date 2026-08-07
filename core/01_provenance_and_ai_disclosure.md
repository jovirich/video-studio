---
doc: bible/06
title: AI disclosure and ethics
status: active
version: 0.1.0
owners: [showrunner, pipeline-engineer, cultural-advisor]
---

# 06 — AI disclosure and ethics

The studio uses generative tools heavily and says so loudly. The position is not
that AI-assisted documentary is a compromise to be concealed; it is that the
technique is legitimate precisely to the degree that it is disclosed and bounded.

## 1. Where generative tools are used

| Stage | Permitted use | Boundary |
|---|---|---|
| Research | Locating material, summarising documents you also read, translating drafts, structuring notes, generating search strategies. | **Model output is never a source.** It is T5 under [02_evidence_and_sourcing.md](../packs/documentary-history/02_evidence_and_sourcing.md) §2. Every lead is verified against the actual document. |
| Writing | Structural critique, alternative phrasings, tightening, readability checks. | The claims are the researcher's. A model may not introduce a fact, a date, a name, or a figure into a script. |
| Image | Reconstruction and interpretive imagery, texture, matte extension, upscaling, cleanup. | Never presented as archival. Never used to alter genuine archival material's content. |
| Video | Motion for reconstruction and interpretive shots. | As above. |
| Voice | Narration (from a licensed, consenting voice), and reference reads. | Never a real or historical person. See [05_sound_and_score.md](../packs/documentary-history/05_sound_and_score.md) §2. |
| Music/SFX | Texture, drones, utility SFX, subject to the music policy. | Never a pastiche of a living tradition. Never sacred material. |
| Post | Rotoscoping, tracking, cleanup, transcription, caption drafting, translation drafting. | Human review before delivery on anything that changes meaning. |
| Pipeline | Automation, validation, reporting. | No autonomous publishing. A human signs every gate. |

## 2. Where generative tools are prohibited

Absolute. No exceptions, no override flag.

1. **Fabricating evidence.** Generating an image, document, recording, or artefact
   intended or likely to be taken for a genuine historical item. This includes
   "restoring" a photograph in a way that invents content, and generating a document
   in a historical hand.
2. **Synthesising a real person's likeness or voice** without documented consent or
   estate clearance — including historical figures, for whom no consent is possible.
3. **Filling an evidentiary gap.** If the research does not know, the model does not
   get to decide. See [02_evidence_and_sourcing.md](../packs/documentary-history/02_evidence_and_sourcing.md) §9.
4. **Generating sacred, initiatory, or restricted material**, or a depiction of it,
   without an advisory ruling.
5. **Generating identifiable victims** of documented violence.
6. **Autonomous publication.** No pipeline path exists from generation to public
   release without human signatures at the gates.
7. **Training on, or generating in the style of, a living artist or a specific
   cultural custodian's work** without agreement.

`studio_ops validate --canon` enforces the mechanically checkable subset: missing
provenance, missing labels, `archival` class on a generated asset, likeness flags
without a clearance reference.

## 3. Disclosure

Disclosure operates at four levels and all four are required:

1. **In-frame mark** on every reconstruction and interpretive shot
   ([04_visual_language.md](../packs/documentary-history/04_visual_language.md) §7).
2. **An explainer card** at the first such shot in each episode.
3. **Credits statement** naming every generative tool used, by category. The
   template is in [../templates/episode/10_publish/credits_ai_statement.md](../templates/production/10_publish/credits_ai_statement.md).
4. **A public methodology page** per series, and a per-episode provenance summary
   published alongside the episode, generated from the manifest by
   `studio_ops report provenance`.

Level 4 is unusual and is the point. A viewer who wants to know exactly which shots
were generated, with which tool, from which prompt, can find out. That is a much
stronger claim to trust than a blanket "some imagery is AI-assisted."

## 4. Provenance record

Every generated asset carries, in the episode manifest:

```yaml
asset_id: AST-NG-S01E01-0142
provenance_class: reconstruction
tool: { vendor: <vendor>, model: <model>, version: <version> }
prompt_card: PC-NG-S01E01-0037   # the versioned card that produced it
seed: <seed>
parameters: { ... }
inputs: [ <reference asset ids or style anchor ids> ]
generated_at: <iso8601>
generated_by: <person>
post_process: [ upscale:<tool>, grade:<lut>, ... ]
evidence_basis: [ CLM-NG-0117, SRC-NG-0042 ]   # required for reconstruction class
label_applied: true
review: { sensitivity: <ref|n/a>, technical_qc: <signature> }
```

An asset without a manifest entry cannot be conformed into the edit. The pipeline
refuses it. See [../automation/studio_ops/pipeline/manifest.py](../automation/studio_ops/pipeline/manifest.py).

## 5. Model terms and rights

Vendor terms govern ownership, commercial use, indemnity, and training on your
inputs, and they change. [../sources/permissions/model_terms_register.md](../rights/permissions/model_terms_register.md)
records the current position per tool, the date checked, and the plan tier the
studio holds. It is re-checked before every delivery. A tool whose terms do not
permit commercial documentary use does not enter the pipeline, however good it is.

## 6. Data handling

- Unpublished archival scans, interview recordings, and restricted material are
  **never** sent to a third-party model endpoint unless the vendor contract
  includes no-training and the source's permission covers it.
- Contributor personal data never enters a prompt.
- Local/self-hosted models are preferred for anything touching restricted material,
  and that preference is recorded per source in its access conditions.

## 7. Labour

Generative tools change what the work costs; they do not change who it belongs to.

- Regional scholars, translators, language consultants, and knowledge holders are
  **paid**, credited by name, and given the opportunity to review the material they
  informed before it airs.
- Where a tool substitutes for a craft role (illustration, VO, score), the studio
  states so in the credits rather than leaving the absence unexplained.
- Consultation with a community is not sourcing; it is a relationship. It carries a
  fee, a credit, and a copy of the finished work.

## 8. The standard this document is written against

The question to ask of any generative choice is not "can we?" or "will anyone
notice?" It is:

> **If a viewer learned exactly how this shot was made, would they feel informed or
> deceived?**

If the honest answer is "deceived", the shot does not ship — regardless of how good
it looks and how much it cost. Everything above is an attempt to make that judgement
mechanical enough to survive a deadline.
