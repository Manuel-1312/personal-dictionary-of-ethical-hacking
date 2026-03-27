# Python Web Helpers

Aquí van las utilidades Python orientadas a inventario y análisis web ligero. No sustituyen a Burp, ZAP o scanners grandes; sirven para automatizar pequeñas tareas repetitivas.

## Scripts actuales
- `http_headers_probe.py` → consulta objetivos HTTP/HTTPS y exporta cabeceras defensivas clave.
- `dir_bruteforce_report.py` → convierte resultados de `ffuf` en reportes Markdown o CSV.

## Recomendaciones
- Guarda resultados en `automation/reporting/` o en notas de caso si el script se usa dentro de una validación web.
- Si luego añades más herramientas web, merece la pena separar `inventory/`, `fuzzing/` y `screenshots/`.
