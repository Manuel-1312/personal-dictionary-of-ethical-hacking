from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_MARKERS = [
    Path('README.md'),
    Path('python/toolkit.md'),
    Path('powershell/toolkit.md'),
    Path('fun-scripts/toolkit.md'),
]


def looks_like_repo_root(path: Path) -> bool:
    return all((path / marker).exists() for marker in REQUIRED_MARKERS)


def discover_repo_root() -> Path:
    candidates: list[Path] = []

    if getattr(sys, 'frozen', False):
        exe_dir = Path(sys.executable).resolve().parent
        candidates.extend([
            exe_dir,
            exe_dir.parent,
            Path.cwd(),
        ])
    else:
        here = Path(__file__).resolve()
        candidates.extend([
            here.parents[2],  # repo/app/services -> repo
            Path.cwd(),
        ])

    seen = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        if looks_like_repo_root(candidate):
            return candidate

    # fallback razonable
    return Path.cwd()
