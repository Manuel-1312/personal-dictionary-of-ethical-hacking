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


CATEGORY_PREFIXES = {
    "Python": "python/",
    "PowerShell": "powershell/",
    "Fun Scripts": "fun-scripts/",
}


def _relative_from_example(example: str, script_name: str, category: str, subcat: str) -> str:
    """Devuelve la ruta relativa del script.

    El comando de ejemplo de cada ficha ya incluye la ruta real
    (p. ej. ``python python/parsers/log_parser.py ...``), así que se prefiere
    ese token. Si no aparece, se reconstruye con el prefijo de la categoría y
    la subcarpeta indicada en la ficha.
    """
    for token in example.replace('\\', '/').split():
        token = token.strip('`"\'')
        if token.endswith(script_name) and '/' in token:
            return token
    prefix = CATEGORY_PREFIXES.get(category, '')
    sub = subcat.strip('`').strip('/')
    sub = f"{sub}/" if sub else ''
    return f"{prefix}{sub}{script_name}"


def parse_toolkit(lines: Iterable[str], toolkit_path: Path, category: str) -> list[ScriptEntry]:
    """Parsea un toolkit.md en formato de fichas: cabecera '### script' y bullets."""
    entries: list[ScriptEntry] = []
    name = description = example = subcat = ''

    def flush() -> None:
        if not name:
            return
        rel = _relative_from_example(example, name, category, subcat)
        entries.append(
            ScriptEntry(
                category=category,
                script=rel,
                description=description,
                example=example,
                source_toolkit=toolkit_path,
            )
        )

    for raw_line in lines:
        stripped = raw_line.strip()
        if stripped.startswith('### '):
            flush()
            name = stripped[4:].strip().strip('`')
            description = example = subcat = ''
        elif stripped.startswith('- **Subcategoría:**'):
            subcat = stripped.split('**Subcategoría:**', 1)[1].strip().strip('`')
        elif stripped.startswith('- **Descripción:**'):
            description = stripped.split('**Descripción:**', 1)[1].strip()
        elif stripped.startswith('- **Comando de ejemplo:**'):
            example = stripped.split('**Comando de ejemplo:**', 1)[1].strip().strip('`')
    flush()
    return entries


def load_registry(repo_root: Path) -> list[ScriptEntry]:
    entries: list[ScriptEntry] = []
    for category, rel_path in TOOLKIT_PATHS.items():
        toolkit = repo_root / rel_path
        if not toolkit.exists():
            continue
        lines = toolkit.read_text(encoding='utf-8', errors='ignore').splitlines()
        entries.extend(parse_toolkit(lines, toolkit, category))
    return entries
