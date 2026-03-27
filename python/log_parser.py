#!/usr/bin/env python
"""Pequeño parser para logs tipo Zeek/Suricata."""
import argparse
from pathlib import Path
import csv

def parse_log(path):
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            line=line.strip()
            if not line or line.startswith('#'):
                continue
            parts=line.split('\t')
            if len(parts)<6:
                continue
            timestamp, src, dst, proto, sport, dport = parts[:6]
            yield {'timestamp': timestamp, 'src': src, 'dst': dst, 'protocol': proto, 'sport': sport, 'dport': dport}

def main():
    parser=argparse.ArgumentParser(description='Parsear logs de red y exportar CSV.')
    parser.add_argument('--input', '-i', required=True, type=Path, help='Ruta del log (Zeek/Suricata).')
    parser.add_argument('--output', '-o', required=True, type=Path, help='CSV de salida.')
    args=parser.parse_args()
    print('Procesando', args.input)
    rows=list(parse_log(args.input))
    if not rows:
        print('No se encontraron entradas válidas. Revisa el log.');
        return
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w', newline='', encoding='utf-8') as csvfile:
        writer=csv.DictWriter(csvfile, fieldnames=['timestamp','src','dst','protocol','sport','dport'])
        writer.writeheader()
        writer.writerows(rows)
    print(f'Archivo generado: {args.output} (total {len(rows)} filas)')

if __name__ == '__main__':
    main()
