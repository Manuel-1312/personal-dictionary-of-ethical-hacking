from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class ScriptEntry:
    category: str
    script: str
    description: str
    example: str
    source_toolkit: Path

    @property
    def relative_path(self) -> str:
        return self.script


TOOLKIT_PATHS = {
    "Python": Path("python/toolkit.md"),
    "PowerShell": Path("powershell/toolkit.md"),
    "Fun Scripts": Path("fun-scripts/toolkit.md"),
}


def parse_markdown_table(lines: Iterable[str], toolkit_path: Path, category: str) -> list[ScriptEntry]:
    entries: list[ScriptEntry] = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        if "---" in stripped or "Script" in stripped and "Comando" in stripped:
            continue
        parts = [part.strip() for part in stripped.strip("|").split("|")]
        if len(parts) < 4:
            continue
        script = parts[0].strip("`")
        description = parts[2] if len(parts) >= 3 else ""
        example = parts[3].strip("`") if len(parts) >= 4 else ""
        entries.append(ScriptEntry(category=category, script=script, description=description, example=example, source_toolkit=toolkit_path))
    return entries


def load_registry(repo_root: Path) -> list[ScriptEntry]:
    entries: list[ScriptEntry] = []
    for category, rel_path in TOOLKIT_PATHS.items():
        toolkit = repo_root / rel_path
        if not toolkit.exists():
            continue
        lines = toolkit.read_text(encoding="utf-8", errors="ignore").splitlines()
        entries.extend(parse_markdown_table(lines, toolkit, category))
    return entries
