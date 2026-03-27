# Toolkit - Defensa 🛡️

Inventario de sensores, dashboards, agentes y playbooks defensivos para Security Onion + Wazuh + Elastic. Cada herramienta describe cómo la configuré, qué comando lanzo para validar detecciones y qué recomendaciones siguen de las pruebas de hunting.

## 1. Sensorización y recolección

### Zeek
- **Enlace:** https://github.com/zeek/zeek
- **Caso de uso:** monitoreo pasivo del tráfico en Security Onion con alertas HTTP/DNS/SMTP.
- **Comando de ejemplo:** `zeekctl deploy` (luego `zeekctl status` y `zeekctl log` para revisar `notice.log`).
- **Notas útiles:** mantengo scripts personalizados en `~/zeek/custom/scripts/` y versiono las `notice.policy` en `defense/zeek/policies/`.
- **Recomendaciones:** exporta los logs rotados a `elastic/zeek/` para hunting en Kibana y cabecera.
- **Cuándo usarlo:** siempre que tengas visibilidad packet-level y quieras detectar beacons.
- **Cuándo no:** cuando trabajas con pocos hosts e infra sin tap (usa Velociraptor en endpoints en su lugar).

### Suricata
- **Enlace:** https://github.com/OISF/suricata
- **Caso de uso:** IDS/IPS para alertar sobre firmas y tráfico sospechoso.
- **Comando de ejemplo:** `suricata -c /etc/suricata/suricata.yaml -i eth0` + `suricata-update` para reglas `emerging-threats`.
- **Notas útiles:** ajusto `max-pending-packets` y `app-layer` en `suricata.yaml`, y los falsos positivos los documenté en `reports/alertas/falsos-positivos.log`.
- **Recomendaciones:** combina con Zeek (alerta + metadata) y con Grafana para gráficos de alertas/sesiones.
- **Cuándo usarlo:** en redes monitoreadas continuamente.
- **Cuándo no:** si estás haciendo un pentest externo sin permiso para activar un IDS.

### Security Onion
- **Enlace:** https://github.com/Security-Onion-Solutions/security-onion
- **Caso de uso:** stack completo SOC que combina Zeek, Suricata, Elastic, Arkime y Wazuh.
- **Comando de ejemplo:** `so-status` para ver sensors y luego `so-logstash-sniff` para revisar pipelines.
- **Notas útiles:** exporto dashboards preconfigurados y guardo capturas de Kibana/Arkime en `defense/screenshots/`.
- **Recomendaciones:** documenta cada sensor en `defense/onion/sensors.md` para mantener cobertura y evitar duplicados.
- **Cuándo usarlo:** en entornos centralizados que toleran múltiples herramientas.
- **Cuándo no:** si necesitas una solución liviana (usa Wazuh o Velociraptor self-hosted).

### Wazuh (HIDS)
- **Enlace:** https://github.com/wazuh/wazuh
- **Caso de uso:** detección en endpoints, monitorización de integridad y reglas personalizadas.
- **Comando de ejemplo:** `agent_control -l` y `manage_agents` para ver agentes activos; las reglas personalizadas se edita en `wazuh/rules/local_rules.xml`.
- **Notas útiles:** documenté `ossec.conf` en `defense/wazuh/ossec.conf` y guardo alertas en `defense/wazuh/alerts.json`.
- **Recomendaciones:** usa `wazuh-logtest` para validar reglas antes de desplegarlas.
- **Cuándo usarlo:** en endpoints con agentes (Windows/Linux/Mac).
- **Cuándo no:** si solo buscas visibilidad de red sin acceso a agentes.

### Elastic Stack (Elasticsearch + Kibana + Logstash)
- **Enlace:** https://www.elastic.co/elastic-stack
- **Caso de uso:** analítica y dashboards de Zeek, Suricata y Wazuh.
- **Comando de ejemplo:** `curl -XPUT http://elastic.local:9200/_template/security_template -H 'Content-Type: application/json' -d @defense/elastic/template.json`
- **Notas útiles:** guardo las queries favoritas en `defense/dashboards/queries.json` y exporto dashboards a `defense/dashboards/json/` para versionado.
- **Recomendaciones:** integra Grafana/Loki para métricas y alertas personalizadas.
- **Cuándo usarlo:** siempre que quieras correlacionar logs con visualizaciones ricas.
- **Cuándo no:** si el stack se vuelve demasiado pesado; en ese caso, usa Loki/Grafana o Splunk ligero.

