#!/usr/bin/env python
"""Genera un índice de evidencias con hash y metadatos básicos."""
import argparse
import csv
import hashlib
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_file():
            yield path


def main():
    parser = argparse.ArgumentParser(description="Indexa una carpeta de evidencias en CSV.")
    parser.add_argument("--input", "-i", required=True, type=Path)
    parser.add_argument("--output", "-o", required=True, type=Path)
    args = parser.parse_args()

    rows = []
    for path in iter_files(args.input):
        rows.append({
            "path": str(path.relative_to(args.input)),
            "size": path.stat().st_size,
            "sha256": sha256_file(path),
        })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["path", "size", "sha256"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Índice generado: {args.output} ({len(rows)} archivos)")


if __name__ == "__main__":
    main()
