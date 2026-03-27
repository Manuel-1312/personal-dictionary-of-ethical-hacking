#!/usr/bin/env python
"""Sonda simple de cabeceras HTTP/HTTPS para inventario defensivo."""
import argparse
import csv
import ssl
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

DEFAULT_HEADERS = [
    "server",
    "content-type",
    "x-frame-options",
    "x-content-type-options",
    "content-security-policy",
    "strict-transport-security",
]


def normalize_target(target: str) -> str:
    if "://" not in target:
        return f"http://{target}"
    return target


def fetch_headers(target: str, timeout: int):
    url = normalize_target(target)
    request = Request(url, headers={"User-Agent": "ethical-lab-http-probe/1.0"}, method="GET")
    context = ssl.create_default_context()
    with urlopen(request, timeout=timeout, context=context) as response:
        headers = {k.lower(): v for k, v in response.headers.items()}
        parsed = urlparse(response.geturl())
        return {
            "target": target,
            "final_url": response.geturl(),
            "scheme": parsed.scheme,
            "status": response.status,
            **{header: headers.get(header, "") for header in DEFAULT_HEADERS},
        }


def main():
    parser = argparse.ArgumentParser(description="Recoge cabeceras HTTP/HTTPS y las exporta a CSV.")
    parser.add_argument("targets", nargs="+", help="URLs o hosts objetivo.")
    parser.add_argument("--output", "-o", type=Path, required=True, help="CSV de salida.")
    parser.add_argument("--timeout", type=int, default=5, help="Timeout por objetivo en segundos.")
    args = parser.parse_args()

    rows = []
    for target in args.targets:
        print(f"[+] Probando {target}")
        try:
            rows.append(fetch_headers(target, args.timeout))
        except Exception as exc:  # pragma: no cover - CLI utility
            print(f"[!] Error con {target}: {exc}", file=sys.stderr)
            rows.append({
                "target": target,
                "final_url": "",
                "scheme": "",
                "status": "ERROR",
                **{header: "" for header in DEFAULT_HEADERS},
            })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["target", "final_url", "scheme", "status", *DEFAULT_HEADERS]
    with open(args.output, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"[+] CSV generado en {args.output}")


if __name__ == "__main__":
    main()
