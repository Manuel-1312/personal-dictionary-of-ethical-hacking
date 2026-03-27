# Toolkit - Defensa 🛡️

Inventario de sensores, dashboards, agentes y playbooks para entornos defensivos basados en Security Onion + Wazuh + Elastic. Cada herramienta sigue la plantilla estándar (enlace, caso de uso, comando, notas, recomendaciones, cuándo usar/no usar) y se enlaza con flujos de hunting y documentación relacionada.

## Plantilla rápida
- **Enlace:** referencia oficial.
- **Caso de uso:** qué cubre del stack defensivo.
- **Comando de ejemplo:** ejecución habitual.
- **Notas útiles:** paths, logs y ajustes.
- **Recomendaciones:** buenas prácticas.
- **Cuándo usar / cuándo no:** límites de cada sensor.

## 1. Sensorización y recolección

### Zeek
- **Enlace:** https://github.com/zeek/zeek
- **Caso de uso:** monitoreo pasivo del tráfico con alertas HTTP/DNS/SMTP.
- **Comando de ejemplo:** `zeekctl deploy` + `zeekctl status` y `zeekctl log` para revisar `notice.log`.
- **Notas útiles:** mantengo scripts personalizados en `~/zeek/custom/scripts/` y versiono `notice.policy` en `defense/zeek/policies/`.
- **Recomendaciones:** exporta logs rotados a `elastic/zeek/` y enlaza con dashboards Kibana.
- **Cuándo usarlo:** siempre que tengas visibilidad packet-level y necesites detectar beacons.
- **Cuándo no:** cuando sólo hay pocos hosts y no hay tap (usa Velociraptor en endpoints).

### Suricata
- **Enlace:** https://github.com/OISF/suricata
- **Caso de uso:** IDS/IPS de firmas y tráfico sospechoso.
- **Comando de ejemplo:** `suricata -c /etc/suricata/suricata.yaml -i eth0` + `suricata-update` para reglas `emerging-threats`.
- **Notas útiles:** registro falsos positivos en `reports/alertas/falsos-positivos.log` y ajusto `max-pending-packets`.
- **Recomendaciones:** combínalo con Zeek y Grafana para gráficos de alertas.
- **Cuándo usarlo:** en redes monitoreadas continuamente.
- **Cuándo no:** durante pentests externos sin permiso para activar un IDS.

### Security Onion
- **Enlace:** https://github.com/Security-Onion-Solutions/security-onion
- **Caso de uso:** stack completo que combina Zeek, Suricata, Elastic, Arkime y Wazuh.
- **Comando de ejemplo:** `so-status` y `so-logstash-sniff` para verificar pipelines.
- **Notas útiles:** exporto dashboards y capturas desde `defense/screenshots/`.
- **Recomendaciones:** documenta cada sensor en `defense/onion/sensors.md` para evitar redundancias.
- **Cuándo usarlo:** cuando quieras una plataforma SOC consolidada.
- **Cuándo no:** si necesitas algo liviano (usa Wazuh o Velociraptor standalone).

### Wazuh (HIDS)
- **Enlace:** https://github.com/wazuh/wazuh
- **Caso de uso:** detección en endpoints, monitorización de integridad y reglas personalizadas.
- **Comando de ejemplo:** `agent_control -l` y edición de `wazuh/rules/local_rules.xml`.
- **Notas útiles:** guardo alertas en `defense/wazuh/alerts.json` y documenté `ossec.conf`.
- **Recomendaciones:** usa `wazuh-logtest` antes de deployar reglas.
- **Cuándo usarlo:** endpoints Windows/Linux/Mac.
- **Cuándo no:** si sólo necesitas visibilidad de red sin agentes.

### Elastic Stack
- **Enlace:** https://www.elastic.co/elastic-stack
- **Caso de uso:** analítica y dashboards para Zeek, Suricata y Wazuh.
- **Comando de ejemplo:** `curl -XPUT http://elastic.local:9200/_template/security_template -H 'Content-Type: application/json' -d @defense/elastic/template.json`
- **Notas útiles:** guardo queries en `defense/dashboards/queries.json` y exporto dashboards a `defense/dashboards/json/`.
- **Recomendaciones:** integra Grafana/Loki para métricas/alertas personalizadas.
- **Cuándo usarlo:** siempre que necesites correlacionar logs con visualizaciones.
- **Cuándo no:** si el stack se vuelve demasiado pesado (usa Loki o Splunk ligero).

