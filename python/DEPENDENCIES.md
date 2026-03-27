# Dependencias de la librería Python

Este documento resume qué necesita cada helper de `python/` para funcionar sin sorpresas. La idea es separar claramente:

- **dependencias Python** instalables con `pip`
- **dependencias externas del sistema**
- **scripts que funcionan solo con librería estándar**

## Instalación base
Dependencias Python comunes:

```bash
pip install -r python/requirements.txt
```

Contenido actual de `python/requirements.txt`:
- `pandas`
- `xmltodict`

## Resumen por subcategoría

### `python/parsers/`
- `log_parser.py`
  - Python: `pandas`
  - Sistema: ninguna
- `inventory_builder.py`
  - Python: `xmltodict` (documentada como dependencia del módulo)
  - Sistema: ninguna
- `masscan_to_csv.py`
  - Python: librería estándar
  - Sistema: ninguna

### `python/web/`
- `http_headers_probe.py`
  - Python: librería estándar
  - Sistema: ninguna
- `dir_bruteforce_report.py`
  - Python: librería estándar
  - Sistema: ninguna
- `web_screenshot_manifest.py`
  - Python: librería estándar
  - Sistema: ninguna

### `python/forensics/`
- `hash_manifest.py`
  - Python: librería estándar
  - Sistema: ninguna
- `ioc_extractor.py`
  - Python: librería estándar
  - Sistema: ninguna
- `ioc_enricher.py`
  - Python: librería estándar
  - Sistema: ninguna
- `evidence_indexer.py`
  - Python: librería estándar
  - Sistema: ninguna
- `chain_of_custody_builder.py`
  - Python: librería estándar
  - Sistema: ninguna
- `pcap_summary.py`
  - Python: librería estándar
  - Sistema: **`tshark`** disponible en `PATH`

### `python/recon/`
- `subdomain_diff.py`
  - Python: librería estándar
  - Sistema: ninguna

### `python/reporting/`
- `nmap_xml_to_markdown.py`
  - Python: librería estándar
  - Sistema: ninguna
- `markdown_case_bundler.py`
  - Python: librería estándar
  - Sistema: ninguna
- `csv_to_markdown_table.py`
  - Python: librería estándar
  - Sistema: ninguna

### `python/ad/`
- `ad_notes_builder.py`
  - Python: librería estándar
  - Sistema: ninguna

## Recomendaciones prácticas
- Si un script necesita una herramienta del sistema, déjalo claro en su `README` y en el ejemplo de uso.
- Si en el futuro metes dependencias opcionales (por ejemplo para screenshots reales o parsing más avanzado), quizá compense separar:
  - `requirements.txt` → base mínima
  - `requirements-dev.txt` → tests, linters, extras
  - `requirements-optional.txt` → helpers menos universales

## Regla simple para crecer con orden
Antes de añadir una dependencia nueva, pregúntate:
1. ¿Resuelve un problema real o solo ahorra unas líneas?
2. ¿La dependencia complica instalar el repo en WSL/Windows/Kali?
3. ¿Ese helper puede vivir con librería estándar y seguir siendo útil?

Si la respuesta es que añade bastante valor, se mete. Si no, mejor mantener la librería ligera.
