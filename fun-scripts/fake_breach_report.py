#!/usr/bin/env python
import argparse
import random
from pathlib import Path

INCIDENTS = ['Credenciales reutilizadas', 'Panel expuesto', 'Token filtrado', 'Bucket público', 'RDP abierto']
IMPACTS = ['acceso limitado', 'exposición de datos de prueba', 'movimiento lateral de laboratorio', 'lectura de ficheros sensibles']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genera un informe ficticio de incidente.')
    parser.add_argument('--company', required=True)
    parser.add_argument('--output', '-o', type=Path, required=True)
    args = parser.parse_args()
    incident = random.choice(INCIDENTS)
    impact = random.choice(IMPACTS)
    content = f"# Fake Breach Report\n\n- Empresa: {args.company}\n- Incidente simulado: {incident}\n- Impacto ficticio: {impact}\n\n## Resumen\nEste documento es solo para prácticas, demos o entrenamiento interno.\n\n## Timeline\n1. Detección inicial\n2. Validación controlada\n3. Contención\n4. Lecciones aprendidas\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(content, encoding='utf-8')
    print(f'Reporte generado: {args.output}')
