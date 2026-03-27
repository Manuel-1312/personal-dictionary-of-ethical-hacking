#!/usr/bin/env python
import argparse

FONT = {
    'A': ['  /\\  ', ' /  \\ ', '/ /\\ \\', '/ ____ \\', '/_/    \\_\\'],
    'B': ['|~~~\\ ', '|---< ', '|---/ ', '|___/ '],
    'L': ['|     ', '|     ', '|     ', '|____ '],
    '0': [' /~~\\ ', '| () |', '| () |', ' \\__/ '],
    '1': [' /| ', '  | ', '  | ', ' _|_'],
    ' ': ['  ', '  ', '  ', '  '],
}

def render(text: str) -> str:
    text = text.upper()
    rows = ['' for _ in range(5)]
    for ch in text:
        pattern = FONT.get(ch, [ch]*5)
        if len(pattern) < 5:
            pattern += [' ' * len(pattern[0])] * (5 - len(pattern))
        for i in range(5):
            rows[i] += pattern[i] + '  '
    return '\n'.join(rows)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genera un banner ASCII simple.')
    parser.add_argument('--text', required=True)
    args = parser.parse_args()
    print(render(args.text))
