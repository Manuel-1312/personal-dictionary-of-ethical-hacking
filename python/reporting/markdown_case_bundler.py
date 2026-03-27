#!/usr/bin/env python
"""Une varias notas Markdown en un solo informe."""
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Une varias notas Markdown en un único documento.")
    parser.add_argument("inputs", nargs="+", type=Path, help="Ficheros Markdown de entrada")
    parser.add_argument("--output", "-o", required=True, type=Path, help="Fichero Markdown final")
    parser.add_argument("--title", default="Case Bundle", help="Título del documento final")
    args = parser.parse_args()

    parts = [f"# {args.title}", ""]
    for input_path in args.inputs:
        parts.append(f"---\n## Fuente: `{input_path}`\n")
        parts.append(input_path.read_text(encoding="utf-8", errors="ignore"))
        parts.append("")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(parts), encoding="utf-8")
    print(f"Bundle generado: {args.output}")


if __name__ == "__main__":
    main()
