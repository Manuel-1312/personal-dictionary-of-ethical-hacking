# Python Tools

Esta carpeta colecciona tus scripts propios para acelerar tareas típicas de la biblioteca: parseo de logs, generación de reportes, inventario, validación de artefactos y pequeños helpers que complementan los toolkits.

Cada script tiene una descripción clara de qué hace, qué dependencias necesita y qué salida produce. Ahora mismo incluye:

- `log_parser.py`: parsea logs de Zeek/Suricata, extrae IPs + puertos y genera un CSV resumido.
- `inventory_builder.py`: combina salidas de `nmap`/`masscan` y las normaliza.
- `http_headers_probe.py`: consulta objetivos HTTP/HTTPS y exporta headers defensivos clave a CSV.
- `hash_manifest.py`: genera manifiestos de hashes para evidencias, muestras o colecciones de laboratorio.
- `ioc_extractor.py`: extrae IOCs básicos (IPs, dominios, URLs y hashes) desde notas o logs de texto plano.

Instala dependencias con `pip install -r python/requirements.txt`. Los scripts nuevos funcionan con librería estándar; `log_parser.py` e `inventory_builder.py` mantienen las dependencias actuales para facilitar futuras ampliaciones.

Ejemplos rápidos:

```bash
python python/http_headers_probe.py https://example.org 10.10.10.5:8080 -o automation/reporting/http-headers.csv
python python/hash_manifest.py -i samples/ -o automation/reporting/hash-manifest.csv --algorithm sha256
python python/ioc_extractor.py -i defense/incident_response/notes.txt -o automation/reporting/iocs.csv
```

Los ejemplos del toolkit (`python/toolkit.md`) muestran líneas exactas para integrarlos en tu repo sin improvisar demasiado.
