#!/usr/bin/env python
"""Convierte una salida grepable de masscan/gnmap en CSV."""
import argparse
import csv
from pathlib import Path


def parse_line(line: str):
    if not line.startswith("Host:"):
        return None
    parts = line.split()
    host = parts[1] if len(parts) > 1 else ""
    port = ""
    proto = ""
    state = ""
    if "Ports:" in line:
        port_data = line.split("Ports:", 1)[1].strip().split(",")[0].strip()
        fields = port_data.split("/")
        if len(fields) >= 3:
            port, state, proto = fields[:3]
    return {"host": host, "port": port, "proto": proto, "state": state}


def main():
    parser = argparse.ArgumentParser(description="Convierte salida de masscan/gnmap a CSV.")
    parser.add_argument("--input", "-i", required=True, type=Path)
    parser.add_argument("--output", "-o", required=True, type=Path)
    args = parser.parse_args()

    rows = []
    for line in args.input.read_text(encoding="utf-8", errors="ignore").splitlines():
        parsed = parse_line(line.strip())
        if parsed:
            rows.append(parsed)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["host", "port", "proto", "state"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV generado: {args.output} ({len(rows)} filas)")


if __name__ == "__main__":
    main()
