# Toolkit - Respuesta a Incidentes 🚨

Documenta cada herramienta, script y recurso usado durante un incidente real o simulado.

## Plantilla base
- **Enlace:** referencia oficial de la herramienta.
- **Caso de uso:** qué fase del incidente cubre (detección, análisis, contención, erradicación).
- **Comando de ejemplo:** comando o workflow típico.
- **Notas útiles:** hallazgos concretos y rutas de evidencia guardada.
- **Recomendaciones:** cómo documentar el uso dentro del caso.
- **Cuándo usar / cuándo no:** en entornos autorizados; enlaza siempre al caso correspondiente.

## 1. Herramientas de respuesta a incidentes

### The Hive
- **Enlace:** https://github.com/TheHive-Project/TheHive
- **Caso de uso:** Gestión de casos de incidentes con tareas, observables y timeline centralizado.
- **Comando de ejemplo:** `curl -XPOST http://thehive:9000/api/case -H 'Authorization: Bearer <key>' -d '{"title":"IR-2026-03-27","severity":3}'`
- **Notas útiles:** Caso `CASE-2026-03-27`: enlace de detección y pasos de contención documentados en el caso.
- **Recomendaciones:** Crea el caso antes de cualquier acción; adjunta evidencias y observables a medida que avanzas.
- **Cuándo usarlo:** Como plataforma central para coordinar la respuesta y mantener la cadena de custodia.
- **Cuándo no:** Sin permisos de escritura o en entornos donde The Hive no está desplegado; usa un documento alternativo.

### Cortex
- **Enlace:** https://github.com/TheHive-Project/Cortex
- **Caso de uso:** Análisis automático de observables (hashes, IPs, URLs) mediante analyzers configurables.
- **Comando de ejemplo:** Desde The Hive: selecciona el observable → Run Analyzer → `VirusTotal_GetReport` + `Hashlookup`.
- **Notas útiles:** Workflow `hashlookup` + `vt` ejecutado sobre muestra sospechosa; resultados adjuntados al caso.
- **Recomendaciones:** Configura las API keys de los analyzers antes del incidente; documenta qué analyzers dieron positivo.
- **Cuándo usarlo:** Para enriquecer observables con contexto de threat intel durante el análisis.
- **Cuándo no:** Sin API keys configuradas los analyzers más útiles no estarán disponibles.

### Velociraptor
- **Enlace:** https://github.com/Velocidex/velociraptor
- **Caso de uso:** Recolección forense remota en endpoints afectados mediante artifacts VQL.
- **Comando de ejemplo:** `velociraptor --config server.config.yaml artifacts collect Generic.System.Pslist`
- **Notas útiles:** Query `pslist` + `carving` y resultados en `defense/incident_response/artifacts/`.
- **Recomendaciones:** Anota qué artifacts ejecutaste, en qué hosts y en qué momento; adjunta resultados al caso.
- **Cuándo usarlo:** Para recolección forense rápida cuando necesitas datos de múltiples endpoints simultáneamente.
- **Cuándo no:** Sin el agente instalado en los hosts o fuera del alcance del incidente declarado.

### GRR Rapid Response
- **Enlace:** https://github.com/google/grr
- **Caso de uso:** Telemetría forense remota con artifacts especializados para análisis de persistencia y archivos.
- **Comando de ejemplo:** `grr_api_client flows start --client <id> --artifact FileFinder --conditions path=/etc/cron*`
- **Notas útiles:** Artifact `filefinder` ejecutado en hosts con alertas de Wazuh; resultados adjuntados al caso.
- **Recomendaciones:** Complementa Velociraptor con GRR cuando necesitas artifacts específicos no disponibles en el primero.
- **Cuándo usarlo:** Para análisis forense en profundidad de hosts específicos con alertas confirmadas.
- **Cuándo no:** En hosts sin agente GRR o fuera del perímetro del incidente.

### Cyber Triage
- **Enlace:** https://www.cynic.es/
- **Caso de uso:** Análisis rápido de artefactos de triage para identificar IOCs en endpoints Windows.
- **Comando de ejemplo:** Abre Cyber Triage → Import → selecciona el archivo de triage → exporta `triage.json`.
- **Notas útiles:** Usa la GUI para validar artefactos y exporta `triage.json` para adjuntarlo al caso.
- **Recomendaciones:** Usa para validación rápida antes de un análisis forense profundo; guarda el `triage.json` con nombre del host y fecha.
- **Cuándo usarlo:** Como primera revisión rápida de un host sospechoso antes de dedicar más recursos.
- **Cuándo no:** Como análisis definitivo; complementa siempre con herramientas forenses más detalladas.

### Elastic Stack
- **Enlace:** https://www.elastic.co/elastic-stack
- **Caso de uso:** Correlación de logs y búsqueda de IOCs en dashboards durante la investigación.
- **Comando de ejemplo:** `GET logs-*/_search { "query": { "match": { "process.name": "mimikatz.exe" } } }`
- **Notas útiles:** Dashboards y filtros aplicados durante la investigación; guarda los filtros como saved searches.
- **Recomendaciones:** Crea saved searches para cada IOC identificado; exporta los resultados relevantes en JSON.
- **Cuándo usarlo:** Para búsqueda rápida de IOCs en el volumen de logs indexados durante el incidente.
- **Cuándo no:** Sin los índices correctos o sin los datos del período del incidente ingestados.

### Playbook personalizado
- **Enlace:** (tu script local)
- **Caso de uso:** Automatización de pasos repetitivos de contención y recolección de logs.
- **Comando de ejemplo:** `bash scripts/contencion.sh <hostname> <case-id>`
- **Notas útiles:** `scripts/contencion.sh`: detiene procesos sospechosos y copia logs al directorio del caso.
- **Recomendaciones:** Versiona el playbook en `defense/incident_response/playbooks/`; documenta cada paso y su propósito.
- **Cuándo usarlo:** Para estandarizar la respuesta y reducir errores humanos en fases repetitivas.
- **Cuándo no:** Sin revisar que el script es correcto para el entorno específico del incidente.

## 2. Flujos y documentación
- Abre el caso en The Hive antes de ejecutar cualquier acción; adjunta observables desde el inicio.
- Guarda evidencias en `defense/incident_response/artifacts/<case-id>/` con hash de verificación.
- Documenta la cadena de custodia: quién recopiló, cuándo, desde qué sistema y qué herramienta usó.
