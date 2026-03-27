#!/usr/bin/env python
"""Genera una nota Markdown estructurada para un caso AD de laboratorio."""
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Genera una nota base para un caso Active Directory.")
    parser.add_argument("--host", required=True, help="Host o DC objetivo")
    parser.add_argument("--user", required=True, help="Usuario principal del caso")
    parser.add_argument("--domain", required=True, help="Dominio de laboratorio")
    parser.add_argument("--finding", required=True, help="Hallazgo principal")
    parser.add_argument("--output", "-o", required=True, type=Path, help="Markdown de salida")
    args = parser.parse_args()

    content = f"""# Caso AD - {args.host}

- **Dominio:** {args.domain}
- **Host / DC:** {args.host}
- **Usuario:** {args.user}
- **Hallazgo principal:** {args.finding}

## Contexto
- Alcance autorizado:
- Fuente del hallazgo:
- Estado inicial del laboratorio:

## Validación
- Técnica usada:
- Evidencia generada:
- Resultado observado:

## Impacto
- Privilegios / acceso conseguido:
- Sistemas relacionados:
- Riesgo en el laboratorio:

## Mitigación
- Control recomendado:
- IOC / detecciones sugeridas:
- Limpieza / reversión:
"""
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(content, encoding="utf-8")
    print(f"Nota AD generada: {args.output}")


if __name__ == "__main__":
    main()
