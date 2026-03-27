#!/usr/bin/env python
import argparse


def make_tree(height: int) -> str:
    lines = []
    for i in range(height):
        stars = '*' * (2 * i + 1)
        lines.append(stars.center(2 * height - 1))
    lines.append('|'.center(2 * height - 1))
    return '\n'.join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genera un arbolito ASCII.')
    parser.add_argument('--height', type=int, default=5)
    args = parser.parse_args()
    print(make_tree(args.height))
