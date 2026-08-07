"""Runtime configuration.

Deliberately thin. Validation is offline by design, so almost nothing here is
required for the implemented gates to run — which is what lets CI validate without
depending on any vendor being up.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from .paths import Layout, find_repo_root


@dataclass(frozen=True)
class Config:
    root: Path
    layout: Layout
    log_level: str = "INFO"
    default_studio: str | None = None
    default_line: str | None = None
    generation_dry_run: bool = True
    generation_budget_usd: float = 0.0

    @classmethod
    def load(cls, root: Path | None = None) -> Config:
        _load_dotenv(root)
        resolved = (
            (root or Path(os.environ.get("STUDIO_ROOT", "") or "")).resolve()
            if (root or os.environ.get("STUDIO_ROOT"))
            else find_repo_root()
        )
        if not (resolved / "core").is_dir():
            resolved = find_repo_root(resolved)
        return cls(
            root=resolved,
            layout=Layout(root=resolved),
            log_level=os.environ.get("STUDIO_LOG_LEVEL", "INFO"),
            default_studio=os.environ.get("STUDIO_DEFAULT_STUDIO") or None,
            default_line=os.environ.get("STUDIO_DEFAULT_LINE") or None,
            # Generation defaults to refusing. Enabling it is a deliberate act with a
            # cost ceiling, never an accident of a missing environment variable.
            generation_dry_run=os.environ.get("GENERATION_DRY_RUN", "true").lower()
            not in {"false", "0", "no"},
            generation_budget_usd=_float(os.environ.get("GENERATION_BUDGET_USD_PER_EPISODE"), 0.0),
        )


def _float(value: str | None, default: float) -> float:
    try:
        return float(value) if value else default
    except ValueError:
        return default


def _load_dotenv(root: Path | None) -> None:
    """Load .env if python-dotenv is present. Absence is not an error."""
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    base = root or find_repo_root()
    env = base / ".env"
    if env.is_file():
        load_dotenv(env, override=False)
