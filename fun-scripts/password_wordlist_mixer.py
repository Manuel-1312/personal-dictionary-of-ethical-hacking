#!/usr/bin/env python
import argparse
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mezcla palabras base para crear una mini wordlist de lab.')
    parser.add_argument('--base', nargs='+', required=True)
    parser.add_argument('--years', nargs='*', default=[])
    parser.add_argument('--output', '-o', type=Path)
    args = parser.parse_args()
    combos = set()
    suffixes = ['', '123', '!', '@', '2024', '2025'] + args.years
    for word in args.base:
        for suffix in suffixes:
            combos.add(f'{word}{suffix}')
            combos.add(f'{word.title()}{suffix}')
    lines = sorted(combos)
    if args.output:
        args.output.write_text('\n'.join(lines) + '\n', encoding='utf-8')
        print(f'Wordlist generada: {args.output}')
    else:
        print('\n'.join(lines))
