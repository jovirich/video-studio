---
chain: archival_restoration
version: 1.0.0
status: active
updated: 2026-08-07
owners: [visual-director, rights-and-clearances]
---

# Chain — archival restoration

For **genuine archival material**: photographs, film, recordings, documents.

## This chain contains no generative steps

That is the entire point of it being a separate chain. The boundary between revealing
what is present and adding what is absent is structural here, not a matter of anyone
remembering it at 2am before a delivery.

If a step you want is not on this list, it does not belong in this chain.

## Steps

| # | Step | Tool | Notes |
|---|---|---|---|
| 1 | Verify rights | human | Clearance record exists; check whether cropping, colouring, or excerpting is restricted — many archive agreements restrict them |
| 2 | Ingest at maximum available quality | — | Never work from a compressed preview |
| 3 | **Preserve the original, untouched** | `studio_ops` | Separate asset record. This is the archive copy. |
| 4 | Non-generative correction | [adobe](../restoration/adobe/) / [resolve](../post/resolve/) | Levels, colour balance, dust and scratch, stabilisation, deinterlace, perspective. Each logged. |
| 5 | Conform | `studio_ops` | Frame rate and resolution. Original cadence preserved where it is historically informative. |
| 6 | Credit | human | Exact wording the rights holder requires, on screen |

## Explicitly not in this chain

| Step | Why |
|---|---|
| Generative upscaling | Invents detail the original does not contain |
| Face restoration | Invents a face |
| Colourisation | Asserts colours the record does not hold — of skin, textile, dye, landscape |
| Frame interpolation | Changes motion character, which is itself historical information |
| Inpainting damage | Fabricates content |
| Object removal | Alters a record |

## The documented exception

Any of the above may be permitted for a specific, argued reason. It requires:

- a written rationale on the asset record,
- approval from the gate owner responsible for evidence in the active pack,
- **on-screen indication** that the image has been altered, and what was done,
- the original available alongside.

The default answer is no. An exception that is granted routinely is not an exception.

## The honest alternative

Where an archival image is too damaged to use, the options in order are:

1. **Use it as it is.** Damage is part of the record and frequently belongs on screen —
   the state of what survives is often more interesting than a cleaned version.
2. **Show it briefly and narrate what it shows.**
3. **Replace it with a labelled reconstruction**, generated through
   [still_to_motion](still_to_motion.md), clearly marked as reconstruction rather than
   as a restored original.

Option 3 is honest. A generatively "restored" archival image presented as archival is
not, and the difference is invisible to the viewer — which is exactly why the studio
draws the line here rather than case by case.

## Provenance

Two asset records minimum: the untouched original and the corrected version, linked,
with the corrected version's `post_process` array listing every step and tool. The
original is never overwritten.
