# Toolkit - Templates ✍️

Documenta cada plantilla, qué variables contiene y qué script la usa. Así cualquiera puede levantar un reporte sin tener que adivinar los campos.

| Template | Herramienta | Variables clave | Uso real |
| --- | --- | --- | --- |
| Markdown + Pandoc | https://pandoc.org/ | `$RESUMEN`, `$HALLAZGOS`, `$REMEDIACION` | `automation/reporting/scripts/render.sh standard.md` genera `standard.pdf` que uso para enviar a stakeholders.
| Allure report | https://qameta.io/allure/ | `results/` | Conecto Playwright + Allure (`npx playwright test --reporter=allure`). El HTML resultante se aloja en `automation/reporting/results/allure/`. |
| CyberChef cookbook | https://gchq.github.io/CyberChef/ | Entrada/Salida | Guardo recetas en `templates/cyberchef/` y las aplico a logs antes de adjuntarlos al reporte. |
| Grafana JSON | https://grafana.com/ | Panels | Exporto dashboards, los edito y los importo a Grafana cuando cambian los índices. |
| Excel template | https://www.libreoffice.org/ | Tablas | Uso para trackers de hallazgos y luego convierto a CSV para adjuntar al proyecto. |