## 2. Hunting y respuesta remota

### Velociraptor
- **Enlace:** https://github.com/Velocidex/velociraptor
- **Caso de uso:** hunting en endpoints, recolección de artefactos y consultas VQL.
- **Comando de ejemplo:** `velociraptor config generate -o defense/velociraptor/server.config` y luego `velociraptor --config defense/velociraptor/server.config client --collect artifacts/windows/Process`.
- **Notas útiles:** guardo VQLs custom en `defense/hunting/vql/` y los resultados en `defense/hunting/results/`.
- **Recomendaciones:** usa `artifacts/windows/Sysmon` para detectar técnicas de MITRE.
- **Cuándo usarlo:** en respuesta a incidentes que requieren evidencia del endpoint.
- **Cuándo no:** cuando solo tienes captura pasiva de red.

### Grafana + Loki
- **Enlaces:** https://grafana.com / https://grafana.com/oss/loki
- **Caso de uso:** dashboards de alertas y logs estructurados. Loki recolecta logs de Suricata/Zeek y Grafana los visualiza.
- **Comando de ejemplo:** `grafana-cli plugins install grafana-piechart-panel` + `loki-canary -config defense/loki/loki-config.yaml`
- **Notas útiles:** guardo paneles en `defense/dashboard/grafana.json` y los conecto con fuentes `Loki`.
- **Recomendaciones:** usa alertas de Grafana (evalúa `thresholds.md`) para notificar incidentes.
- **Cuándo usarlo:** cuando querés métricas en tiempo real.
- **Cuándo no:** si solo trabajas con logs históricos y no necesitas visualizaciones en vivo.

### Arkime
- **Enlace:** https://arkime.com
- **Caso de uso:** captura y búsqueda de paquetes, especialmente para reconstrucción de sesiones.
- **Comando de ejemplo:** `arkime-capture --config /etc/arkime/capture.ini` y luego `arkime-viewer`.
- **Notas útiles:** guardo las consultas en `defense/arkime/queries.txt` y exporto PCAPs para análisis forense.
- **Recomendaciones:** combina con Zeek (usa `zeek_conn.log` para ubicar la sesión en Arkime).
- **Cuándo usarlo:** cuando necesitas reconstruir una sesión completa.
- **Cuándo no:** si solo te interesa análisis de alertas (usa Kibana).

### GRR Rapid Response
- **Enlace:** https://github.com/google/grr
- **Caso de uso:** telemetría remota y respuestas en caliente en endpoints.
- **Comando de ejemplo:** `grr_api_shell --username=admin --password=xxx client 00000 expand --path /tmp --output=defense/grr/`.
- **Notas útiles:** documenté los hunts en `defense/grr/hunts/{hunt_id}/report.md` y guardé las queries en `defense/grr/queries/`.
- **Recomendaciones:** usa packs previamente revisados para evitar artefactos ruidosos.
- **Cuándo usarlo:** en respuesta a incidentes cuando Velociraptor no alcanza.
- **Cuándo no:** si necesitas solo monitoreo cotidiano.

## 3. Procedimientos y documentación
- Todos los dashboards se versionan en `defense/dashboards/` (Grafana, Kibana, Arkime).
- Las detecciones y falsos positivos van a `reports/defense/alerts/` con contexto: `fecha, sensor, regla, evidencia`.
- Para cada activación de alerta, documenta la acción tomada en `defense/playbooks/` y enlaza con el caso de The Hive (`defense/thehive/cases/`).
- Uso `velocity` (Velociraptor) y `wazuh-logtest` antes de subir nuevas reglas para asegurar que no se disparan falsos positivos.
