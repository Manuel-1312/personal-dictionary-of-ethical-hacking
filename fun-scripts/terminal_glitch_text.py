#!/usr/bin/env python
import argparse
import random

GLITCH = ['░', '▒', '▓', '#', '@', '%']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Aplica estilo glitch a un texto.')
    parser.add_argument('--text', required=True)
    parser.add_argument('--intensity', type=float, default=0.25)
    args = parser.parse_args()
    out = []
    for ch in args.text:
        if ch != ' ' and random.random() < args.intensity:
            out.append(random.choice(GLITCH))
        out.append(ch)
    print(''.join(out))
