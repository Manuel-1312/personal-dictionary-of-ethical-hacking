# Toolkit - Defensa 🛡️

Este es mi inventario de sensores, dashboards y playbooks defensivos. Cada herramienta tiene una nota sobre cómo la configuré en mi laboratorio de Security Onion + Wazuh.

| Herramienta | Enlace | Rol en el stack | Notas personales |
| --- | --- | --- | --- |
| Zeek | https://github.com/zeek/zeek | Sensor de red | Guarda scripts personalizados en `~/zeek/scripts/`; uso `notice.log` para alertas de HTTP y lo correlaciono con Elastic.
| Suricata | https://github.com/OISF/suricata | IDS/IPS | Cargando reglas `emerging-threats` y ajusto `max-pending-packets`. Anoto los falsos positivos de `HTTP_ATTACK` en `reports/alertas.log`.
| Security Onion | https://github.com/Security-Onion-Solutions/security-onion | Stack completo SOC | Stack completo (Zeek+Suricata+Elastic); exporto consultas de Kibana y guardo screenshots del dashboard `sockeye/logs`.
| Wazuh | https://github.com/wazuh/wazuh | Detección de endpoints | Configuré reglas HIDS para monitorear cambios en `C:	mp	est`. Documenté los `ossec.conf` que uso y los alertas que se dispararon.
| OSSEC | https://github.com/ossec/ossec-hids | HIDS | Lo uso en máquinas Windows con `agent.conf` personalizados y listo los logs en `defense/ossec/alerts.json`.
| The Hive + Cortex | https://github.com/TheHive-Project/TheHive | IR & automatización | Cada caso se guarda en `Hive/cases`. Apunto qué workflows de Cortex usé (hashlookup, dynamic analysis) y los tiempos de respuesta.
| Elastic Stack | https://www.elastic.co/elastic-stack | Analítica | Genero dashboards para `Zeek`, `Suricata` y `Wazuh`; guardo los JSON y las queries que uso para hunting.
| Velociraptor | https://github.com/Velocidex/velociraptor | Hunting en endpoints | Guardo VQLs en `defense/hunting/vql/` y los resultados en `defense/hunting/results/`. Anoto qué detalles del endpoint examiné.
| GRR Rapid Response | https://github.com/google/grr | Telemetría remota | Uso GRR para recolectar archivos y memorias; documento los clientes activos y las queries que ejecuté.
| RITA | https://github.com/activecm/rita | Análisis de DNS/Netflow | Lo lanzo sobre los logs de Security Onion para detectar beacons y guardo `rita/reports/beacons.csv`.
