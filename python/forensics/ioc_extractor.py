#!/usr/bin/env python
"""Extrae IOCs básicos (IPs, dominios, URLs, hashes) de texto plano.

Cuando analizas un log de incidentes o un informe de amenazas, a menudo
necesitas separar rápidamente los indicadores de compromiso del texto
que los rodea. Este script busca patrones conocidos y los exporta a CSV,
evitando duplicados y ordenando por tipo para facilitar la revisión.

Uso típico:
    python ioc_extractor.py -i informe_amenazas.txt -o iocs.csv
"""
import argparse
import csv
import re
from pathlib import Path

# Cada patrón busca un tipo de IOC distinto en texto libre.
# Los hashes van de más largo (SHA256) a más corto (MD5) para evitar
# que un SHA256 se detecte también como dos MD5 falsos.
PATTERNS = {
    "ipv4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "domain": re.compile(r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"),
    "url": re.compile(r"\bhttps?://[^\s\]\)>'\"]+"),
    "sha256": re.compile(r"\b[a-fA-F0-9]{64}\b"),
    "md5": re.compile(r"\b[a-fA-F0-9]{32}\b"),
}


def main():
    parser = argparse.ArgumentParser(description="Extrae IOCs comunes desde un fichero de texto.")
    parser.add_argument("--input", "-i", type=Path, required=True, help="Fichero de entrada.")
    parser.add_argument("--output", "-o", type=Path, required=True, help="CSV de salida.")
    args = parser.parse_args()

    content = args.input.read_text(encoding="utf-8", errors="ignore")
    rows = []
    for kind, pattern in PATTERNS.items():
        seen = set()
        for match in pattern.findall(content):
            if match in seen:
                continue
            seen.add(match)
            rows.append({"type": kind, "value": match})

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["type", "value"])
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: (row["type"], row["value"])))
    print(f"IOCs exportados a {args.output} ({len(rows)} elementos)")


if __name__ == "__main__":
    main()
