#!/usr/bin/env python
"""Genera una plantilla Markdown de cadena de custodia a partir de un índice CSV."""
import argparse
import csv
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Genera cadena de custodia Markdown desde un CSV de evidencias.")
    parser.add_argument("--input", "-i", required=True, type=Path, help="CSV con evidencias")
    parser.add_argument("--output", "-o", required=True, type=Path, help="Markdown de salida")
    parser.add_argument("--case", required=True, help="Nombre del caso")
    args = parser.parse_args()

    with args.input.open(encoding="utf-8", errors="ignore") as fh:
        rows = list(csv.DictReader(fh))

    lines = [
        f"# Cadena de custodia - {args.case}",
        "",
        "## Resumen",
        f"- Caso: {args.case}",
        f"- Fuente: `{args.input}`",
        f"- Artefactos: {len(rows)}",
        "",
        "## Evidencias",
        "| Ruta | Tamaño | SHA256 |",
        "| --- | --- | --- |",
    ]
    for row in rows:
        lines.append(f"| {row.get('path','')} | {row.get('size','')} | {row.get('sha256','')} |")
    lines += ["", "## Custodia", "- Responsable inicial:", "- Fecha/hora de recogida:", "- Transferencias:", "- Observaciones:", ""]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Documento generado: {args.output}")


if __name__ == "__main__":
    main()
