# Toolkit - Reporting 📊

Conservo aquí las herramientas que convierten datos crudos en entregables. En cada fila explico qué script ejecuté, qué archivo genera y qué incluí en el reporte.

| Herramienta | Enlace | Output | Notas del reporte |
| --- | --- | --- | --- |
| Allure | https://qameta.io/allure/ | HTML | `npx playwright test --reporter=allure` → carpeta `automation/reporting/results/allure/`; incrusto el enlace en el README del caso. |
| CyberChef | https://gchq.github.io/CyberChef/ | Transformaciones | Aplico recetas para normalizar logs y guardo la receta en `automation/reporting/templates/cyberchef/`. |
| Pandoc | https://pandoc.org/ | PDF/HTML | Convierte Markdown a PDF con la plantilla `automation/reporting/templates/report.tpl`. |
| Grafana | https://grafana.com/ | JSON/Dashboards | Exporto paneles (`defense/monitoring/dashboard.json`) y explico qué métricas muestra el panel. |
| LibreOffice / Excel | https://www.libreoffice.org/ | XLSX | Las tablas de hallazgos exportadas se guardan en `automation/reporting/results/xlsx/`. |
| Markdown templating (Jinja2) | https://jinja.palletsprojects.com/ | Markdown | `scripts/render-report.py` rellena `TEMPLATE.md` con variables (`$IMPACTO`, `$REMEDIACION`). |
