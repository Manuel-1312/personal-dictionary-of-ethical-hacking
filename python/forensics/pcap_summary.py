#!/usr/bin/env python
"""Resume un PCAP en texto/markdown a partir de tshark."""
import argparse
import json
import shutil
import subprocess
from collections import Counter
from pathlib import Path


def run_tshark(pcap: Path) -> list[dict]:
    if not shutil.which("tshark"):
        raise SystemExit("tshark no está disponible en PATH")
    cmd = [
        "tshark",
        "-r",
        str(pcap),
        "-T",
        "fields",
        "-E",
        "separator=,",
        "-e",
        "frame.time_epoch",
        "-e",
        "ip.src",
        "-e",
        "ip.dst",
        "-e",
        "_ws.col.Protocol",
        "-e",
        "tcp.dstport",
        "-e",
        "udp.dstport",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    packets = []
    for line in result.stdout.splitlines():
        parts = [part.strip() for part in line.split(",")]
        if len(parts) < 6:
            continue
        ts, src, dst, proto, tcp_port, udp_port = parts[:6]
        port = tcp_port or udp_port or ""
        packets.append({"ts": ts, "src": src, "dst": dst, "proto": proto, "port": port})
    return packets


def to_markdown(packets: list[dict], source: Path) -> str:
    protos = Counter(pkt["proto"] for pkt in packets if pkt["proto"])
    srcs = Counter(pkt["src"] for pkt in packets if pkt["src"])
    dsts = Counter(pkt["dst"] for pkt in packets if pkt["dst"])
    ports = Counter(pkt["port"] for pkt in packets if pkt["port"])
    lines = [
        "# PCAP Summary",
        "",
        f"- Fuente: `{source}`",
        f"- Paquetes analizados: {len(packets)}",
        "",
        "## Protocolos más vistos",
    ]
    lines.extend(f"- {proto}: {count}" for proto, count in protos.most_common(10))
    lines += ["", "## Top IP origen"]
    lines.extend(f"- {ip}: {count}" for ip, count in srcs.most_common(10))
    lines += ["", "## Top IP destino"]
    lines.extend(f"- {ip}: {count}" for ip, count in dsts.most_common(10))
    lines += ["", "## Top puertos destino"]
    lines.extend(f"- {port}: {count}" for port, count in ports.most_common(10))
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Genera un resumen Markdown o JSON de un PCAP usando tshark.")
    parser.add_argument("--input", "-i", required=True, type=Path)
    parser.add_argument("--output", "-o", required=True, type=Path)
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()

    packets = run_tshark(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.format == "json":
        args.output.write_text(json.dumps(packets, indent=2), encoding="utf-8")
    else:
        args.output.write_text(to_markdown(packets, args.input), encoding="utf-8")
    print(f"Resumen generado: {args.output}")


if __name__ == "__main__":
    main()
