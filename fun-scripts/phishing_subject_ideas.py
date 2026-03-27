#!/usr/bin/env python
import argparse
import random

TOPICS = ['verificación de cuenta', 'documento pendiente', 'cambio de contraseña', 'factura urgente', 'nómina actualizada']
TONES = ['IMPORTANTE', 'Acción requerida', 'Recordatorio', 'Revisión pendiente', 'Último aviso']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genera asuntos ficticios para awareness.')
    parser.add_argument('--count', type=int, default=5)
    args = parser.parse_args()
    for _ in range(args.count):
        print(f"{random.choice(TONES)}: {random.choice(TOPICS).title()}")
