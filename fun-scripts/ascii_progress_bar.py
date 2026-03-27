#!/usr/bin/env python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genera una barra de progreso ASCII.')
    parser.add_argument('--percent', type=int, required=True)
    parser.add_argument('--width', type=int, default=30)
    args = parser.parse_args()
    percent = max(0, min(100, args.percent))
    filled = int(args.width * percent / 100)
    bar = '[' + '#' * filled + '-' * (args.width - filled) + ']'
    print(f'{bar} {percent}%')
