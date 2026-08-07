"""Asset store — the byte layer the manifest points at.

    Media never goes into git. The manifest does. `sha256` is what ties one to
    the other.

Everything here follows from that sentence. This module owns exactly two
operations, because those are the two the guarantee needs:

- `put` — bytes land in the store, and the caller is handed the hash and size it
  must record. There is no way to put something and not learn its hash.
- `check` / `verify` — the bytes still are what the record says they are.

Nothing is overwritten. A revised asset is a new file at a new path with its own
manifest entry; supersession is recorded, never performed by deletion. `put`
refuses a path that already holds different bytes, and is a no-op when it already
holds the same ones, so re-running an ingest is safe and re-running it over a
changed file is loud.

Only the `local` driver exists. The seam for `s3` / `r2` / `gcs` is `driver()` and
`root()`: a driver swap must be a configuration change and nothing else, which is
why the path convention below is driver-independent. Prove the round trip on one
disk before adding a network to the failure modes.

Configuration: the `ASSET_STORE_*` variables in .env.example.
Runbook: docs/runbook/asset_storage.md
"""

from __future__ import annotations

import hashlib
import os
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..config import Config

CHUNK_BYTES = 1 << 20

DRIVER_ENV = "ASSET_STORE_DRIVER"
LOCAL_PATH_ENV = "ASSET_STORE_LOCAL_PATH"

# A sibling of the repository, never a child of it. Inside the working tree it
# gets committed by accident exactly once, and git does not forget it.
DEFAULT_LOCAL_PATH = "../ahs-assets"

KNOWN_DRIVERS: frozenset[str] = frozenset({"local", "s3", "r2", "gcs"})
IMPLEMENTED_DRIVERS: frozenset[str] = frozenset({"local"})

SHA256_HEX_LENGTH = 64


class StoreError(RuntimeError):
    """Base for every refusal from the asset store."""


class StoreConfigError(StoreError):
    """The store is pointed somewhere it must not be, or nowhere at all."""


class StoreDriverNotBuiltError(StoreError):
    """A driver named in configuration that this build does not implement."""


class StoreCollisionError(StoreError):
    """The destination already holds different bytes. Nothing is overwritten."""


@dataclass(frozen=True)
class StoredAsset:
    """What the manifest entry needs after the bytes have landed."""

    store_path: str  # POSIX, relative to the store root — what goes in the manifest
    path: Path  # absolute, for this machine only — never recorded
    bytes: int
    sha256: str
    created: bool = True  # False when the identical file was already present


# --------------------------------------------------------------- configuration


def driver(cfg: Config) -> str:
    """The configured driver, refusing anything this build cannot honour."""
    _ = cfg  # the driver is process-level configuration, not repository state
    name = (os.environ.get(DRIVER_ENV) or "local").strip().lower()
    if name in IMPLEMENTED_DRIVERS:
        return name
    if name in KNOWN_DRIVERS:
        raise StoreDriverNotBuiltError(
            f"{DRIVER_ENV}={name} is NOT BUILT. Only 'local' is implemented; the "
            "round trip is proved on one disk before a network is added. "
            "See docs/runbook/asset_storage.md."
        )
    raise StoreConfigError(
        f"{DRIVER_ENV}={name!r} is not a known driver. Expected one of: "
        f"{', '.join(sorted(KNOWN_DRIVERS))}."
    )


def root(cfg: Config) -> Path:
    """Resolve the store root for the `local` driver.

    Relative paths resolve against the repository root, so `../ahs-assets` means
    a sibling of the repository whatever the working directory is.
    """
    if driver(cfg) != "local":  # pragma: no cover - driver() raises first today
        raise StoreDriverNotBuiltError("only the local driver has a filesystem root")

    raw = (os.environ.get(LOCAL_PATH_ENV) or "").strip() or DEFAULT_LOCAL_PATH
    candidate = Path(raw)
    resolved = (candidate if candidate.is_absolute() else cfg.root / candidate).resolve()

    repo = cfg.root.resolve()
    if (repo / ".git").exists() and resolved.is_relative_to(repo):
        raise StoreConfigError(
            f"{LOCAL_PATH_ENV} resolves to {resolved}, inside the git working tree at "
            f"{repo}. Media does not belong in git: point it at a sibling directory "
            f"such as {DEFAULT_LOCAL_PATH!r}. See docs/runbook/asset_storage.md."
        )
    return resolved


