#!/usr/bin/env python
"""Combina salidas de nmap y masscan en un único inventario consolidado.

Útil para fusionar resultados de distintas herramientas de escaneo
y obtener una vista unificada de los hosts descubiertos, indicando
qué herramienta detectó cada uno.

Uso típico:
    python inventory_builder.py --nmap scan.nmap --masscan scan.gnmap --out hosts.csv
"""
import argparse
import csv
from pathlib import Path


def parse_masscan(path: Path) -> set[str]:
    """Extrae IPs desde una salida grepable de masscan (líneas 'Host: ...')."""
    hosts = set()
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("Host:"):
                parts = line.split()
                if len(parts) >= 2:
                    hosts.add(parts[1])
    return hosts


def parse_nmap(path: Path) -> set[str]:
    """Extrae IPs desde una salida normal de nmap (líneas 'Nmap scan report for ...')."""
    hosts = set()
    with open(path, encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            line = line.strip()
            if line.startswith("Nmap scan report for"):
                hosts.add(line.split()[-1])
    return hosts


def main():
    parser = argparse.ArgumentParser(
        description="Crea inventario combinado de nmap y masscan."
    )
    parser.add_argument("--nmap", type=Path, required=True, help="Salida de nmap.")
    parser.add_argument("--masscan", type=Path, required=True, help="Salida grepable de masscan.")
    parser.add_argument("--out", type=Path, required=True, help="CSV de salida.")
    args = parser.parse_args()

    nmap_hosts = parse_nmap(args.nmap)
    masscan_hosts = parse_masscan(args.masscan)
    combined = sorted(nmap_hosts | masscan_hosts)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["Host", "Origin"])
        for host in combined:
            origin = "both" if host in nmap_hosts and host in masscan_hosts else (
                "nmap" if host in nmap_hosts else "masscan"
            )
            writer.writerow([host, origin])
    print(f"Inventario generado: {args.out} ({len(combined)} hosts)")


if __name__ == "__main__":
    main()
