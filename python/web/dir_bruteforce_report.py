#!/usr/bin/env python
"""Resume resultados de ffuf/dirsearch en Markdown o CSV."""
import argparse
import csv
import json
from pathlib import Path


def load_ffuf(path: Path):
    data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    rows = []
    for item in data.get("results", []):
        rows.append({
            "url": item.get("url", ""),
            "status": item.get("status", ""),
            "length": item.get("length", ""),
            "words": item.get("words", ""),
            "lines": item.get("lines", ""),
        })
    return rows


def write_markdown(rows, output: Path):
    lines = ["# Directory Bruteforce Report", "", f"Total resultados: {len(rows)}", "", "| URL | Status | Length | Words | Lines |", "| --- | --- | --- | --- | --- |"]
    for row in rows:
        lines.append(f"| {row['url']} | {row['status']} | {row['length']} | {row['words']} | {row['lines']} |")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_csv(rows, output: Path):
    with output.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["url", "status", "length", "words", "lines"])
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Convierte resultados de ffuf a Markdown/CSV.")
    parser.add_argument("--input", "-i", required=True, type=Path)
    parser.add_argument("--output", "-o", required=True, type=Path)
    parser.add_argument("--format", choices=["markdown", "csv"], default="markdown")
    args = parser.parse_args()

    rows = load_ffuf(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.format == "csv":
        write_csv(rows, args.output)
    else:
        write_markdown(rows, args.output)
    print(f"Reporte generado: {args.output}")


if __name__ == "__main__":
    main()
