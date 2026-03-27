# Python Tools

Esta carpeta ya no funciona como un cajón de scripts sueltos: ahora está organizada por subcategorías para que la librería pueda crecer sin perder claridad.

## Estructura actual
- `parsers/` → transformación de logs, XML y salidas de scanners a formatos reutilizables.
- `web/` → helpers ligeros para inventario y análisis HTTP/HTTPS.
- `forensics/` → hashes, artefactos, IOCs y utilidades de apoyo para evidencias.
- `requirements.txt` → dependencias comunes.
- `toolkit.md` → catálogo vivo de scripts y ejemplos de uso.
- `ROADMAP.md` → ideas priorizadas para futuras ampliaciones.

## Scripts actuales por subcategoría
### `parsers/`
- `parsers/log_parser.py`: parsea logs de Zeek/Suricata y genera CSV resumido.
- `parsers/inventory_builder.py`: combina salidas de `nmap`/`masscan` y las normaliza.

### `web/`
- `web/http_headers_probe.py`: consulta objetivos HTTP/HTTPS y exporta headers defensivos clave a CSV.

### `forensics/`
- `forensics/hash_manifest.py`: genera manifiestos de hashes para evidencias, muestras o colecciones de laboratorio.
- `forensics/ioc_extractor.py`: extrae IOCs básicos (IPs, dominios, URLs y hashes) desde notas o logs de texto plano.

## Dependencias
Instala dependencias con:

```bash
pip install -r python/requirements.txt
```

Los scripts actuales siguen siendo pequeños y directos. La reorganización busca que, cuando la carpeta crezca, no tengas que rebuscar entre archivos sin contexto.

## Ejemplos rápidos
```bash
python python/web/http_headers_probe.py https://example.org 10.10.10.5:8080 -o automation/reporting/http-headers.csv
python python/forensics/hash_manifest.py -i samples/ -o automation/reporting/hash-manifest.csv --algorithm sha256
python python/forensics/ioc_extractor.py -i defense/incident_response/notes.txt -o automation/reporting/iocs.csv
python python/parsers/log_parser.py --input defense/monitoring/logs/zeek.log --output automation/reporting/results/defense/zeek-summary.csv
```

Los ejemplos del toolkit (`python/toolkit.md`) muestran líneas exactas para integrarlos en tu repo sin improvisar demasiado.

Si quieres ampliar la carpeta con nuevas utilidades, revisa también `python/ROADMAP.md`: ahí tienes una selección razonada de scripts candidatos para futuras tandas.
