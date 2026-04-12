# Toolkit - Threat Hunting 🕵️‍♂️

Registro de hunts que he ejecutado, con las herramientas, fuentes y conclusiones.

## Plantilla base
- **Enlace:** referencia oficial de la herramienta.
- **Caso de uso:** qué tipo de hunt o análisis realiza.
- **Comando de ejemplo:** query o comando utilizado en el hunt.
- **Notas útiles:** hallazgos concretos y rutas de evidencia guardada.
- **Recomendaciones:** cómo documentar y reproducir el hunt.
- **Cuándo usar / cuándo no:** en entornos autorizados; documenta cada hunt con hipótesis y conclusión.

## 1. Herramientas de threat hunting

### Velociraptor
- **Enlace:** https://github.com/Velocidex/velociraptor
- **Caso de uso:** Caza en endpoints mediante VQL para detectar procesos, artefactos y comportamientos sospechosos.
- **Comando de ejemplo:** `SELECT * FROM processes WHERE command_line LIKE '%powershell%'`
- **Notas útiles:** Query `SELECT * FROM processes WHERE command_line LIKE '%powershell%'` y guardé los resultados en `defense/threat_hunting/results/hunt-powershell.json`.
- **Recomendaciones:** Anota la hipótesis del hunt antes de ejecutar; guarda los resultados en JSON con nombre descriptivo.
- **Cuándo usarlo:** Para hunts en endpoints cuando tienes el agente desplegado y necesitas visibilidad profunda del host.
- **Cuándo no:** Sin agente instalado o en hosts donde el despliegue no está autorizado.

### Sigma rules
- **Enlace:** https://github.com/SigmaHQ/sigma
- **Caso de uso:** Análisis de logs mediante reglas agnósticas a la plataforma, convertibles a Elastic, Splunk, etc.
- **Comando de ejemplo:** `sigma convert -t elasticsearch -p ecs-windows windows/sysmon/process_creation.yml`
- **Notas útiles:** Convertí la regla `windows.sysmon.process_creation` a Elastic y anoté 3 alertas válidas en `defense/threat_hunting/alerts/`.
- **Recomendaciones:** Mantén las reglas versionadas en `defense/threat_hunting/sigma/`; anota falsos positivos y ajustes.
- **Cuándo usarlo:** Para estandarizar detecciones y reutilizarlas en diferentes plataformas de SIEM.
- **Cuándo no:** Sin validar que la conversión es correcta para tu versión del SIEM específico.

### GRR Rapid Response
- **Enlace:** https://github.com/google/grr
- **Caso de uso:** Recolección de telemetría remota y análisis forense en endpoints a escala.
- **Comando de ejemplo:** `grr_api_client --api-endpoint http://grr:8000 flows list --client <id>`
- **Notas útiles:** Ejecuté artifact `autoruns` y adjunté los XML al caso `CASE-2026-03-27`.
- **Recomendaciones:** Documenta qué artifacts ejecutaste y adjunta los resultados XML al caso correspondiente.
- **Cuándo usarlo:** Para recolección forense remota en múltiples endpoints durante un incidente activo.
- **Cuándo no:** Sin autorización del propietario del endpoint o en hosts fuera del alcance del incidente.

### Elastic alerting
- **Enlace:** https://www.elastic.co/guide/en/elasticsearch/reference/current/xpack-alerting.html
- **Caso de uso:** Watcher que monitorea eventos de Zeek u otras fuentes y dispara playbooks automáticos.
- **Comando de ejemplo:** `PUT _watcher/watch/zeek-anomaly { "trigger": {...}, "actions": {...} }`
- **Notas útiles:** Un watcher monitorea `Zeek` y enciende un playbook en The Hive; guardo el JSON en `defense/incident_response/playbooks/zk-watch.json`.
- **Recomendaciones:** Versiona el JSON del watcher en `defense/incident_response/playbooks/`; documenta el umbral y la lógica de disparo.
- **Cuándo usarlo:** Para detección continua y respuesta automática en entornos con Elastic Stack desplegado.
- **Cuándo no:** Sin ajustar los umbrales; las alertas genéricas generan demasiado ruido.

### RITA
- **Enlace:** https://github.com/activecm/rita
- **Caso de uso:** Análisis de DNS y Netflow para detectar beacons, DGA y conexiones C2.
- **Comando de ejemplo:** `rita -i netflow.pcap -o reports/beacons.csv`
- **Notas útiles:** Usé `rita -i netflow.pcap -o reports/beacons.csv` para detectar beacons. Documenté la IP sospechosa y el dominio asociado.
- **Recomendaciones:** Ejecuta sobre capturas de al menos 24h para que los patrones de beacon sean estadísticamente significativos.
- **Cuándo usarlo:** Para identificar comunicaciones periódicas C2 en capturas de tráfico de red.
- **Cuándo no:** Con capturas de menos de unas pocas horas; los beacons de baja frecuencia no serán detectados.

### Wazuh
- **Enlace:** https://github.com/wazuh/wazuh
- **Caso de uso:** Correlación de eventos y detección mediante reglas personalizadas sobre logs de Sysmon y otros agentes.
- **Comando de ejemplo:** `<rule id="100001" level="12"><description>Encoded PowerShell detected</description></rule>`
- **Notas útiles:** Regla `sysmon-injected` generó un hunt con `eid=4688`; guardé la cadena en `defense/wazuh/rules/`.
- **Recomendaciones:** Guarda las reglas personalizadas en `defense/wazuh/rules/` con comentario de la hipótesis que cubren.
- **Cuándo usarlo:** Para correlación centralizada de eventos cuando Wazuh está desplegado como SIEM/XDR.
- **Cuándo no:** Sin afinar las reglas base; generarán demasiado ruido antes de llegar a alertas útiles.

## 2. Flujos y documentación
- Define la hipótesis del hunt antes de ejecutar cualquier query o rule.
- Guarda resultados en `defense/threat_hunting/results/hunt-<hipotesis>-<fecha>.json`.
- Anota si el hunt fue positivo, negativo o inconcluso, y qué ajustes harías en la próxima iteración.
