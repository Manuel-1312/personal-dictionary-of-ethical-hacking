#!/usr/bin/env python
import argparse


def render(nodes):
    if len(nodes) < 2:
        return '[ ' + (nodes[0] if nodes else 'EMPTY') + ' ]'
    out = []
    for i, node in enumerate(nodes):
        out.append(f'[ {node} ]')
        if i < len(nodes) - 1:
            out.append('   |\n   v')
    return '\n'.join(out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genera un mapa ASCII simple de nodos.')
    parser.add_argument('nodes', nargs='*')
    args = parser.parse_args()
    print(render(args.nodes))
