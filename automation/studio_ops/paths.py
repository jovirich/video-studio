"""The folder contract, in one place.

Every other module asks this one where things live. Moving a directory should be a
single edit here, not a grep across the codebase.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

# Files permitted at the repository root. Anything else is a placement error.
# Mirrors CONTRIBUTING.md § File placement; keep the two in step.
ROOT_WHITELIST: frozenset[str] = frozenset(
    {
        "README.md",
        "ROADMAP.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        "pyproject.toml",
        "requirements.txt",
        "Makefile",
        ".gitignore",
        ".gitattributes",
        ".editorconfig",
        ".env.example",
        ".env",
    }
)

ROOT_WHITELIST_SUFFIXES: tuple[str, ...] = (".code-workspace",)

# Directories permitted at the repository root.
ROOT_DIRS: frozenset[str] = frozenset(
    {
        ".git",
        ".github",
        ".vscode",
        ".venv",
        "core",
        "packs",
        "standards",
        "prompts",
        "templates",
        "automation",
        "rights",
        "library",
        "ops",
        "docs",
        "studios",
    }
)


@dataclass(frozen=True)
class Layout:
    """Resolved locations for one repository."""

    root: Path

    @property
    def core(self) -> Path:
        return self.root / "core"

    @property
    def packs(self) -> Path:
        return self.root / "packs"

    @property
    def standards(self) -> Path:
        return self.root / "standards"

    @property
    def schemas(self) -> Path:
        return self.root / "standards" / "schemas"

    @property
    def prompts(self) -> Path:
        return self.root / "prompts"

    @property
    def templates(self) -> Path:
        return self.root / "templates"

    @property
    def rights(self) -> Path:
        return self.root / "rights"

    @property
    def library(self) -> Path:
        return self.root / "library"

    @property
    def ops(self) -> Path:
        return self.root / "ops"

    @property
    def docs(self) -> Path:
        return self.root / "docs"

    @property
    def studios(self) -> Path:
        return self.root / "studios"

    def studio(self, code: str) -> Path:
        return self.studios / code

    def lines(self, studio: str) -> Path:
        return self.studio(studio) / "lines"

    def line(self, studio: str, code: str) -> Path:
        return self.lines(studio) / code

    def productions(self, studio: str, line: str) -> Path:
        return self.line(studio, line) / "productions"

    def production(self, studio: str, line: str, code: str) -> Path:
        return self.productions(studio, line) / code

    def pack(self, code: str) -> Path:
        return self.packs / code

    # --- discovery -------------------------------------------------------

    def iter_studios(self) -> list[Path]:
        if not self.studios.is_dir():
            return []
        return sorted(
            p for p in self.studios.iterdir() if p.is_dir() and not p.name.startswith("_")
        )

    def iter_packs(self) -> list[Path]:
        if not self.packs.is_dir():
            return []
        return sorted(p for p in self.packs.iterdir() if p.is_dir() and not p.name.startswith("_"))

    def iter_lines(self) -> list[Path]:
        out: list[Path] = []
        for studio in self.iter_studios():
            lines = studio / "lines"
            if lines.is_dir():
                out.extend(
                    sorted(p for p in lines.iterdir() if p.is_dir() and not p.name.startswith("_"))
                )
        return out


# Paths never walked by validators: generated, vendored, or binary.
IGNORE_DIRS: frozenset[str] = frozenset(
    {
        ".git",
        ".venv",
        "venv",
        "node_modules",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        "build",
        "dist",
        "05_assets",
        "masters",
        "renders",
        "cache",
    }
)


def iter_files(root: Path, suffix: str | None = None) -> list[Path]:
    """Walk `root`, skipping IGNORE_DIRS. Optionally filter by suffix."""
    out: list[Path] = []
    for path in root.rglob("*"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if not path.is_file():
            continue
        if suffix and path.suffix != suffix:
            continue
        out.append(path)
    return sorted(out)


def find_repo_root(start: Path | None = None) -> Path:
    """Walk upward for the repository root.

    Identified by the co-presence of `core/` and `packs/` — the two directories that
    define this platform's shape. Falls back to the git root, then to cwd.
    """
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "core").is_dir() and (candidate / "packs").is_dir():
            return candidate
        if (candidate / ".git").is_dir():
            return candidate
    return current
