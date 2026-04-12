"""Tests para python/forensics/ — verifican extracción de IOCs, hashing y cadena de custodia."""
import csv
import textwrap
from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# Helpers para cargar módulos sin instalar el paquete
# ---------------------------------------------------------------------------

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
# ioc_extractor
# ---------------------------------------------------------------------------

class TestIOCExtractor:
    """El extractor de IOCs debe encontrar IPs, dominios, URLs y hashes en texto plano."""

    @pytest.fixture
    def extractor(self):
        return _load_module("ioc_extractor", "python/forensics/ioc_extractor.py")

    def test_extracts_ipv4(self, extractor):
        """Debe encontrar direcciones IPv4 válidas."""
        import re
        matches = extractor.PATTERNS["ipv4"].findall("Conexión desde 192.168.1.100 a 10.0.0.1")
        assert "192.168.1.100" in matches
        assert "10.0.0.1" in matches

    def test_extracts_urls(self, extractor):
        """Debe encontrar URLs HTTP/HTTPS."""
        matches = extractor.PATTERNS["url"].findall("Visita https://evil.example.com/payload y http://test.lab")
        assert len(matches) == 2

    def test_extracts_sha256(self, extractor):
        """Debe encontrar hashes SHA256 (64 caracteres hex)."""
        fake_hash = "a" * 64
        matches = extractor.PATTERNS["sha256"].findall(f"Hash: {fake_hash}")
        assert fake_hash in matches

    def test_extracts_md5(self, extractor):
        """Debe encontrar hashes MD5 (32 caracteres hex)."""
        fake_hash = "b" * 32
        matches = extractor.PATTERNS["md5"].findall(f"MD5: {fake_hash}")
        assert fake_hash in matches

    def test_full_extraction_to_csv(self, extractor, tmp_path):
        """El flujo completo debe escribir IOCs extraídos en un CSV válido."""
        input_file = tmp_path / "sample.txt"
        input_file.write_text(
            "Conexión desde 192.168.1.1 a https://malware.example.com/drop\n"
            "Hash SHA256: " + "c" * 64 + "\n",
            encoding="utf-8",
        )
        output_file = tmp_path / "iocs.csv"

        # Simulamos la lógica de main() sin argparse
        content = input_file.read_text(encoding="utf-8")
        rows = []
        for kind, pattern in extractor.PATTERNS.items():
            seen = set()
            for match in pattern.findall(content):
                if match not in seen:
                    seen.add(match)
                    rows.append({"type": kind, "value": match})

        with output_file.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=["type", "value"])
            writer.writeheader()
            writer.writerows(sorted(rows, key=lambda r: (r["type"], r["value"])))

        # Verificamos el CSV generado
        with output_file.open(encoding="utf-8") as fh:
            reader = list(csv.DictReader(fh))

        types_found = {r["type"] for r in reader}
        assert "ipv4" in types_found
        assert "url" in types_found
        assert "sha256" in types_found


# ---------------------------------------------------------------------------
# ioc_enricher
# ---------------------------------------------------------------------------

class TestIOCEnricher:
    """El enriquecedor debe clasificar IOCs por tipo y contexto."""

    @pytest.fixture
    def enricher(self):
        return _load_module("ioc_enricher", "python/forensics/ioc_enricher.py")

    def test_classifies_private_ip(self, enricher):
        kind, context = enricher.classify("192.168.1.1")
        assert kind == "ipv4"
        assert context == "private"

    def test_classifies_public_ip(self, enricher):
        kind, context = enricher.classify("8.8.8.8")
        assert kind == "ipv4"
        assert context == "public"

    def test_classifies_url(self, enricher):
        kind, context = enricher.classify("https://example.com/path")
        assert kind == "url"
        assert context == "web"

    def test_classifies_domain(self, enricher):
        kind, context = enricher.classify("malware.example.com")
        assert kind == "domain"
        assert context == "fqdn"

    def test_classifies_sha256(self, enricher):
        kind, context = enricher.classify("a" * 64)
        assert kind == "sha256"
        assert context == "hash"

    def test_classifies_md5(self, enricher):
        kind, context = enricher.classify("b" * 32)
        assert kind == "md5"
        assert context == "hash"

    def test_unknown_value(self, enricher):
        kind, context = enricher.classify("not-a-valid-ioc")
        assert kind == "unknown"


# ---------------------------------------------------------------------------
# hash_manifest
# ---------------------------------------------------------------------------

class TestHashManifest:
    """El generador de hashes debe calcular digests correctos para archivos."""

    @pytest.fixture
    def manifest(self):
        return _load_module("hash_manifest", "python/forensics/hash_manifest.py")

    def test_sha256_digest(self, manifest, tmp_path):
        """digest_file con SHA256 debe coincidir con el hash esperado."""
        import hashlib
        test_file = tmp_path / "test.txt"
        test_file.write_text("contenido de prueba", encoding="utf-8")

        expected = hashlib.sha256(b"contenido de prueba").hexdigest()
        result = manifest.digest_file(test_file, "sha256")
        assert result == expected

    def test_md5_digest(self, manifest, tmp_path):
        """digest_file con MD5 debe coincidir con el hash esperado."""
        import hashlib
        test_file = tmp_path / "test.bin"
        test_file.write_bytes(b"\x00\x01\x02\x03")

        expected = hashlib.md5(b"\x00\x01\x02\x03").hexdigest()
        result = manifest.digest_file(test_file, "md5")
        assert result == expected

    def test_iter_files(self, manifest, tmp_path):
        """iter_files debe listar archivos recursivamente, ignorando directorios."""
        (tmp_path / "sub").mkdir()
        (tmp_path / "a.txt").write_text("a")
        (tmp_path / "sub" / "b.txt").write_text("b")

        files = list(manifest.iter_files(tmp_path))
        names = [f.name for f in files]
        assert "a.txt" in names
        assert "b.txt" in names
        assert len(files) == 2


# ---------------------------------------------------------------------------
# evidence_indexer
# ---------------------------------------------------------------------------

class TestEvidenceIndexer:
    """El indexador de evidencias debe generar hashes SHA256 para cada archivo."""

    @pytest.fixture
    def indexer(self):
        return _load_module("evidence_indexer", "python/forensics/evidence_indexer.py")

    def test_sha256_file(self, indexer, tmp_path):
        import hashlib
        f = tmp_path / "evidence.bin"
        f.write_bytes(b"evidencia forense")
        expected = hashlib.sha256(b"evidencia forense").hexdigest()
        assert indexer.sha256_file(f) == expected
