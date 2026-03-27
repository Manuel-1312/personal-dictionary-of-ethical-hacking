#!/usr/bin/env python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genera separadores ASCII para notas o terminal.')
    parser.add_argument('--char', default='=')
    parser.add_argument('--width', type=int, default=50)
    parser.add_argument('--label', default='')
    args = parser.parse_args()
    if args.label:
        side = max(2, (args.width - len(args.label) - 2) // 2)
        print(args.char * side + ' ' + args.label + ' ' + args.char * side)
    else:
        print(args.char * args.width)
