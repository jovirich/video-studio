"""Regression tests for the card-self-contradiction gate.

Two bugs are pinned here, both of which shipped silently.

The first is the defect the gate exists to catch: an edit replaced Character B's
acceptance checklist but not the prompt, so the card asked for a cheek birthmark,
forbade a cheek birthmark, and checked for a nose-bridge one. It cost a real
generation, and no schema check could have found it — every field was valid on its
own, and the contradiction lived between them.

The second is a defect in the gate itself. A shell heredoc wrote a literal backspace
byte (0x08) where the regex needed `\\b`, so every pattern was `\\x08word`, matched
nothing, and the gate reported clean on the very card it was written to catch. Source
inspection did not reveal it: a backspace renders as nothing. Hence
`test_gate_source_has_no_control_bytes` — the only check that would have caught it.
"""

from __future__ import annotations

from studio_ops.validate.prompts import PROXIMITY_CHARS, _appear_together

BROKEN = (
    "rounder face, softer jaw, broader cheek area, medium-width nose. a small "
    "circular dark birthmark high on the left cheek, clearly resolved."
)

HONEST = (
    "rounder face, softer jaw, broader cheek area, medium-width nose, dark brown "
    "eyes. a small round dark birthmark centred on the bridge of the nose, between "
    "the brows, on the midline, clearly resolved."
)


def test_catches_the_contradiction_that_cost_a_generation() -> None:
    assert _appear_together(["cheek", "birthmark"], BROKEN) is True


def test_does_not_flag_the_corrected_card() -> None:
    """The honest card names a cheek and a birthmark — far apart, and unrelated.

    Flagging this would be worse than not flagging the broken one. A gate that cries
    on correct cards is a gate someone switches off.
    """
    assert _appear_together(["cheek", "birthmark"], HONEST) is False


def test_absent_word_is_not_a_contradiction() -> None:
    assert _appear_together(["cheek", "birthmark"], "a plain neutral background") is False


def test_proximity_boundary_is_inclusive() -> None:
    gap = "x" * (PROXIMITY_CHARS - len("alpha"))
    assert _appear_together(["alpha", "beta"], f"alpha{gap}beta") is True
    assert _appear_together(["alpha", "beta"], f"alpha{gap}xbeta") is False


def test_gate_source_has_no_control_bytes() -> None:
    """Pins the backspace-byte bug directly.

    An invisible control character silently turned the gate into a no-op that still
    reported success. Reading the file proved nothing, because there was nothing to
    see. Only the bytes tell the truth.
    """
    from pathlib import Path

    import studio_ops.validate.prompts as gate

    source = Path(gate.__file__).read_text(encoding="utf-8")
    offenders = {ord(c) for c in source if ord(c) < 32 and c not in "\n\t"}
    assert offenders == set(), f"control bytes in gate source: {sorted(offenders)}"
