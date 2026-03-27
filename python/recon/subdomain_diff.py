#!/usr/bin/env python
"""Compara dos listas de subdominios y genera un resumen en Markdown."""
import argparse
from pathlib import Path


def load_lines(path: Path) -> set[str]:
    return {
        line.strip().lower()
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines()
        if line.strip()
    }


def section(title: str, items: list[str]) -> str:
    lines = [f"## {title}", f"Total: {len(items)}", ""]
    if items:
        lines.extend(f"- {item}" for item in items)
    else:
        lines.append("- (vacío)")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Compara dos listas de subdominios.")
    parser.add_argument("--old", required=True, type=Path, help="Lista antigua")
    parser.add_argument("--new", required=True, type=Path, help="Lista nueva")
    parser.add_argument("--output", "-o", required=True, type=Path, help="Markdown de salida")
    args = parser.parse_args()

    old = load_lines(args.old)
    new = load_lines(args.new)

    added = sorted(new - old)
    removed = sorted(old - new)
    unchanged = sorted(old & new)

    content = [
        "# Subdomain Diff",
        "",
        f"- Fuente antigua: `{args.old}`",
        f"- Fuente nueva: `{args.new}`",
        f"- Antiguos: {len(old)}",
        f"- Nuevos: {len(new)}",
        "",
        section("Aparecidos", added),
        section("Desaparecidos", removed),
        section("Sin cambios", unchanged),
    ]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(content), encoding="utf-8")
    print(f"Diff generado: {args.output}")


if __name__ == "__main__":
    main()
