# Toolkit - Monitoring 📡

Lista sensores, plataformas y herramientas de observabilidad defensiva. La idea es poder montar una vista razonable del entorno, cazar actividad sospechosa y documentar cómo llegaste a cada hallazgo.

## Plantilla base
- **Enlace:** referencia oficial.
- **Caso de uso:** propósito de la herramienta.
- **Comando de ejemplo:** comando representativo.
- **Notas útiles:** observaciones clave.
- **Recomendaciones:** consejos de uso.
- **Cuándo usar / cuándo no:** límites y contexto.

## 1. Sensores y plataformas de monitorización

### Zeek
- **Enlace:** https://github.com/zeek/zeek
- **Caso de uso:** Sensor IDS / NSM para telemetría de red rica.
- **Comando de ejemplo:** `zeekctl deploy`
- **Notas útiles:** `notice.log`, `conn.log` y `dns.log` dan muchísimo contexto; imprescindible para hunting.
- **Recomendaciones:** Configura `local.zeek` para ajustar scripts activos; exporta logs a Elastic o Loki.
- **Cuándo usarlo:** Cuando necesitas telemetría de red profunda y reproducible para hunting o análisis.
- **Cuándo no:** Entornos con recursos muy limitados; Zeek consume bastante CPU/IO en tráfico alto.

### Suricata
- **Enlace:** https://github.com/OISF/suricata
- **Caso de uso:** IDS/IPS con detección basada en firmas y análisis de protocolos.
- **Comando de ejemplo:** `suricata-update && suricata -c /etc/suricata/suricata.yaml`
- **Notas útiles:** Ideal para firmas y detección más inmediata; conviene revisar reglas conflictivas.
- **Recomendaciones:** Actualiza reglas con `suricata-update`; revisa `fast.log` y `eve.json` tras cada sesión.
- **Cuándo usarlo:** Detección en tiempo real de tráfico sospechoso con alertas inmediatas.
- **Cuándo no:** Sin ajuste previo de reglas; el ruido inicial puede ser abrumador.

### Security Onion
- **Enlace:** https://github.com/Security-Onion-Solutions/security-onion
- **Caso de uso:** Stack SOC completo con Zeek, Suricata, Elastic y dashboards integrados.
- **Comando de ejemplo:** `so-status`
- **Notas útiles:** Muy útil para laboratorio si quieres juntar Zeek, Suricata, Elastic y dashboards en un solo stack.
- **Recomendaciones:** Despliega en VM dedicada con al menos 8 GB RAM; revisa la guía de tuning post-instalación.
- **Cuándo usarlo:** Labs donde quieres un SOC completo sin ensamblar componentes manualmente.
- **Cuándo no:** Equipos con recursos limitados o cuando solo necesitas un sensor concreto.

### Wazuh
- **Enlace:** https://github.com/wazuh/wazuh
- **Caso de uso:** HIDS y SIEM orientado a endpoints con correlación básica.
- **Comando de ejemplo:** `agent-control -lc`
- **Notas útiles:** Bueno para visibilidad de host y correlación básica si quieres algo orientado a endpoints.
- **Recomendaciones:** Despliega agentes en todos los hosts del lab; configura reglas personalizadas para reducir ruido.
- **Cuándo usarlo:** Monitorización de endpoints y correlación de eventos de host en laboratorio.
- **Cuándo no:** Como reemplazo de telemetría de red; complementa con Zeek/Suricata para cobertura completa.

### Elastic Stack
- **Enlace:** https://www.elastic.co/elastic-stack
- **Caso de uso:** Plataforma de analítica, búsqueda y dashboards sobre logs centralizados.
- **Comando de ejemplo:** consultas en Kibana / exportación de dashboards
- **Notas útiles:** La base para dashboards, hunting y correlación si ya tienes logs centralizados.
- **Recomendaciones:** Guarda las queries y dashboards que realmente sirven; usa ILM para gestionar retención.
- **Cuándo usarlo:** Cuando tienes múltiples fuentes de logs y necesitas correlación y búsqueda eficiente.
- **Cuándo no:** Labs muy pequeños donde Loki o simplemente grep sobre ficheros es suficiente.

### Sigma
- **Enlace:** https://github.com/SigmaHQ/sigma
- **Caso de uso:** Reglas de detección portables independientes del SIEM.
- **Comando de ejemplo:** `sigma convert -t es-qs rule.yml`
- **Notas útiles:** Muy útil para pensar detecciones de forma portable antes de casarlas con tu SIEM concreto.
- **Recomendaciones:** Mantén un repositorio local de reglas Sigma útiles; convierte solo las relevantes para tu stack.
- **Cuándo usarlo:** Diseño y documentación de detecciones reutilizables entre diferentes plataformas.
- **Cuándo no:** Detección en tiempo real directa; Sigma es definición, no ejecución.

