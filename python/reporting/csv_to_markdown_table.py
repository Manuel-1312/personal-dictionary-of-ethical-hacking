#!/usr/bin/env python
"""Convierte un CSV sencillo en una tabla Markdown."""
import argparse
import csv
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Convierte CSV a tabla Markdown.")
    parser.add_argument("--input", "-i", required=True, type=Path)
    parser.add_argument("--output", "-o", required=True, type=Path)
    args = parser.parse_args()

    with args.input.open(encoding="utf-8", errors="ignore") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        headers = reader.fieldnames or []

    lines = ["# CSV to Markdown", ""]
    if not headers:
        lines.append("Sin columnas detectadas.")
    else:
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
        for row in rows:
            lines.append("| " + " | ".join(str(row.get(header, "")) for header in headers) + " |")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Tabla generada: {args.output}")


if __name__ == "__main__":
    main()
