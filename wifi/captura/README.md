# Captura WiFi

Documenta cada sesión de captura: qué canal monitorizas, qué adaptador usas y qué archivos `.cap` o `.pcap` generas. Mantén control de las antenas y el alcance, y siempre borra capturas sensibles cuando terminas.

Usa `toolkit.md` para listar herramientas y filtros, y guarda ejemplos de comandos (`airodump-ng --write`, `tcpdump -i wlan0`) con notas de hardware y condiciones ambientales.

## Comandos utilizados
- `airodump-ng --write captures/session-20260327 --output-format csv,pcap wlan0mon`.
- `tcpdump -i wlan0 -w captures/raw-20260327.pcap`.

## Técnicas aplicadas
- Captura segmentada por canal y verificación con Wireshark.
- Registro de señal y ruido para ajustar `channel`.

## Recomendaciones personales
- Guarda las capturas en carpetas fechadas y documenta la antena usada.
- Limpia los archivos temporales (`rm captures/tmp-*`) antes de cerrar la sesión.