## 2. Hunting y respuesta remota

### Velociraptor
- **Enlace:** https://github.com/Velocidex/velociraptor
- **Caso de uso:** hunting en endpoints y recolección de artefactos.
- **Comando de ejemplo:** `velociraptor config generate -o defense/velociraptor/server.config` y luego `client --collect artifacts/windows/Process`.
- **Notas útiles:** guardo VQLs en `defense/hunting/vql/` y resultados en `defense/hunting/results/`.
- **Recomendaciones:** usa `artifacts/windows/Sysmon` para detectar técnicas MITRE.
- **Cuándo usarlo:** en respuesta a incidentes con evidencia de endpoint.
- **Cuándo no:** si sólo tienes captura pasiva de red.

### Grafana + Loki
- **Enlaces:** https://grafana.com / https://grafana.com/oss/loki
- **Caso de uso:** dashboards y alertas a partir de logs estructurados.
- **Comando de ejemplo:** `grafana-cli plugins install grafana-piechart-panel` + `loki-canary -config defense/loki/loki-config.yaml`
- **Notas útiles:** paneles en `defense/dashboard/grafana.json` conectados a Loki.
- **Recomendaciones:** activa alertas con umbrales definidos en `thresholds.md`.
- **Cuándo usarlo:** cuando necesitas métricas en tiempo real.
- **Cuándo no:** si solo trabajas con logs históricos.

### Arkime
- **Enlace:** https://arkime.com
- **Caso de uso:** captura y búsqueda de paquetes para reconstrucción.
- **Comando de ejemplo:** `arkime-capture --config /etc/arkime/capture.ini` + `arkime-viewer`.
- **Notas útiles:** guardo consultas en `defense/arkime/queries.txt` y exporto PCAPs.
- **Recomendaciones:** combínalo con Zeek (`zeek_conn.log`) para ubicar sesiones.
- **Cuándo usarlo:** cuando necesitas reconstruir conexiones.
- **Cuándo no:** si sólo necesitas análisis de alertas (usa Kibana).

### GRR Rapid Response
- **Enlace:** https://github.com/google/grr
- **Caso de uso:** telemetría remota y respuestas calientes.
- **Comando de ejemplo:** `grr_api_shell --username=admin --password=xxx client 00000 expand --path /tmp --output=defense/grr/`.
- **Notas útiles:** documenté hunts y queries en `defense/grr/`.
- **Recomendaciones:** usa packs verificados.
- **Cuándo usarlo:** cuando Velociraptor no alcanza.
- **Cuándo no:** si solo necesitas monitoreo cotidiano.

### RITA
- **Enlace:** https://github.com/activecm/rita
- **Caso de uso:** análisis de DNS/Netflow para detectar beacons.
- **Comando de ejemplo:** `rita --input securityonion/netflow.log --output forensics/rita/beacons.csv`
- **Notas útiles:** guardo los CSV en `rita/reports/beacons.csv`.
- **Recomendaciones:** combina con Zeek para entender contexto.
- **Cuándo usarlo:** cuando buscas detección de beacons.
- **Cuándo no:** en redes sin Netflow.

## 3. Flujos y documentación relacionada
- Flujo típico: Zeek y Suricata alimentan Elastic, Grafana y Arkime; Velociraptor complementa con endpoints y GRR/RITA respalda piezas específicas.
- Guarda dashboards versionados en `defense/dashboards/` y alertas/falsos positivos en `reports/defense/alerts/`.
- Documenta cada playbook en `defense/playbooks/` y enlázalo con el caso correspondiente en The Hive (`defense/thehive/cases/`).
- Usa `velocity` y `wazuh-logtest` antes de subir reglas para asegurarte de que no disparan falsos positivos.
