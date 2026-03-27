# Auditorías WiFi

Este espacio describe flujos de auditoría estructurados: escanea redes, captura handshakes o PMKID, y luego realiza análisis offline. Añade bitácoras de cada paso y limita la duración de los ataques automáticos para no saturar el entorno.

Puedes incluir subnotas para WPA2, WPA3, RADIUS, e identificar qué controladores y antenas soportan cada técnica.

## Comandos utilizados
- `aireplay-ng --deauth 10 -a <BSSID> wlan0mon`.
- `reaver -i wlan0mon -b <BSSID> -vv --no-nacks` para pruebas controladas.

## Técnicas aplicadas
- Recolección de PMKID con `hcxdumptool` y posterior análisis con `hcxpcaptool`.
- Bruteforce WPS con `reaver` y `bully` en entornos aislados.

## Recomendaciones personales
- Documenta qué adaptador se usó y qué versión de firmware.
- Siempre avisa a quien supervisa el laboratorio antes de lanzar ataques de larga duración.
