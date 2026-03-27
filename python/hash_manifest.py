#!/usr/bin/env python
"""Genera un manifiesto de hashes para artefactos de laboratorio."""
import argparse
import csv
import hashlib
from pathlib import Path

ALGORITHMS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
}


def digest_file(path: Path, algorithm: str) -> str:
    hasher = ALGORITHMS[algorithm]()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_file():
            yield path


def main():
    parser = argparse.ArgumentParser(description="Genera hashes MD5/SHA1/SHA256 de una carpeta.")
    parser.add_argument("--input", "-i", type=Path, required=True, help="Carpeta a procesar.")
    parser.add_argument("--output", "-o", type=Path, required=True, help="CSV de salida.")
    parser.add_argument("--algorithm", choices=sorted(ALGORITHMS), default="sha256", help="Algoritmo de hash.")
    args = parser.parse_args()

    rows = []
    for path in iter_files(args.input):
        rel_path = path.relative_to(args.input)
        rows.append({
            "path": str(rel_path),
            "size": path.stat().st_size,
            "algorithm": args.algorithm,
            "digest": digest_file(path, args.algorithm),
        })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["path", "size", "algorithm", "digest"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Manifest generado: {args.output} ({len(rows)} archivos)")


if __name__ == "__main__":
    main()
