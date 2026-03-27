#!/usr/bin/env python
"""Convierte XML de Nmap en un resumen Markdown legible."""
import argparse
from pathlib import Path
import xml.etree.ElementTree as ET


def service_label(port):
    service = port.find("service")
    if service is None:
        return ""
    product = service.attrib.get("product", "").strip()
    version = service.attrib.get("version", "").strip()
    extrainfo = service.attrib.get("extrainfo", "").strip()
    return " ".join(part for part in [product, version, extrainfo] if part).strip()


def main():
    parser = argparse.ArgumentParser(description="Convierte un XML de Nmap a Markdown.")
    parser.add_argument("--input", "-i", required=True, type=Path, help="Fichero XML de Nmap")
    parser.add_argument("--output", "-o", required=True, type=Path, help="Markdown de salida")
    args = parser.parse_args()

    root = ET.parse(args.input).getroot()
    lines = ["# Nmap Report", "", f"Fuente: `{args.input}`", ""]

    for host in root.findall("host"):
        addr = host.find("address")
        if addr is None:
            continue
        ip = addr.attrib.get("addr", "desconocido")
        hostname_nodes = host.findall("hostnames/hostname")
        hostnames = ", ".join(node.attrib.get("name", "") for node in hostname_nodes if node.attrib.get("name"))
        lines.append(f"## {ip}" + (f" ({hostnames})" if hostnames else ""))
        lines.append("")
        ports = host.findall("ports/port")
        if not ports:
            lines.append("- Sin puertos registrados")
            lines.append("")
            continue
        lines.append("| Puerto | Protocolo | Estado | Servicio | Detalle |")
        lines.append("| --- | --- | --- | --- | --- |")
        for port in ports:
            state = port.find("state")
            service = port.find("service")
            lines.append(
                f"| {port.attrib.get('portid','')} | {port.attrib.get('protocol','')} | {state.attrib.get('state','') if state is not None else ''} | {service.attrib.get('name','') if service is not None else ''} | {service_label(port)} |"
            )
        lines.append("")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Markdown generado: {args.output}")


if __name__ == "__main__":
    main()
