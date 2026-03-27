#!/usr/bin/env python
"""Enriquece IOCs básicos con una clasificación simple y contexto de formato."""
import argparse
import csv
import ipaddress
import re
from pathlib import Path

DOMAIN_RE = re.compile(r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")
URL_RE = re.compile(r"^https?://")
HEX32_RE = re.compile(r"^[a-fA-F0-9]{32}$")
HEX64_RE = re.compile(r"^[a-fA-F0-9]{64}$")


def classify(value: str) -> tuple[str, str]:
    try:
        ip = ipaddress.ip_address(value)
        scope = "private" if ip.is_private else "public"
        return "ipv4" if ip.version == 4 else "ipv6", scope
    except ValueError:
        pass
    if URL_RE.match(value):
        return "url", "web"
    if DOMAIN_RE.match(value):
        return "domain", "fqdn"
    if HEX64_RE.match(value):
        return "sha256", "hash"
    if HEX32_RE.match(value):
        return "md5", "hash"
    return "unknown", "unknown"


def main():
    parser = argparse.ArgumentParser(description="Enriquece una lista CSV de IOCs con clasificación básica.")
    parser.add_argument("--input", "-i", required=True, type=Path, help="CSV con columna 'value'")
    parser.add_argument("--output", "-o", required=True, type=Path)
    args = parser.parse_args()

    rows = []
    with args.input.open(encoding="utf-8", errors="ignore") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            value = (row.get("value") or "").strip()
            kind, context = classify(value)
            row["kind"] = kind
            row["context"] = context
            rows.append(row)

    fieldnames = list(rows[0].keys()) if rows else ["value", "kind", "context"]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"IOC enriquecidos: {args.output}")


if __name__ == "__main__":
    main()
