# Prohibited and flagged language

Checked by `studio_ops validate --canon` against narration, on-screen text, titles, *(NOT BUILT)*
descriptions, and thumbnails text. Two severities: **fail** blocks the build,
**warn** requires a reviewer to acknowledge.

The point is not word policing. Each entry below marks a place where language does
evidentiary work it has not earned, or where a phrase carries a framing the studio
has decided against.

## FAIL — unattributed attribution

These assert a source without naming one. Replace with a named holder of the view.

| Pattern | Replace with |
|---|---|
| "it is believed" / "it is thought" / "it is said" | Who believes it? Name them or the tradition. |
| "some historians say" / "many scholars think" | Which ones, and what do they actually argue? |
| "legend has it" | Whose legend? Recorded by whom, when? |
| "according to tradition" (bare) | Which tradition, held by whom, transmitted how? |
| "sources suggest" | Cite the source. |
| "experts agree" | If they do, cite two. If they don't, say `contested`. |

## FAIL — unsourced superlative or quantity

Any of the following in narration or on-screen text requires an adjacent claim ID:

`first`, `last`, `only`, `largest`, `oldest`, `richest`, `most powerful`,
`unprecedented`, `never before`, `greatest`, `biggest`, any bare numeral above ten,
any date, any named person, any named place.

The validator flags them; the claim ID clears them.

## FAIL — colonial framing

| Pattern | Why | Use instead |
|---|---|---|
| "discovered" (of an inhabited place) | Asserts that it did not exist until an outsider arrived | "reached", "arrived at", "first recorded by <name> in <year>" |
| "tribe" / "tribal" | Applied almost exclusively to African and Indigenous polities; implies pre-political organisation | Name the actual unit: kingdom, city-state, confederacy, lineage, people, clan |
| "primitive", "backward", "undeveloped", "simple" | Evaluative, not descriptive | Describe the specific technology or institution |
| "pre-history" for periods with oral, material, or written records | Equates history with European-style writing | "before written records", or name the period |
| "the dark continent", "darkest Africa" | — | Never |
| "witch doctor", "juju", "fetish", "idol" | Missionary-era pejoratives for religious practice | The tradition's own term, glossed |
| "native" as a noun | — | The people's own name for themselves |
| "chief" applied to all rulers regardless of office | Flattens distinct institutions into one colonial category | The actual title, glossed on first use |
| "civilised" / "uncivilised" | — | Never |
| "exotic", "mysterious", "lost civilisation" | Positions the subject as spectacle for an outside gaze | Describe what is actually not known and why |

## WARN — unearned grandeur

Permitted with a reviewer acknowledgement, because sometimes the evidence supports
them and sometimes the writer is reaching:

`vast`, `mighty`, `legendary`, `fabled`, `golden age`, `empire` (when the polity's
own structure is better described otherwise), `mysterious`, `enigmatic`,
`sophisticated` (when used as though it were surprising), `advanced for its time`.

That last phrase deserves special mention: it almost always encodes an assumption
about what one should have expected, and the assumption is usually the thing that
needs examining.

## WARN — false precision

`exactly`, `precisely`, a figure given to more significant digits than the source
supports, a date given as a year where the source gives a decade, "over N" and
"nearly N" without the underlying figure recorded.

## WARN — passive erasure

Passive constructions that remove an actor from an action: "the city was destroyed",
"the population was reduced", "slaves were taken". Someone did these things. Naming
them is both more accurate and better writing.

## FAIL — AI presentation

| Pattern | Why |
|---|---|
| "archival footage" / "rare photograph" / "recovered" applied to a shot whose `provenance_class` is `reconstruction` or `interpretive` | Direct violation of [../bible/06_ai_disclosure_and_ethics.md](../core/01_provenance_and_ai_disclosure.md) §2 |
| "restored" applied to a generated image | As above |
| "as it would have looked" without the reconstruction label present | Same claim, unlabelled |

## Configuring the checker

The machine-readable list is `standards/schemas/prohibited_patterns.json`, generated
from this document. Editing that file directly is a `studio/*` change requiring
Showrunner and Cultural Advisor sign-off — the list is canon, not configuration.

## Adding an entry

Anyone may propose one. Include: the pattern, an example of it doing damage, the
suggested replacement, and the severity. Language changes; a list written once and
never revisited becomes its own kind of problem.
