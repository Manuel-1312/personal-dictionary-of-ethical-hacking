# Toolkit - Auditorías WiFi 🔍

Documenta el flujo completo: escaneo, captura, análisis y mitigación durante una auditoría inalámbrica.

| Herramienta | Enlace | Etapa | Detalle de laboratorio |
| --- | --- | --- | --- |
| airmon-ng | https://www.aircrack-ng.org/ | Preparación | Activa monitor mode, documenta interfaces usadas y drivers.
| aireplay-ng | https://www.aircrack-ng.org/ | Inyección | Prueba desautenticaciones controladas y documenta la respuesta.
| reaver | https://github.com/t6x/reaver | WPS bruteforce | Solo en laboratorios con WPS habilitado; guarda tiempos y tasa de intentos.
| bully | https://github.com/wiire-a/bully | WPS | Alternativa a reaver; registras handshake y comparas detecciones.
| wifite2 | https://github.com/derv82/wifite2 | Auditoría automatizada | Usa secuencias de retries con logs, ideal para QA.
| hostapd | https://w1.fi/hostapd/ | Emulación | Lanza redes falsas o simuladas para pruebas de detección.

## Comandos utilizados
- `aireplay-ng --deauth 10 -a <BSSID> wlan0mon`.
- `reaver -i wlan0mon -b <BSSID> -vv --no-nacks`.
- `bully -b <BSSID> -c 6 --timeout 10`.

## Técnicas aplicadas
- Automatización de bruteforce con wifite2 y logging de resultados.
- Comparativa de detecciones entre reaver y bully.

## Recomendaciones personales
- Documenta cómo revertir los cambios en la red y cuándo detener los ataques.
- Guarda logs en `wifi/auditorias/logs/` y resúmelos en `wifi/auditorias/reportes.md`.