### Arkime
- **Enlace:** https://arkime.com/
- **Caso de uso:** Full packet capture y búsqueda de sesiones históricas.
- **Comando de ejemplo:** panel web / búsqueda de sesiones
- **Notas útiles:** Muy potente cuando quieres volver sobre tráfico histórico con bastante detalle.
- **Recomendaciones:** Dimensiona el almacenamiento correctamente; indexa solo el tráfico relevante para no saturar.
- **Cuándo usarlo:** Investigación post-incidente donde necesitas reconstruir sesiones de red completas.
- **Cuándo no:** Labs con poco almacenamiento; el full packet capture crece rápidamente.

### Sysmon
- **Enlace:** https://learn.microsoft.com/sysinternals/downloads/sysmon
- **Caso de uso:** Telemetría enriquecida de procesos, red y ficheros en Windows.
- **Comando de ejemplo:** `sysmon64 -accepteula -i sysmon.xml`
- **Notas útiles:** Excelente para enriquecer endpoint logging en laboratorios Windows.
- **Recomendaciones:** Usa una configuración base como SwiftOnSecurity o Olaf Hartong para evitar ruido excesivo.
- **Cuándo usarlo:** Laboratorios Windows donde el Event Log estándar no da suficiente visibilidad de procesos.
- **Cuándo no:** Sistemas de producción sin evaluación previa del impacto en rendimiento.

### osquery
- **Enlace:** https://github.com/osquery/osquery
- **Caso de uso:** Inventario y telemetría de host mediante consultas SQL.
- **Comando de ejemplo:** `osqueryi` o paquetes programados
- **Notas útiles:** Ideal para consultas tipo inventario, procesos, users, autoruns y estado del host.
- **Recomendaciones:** Crea un schedule de queries útiles en `osquery.conf`; integra con Elastic o Wazuh.
- **Cuándo usarlo:** Inventario continuo y auditoría de estado de host de forma estandarizada.
- **Cuándo no:** Detección en tiempo real de tráfico de red; osquery es orientado a host, no a red.

### Velociraptor
- **Enlace:** https://github.com/Velocidex/velociraptor
- **Caso de uso:** DFIR y visibilidad avanzada con artefactos y colección desde consola.
- **Comando de ejemplo:** artefactos y colección desde consola
- **Notas útiles:** Muy bueno para ir más allá del SIEM y entrar en respuesta e investigación.
- **Recomendaciones:** Aprende VQL (Velociraptor Query Language); crea artefactos personalizados para tu lab.
- **Cuándo usarlo:** Respuesta a incidentes y hunting profundo cuando el SIEM no da suficiente detalle.
- **Cuándo no:** Monitorización continua ligera; es más una herramienta de investigación que de vigilancia pasiva.

### Grafana
- **Enlace:** https://grafana.com/
- **Caso de uso:** Dashboards de métricas y visualización sobre múltiples fuentes de datos.
- **Comando de ejemplo:** paneles sobre Prometheus / Loki / Elastic
- **Notas útiles:** Útil para visualización limpia cuando quieres separar métricas de logs.
- **Recomendaciones:** Guarda los dashboards como JSON en el repositorio para reproducirlos fácilmente.
- **Cuándo usarlo:** Visualización de métricas de infraestructura y tendencias junto a logs de seguridad.
- **Cuándo no:** Búsqueda y correlación de logs; para eso Kibana o la UI de Loki son más adecuadas.

### Loki
- **Enlace:** https://grafana.com/oss/loki/
- **Caso de uso:** Agregación de logs ligera con consultas LogQL.
- **Comando de ejemplo:** consultas LogQL
- **Notas útiles:** Ligero para labs cuando no quieres desplegar un Elastic completo.
- **Recomendaciones:** Úsalo con Promtail para ingesta; integra con Grafana para dashboards combinados.
- **Cuándo usarlo:** Labs donde Elastic es demasiado pesado pero necesitas centralizar y buscar logs.
- **Cuándo no:** Analítica avanzada o búsqueda de texto completo a gran escala; Elastic escala mejor.

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
- Guarda las queries y dashboards que realmente sirven; la memoria de "cómo lo encontré" se pierde rápido si no la escribes.
- Diferencia siempre entre señal de laboratorio y señal de producción simulada: si no, las detecciones se vuelven poco creíbles.
- Si introduces una nueva fuente de logs, anota volumen, formato y utilidad real; no todo lo que genera datos genera valor.
