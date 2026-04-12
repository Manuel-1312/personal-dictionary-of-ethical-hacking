# Toolkit - Reporting 📊

Herramientas que convierten datos crudos en entregables. Para cada una explico qué script ejecuté, qué archivo genera y qué incluí en el reporte.

## Plantilla base
- **Enlace:** referencia oficial de la herramienta.
- **Caso de uso:** qué tipo de output genera (HTML, PDF, JSON, XLSX).
- **Comando de ejemplo:** comando típico con opciones de output.
- **Notas útiles:** rutas de salida y qué incluir en el reporte.
- **Recomendaciones:** cómo organizar y versionar los reportes generados.
- **Cuándo usar / cuándo no:** adapta el formato al audiencia del reporte.

## 1. Herramientas de reporting

### Allure
- **Enlace:** https://qameta.io/allure/
- **Caso de uso:** Generación de reportes HTML interactivos a partir de resultados de tests automatizados.
- **Comando de ejemplo:** `npx playwright test --reporter=allure && allure generate allure-results -o allure-report`
- **Notas útiles:** `npx playwright test --reporter=allure` → carpeta `automation/reporting/results/allure/`; incrusta el enlace en el README del caso.
- **Recomendaciones:** Guarda el directorio `allure-results/` en el repositorio para poder regenerar el reporte; añade el enlace al caso en The Hive.
- **Cuándo usarlo:** Cuando los tests automatizados generan los resultados de la auditoría y necesitas un reporte visual.
- **Cuándo no:** Para reportes manuales sin tests automatizados; usa Pandoc + Markdown en esos casos.

### CyberChef
- **Enlace:** https://gchq.github.io/CyberChef/
- **Caso de uso:** Transformaciones y normalización de datos de logs para prepararlos antes de adjuntarlos al reporte.
- **Comando de ejemplo:** Abre https://gchq.github.io/CyberChef/ → carga la receta desde `automation/reporting/templates/cyberchef/`.
- **Notas útiles:** Aplico recetas para normalizar logs y guardo la receta JSON en `automation/reporting/templates/cyberchef/`.
- **Recomendaciones:** Exporta la receta en JSON y versiona en el repositorio para que sea reproducible por otros.
- **Cuándo usarlo:** Para decodificar, descomprimir o normalizar datos de logs antes de incluirlos en el reporte.
- **Cuándo no:** Para transformaciones que pueden automatizarse con un script; la GUI no es reproducible sin exportar la receta.

### Pandoc
- **Enlace:** https://pandoc.org/
- **Caso de uso:** Conversión de Markdown a PDF, HTML u otros formatos usando plantillas personalizadas.
- **Comando de ejemplo:** `pandoc report.md -o report.pdf --template=automation/reporting/templates/report.tpl`
- **Notas útiles:** Convierte Markdown a PDF con la plantilla `automation/reporting/templates/report.tpl`.
- **Recomendaciones:** Versiona la plantilla en el repositorio; usa variables YAML en el front matter del Markdown para los metadatos del reporte.
- **Cuándo usarlo:** Para generar entregables PDF/HTML a partir de reportes escritos en Markdown.
- **Cuándo no:** Para documentos con formato muy complejo; considera LibreOffice o una herramienta dedicada en esos casos.

### Grafana
- **Enlace:** https://grafana.com/
- **Caso de uso:** Dashboards interactivos para visualizar métricas de seguridad, logs y alertas en tiempo real.
- **Comando de ejemplo:** Grafana UI → Dashboard → Export → Save JSON → guarda en `defense/monitoring/dashboard.json`.
- **Notas útiles:** Exporto paneles (`defense/monitoring/dashboard.json`) y explico qué métricas muestra cada panel.
- **Recomendaciones:** Incluye una descripción en el dashboard exportado de qué fuentes de datos usa y qué métricas visualiza.
- **Cuándo usarlo:** Para presentar métricas de monitoreo y detección de forma visual a stakeholders o durante un incidente.
- **Cuándo no:** Para reportes estáticos; en esos casos genera una captura del dashboard y adjúntala al reporte.

### LibreOffice / Excel
- **Enlace:** https://www.libreoffice.org/
- **Caso de uso:** Generación y edición de hojas de cálculo XLSX para tablas de hallazgos y trackers de remediación.
- **Comando de ejemplo:** `libreoffice --headless --convert-to xlsx findings.ods --outdir automation/reporting/results/xlsx/`
- **Notas útiles:** Las tablas de hallazgos exportadas se guardan en `automation/reporting/results/xlsx/`.
- **Recomendaciones:** Usa una plantilla estandarizada con las columnas: ID, Severidad, Descripción, Remediación, Estado.
- **Cuándo usarlo:** Para entregar tablas de hallazgos a clientes o stakeholders que prefieren formato XLSX.
- **Cuándo no:** Para reportes narrativos; en esos casos usa Pandoc + Markdown para mejor control de versiones.

### Markdown templating (Jinja2)
- **Enlace:** https://jinja.palletsprojects.com/
- **Caso de uso:** Generación de reportes Markdown a partir de plantillas con variables rellenadas automáticamente.
- **Comando de ejemplo:** `python scripts/render-report.py --template TEMPLATE.md --vars vars.json -o report-final.md`
- **Notas útiles:** `scripts/render-report.py` rellena `TEMPLATE.md` con variables (`$IMPACTO`, `$REMEDIACION`).
- **Recomendaciones:** Versiona tanto la plantilla como el script; documenta las variables disponibles en un `README.md` de plantillas.
- **Cuándo usarlo:** Para generar reportes estandarizados de forma automática con datos de múltiples fuentes.
- **Cuándo no:** Para reportes únicos sin patrón repetible; en esos casos es más rápido escribir el Markdown directamente.

## 2. Flujos y documentación
- Guarda cada reporte generado en `automation/reporting/results/<tipo>/<fecha>/` con el nombre del caso.
- Versiona las plantillas usadas en `automation/reporting/templates/` para reproducibilidad.
- Documenta qué herramienta generó cada entregable y con qué parámetros en el README del caso.
