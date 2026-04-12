# Toolkit - Templates ✍️

Documenta cada plantilla, qué variables contiene y qué script la usa. Así cualquiera puede levantar un reporte sin tener que adivinar los campos.

## Plantilla base
- **Enlace:** referencia oficial de la herramienta de plantillas.
- **Caso de uso:** qué tipo de reporte genera esta plantilla.
- **Comando de ejemplo:** comando para renderizar la plantilla.
- **Notas útiles:** variables clave y rutas de salida.
- **Recomendaciones:** cómo mantener y versionar la plantilla.
- **Cuándo usar / cuándo no:** adapta la plantilla al formato requerido por el destinatario.

## 1. Plantillas disponibles

### Markdown + Pandoc
- **Enlace:** https://pandoc.org/
- **Caso de uso:** Generación de reportes PDF estándar para stakeholders a partir de Markdown con variables.
- **Comando de ejemplo:** `bash automation/reporting/scripts/render.sh standard.md`
- **Notas útiles:** Variables: `$RESUMEN`, `$HALLAZGOS`, `$REMEDIACION`; genera `standard.pdf` para enviar a stakeholders.
- **Recomendaciones:** Documenta las variables disponibles en un `README.md` de la plantilla; usa YAML front matter para metadatos.
- **Cuándo usarlo:** Para reportes narrativos estandarizados que se entregan como PDF a clientes o gestión.
- **Cuándo no:** Para reportes con tablas muy complejas o gráficos; considera LibreOffice para esos casos.

### Allure report
- **Enlace:** https://qameta.io/allure/
- **Caso de uso:** Reportes HTML interactivos generados automáticamente a partir de resultados de tests Playwright.
- **Comando de ejemplo:** `npx playwright test --reporter=allure && allure generate allure-results -o allure-report`
- **Notas útiles:** Conecto Playwright + Allure; el HTML resultante se aloja en `automation/reporting/results/allure/`.
- **Recomendaciones:** Versiona el directorio `allure-results/` para poder regenerar el reporte; añade el enlace al caso.
- **Cuándo usarlo:** Cuando los tests automatizados son la fuente de evidencia principal del reporte.
- **Cuándo no:** Para reportes manuales sin cobertura de tests automatizados.

### CyberChef cookbook
- **Enlace:** https://gchq.github.io/CyberChef/
- **Caso de uso:** Recetas reutilizables para transformar y normalizar datos de logs antes de adjuntarlos al reporte.
- **Comando de ejemplo:** Carga la receta desde `templates/cyberchef/normalizar-base64.json` en CyberChef.
- **Notas útiles:** Guarda recetas en `templates/cyberchef/` y aplica a logs antes de adjuntarlos; entrada y salida documentadas.
- **Recomendaciones:** Exporta cada receta en JSON con un nombre descriptivo; documenta qué tipo de datos transforma.
- **Cuándo usarlo:** Para normalizar o decodificar artefactos antes de incluirlos como evidencia en el reporte.
- **Cuándo no:** Para transformaciones simples que se pueden hacer con una línea de `awk` o `sed`.

### Grafana JSON
- **Enlace:** https://grafana.com/
- **Caso de uso:** Dashboards exportados para importar en Grafana cuando cambian índices o se monta un nuevo entorno.
- **Comando de ejemplo:** Grafana → Dashboard → Export JSON → guarda en `templates/grafana/<nombre>-dashboard.json`.
- **Notas útiles:** Exporto dashboards, los edito y los importo a Grafana cuando cambian los índices de datos.
- **Recomendaciones:** Versiona el JSON del dashboard en Git; documenta qué fuente de datos y qué índice usa cada panel.
- **Cuándo usarlo:** Para reutilizar dashboards entre entornos o cuando necesitas compartir una visualización estándar.
- **Cuándo no:** Sin documentar la fuente de datos; un dashboard importado sin la fuente configurada no mostrará datos.

### Excel template
- **Enlace:** https://www.libreoffice.org/
- **Caso de uso:** Hojas de cálculo para trackers de hallazgos que luego se convierten a CSV para adjuntar al proyecto.
- **Comando de ejemplo:** `libreoffice --headless --convert-to csv findings-tracker.ods --outdir results/`
- **Notas útiles:** Usa para trackers de hallazgos y luego convierte a CSV para adjuntar al proyecto.
- **Recomendaciones:** Mantén una plantilla base con las columnas estándar (ID, Severidad, Descripción, Remediación, Estado, Responsable).
- **Cuándo usarlo:** Para entregar tablas de hallazgos en formato XLSX cuando el cliente o stakeholder lo requiere.
- **Cuándo no:** Para reportes narrativos; el formato Markdown + Pandoc es más adecuado y tiene mejor control de versiones.

## 2. Flujos y documentación
- Versiona todas las plantillas en `automation/reporting/templates/` con un `README.md` que describa las variables de cada una.
- Guarda los reportes generados en `automation/reporting/results/<tipo>/<fecha>/` separados de las plantillas fuente.
- Documenta qué plantilla se usó para cada entregable en el README del caso correspondiente.