# ---------------------------------------------------------------------- hashing


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    """Hash a file in chunks — assets are routinely larger than memory."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(CHUNK_BYTES):
            digest.update(chunk)
    return digest.hexdigest()


# ------------------------------------------------------------------------ paths


def normalise_relative_path(relative_path: str) -> str:
    """Validate and POSIX-ify a store-relative path.

    Store paths are recorded in the manifest and read on another machine with
    another operating system, so they are POSIX and they never escape the root.
    """
    text = str(relative_path).replace("\\", "/").strip()
    if not text:
        raise StoreConfigError("relative_path is empty")
    if text.startswith("/") or Path(text).is_absolute():
        raise StoreConfigError(f"relative_path must be relative to the store root: {text!r}")
    parts = [p for p in text.split("/") if p not in ("", ".")]
    if any(p == ".." for p in parts):
        raise StoreConfigError(f"relative_path must not escape the store root: {text!r}")
    if not parts:
        raise StoreConfigError("relative_path is empty")
    return "/".join(parts)


def resolve(store_root: Path, store_path: str) -> Path:
    """Absolute location of a recorded store path."""
    return store_root / normalise_relative_path(store_path)


# ------------------------------------------------------------------------ write


def put(cfg: Config, src_or_bytes: Path | bytes, *, relative_path: str) -> StoredAsset:
    """Write into the store and return path, size, and SHA-256.

    The hash is computed from the bytes as written, not from anything the caller
    asserted about them, because a hash the caller supplied verifies nothing.

    Refuses to overwrite. If the destination already holds these exact bytes the
    call is a no-op and `created` is False; if it holds different bytes it raises.
    """
    store_root = root(cfg)
    rel = normalise_relative_path(relative_path)
    dest = store_root / rel

    payload: bytes | None = None
    source: Path | None = None
    if isinstance(src_or_bytes, bytes | bytearray):
        payload = bytes(src_or_bytes)
        digest = sha256_bytes(payload)
        size = len(payload)
    else:
        source = Path(src_or_bytes)
        if not source.is_file():
            raise StoreConfigError(f"source file does not exist: {source}")
        digest = sha256_file(source)
        size = source.stat().st_size

    if dest.exists():
        existing = sha256_file(dest)
        if existing == digest:
            return StoredAsset(rel, dest, size, digest, created=False)
        raise StoreCollisionError(
            f"{rel} already exists with a different hash ({existing} on disk, {digest} "
            "offered). Nothing in the store is overwritten — a revised asset is a new "
            "file with a new version suffix and its own manifest entry."
        )

    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(f".{dest.name}.partial")
    try:
        if payload is not None:
            tmp.write_bytes(payload)
        elif source is not None:
            _copy(source, tmp)
        # Rename last: a reader never sees a half-written asset at a real path.
        os.replace(tmp, dest)
    except OSError:
        tmp.unlink(missing_ok=True)
        raise

    written = sha256_file(dest)
    if written != digest:  # pragma: no cover - a failing disk, not a failing branch
        dest.unlink(missing_ok=True)
        raise StoreError(
            f"{rel}: hash changed between source and store ({digest} -> {written}). "
            "The write is not trustworthy; nothing was recorded."
        )
    return StoredAsset(rel, dest, size, digest, created=True)


def _copy(source: Path, dest: Path) -> None:
    with source.open("rb") as reader, dest.open("wb") as writer:
        while chunk := reader.read(CHUNK_BYTES):
            writer.write(chunk)


# ----------------------------------------------------------------- verification


def check(store_root: Path, entry: Mapping[str, Any]) -> str | None:
    """Return a finding for one manifest entry, or None if the bytes match.

    A mismatch is an incident, not a warning: the file is not the file the
    manifest describes, and the manifest is the side that must not be edited to
    make the problem go away. See docs/runbook/incident_response.md.
    """
    asset_id = str(entry.get("asset_id", "(no asset_id)"))
    store_path = entry.get("store_path")
    recorded = entry.get("sha256")

    if not store_path:
        return f"{asset_id}: no store_path — the entry points at nothing"
    if not recorded:
        return f"{asset_id}: no sha256 — the entry cannot be verified"

    try:
        path = resolve(store_root, str(store_path))
    except StoreConfigError as exc:
        return f"{asset_id}: {exc}"

    if not path.is_file():
        return f"{asset_id}: missing from the asset store at {store_path}"

    actual = sha256_file(path)
    if actual != str(recorded):
        return (
            f"{asset_id}: INTEGRITY FAILURE at {store_path} — recorded {recorded}, "
            f"found {actual}. Stop using the file and do NOT re-hash the manifest to "
            "match: that converts an integrity failure into a permanent silent "
            "falsehood. See docs/runbook/incident_response.md."
        )
    return None


def verify(cfg: Config, entry: Mapping[str, Any]) -> bool:
    """True when the referenced file exists and its hash matches the record."""
    return check(root(cfg), entry) is None
