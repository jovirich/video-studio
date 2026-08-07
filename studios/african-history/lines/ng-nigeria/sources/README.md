---
title: Sources and claims — Nigeria line
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# Source and claim registry

The evidence base for this line. Two registers, one relationship, and the whole
verification system rests on keeping them separate.

Maturity: **DESIGNED** for structure, **NOT STARTED** for content. **Both registers
are empty.** No source record and no claim record exists in this line.

## 1. Two registers, and why they are not one

```
records/SRC-NG-NNNN.yaml     the evidence      what exists, who made it, what it is
       ▲                                       reliable about, where it is held
       │ cited by
claims/CLM-NG-NNNN.yaml      the fact          what the production will say, at what
       ▲                                       confidence, on which sources
       │ referenced by
../productions/<code>/02_script/               "... {{CLM-NG-NNNN}} ..."
```

A source is not a fact. A source is an object with an author, a purpose, an audience,
and a history of handling — and the same source can be excellent evidence for one
statement and worthless for the next. Collapsing the two registers into "a
bibliography" loses exactly the information that makes the second judgement possible.

The split is also what makes the chain checkable. `studio_ops validate --sources` walks
from every reference in every script to a claim, and from every claim to its sources,
and fails the build on a break. It is **NOT BUILT**
([docs/status.md](../../../../../docs/status.md)); until it is, the chain is a human
discipline with no net under it, which is worth stating plainly rather than assuming
the tooling covers it.

The rule the registry exists to enforce is the pack's and is not restated here beyond
its one line:

> **No factual statement reaches a script without a claim ID, and no claim ID exists
> without at least one source record.**
> — [02_evidence_and_sourcing.md §1](../../../../../packs/documentary-history/02_evidence_and_sourcing.md)

## 2. [records/](records/) — source records

`SRC-NG-NNNN`. Currently empty.

One record per evidential item. Created **before** the item is read, so that custody,
access conditions, and rights status are captured while the item is in front of the
researcher rather than reconstructed from memory afterwards.

Every record carries a **`critique` block**, and it is the part of the record that
does the work. A citation is a location, not a warrant. The block answers who made
this and for whom, what they were in a position to know, what interest they had, what
has happened to the item since, and what its silence means. Write it with
[bias_register.md](../../../../../packs/documentary-history/methodology/bias_register.md)
open.

"Should be treated with caution" is not a critique. It is a way of appearing careful
while deciding nothing. A source is not reliable or unreliable; it is reliable *about
certain things*, and the block's only job is to establish which.

Tiers — T1 to T5, defined in
[02_evidence_and_sourcing.md §2](../../../../../packs/documentary-history/02_evidence_and_sourcing.md).
Two points that get misread, both worth repeating at line level because this line's
evidence base will make both live:

- **T5 includes any output of a language model, absolutely.** A model may locate,
  summarise, or structure. Its assertions are leads. A lead is verified against the
  actual document before it becomes anything at all.
- **The tier numbers describe what kind of verification a claim needs, not whose
  knowledge counts.** Oral tradition frequently preserves what no archive recorded,
  and a T1 colonial document is often less reliable about a society than the T4
  testimony of people inside it. The correct response is the right register with named
  attribution — never laundering a T4 account into `established` by finding a T3 that
  repeats it.

Sources spanning more than one line use the `STUDIO` scope (`SRC-STUDIO-*`) and live
in the studio's shared registry, not here. Trade, migration, and diaspora do not
respect modern borders, and duplicating a source per line produces two records that
disagree after the first amendment.

## 3. [claims/](claims/) — claim records

`CLM-NG-NNNN`. Currently empty.

One record per statement the production will make. Each carries the statement, its
**confidence register**, its sources with their tiers, and — for anything at
`established` — an explicit record of which sources are demonstrably *not* derived
from a common upstream.

That independence field is the defence against circular sourcing, which is the most
consequential failure in popular history and the hardest to see: a claim appears once
in the nineteenth century, is repeated down a chain of increasingly reputable
publications, and now appears in five "independent" sources. **Trace every claim to
its earliest attestation and record the chain.** Five repetitions of one source are
one source.

Registers — `established`, `probable`, `contested`, `inferred`, `traditional`,
`unknown` — and their corroboration requirements are in
[02_evidence_and_sourcing.md §3](../../../../../packs/documentary-history/02_evidence_and_sourcing.md)
and their verbal forms in
[01_editorial_standards.md §2](../../../../../packs/documentary-history/01_editorial_standards.md).

`unknown` is a legitimate, frequently correct value. A script that never uses it
across a full production is not a careful script; it is an incurious one, and the
Research Lead treats its absence as a smell.

## 4. IDs and lifecycle

| | |
|---|---|
| Scope | `NG` for this line, `STUDIO` for cross-line |
| Sources | `SRC-NG-0001`, `SRC-STUDIO-0001` |
| Claims | `CLM-NG-0001` |
| In prose | `{{CLM-NG-0001}}` — double braces, stripped at render, compiled into the citation appendix |
| In YAML | Bare string: `sources: [SRC-NG-0001]` |
| Filenames | `<ID>_<slug>.yaml`, ASCII only — diacritics belong in the content, never in a path |
| Allocation | By the toolkit, never by hand. **NOT BUILT.** |

Full grammar: [standards/id_system.md](../../../../../standards/id_system.md).

**IDs are permanent and never reused.** A claim the studio got wrong is marked
`retracted`, keeps its ID, and records what replaced it. Deleting it would produce a
registry that looks clean because its mistakes were removed — which destroys the audit
trail that justified building the registry at all, and makes the public correction log
([bible/corrections.md](../../../bible/corrections.md)) unverifiable.

## 5. Retention and restricted material

Scans, recordings, transcripts, and correspondence are retained in the asset store
under the source record's ID — never in git — for the life of the studio plus seven
years, or a shorter term where a contributor set one.

Restricted material does not enter the general asset store. Where a T4 recording
contains knowledge restricted by initiation, office, gender, or age, the protocol is
to stop, flag, and raise it with the Cultural Advisor; the default outcome is that it
is not used and the recording is returned or destroyed at the holder's direction. A
recording that exists is a recording that can leak, and the only reliable protection
is not keeping it.

## 6. Before any of this can begin

This line has **no research lead** and **no surveyed archive landscape** — conditions 1
and 3 of the three that block opening ([../README.md](../README.md) §2). The survey
comes first in practice as well as on paper: without it, source collection follows
accessibility, and accessibility follows who catalogued, digitised, and translated.
See [archive_landscape.md](archive_landscape.md).
