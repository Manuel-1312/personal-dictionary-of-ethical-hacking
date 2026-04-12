# Toolkit - Python Tools 🐍

Documenta cada script, comando o helper que programas para esta biblioteca y anota qué dependencias necesita.

## Plantilla de scripts
- **Subcategoría:** carpeta a la que pertenece.
- **Descripción:** qué hace el script.
- **Comando de ejemplo:** cómo lanzarlo.
- **Notas:** dependencias o advertencias clave.

## 1. parsers/

### `log_parser.py`
- **Subcategoría:** `parsers/`
- **Descripción:** Extrae IPs, puertos y alertas de Zeek/Suricata para CSV/Markdown.
- **Comando de ejemplo:** `python python/parsers/log_parser.py --input defense/monitoring/logs/bro.log --output automation/reporting/results/zeek-summary.csv`
- **Notas:** Usa pandas y argparse; genera un CSV con columnas `timestamp`, `src`, `dst`, `protocol`, `port`.

### `inventory_builder.py`
- **Subcategoría:** `parsers/`
- **Descripción:** Combina `nmap` y `masscan` para generar inventario unificado en Markdown/CSV.
- **Comando de ejemplo:** `python python/parsers/inventory_builder.py --nmap reports/network/nmap-full.xml --masscan reports/network/masscan.gnmap --out reports/network/inventory.md`
- **Notas:** Requiere `xmltodict`; el Markdown/CSV resultante alimenta inventarios y reportes.

### `masscan_to_csv.py`
- **Subcategoría:** `parsers/`
- **Descripción:** Convierte salida grepable de Masscan/GNMAP a CSV.
- **Comando de ejemplo:** `python python/parsers/masscan_to_csv.py -i reports/network/masscan.gnmap -o reports/network/masscan.csv`
- **Notas:** Útil para inventario rápido y reporting.

## 2. web/

### `http_headers_probe.py`
- **Subcategoría:** `web/`
- **Descripción:** Recoge cabeceras HTTP/HTTPS y detecta controles defensivos básicos.
- **Comando de ejemplo:** `python python/web/http_headers_probe.py https://example.org app.lab.local:8080 -o automation/reporting/http-headers.csv`
- **Notas:** Útil para inventario web rápido; usa solo librería estándar.

### `dir_bruteforce_report.py`
- **Subcategoría:** `web/`
- **Descripción:** Convierte resultados de `ffuf` en reporte Markdown o CSV.
- **Comando de ejemplo:** `python python/web/dir_bruteforce_report.py -i web/apps/ffuf/results.json -o web/apps/ffuf/report.md`
- **Notas:** Bueno para no perder rutas entre JSON y notas manuales.

### `web_screenshot_manifest.py`
- **Subcategoría:** `web/`
- **Descripción:** Indexa capturas web y crea un manifiesto CSV.
- **Comando de ejemplo:** `python python/web/web_screenshot_manifest.py -i web/screenshots -o web/screenshots/manifest.csv`
- **Notas:** Útil para inventario visual ligero.

## 3. forensics/

### `hash_manifest.py`
- **Subcategoría:** `forensics/`
- **Descripción:** Genera manifiestos MD5/SHA1/SHA256 de directorios completos.
- **Comando de ejemplo:** `python python/forensics/hash_manifest.py -i samples/ -o automation/reporting/hash-manifest.csv --algorithm sha256`
- **Notas:** Ayuda a preservar evidencias y verificar integridad entre entornos.

### `ioc_extractor.py`
- **Subcategoría:** `forensics/`
- **Descripción:** Extrae IOCs comunes desde notas, tickets o logs de texto plano.
- **Comando de ejemplo:** `python python/forensics/ioc_extractor.py -i defense/incident_response/notes.txt -o automation/reporting/iocs.csv`
- **Notas:** Saca IPs, dominios, URLs y hashes; ideal para triage inicial.

### `ioc_enricher.py`
- **Subcategoría:** `forensics/`
- **Descripción:** Añade clasificación y contexto simple a un CSV de IOCs.
- **Comando de ejemplo:** `python python/forensics/ioc_enricher.py -i automation/reporting/iocs.csv -o automation/reporting/iocs-enriched.csv`
- **Notas:** Útil para triage rápido y análisis preliminar.

