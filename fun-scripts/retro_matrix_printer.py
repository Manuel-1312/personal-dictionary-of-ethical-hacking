#!/usr/bin/env python
import argparse
import random
import string
import sys
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Imprime una animación terminal estilo matrix.')
    parser.add_argument('--seconds', type=float, default=3.0)
    parser.add_argument('--width', type=int, default=60)
    args = parser.parse_args()
    end = time.time() + args.seconds
    chars = string.ascii_letters + string.digits + '@#$%&*'
    while time.time() < end:
        line = ''.join(random.choice(chars) for _ in range(args.width))
        sys.stdout.write(line + '\n')
        sys.stdout.flush()
        time.sleep(0.05)
