# Toolkit - Python Tools 🐍

Documenta cada script, comando o helper que programas para esta biblioteca y anota qué dependencias necesita.

| Script | Descripción | Comando de ejemplo | Notas |
| --- | --- | --- | --- |
| `log_parser.py` | Extrae IPs, puertos y alertas de Zeek/Suricata para CSV/Markdown | `python python/log_parser.py --input defense/monitoring/logs/bro.log --output automation/reporting/results/zeek-summary.csv` | Usa pandas y argparse; genera un CSV con columnas `timestamp`, `src`, `dst`, `protocol`, `port`. |
| `inventory_builder.py` | Combina `nmap` y `masscan` para generar inventario unificado | `python python/inventory_builder.py --nmap reports/network/nmap-full.xml --masscan reports/network/masscan.gnmap --out reports/network/inventory.md` | Requiere `xmltodict`; el Markdown/CSV resultante alimenta inventarios y reportes. |
| `http_headers_probe.py` | Recoge cabeceras HTTP/HTTPS y detecta controles defensivos básicos | `python python/http_headers_probe.py https://example.org app.lab.local:8080 -o automation/reporting/http-headers.csv` | Útil para inventario web rápido; usa solo librería estándar. |
| `hash_manifest.py` | Genera manifiestos MD5/SHA1/SHA256 de directorios completos | `python python/hash_manifest.py -i samples/ -o automation/reporting/hash-manifest.csv --algorithm sha256` | Ayuda a preservar evidencias y verificar integridad entre entornos. |
| `ioc_extractor.py` | Extrae IOCs comunes desde notas, tickets o logs de texto plano | `python python/ioc_extractor.py -i defense/incident_response/notes.txt -o automation/reporting/iocs.csv` | Saca IPs, dominios, URLs y hashes; ideal para triage inicial. |

## Comandos utilizados recientemente
- `python python/log_parser.py --input defense/monitoring/logs/zeek.log --output automation/reporting/results/defense/zeek-summary.csv`.
- `python python/inventory_builder.py --nmap reports/network/nmap-full.xml --masscan reports/network/masscan.gnmap --out reports/network/inventory.md`.
- `python python/http_headers_probe.py https://example.org app.lab.local:8080 -o automation/reporting/http-headers.csv`.
- `python python/hash_manifest.py -i samples/ -o automation/reporting/hash-manifest.csv --algorithm sha256`.
- `python python/ioc_extractor.py -i defense/incident_response/notes.txt -o automation/reporting/iocs.csv`.

## Técnicas de desarrollo
1. Mantengo `python/requirements.txt` con las dependencias (`pandas`, `xmltodict`) y uso un entorno virtual para aislar.
2. Cada script imprime pasos clave (`start`, `processing`, `done`) para poder rastrear errores desde la línea de comandos.
3. Prefiero scripts pequeños, portables y orientados a transformar input en CSV/Markdown reutilizable.

## Recomendaciones personales
- Documenta qué entornos (WSL, virtualenv) probaste y qué versiones de Python (3.11) usas.
- Añade tests simples (input mock + expected output) para que cualquiera pueda validar el script.
- Si un helper crece demasiado, muévelo a una subcarpeta (`python/parsers/`, `python/reporting/`, etc.) para mantener orden.