### `pcap_summary.py`
- **Subcategoría:** `forensics/`
- **Descripción:** Resume un PCAP mediante `tshark` y genera Markdown o JSON.
- **Comando de ejemplo:** `python python/forensics/pcap_summary.py -i captures/session.pcapng -o reports/pcap-summary.md`
- **Notas:** Requiere `tshark` disponible en PATH.

### `evidence_indexer.py`
- **Subcategoría:** `forensics/`
- **Descripción:** Crea un índice CSV de evidencias con hash y tamaño.
- **Comando de ejemplo:** `python python/forensics/evidence_indexer.py -i exploitation/notes -o reports/evidence-index.csv`
- **Notas:** Muy útil para cadena de custodia ligera.

### `chain_of_custody_builder.py`
- **Subcategoría:** `forensics/`
- **Descripción:** Genera una plantilla de cadena de custodia desde CSV.
- **Comando de ejemplo:** `python python/forensics/chain_of_custody_builder.py -i reports/evidence-index.csv -o reports/chain-of-custody.md --case "Caso 01"`
- **Notas:** Bueno para cierre de evidencias y documentación.

## 4. recon/

### `subdomain_diff.py`
- **Subcategoría:** `recon/`
- **Descripción:** Compara dos listas de subdominios y resalta cambios.
- **Comando de ejemplo:** `python python/recon/subdomain_diff.py --old recon/old.txt --new recon/new.txt -o recon/subdomain-diff.md`
- **Notas:** Muy útil para ver evolución de superficie expuesta.

## 5. reporting/

### `nmap_xml_to_markdown.py`
- **Subcategoría:** `reporting/`
- **Descripción:** Convierte XML de Nmap en informe Markdown legible.
- **Comando de ejemplo:** `python python/reporting/nmap_xml_to_markdown.py -i reports/network/nmap-full.xml -o reports/network/nmap-report.md`
- **Notas:** Ayuda a transformar XML en algo más humano para revisar o compartir.

### `markdown_case_bundler.py`
- **Subcategoría:** `reporting/`
- **Descripción:** Une varias notas Markdown en un solo documento.
- **Comando de ejemplo:** `python python/reporting/markdown_case_bundler.py case.md evidence.md timeline.md -o reports/final-case.md --title "Caso 01"`
- **Notas:** Útil para cierres de sesión y reporting rápido.

### `csv_to_markdown_table.py`
- **Subcategoría:** `reporting/`
- **Descripción:** Convierte un CSV simple en tabla Markdown.
- **Comando de ejemplo:** `python python/reporting/csv_to_markdown_table.py -i reports/network/masscan.csv -o reports/network/masscan.md`
- **Notas:** Bueno para pasar inventarios a algo legible.

## 6. ad/

### `ad_notes_builder.py`
- **Subcategoría:** `ad/`
- **Descripción:** Genera una nota estructurada para un caso AD de laboratorio.
- **Comando de ejemplo:** `python python/ad/ad_notes_builder.py --host dc01 --user analyst --domain lab.local --finding "Delegación débil" -o exploitation/active_directory/case-dc01.md`
- **Notas:** Estandariza la documentación en Active Directory.

## Subcategorías actuales
- `parsers/` → conversión y normalización de salidas.
- `web/` → utilidades ligeras para inventario HTTP/HTTPS y reporting de fuzzing.
- `forensics/` → hashes, IOCs, PCAPs y apoyo a evidencias.
- `recon/` → helpers para comparar hallazgos de reconocimiento.
- `reporting/` → scripts para convertir resultados en informes legibles.
- `ad/` → ayudas para documentar mejor laboratorios Active Directory.

## Técnicas de desarrollo
1. Mantengo `python/requirements.txt` con las dependencias (`pandas`, `xmltodict`) y uso un entorno virtual para aislar.
2. Cada script imprime pasos clave (`start`, `processing`, `done`) para poder rastrear errores desde la línea de comandos.
3. Prefiero scripts pequeños, portables y orientados a transformar input en CSV/Markdown reutilizable.

## Recomendaciones personales
- Documenta qué entornos (WSL, virtualenv) probaste y qué versiones de Python (3.11) usas.
- Añade tests simples (input mock + expected output) para que cualquiera pueda validar los scripts.
- Si una subcategoría crece mucho, crea su propio `README.md` y ejemplos dedicados en `examples/`.
