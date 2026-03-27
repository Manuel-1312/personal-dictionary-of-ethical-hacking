#!/usr/bin/env python
import argparse
import random
from datetime import datetime, timedelta
from pathlib import Path

LEVELS = ['INFO', 'WARN', 'ERROR']
EVENTS = ['login_failed', 'port_scan_detected', 'token_refreshed', 'service_restart', 'dns_query', 'suspicious_macro']
IPS = ['10.0.0.5', '10.0.0.8', '192.168.1.10', '172.16.0.12']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genera logs falsos para pruebas.')
    parser.add_argument('--count', type=int, default=20)
    parser.add_argument('--output', '-o', type=Path, required=True)
    args = parser.parse_args()
    now = datetime.now()
    lines = []
    for i in range(args.count):
        ts = (now + timedelta(seconds=i)).isoformat()
        lines.append(f"{ts} level={random.choice(LEVELS)} event={random.choice(EVENTS)} src={random.choice(IPS)}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'Logs generados: {args.output}')
