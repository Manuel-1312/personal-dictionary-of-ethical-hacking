# Templates de Reportes

Este directorio almacena las plantillas base que uso para generar reportes rápidos sin volver a escribir de cero. Cada archivo incluye variables (`$HALLAZGOS`, `$IMPACTO`, `$REMEDIACION`) y una breve guía sobre cuándo usarlo.

- Markdown + Pandoc: plantilla `standard.md` con encabezados, tablas y secciones `Resumen`, `Hallazgos`, `Recomendaciones`. Lo convierto en PDF con `pandoc standard.md -o standard.pdf`.
- Allure: guardo plantillas JSON en `allure/` que se rellenan con los resultados automatizados.
- Grafana: exporto dashboards JSON y los actualizo cuando la telemetría cambia.

Copia la plantilla, rellena los campos, ejecuta el script `automation/reporting/scripts/render.sh` y guarda la salida en `automation/reporting/results/` para tener trazabilidad.

## Comandos utilizados
- `pandoc automation/reporting/templates/standard.md -o automation/reporting/results/report-20260327.pdf`.
- `python automation/reporting/scripts/render.py --template automation/reporting/templates/standard.md`.

## Técnicas aplicadas
- Plantillas en Markdown con variables para campos dinámicos.
- Allure + Grafana para cubrir resultados automáticos y manuales.

## Recomendaciones personales
- Mantén las plantillas versionadas en Git y anota qué variable es obligatoria.
- Documenta en `templates/notes.md` qué datos necesitas para cada template.