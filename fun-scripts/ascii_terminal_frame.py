#!/usr/bin/env python
import argparse


def frame(text: str, title: str = 'terminal') -> str:
    lines = text.splitlines() or ['']
    width = max(len(line) for line in lines)
    top = f'.-[{title}]' + '-' * max(1, width - len(title) + 1) + '.'
    body = ['| ' + line.ljust(width) + ' |' for line in lines]
    bottom = "'" + '-' * (len(top) - 2) + "'"
    return '\n'.join([top, *body, bottom])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mete texto dentro de un marco estilo terminal.')
    parser.add_argument('--text', required=True)
    parser.add_argument('--title', default='terminal')
    args = parser.parse_args()
    print(frame(args.text, args.title))
