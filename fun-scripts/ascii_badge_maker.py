#!/usr/bin/env python
import argparse


def badge(left: str, right: str) -> str:
    return f'[ {left} ]====[ {right} ]'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genera un badge ASCII simple.')
    parser.add_argument('--left', required=True)
    parser.add_argument('--right', required=True)
    args = parser.parse_args()
    print(badge(args.left, args.right))
