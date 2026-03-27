# Python Tools

Esta carpeta ya no funciona como un cajón de scripts sueltos: ahora está organizada por subcategorías para que la librería pueda crecer sin perder claridad.

## Estructura actual
- `parsers/` → transformación de logs, XML y salidas de scanners a formatos reutilizables.
- `web/` → helpers ligeros para inventario y análisis HTTP/HTTPS.
- `forensics/` → hashes, artefactos, IOCs y utilidades de apoyo para evidencias.
- `recon/` → comparación y normalización de hallazgos de reconocimiento.
- `reporting/` → conversión de resultados técnicos en informes Markdown reutilizables.
- `ad/` → helpers para documentar mejor casos de Active Directory en laboratorio.
- `requirements.txt` → dependencias comunes.
- `DEPENDENCIES.md` → mapa rápido de dependencias Python y herramientas externas por script.
- `toolkit.md` → catálogo vivo de scripts y ejemplos de uso.
- `ROADMAP.md` → ideas priorizadas para futuras ampliaciones.

## Scripts actuales por subcategoría
### `parsers/`
- `parsers/log_parser.py`: parsea logs de Zeek/Suricata y genera CSV resumido.
- `parsers/inventory_builder.py`: combina salidas de `nmap`/`masscan` y las normaliza.
- `parsers/masscan_to_csv.py`: convierte salidas grepables de Masscan/GNMAP en CSV limpio.

### `web/`
- `web/http_headers_probe.py`: consulta objetivos HTTP/HTTPS y exporta headers defensivos clave a CSV.
- `web/dir_bruteforce_report.py`: resume resultados de `ffuf` en Markdown o CSV.
- `web/web_screenshot_manifest.py`: indexa capturas web y genera un manifiesto CSV.

### `forensics/`
- `forensics/hash_manifest.py`: genera manifiestos de hashes para evidencias, muestras o colecciones de laboratorio.
- `forensics/ioc_extractor.py`: extrae IOCs básicos (IPs, dominios, URLs y hashes) desde notas o logs de texto plano.
- `forensics/ioc_enricher.py`: clasifica y contextualiza IOCs a partir de un CSV.
- `forensics/pcap_summary.py`: resume un PCAP mediante `tshark` y genera Markdown o JSON.
- `forensics/evidence_indexer.py`: crea un índice CSV de evidencias con hash y tamaño.
- `forensics/chain_of_custody_builder.py`: genera una plantilla Markdown de cadena de custodia a partir de un índice CSV.

### `recon/`
- `recon/subdomain_diff.py`: compara dos listas de subdominios y genera un resumen Markdown con altas, bajas y coincidencias.

### `reporting/`
- `reporting/nmap_xml_to_markdown.py`: convierte XML de Nmap en un informe Markdown legible.
- `reporting/markdown_case_bundler.py`: une varias notas Markdown en un único informe final.
- `reporting/csv_to_markdown_table.py`: convierte un CSV sencillo en tabla Markdown.

### `ad/`
- `ad/ad_notes_builder.py`: genera una nota estructurada para casos de Active Directory en laboratorio.

## Dependencias
Instala dependencias con:

```bash
pip install -r python/requirements.txt
```

Algunos scripts pueden depender además de utilidades externas del entorno (por ejemplo `tshark` para procesar PCAPs). Si un helper lo necesita, la idea es dejarlo claro en su README y en el ejemplo de uso.

## Ejemplos rápidos
```bash
python python/web/http_headers_probe.py https://example.org 10.10.10.5:8080 -o automation/reporting/http-headers.csv
python python/web/dir_bruteforce_report.py -i web/apps/ffuf/results.json -o web/apps/ffuf/report.md
python python/web/web_screenshot_manifest.py -i web/screenshots -o web/screenshots/manifest.csv
python python/forensics/hash_manifest.py -i samples/ -o automation/reporting/hash-manifest.csv --algorithm sha256
python python/forensics/ioc_extractor.py -i defense/incident_response/notes.txt -o automation/reporting/iocs.csv
python python/forensics/ioc_enricher.py -i automation/reporting/iocs.csv -o automation/reporting/iocs-enriched.csv
python python/forensics/pcap_summary.py -i captures/session.pcapng -o reports/pcap-summary.md
python python/forensics/evidence_indexer.py -i exploitation/notes -o reports/evidence-index.csv
python python/forensics/chain_of_custody_builder.py -i reports/evidence-index.csv -o reports/chain-of-custody.md --case "Caso 01"
python python/parsers/log_parser.py --input defense/monitoring/logs/zeek.log --output automation/reporting/results/defense/zeek-summary.csv
python python/parsers/masscan_to_csv.py -i reports/network/masscan.gnmap -o reports/network/masscan.csv
python python/recon/subdomain_diff.py --old recon/old.txt --new recon/new.txt -o recon/subdomain-diff.md
python python/reporting/nmap_xml_to_markdown.py -i reports/network/nmap-full.xml -o reports/network/nmap-report.md
python python/reporting/csv_to_markdown_table.py -i reports/network/masscan.csv -o reports/network/masscan.md
python python/ad/ad_notes_builder.py --host dc01 --user analyst --domain lab.local --finding "Delegación débil" -o exploitation/active_directory/case-dc01.md
```

Los ejemplos del toolkit (`python/toolkit.md`) muestran líneas exactas para integrarlos en tu repo sin improvisar demasiado.

Si quieres ampliar la carpeta con nuevas utilidades, revisa también `python/ROADMAP.md`: ahí tienes una selección razonada de scripts candidatos para futuras tandas.
