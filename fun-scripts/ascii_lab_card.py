#!/usr/bin/env python
import argparse


def card(title: str, subtitle: str) -> str:
    lines = [title, subtitle]
    width = max(len(x) for x in lines) + 4
    top = '+' + '-' * width + '+'
    body = [f"|  {line.ljust(width-2)}|" for line in lines]
    return '\n'.join([top, *body, top])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genera una tarjeta ASCII simple para un lab.')
    parser.add_argument('--title', required=True)
    parser.add_argument('--subtitle', default='')
    args = parser.parse_args()
    print(card(args.title, args.subtitle))
