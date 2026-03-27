# Toolkit - Respuesta a Incidentes 🚨

Documenta cada herramienta, script y recurso usado durante un incidente real o simulado.

| Recurso | Enlace | Fase | Notas reales |
| --- | --- | --- | --- |
| The Hive | https://github.com/TheHive-Project/TheHive | Gestión de casos | Caso `CASE-2026-03-27`: enlace de detección y pasos de contención.
| Cortex | https://github.com/TheHive-Project/Cortex | Análisis | Workflow `hashlookup` + `vt` ejecutado sobre muestra sospechosa.
| Velociraptor | https://github.com/Velocidex/velociraptor | Recolección | Query `pslist` + `carving` y resultados en `defense/incident_response/artifacts/`.
| GRR Rapid Response | https://github.com/google/grr | Telemetría | Artifact `filefinder` en hosts con alertas de Wazuh.
| Cyber Triage | https://www.cynic.es/ | Análisis rápido | Usa la GUI para validar artefactos y exporta `triage.json`.
| Elastic Stack | https://www.elastic.co/elastic-stack | Correlación | Dashboards y filtros aplicados durante la investigación.
| Playbook personalizado | (tu script) | Automación | `scripts/contención.sh`: detiene procesos y copia logs a `/tmp/incidente/`.
