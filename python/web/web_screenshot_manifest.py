#!/usr/bin/env python
"""Genera un manifiesto de capturas web a partir de una carpeta o lista de archivos."""
import argparse
import csv
from pathlib import Path

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}


def iter_images(path: Path):
    if path.is_file():
        yield path
        return
    for item in sorted(path.rglob("*")):
        if item.is_file() and item.suffix.lower() in IMAGE_EXTS:
            yield item


def guess_title(path: Path) -> str:
    return path.stem.replace("_", " ").replace("-", " ").strip()


def main():
    parser = argparse.ArgumentParser(description="Crea un manifiesto CSV de capturas web.")
    parser.add_argument("--input", "-i", required=True, type=Path, help="Carpeta o fichero de entrada")
    parser.add_argument("--output", "-o", required=True, type=Path, help="CSV de salida")
    args = parser.parse_args()

    rows = []
    for image in iter_images(args.input):
        rows.append({
            "path": str(image.relative_to(args.input)) if args.input.is_dir() else image.name,
            "title": guess_title(image),
            "size": image.stat().st_size,
        })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["path", "title", "size"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Manifiesto generado: {args.output} ({len(rows)} imágenes)")


if __name__ == "__main__":
    main()
