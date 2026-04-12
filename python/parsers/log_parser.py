#!/usr/bin/env python
"""Parser de logs tipo Zeek/Suricata: convierte líneas tab-separated en CSV limpio.

Pensado para normalizar logs de red que siguen el formato clásico de Zeek
(campos separados por tabulación) y exportarlos a CSV, facilitando el análisis
posterior con herramientas como pandas, Excel o scripts de reporting.

Uso típico:
    python log_parser.py -i zeek_conn.log -o conexiones.csv
"""
import argparse
import csv
from pathlib import Path

FIELDNAMES = ["timestamp", "src", "dst", "protocol", "sport", "dport"]
MIN_FIELDS = 6  # Mínimo de columnas para considerar una línea válida


def parse_log(path: Path):
    """Lee un log tab-separated y devuelve diccionarios con los campos de red.

    Ignora comentarios (líneas que empiezan con #) y líneas con menos de
    MIN_FIELDS columnas, ya que probablemente sean cabeceras o metadatos.
    """
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < MIN_FIELDS:
                continue
            timestamp, src, dst, proto, sport, dport = parts[:MIN_FIELDS]
            yield {
                "timestamp": timestamp,
                "src": src,
                "dst": dst,
                "protocol": proto,
                "sport": sport,
                "dport": dport,
            }


def main():
    parser = argparse.ArgumentParser(
        description="Parsea logs de red (Zeek/Suricata) y exporta CSV normalizado."
    )
    parser.add_argument("--input", "-i", required=True, type=Path, help="Ruta del log.")
    parser.add_argument("--output", "-o", required=True, type=Path, help="CSV de salida.")
    args = parser.parse_args()

    print(f"Procesando {args.input}")
    rows = list(parse_log(args.input))

    if not rows:
        print("No se encontraron entradas válidas. Revisa el formato del log.")
        return

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Archivo generado: {args.output} ({len(rows)} filas)")


if __name__ == "__main__":
    main()
