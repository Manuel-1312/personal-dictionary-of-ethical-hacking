# Toolkit - Monitoring 📡

Lista sensores, plataformas y herramientas de observabilidad defensiva. La idea es poder montar una vista razonable del entorno, cazar actividad sospechosa y documentar cómo llegaste a cada hallazgo.

| Recurso | Enlace | Tipo | Comando / uso típico | Notas del día |
| --- | --- | --- | --- | --- |
| Zeek | https://github.com/zeek/zeek | Sensor IDS / NSM | `zeekctl deploy` | Muy bueno para telemetría de red rica; `notice.log`, `conn.log` y `dns.log` dan muchísimo contexto. |
| Suricata | https://github.com/OISF/suricata | IDS/IPS | `suricata-update` + `suricata -c /etc/suricata/suricata.yaml` | Ideal para firmas y detección más inmediata; conviene revisar reglas conflictivas. |
| Security Onion | https://github.com/Security-Onion-Solutions/security-onion | Stack SOC | `so-status` / dashboards de SOC | Muy útil para laboratorio si quieres juntar Zeek, Suricata, Elastic y dashboards en un solo stack. |
| Wazuh | https://github.com/wazuh/wazuh | HIDS / SIEM | `agent-control -lc` / panel Wazuh | Bueno para visibilidad de host y correlación básica si quieres algo más orientado a endpoints. |
| Elastic Stack | https://www.elastic.co/elastic-stack | Analítica / búsqueda | consultas en Kibana / export de dashboards | La base para dashboards, hunting y correlación si ya tienes logs centralizados. |
| Sigma | https://github.com/SigmaHQ/sigma | Reglas de detección | `sigma convert -t es-qs rule.yml` | Muy útil para pensar detecciones de forma portable antes de casarlas con tu SIEM concreto. |
| Arkime | https://arkime.com/ | Full packet / session search | panel web / búsqueda de sesiones | Muy potente cuando quieres volver sobre tráfico histórico con bastante detalle. |
| Sysmon | https://learn.microsoft.com/sysinternals/downloads/sysmon | Telemetría de Windows | `sysmon64 -accepteula -i sysmon.xml` | Excelente para enriquecer endpoint logging en laboratorios Windows. |
| osquery | https://github.com/osquery/osquery | Inventario / telemetry | `osqueryi` o paquetes programados | Ideal para consultas tipo inventario, procesos, users, autoruns y estado del host. |
| Velociraptor | https://github.com/Velocidex/velociraptor | DFIR / visibility | artefactos y colección desde consola | Muy bueno para ir más allá del SIEM y entrar en respuesta e investigación. |
| Grafana | https://grafana.com/ | Dashboards | paneles sobre Prometheus / Loki / Elastic | Útil para visualización limpia cuando quieres separar métricas de logs. |
| Loki | https://grafana.com/oss/loki/ | Agregación de logs | consultas LogQL | Ligero para labs cuando no quieres desplegar un Elastic completo. |

## Comandos utilizados recientemente
- `zeekctl deploy` y revisión de `notice.log` / `conn.log`.
- `suricata-update` seguido de reinicio del servicio para aplicar reglas nuevas.
- `sigma convert -t es-qs rules/web_suspicious.yml` para llevar reglas a Elastic.
- `osqueryi --json "select name, path from services;"` para una comprobación rápida de host.

## Técnicas aplicadas
- Combino telemetría de red (Zeek/Suricata) con telemetría de host (Wazuh, Sysmon, osquery) para no quedarme ciego por un solo lado.
- Si una alerta salta, intento enlazarla con logs de contexto, artefactos y cronología antes de concluir nada.
- Mantengo dashboards y queries guardadas; repetir una búsqueda útil debería costar segundos, no media hora.

## Recomendaciones personales
- Guarda las queries y dashboards que realmente sirven; la memoria de “cómo lo encontré” se pierde rápido si no la escribes.
- Diferencia siempre entre señal de laboratorio y señal de producción simulada: si no, las detecciones se vuelven poco creíbles.
- Si introduces una nueva fuente de logs, anota volumen, formato y utilidad real; no todo lo que genera datos genera valor.
