# Toolkit - Captura WiFi 📥

Catálogo corto para cada técnica de captura en laboratorio. Incluye filtros, interfaces usadas y cómo proteges los datos.

| Herramienta | Enlace | Uso concreto | Notas |
| --- | --- | --- | --- |
| airodump-ng | https://www.aircrack-ng.org/ | Captura de tramas | Guarda canal/ESSID y usa `--write-interval` para segmentar.
| tcpdump | https://www.tcpdump.org/ | Captura general en modo monitor | Aplica filtros `port 80` o `wlan host` para reducir volumen.
| hcxdumptool | https://github.com/ZerBea/hcxdumptool | Captura PMKID/handshake | Usa `--enable_status=1` y comprueba handshake con `hcxpcaptool`.
| Wireshark | https://www.wireshark.org/ | Visualización de capturas | Marca anomalías y exporta a JSON para reportes.
| Dumpcap | https://www.wireshark.org/docs/man-pages/dumpcap.html | Capturas headless | Usa `-P -w` y rota archivos por tamaño.
| Airgraph-ng | https://github.com/aircrack-ng/airgraph-ng | Topografía | Genera diagramas SSID↔MAC a partir de CSV.

## Comandos utilizados
- `airodump-ng --write captures/session-20260327 --output-format csv,pcap wlan0mon`.
- `tcpdump -i wlan0 -w captures/raw-20260327.pcap`.

## Técnicas aplicadas
- Filtro por canal y export de CSV para Airgraph.
- Análisis de ruido y beacon para calibrar la antena.

## Recomendaciones personales
- Mantén un inventario de `captures/` por fecha.
- Limpia capturas sensibles al terminar: `rm captures/tmp-*`.