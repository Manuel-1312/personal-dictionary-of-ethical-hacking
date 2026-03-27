# Monitoring

Aquí detallo los sensores y dashboards que reviso cada día. Apunto qué paneles miro en Kibana, qué filtros aplico y qué alertas me tomaron más tiempo en validar. Ejemplo: la semana pasada ajusté la query `event.dataset:zeek.http` para ignorar el tráfico interno y dejó de disparar falsos positivos.

Los pasos son siempre:
1. Arrancar Zeek + Suricata en Security Onion.
2. Reconectar Wazuh/Windshield a los endpoints.
3. Revisar el dashboard `security-onion/default` y exportar `alertas.json` para actualizar `defense/monitoring/alerts/`.

Guarda en esta carpeta pantallazos (PNG) y notas sobre qué reglas (IDS/HIDS) reaccionaron o fallaron, y enlaza los hunts en `threat_hunting/` cuando pases a esa fase.