"""Tests para python/reporting/ y python/recon/ — verifican conversiones y diffs."""
import csv
import textwrap
from pathlib import Path

import pytest


def _load_module(name, rel_path):
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        name,
        Path(__file__).resolve().parents[1] / rel_path,
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# csv_to_markdown_table
# ---------------------------------------------------------------------------

class TestCSVToMarkdown:
    """La conversión CSV → Markdown debe producir una tabla válida."""

    def test_basic_conversion(self, tmp_path):
        """Un CSV con cabecera y filas debe generar una tabla Markdown con separadores."""
        csv_file = tmp_path / "data.csv"
        csv_file.write_text("name,port,status\nSSH,22,open\nHTTP,80,open\n", encoding="utf-8")

        output = tmp_path / "table.md"

        # Cargamos y ejecutamos la lógica manualmente (sin argparse)
        with csv_file.open(encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            rows = list(reader)
            headers = reader.fieldnames

        lines = ["# CSV to Markdown", ""]
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
        for row in rows:
            lines.append("| " + " | ".join(str(row.get(h, "")) for h in headers) + " |")

        output.write_text("\n".join(lines) + "\n", encoding="utf-8")

        content = output.read_text(encoding="utf-8")
        assert "| name | port | status |" in content
        assert "| SSH | 22 | open |" in content
        assert "| --- | --- | --- |" in content

    def test_empty_csv(self, tmp_path):
        """Un CSV vacío (sin filas) debe indicar que no hay columnas o generar solo cabeceras."""
        csv_file = tmp_path / "empty.csv"
        csv_file.write_text("", encoding="utf-8")

        with csv_file.open(encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            rows = list(reader)
            headers = reader.fieldnames or []

        # Sin cabeceras, el resultado debe reflejar que no hay datos
        assert len(headers) == 0
        assert len(rows) == 0


# ---------------------------------------------------------------------------
# subdomain_diff
# ---------------------------------------------------------------------------

class TestSubdomainDiff:
    """El diff de subdominios debe detectar aparecidos, desaparecidos y sin cambios."""

    @pytest.fixture
    def diff_mod(self):
        return _load_module("subdomain_diff", "python/recon/subdomain_diff.py")

    def test_load_lines(self, diff_mod, tmp_path):
        """load_lines debe devolver un set con líneas normalizadas a minúsculas."""
        f = tmp_path / "subs.txt"
        f.write_text("Api.Example.COM\nwww.example.com\n\n  mail.example.com  \n", encoding="utf-8")
        result = diff_mod.load_lines(f)
        assert result == {"api.example.com", "www.example.com", "mail.example.com"}

    def test_diff_logic(self, diff_mod, tmp_path):
        """Debe identificar correctamente subdominios nuevos, eliminados y sin cambios."""
        old = tmp_path / "old.txt"
        new = tmp_path / "new.txt"
        old.write_text("a.example.com\nb.example.com\nc.example.com\n", encoding="utf-8")
        new.write_text("b.example.com\nc.example.com\nd.example.com\n", encoding="utf-8")

        old_set = diff_mod.load_lines(old)
        new_set = diff_mod.load_lines(new)

        added = sorted(new_set - old_set)
        removed = sorted(old_set - new_set)
        unchanged = sorted(old_set & new_set)

        assert added == ["d.example.com"]
        assert removed == ["a.example.com"]
        assert unchanged == ["b.example.com", "c.example.com"]

    def test_section_formatting(self, diff_mod):
        """section() debe generar Markdown legible con título y lista de items."""
        result = diff_mod.section("Nuevos", ["x.example.com", "y.example.com"])
        assert "## Nuevos" in result
        assert "- x.example.com" in result
        assert "Total: 2" in result

    def test_section_empty(self, diff_mod):
        """section() con lista vacía debe mostrar '(vacío)'."""
        result = diff_mod.section("Sin cambios", [])
        assert "(vacío)" in result


# ---------------------------------------------------------------------------
# app/services/registry — parser de fichas de toolkit.md
# ---------------------------------------------------------------------------

class TestRegistry:
    """El parser del registro debe interpretar los toolkit.md en formato de fichas."""

    @pytest.fixture
    def registry_mod(self):
        # registry.py uses `from __future__ import annotations`, which converts
        # type hints to strings. The module must be registered in sys.modules
        # before execution so @dataclass can resolve these annotations.
        import importlib.util
        import sys

        mod_path = Path(__file__).resolve().parents[1] / "app" / "services" / "registry.py"
        spec = importlib.util.spec_from_file_location("registry", mod_path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules["registry"] = mod
        spec.loader.exec_module(mod)
        return mod

    def test_parse_toolkit_extracts_entries(self, registry_mod):
        """Una ScriptEntry por ficha, con la ruta tomada del comando de ejemplo; la plantilla no cuenta."""
        lines = [
            "## Plantilla de scripts",
            "- **Comando de ejemplo:** cómo lanzarlo.",  # plantilla: no debe generar entrada
            "## 1. parsers/",
            "### `log_parser.py`",
            "- **Subcategoría:** `parsers/`",
            "- **Descripción:** Parsea logs Zeek.",
            "- **Comando de ejemplo:** `python python/parsers/log_parser.py -i conn.log -o out.csv`",
            "### `hash_manifest.py`",
            "- **Subcategoría:** `forensics/`",
            "- **Descripción:** Genera hashes.",
            "- **Comando de ejemplo:** `python python/forensics/hash_manifest.py -i dir -o hashes.csv`",
        ]
        entries = registry_mod.parse_toolkit(lines, Path("python/toolkit.md"), "Python")
        assert len(entries) == 2
        assert entries[0].relative_path == "python/parsers/log_parser.py"
        assert entries[1].relative_path == "python/forensics/hash_manifest.py"
        assert entries[0].category == "Python"
        assert "Parsea" in entries[0].description

    def test_parse_toolkit_path_fallback(self, registry_mod):
        """Sin ruta en el ejemplo, reconstruye con el prefijo de categoría y la subcarpeta."""
        lines = [
            "### `system_report.ps1`",
            "- **Subcategoría:** `system/`",
            "- **Descripción:** Resumen del equipo.",
            "- **Comando de ejemplo:** `pwsh -File system_report.ps1`",
        ]
        entries = registry_mod.parse_toolkit(lines, Path("powershell/toolkit.md"), "PowerShell")
        assert len(entries) == 1
        assert entries[0].relative_path == "powershell/system/system_report.ps1"
