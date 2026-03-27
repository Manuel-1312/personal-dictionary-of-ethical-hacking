# Reporting

Aquí guardo plantillas, scripts y dashboards que transforman los hallazgos del laboratorio en informes comprensibles. Cada vez que corro un script (`./automation/reporting/render.sh`) exporta un HTML/PDF, y ese artefacto queda en `automation/reporting/results/`.

- `templates/`: Markdown, Allure e incluso dashboards JSON que reutilizo.
- `results/`: salidas reales (PDF, CSV, HTML) que enlazo desde los casos para mostrar evidencia.
- `reports/`: actualizo con fechas y qué datos alimenté (captures, scans, hunts).

Cuando preparo un reporte final, incluyo tablas de resumen con `Impacto`, `Severidad`, `Remediación` y adjunto los outputs del kit de vulnerabilidades. Si algo queda pendiente, añado una nota `PRÓXIMOS PASOS` al final del reporte.

## Comandos utilizados
- `python automation/reporting/scripts/render.py --template automation/reporting/templates/standard.md --output automation/reporting/results/report-20260327.pdf`.
- `npx playwright test --reporter=allure && mv allure-results automation/reporting/results/allure/2026-03-27`.

## Técnicas aplicadas
- Uso de plantillas Markdown + Pandoc y dashboards Allure para combinar pruebas manuales + automatizadas.
- Exporto Grafana dashboards en JSON y los guardo en `automation/reporting/results/grafana/`.

## Recomendaciones personales
- Guarda los resultados (PDF, HTML) junto a un pequeño resumen con las conclusiones.
- Si un reporte falla en render: verifica la plantilla y los datos (checa `automation/reporting/templates/variables.md`).