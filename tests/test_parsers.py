"""Tests para python/parsers/ — verifican que los parsers transforman datos correctamente."""
import csv
import textwrap
from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# log_parser
# ---------------------------------------------------------------------------

@pytest.fixture
def zeek_log(tmp_path):
    """Genera un log tipo Zeek con líneas tab-separated de ejemplo."""
    content = textwrap.dedent("""\
        # Este es un comentario de cabecera
        1681234567.123456\t10.0.0.1\t192.168.1.5\tTCP\t54321\t80
        1681234568.654321\t10.0.0.2\t192.168.1.10\tUDP\t12345\t53
        # Otro comentario
        1681234569.111111\t10.0.0.3\t192.168.1.20\tTCP\t65432\t443
    """)
    log_file = tmp_path / "conn.log"
    log_file.write_text(content, encoding="utf-8")
    return log_file


def test_log_parser_produces_correct_csv(zeek_log, tmp_path):
    """El parser debe leer líneas tab-separated y generar un CSV con 6 columnas."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "log_parser",
        Path(__file__).resolve().parents[1] / "python" / "parsers" / "log_parser.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    rows = list(mod.parse_log(zeek_log))
    assert len(rows) == 3, "Debe encontrar exactamente 3 entradas válidas (ignorando comentarios)"
    assert rows[0]["src"] == "10.0.0.1"
    assert rows[1]["protocol"] == "UDP"
    assert rows[2]["dport"] == "443"


def test_log_parser_ignores_short_lines(tmp_path):
    """Líneas con menos de 6 campos deben ignorarse sin error."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "log_parser",
        Path(__file__).resolve().parents[1] / "python" / "parsers" / "log_parser.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    log_file = tmp_path / "short.log"
    log_file.write_text("campo1\tcampo2\n\n# comment\n", encoding="utf-8")
    rows = list(mod.parse_log(log_file))
    assert len(rows) == 0


# ---------------------------------------------------------------------------
# masscan_to_csv
# ---------------------------------------------------------------------------

@pytest.fixture
def gnmap_file(tmp_path):
    """Genera un archivo grepable tipo masscan con entradas de ejemplo."""
    content = textwrap.dedent("""\
        # Masscan output
        Host: 10.0.0.1 ()   Ports: 80/open/tcp//http//
        Host: 10.0.0.2 ()   Ports: 443/open/tcp//https//
        Host: 10.0.0.3 ()   Ports: 22/open/tcp//ssh//
        # Finished
    """)
    gnmap = tmp_path / "scan.gnmap"
    gnmap.write_text(content, encoding="utf-8")
    return gnmap


def test_masscan_parse_line():
    """parse_line debe extraer host, port, proto y state de una línea grepable."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "masscan_to_csv",
        Path(__file__).resolve().parents[1] / "python" / "parsers" / "masscan_to_csv.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    result = mod.parse_line("Host: 10.0.0.1 ()   Ports: 80/open/tcp//http//")
    assert result is not None
    assert result["host"] == "10.0.0.1"
    assert result["port"] == "80"
    assert result["state"] == "open"
    assert result["proto"] == "tcp"


def test_masscan_parse_line_ignores_comments():
    """Líneas que no empiezan con 'Host:' deben devolver None."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "masscan_to_csv",
        Path(__file__).resolve().parents[1] / "python" / "parsers" / "masscan_to_csv.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    assert mod.parse_line("# Masscan output") is None
    assert mod.parse_line("") is None


# ---------------------------------------------------------------------------
# inventory_builder
# ---------------------------------------------------------------------------

def test_inventory_parse_nmap(tmp_path):
    """parse_nmap debe extraer IPs de líneas 'Nmap scan report for ...'."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "inventory_builder",
        Path(__file__).resolve().parents[1] / "python" / "parsers" / "inventory_builder.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    nmap_file = tmp_path / "scan.nmap"
    nmap_file.write_text(
        "Starting Nmap\nNmap scan report for 10.0.0.1\nNmap scan report for 10.0.0.2\nDone\n",
        encoding="utf-8",
    )
    hosts = mod.parse_nmap(nmap_file)
    assert hosts == {"10.0.0.1", "10.0.0.2"}


def test_inventory_parse_masscan(tmp_path):
    """parse_masscan debe extraer IPs de líneas 'Host: ...'."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "inventory_builder",
        Path(__file__).resolve().parents[1] / "python" / "parsers" / "inventory_builder.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    masscan_file = tmp_path / "scan.gnmap"
    masscan_file.write_text("Host: 10.0.0.2 ()\nHost: 10.0.0.3 ()\n", encoding="utf-8")
    hosts = mod.parse_masscan(masscan_file)
    assert hosts == {"10.0.0.2", "10.0.0.3"}
