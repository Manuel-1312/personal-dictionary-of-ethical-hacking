# Toolkit - Python Tools 🐍

Documenta cada script, comando o helper que programas para esta biblioteca y anota qué dependencias necesita.

| Script | Subcategoría | Descripción | Comando de ejemplo | Notas |
| --- | --- | --- | --- | --- |
| `parsers/log_parser.py` | `parsers/` | Extrae IPs, puertos y alertas de Zeek/Suricata para CSV/Markdown | `python python/parsers/log_parser.py --input defense/monitoring/logs/bro.log --output automation/reporting/results/zeek-summary.csv` | Usa pandas y argparse; genera un CSV con columnas `timestamp`, `src`, `dst`, `protocol`, `port`. |
| `parsers/inventory_builder.py` | `parsers/` | Combina `nmap` y `masscan` para generar inventario unificado | `python python/parsers/inventory_builder.py --nmap reports/network/nmap-full.xml --masscan reports/network/masscan.gnmap --out reports/network/inventory.md` | Requiere `xmltodict`; el Markdown/CSV resultante alimenta inventarios y reportes. |
| `web/http_headers_probe.py` | `web/` | Recoge cabeceras HTTP/HTTPS y detecta controles defensivos básicos | `python python/web/http_headers_probe.py https://example.org app.lab.local:8080 -o automation/reporting/http-headers.csv` | Útil para inventario web rápido; usa solo librería estándar. |
| `forensics/hash_manifest.py` | `forensics/` | Genera manifiestos MD5/SHA1/SHA256 de directorios completos | `python python/forensics/hash_manifest.py -i samples/ -o automation/reporting/hash-manifest.csv --algorithm sha256` | Ayuda a preservar evidencias y verificar integridad entre entornos. |
| `forensics/ioc_extractor.py` | `forensics/` | Extrae IOCs comunes desde notas, tickets o logs de texto plano | `python python/forensics/ioc_extractor.py -i defense/incident_response/notes.txt -o automation/reporting/iocs.csv` | Saca IPs, dominios, URLs y hashes; ideal para triage inicial. |
| `recon/subdomain_diff.py` | `recon/` | Compara dos listas de subdominios y resalta cambios | `python python/recon/subdomain_diff.py --old recon/old.txt --new recon/new.txt -o recon/subdomain-diff.md` | Muy útil para ver evolución de superficie expuesta. |
| `reporting/nmap_xml_to_markdown.py` | `reporting/` | Convierte XML de Nmap en informe Markdown legible | `python python/reporting/nmap_xml_to_markdown.py -i reports/network/nmap-full.xml -o reports/network/nmap-report.md` | Ayuda a transformar XML en algo más humano para revisar o compartir. |
| `reporting/markdown_case_bundler.py` | `reporting/` | Une varias notas Markdown en un solo documento | `python python/reporting/markdown_case_bundler.py case.md evidence.md timeline.md -o reports/final-case.md --title "Caso 01"` | Útil para cierres de sesión y reporting rápido. |
| `ad/ad_notes_builder.py` | `ad/` | Genera una nota estructurada para un caso AD de laboratorio | `python python/ad/ad_notes_builder.py --host dc01 --user analyst --domain lab.local --finding "Delegación débil" -o exploitation/active_directory/case-dc01.md` | Estandariza la documentación en Active Directory. |

## Comandos utilizados recientemente
- `python python/parsers/log_parser.py --input defense/monitoring/logs/zeek.log --output automation/reporting/results/defense/zeek-summary.csv`.
- `python python/parsers/inventory_builder.py --nmap reports/network/nmap-full.xml --masscan reports/network/masscan.gnmap --out reports/network/inventory.md`.
- `python python/web/http_headers_probe.py https://example.org app.lab.local:8080 -o automation/reporting/http-headers.csv`.
- `python python/forensics/hash_manifest.py -i samples/ -o automation/reporting/hash-manifest.csv --algorithm sha256`.
- `python python/forensics/ioc_extractor.py -i defense/incident_response/notes.txt -o automation/reporting/iocs.csv`.
- `python python/recon/subdomain_diff.py --old recon/old.txt --new recon/new.txt -o recon/subdomain-diff.md`.
- `python python/reporting/nmap_xml_to_markdown.py -i reports/network/nmap-full.xml -o reports/network/nmap-report.md`.
- `python python/reporting/markdown_case_bundler.py case.md evidence.md timeline.md -o reports/final-case.md --title "Caso 01"`.
- `python python/ad/ad_notes_builder.py --host dc01 --user analyst --domain lab.local --finding "Delegación débil" -o exploitation/active_directory/case-dc01.md`.

## Subcategorías actuales
- `parsers/` → conversión y normalización de salidas.
- `web/` → utilidades ligeras para inventario HTTP/HTTPS.
- `forensics/` → hashes, IOCs y apoyo a evidencias.
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
