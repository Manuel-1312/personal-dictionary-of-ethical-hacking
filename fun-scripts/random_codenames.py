#!/usr/bin/env python
import argparse
import random

ADJ = ['Silent', 'Velvet', 'Ghost', 'Neon', 'Dusty', 'Crimson', 'Midnight', 'Broken']
NOUN = ['Cactus', 'Packet', 'Lantern', 'Router', 'Mantis', 'Signal', 'Falcon', 'Circuit']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genera nombres de operación aleatorios.')
    parser.add_argument('--count', type=int, default=1)
    args = parser.parse_args()
    for _ in range(args.count):
        print(f"{random.choice(ADJ)} {random.choice(NOUN)}")
