"""Prompt-card gate — catches a card that contradicts itself.

Built because it cost a real generation. An edit to Character B's card replaced the
acceptance checklist but silently failed to replace the prompt, so the card asked for
a cheek birthmark, forbade a cheek birthmark in its negatives, and then checked for a
nose-bridge one. The operator followed the prompt, the model complied exactly, and the
candidate failed a checklist it was never given a chance to satisfy.

Nothing caught it. Schema validation could not: every field was individually valid.
The contradiction lived *between* fields.

So this gate reads a card the way a reader would — asking whether the thing it asks
for is the same thing it forbids and the same thing it checks. That is a narrow test,
deliberately: a general "does this prompt mean what the checklist means" check is not
mechanisable, but the flat contradiction is, and the flat contradiction is what
happened.

Maturity: IMPLEMENTED. Covers self-contradiction only; the staleness and
terms-currency checks originally specified for this gate remain unbuilt.
"""

from __future__ import annotations

import re

from ..config import Config
from ..frontmatter import is_template, read_yaml
from ..paths import iter_files
from ..result import Finding, GateReport, Severity, rel

GATE = "prompts"

# Words too common to carry meaning in an overlap test. A negative saying "no
# background detail" against a prompt that mentions a background is not a
# contradiction; a negative saying "cheek birthmark" against a prompt asking for one
# is.
STOPWORDS: frozenset[str] = frozenset(
    {
        "a",
        "an",
        "and",
        "any",
        "are",
        "as",
        "at",
        "background",
        "be",
        "by",
        "clear",
        "clearly",
        "detail",
        "environment",
        "for",
        "from",
        "front",
        "in",
        "into",
        "is",
        "it",
        "light",
        "lighting",
        "natural",
        "no",
        "not",
        "of",
        "on",
        "one",
        "or",
        "plain",
        "props",
        "resolved",
        "single",
        "skin",
        "small",
        "the",
        "to",
        "with",
        "neutral",
        "face",
        "hair",
        "dark",
        "brown",
        "black",
        "grey",
        "gray",
        "image",
        "shot",
        "view",
        "camera",
        "eye",
        "level",
        "focus",
        "frame",
        "colour",
        "color",
    }
)

MIN_PHRASE_WORDS = 2

# A negative's words must appear CLOSE TOGETHER in the prompt, not merely somewhere in
# it. "cheek" in a facial description and "birthmark" on the nose are eighty characters
# apart and mean nothing together; "birthmark high on the left cheek" is a phrase. Mere
# presence flagged the honest card as loudly as the broken one, which is how a gate
# gets switched off.
PROXIMITY_CHARS = 60


def run(cfg: Config) -> GateReport:
    report = GateReport(gate=GATE)
    root = cfg.root

    for path in iter_files(root, suffix=".yaml"):
        if is_template(path) or not path.name.endswith(".prompt.yaml"):
            continue
        data, error = read_yaml(path)
        if error is not None:
            report.findings.append(Finding(GATE, Severity.ERROR, error, rel(path, root)))
            continue
        card = data or {}
        report.files_checked += 1

        prompt = card.get("prompt")
        if not isinstance(prompt, dict):
            continue

        positive = " ".join(
            str(prompt.get(field) or "")
            for field in ("subject", "action", "setting", "composition", "texture")
        ).lower()
        if not positive.strip():
            continue

        for term in prompt.get("negative") or []:
            phrase = str(term).strip().lower()
            words = [w for w in re.findall(r"[a-z]+", phrase) if w not in STOPWORDS]
            if len(words) < MIN_PHRASE_WORDS:
                continue
            if _appear_together(words, positive):
                report.findings.append(
                    Finding(
                        GATE,
                        Severity.ERROR,
                        f"the prompt asks for what the negatives forbid: {term!r}",
                        rel(path, root),
                        rule="card-contradicts-itself",
                        hint=(
                            "Every significant word of this negative also appears in the "
                            "prompt. Usually it means an edit changed one and not the "
                            "other. The operator follows the prompt, so the card fails a "
                            "check it never gave the render a chance to pass."
                        ),
                    )
                )

    return report


def _appear_together(words: list[str], positive: str) -> bool:
    """True where every word occurs inside one PROXIMITY_CHARS window of the prompt.

    Not proof of contradiction — it is what a flat one looks like. A false positive
    costs a reader ten seconds; a miss costs a render and a director's afternoon.
    """
    spans: list[list[int]] = []
    for word in words:
        found = [m.start() for m in re.finditer(re.escape(word), positive)]
        if not found:
            return False
        spans.append(found)

    for anchor in spans[0]:
        if all(
            any(abs(position - anchor) <= PROXIMITY_CHARS for position in other)
            for other in spans[1:]
        ):
            return True
    return False
