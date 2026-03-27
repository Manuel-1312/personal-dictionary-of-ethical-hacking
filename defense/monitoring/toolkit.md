# Toolkit - Monitoring 📡

Lista los sensores y dashboards activos. Cada registro incluye qué queries ejecuté y dónde guardé la evidencia.

| Recurso | Enlace | Tipo | Notas del día |
| --- | --- | --- | --- |
| Zeek | https://github.com/zeek/zeek | Sensor IDS | `zeekctl deploy` sobre `security-onion`. Guardo `notice.log` en `defense/monitoring/logs/zeek`.
| Suricata | https://github.com/OISF/suricata | IDS/IPS | `suricata-update` para normas, luego `suricata -c /etc/suricata/suricata.yaml` y anoto reglas conflictivas.
| Security Onion | https://github.com/Security-Onion-Solutions/security-onion | Stack SOC | Dashboard `SoC-Overview`; exporto alertas que hagan match con `alert.alert.source`.
| Wazuh | https://github.com/wazuh/wazuh | HIDS | Monitorizo con `agent-control -lc` y correlaciono con Kibana; los scripts que escribí están en `defense/wazuh/`.
| Elastic Stack | https://www.elastic.co/elastic-stack | Analítica | Guardo queries en `defense/monitoring/dashboards/elk` y exporto JSON de cada panel.
| Sigma rules | https://github.com/SigmaHQ/sigma | Correlación | Las convierto a `rule.yml` y las pruebo en Elastic. Documenta qué alertas generaron y cuántas coincidencias hubo.
