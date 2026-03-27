#!/usr/bin/env python
import argparse


def make_box(text: str, padding: int = 1) -> str:
    lines = text.splitlines() or [text]
    width = max(len(line) for line in lines)
    inner = width + padding * 2
    top = '┌' + '─' * inner + '┐'
    bottom = '└' + '─' * inner + '┘'
    body = ['│' + ' ' * padding + line.ljust(width) + ' ' * padding + '│' for line in lines]
    return '\n'.join([top, *body, bottom])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Envuelve texto en una caja ASCII.')
    parser.add_argument('--text', required=True)
    parser.add_argument('--padding', type=int, default=1)
    args = parser.parse_args()
    print(make_box(args.text, args.padding))
