# Toolkit - Captura WiFi 📥

Catálogo corto para cada técnica de captura en laboratorio. Incluye filtros, interfaces usadas y cómo proteges los datos.

## Plantilla base
- **Enlace:** referencia oficial.
- **Caso de uso:** propósito de la herramienta.
- **Comando de ejemplo:** comando representativo.
- **Notas útiles:** observaciones clave.
- **Recomendaciones:** consejos de uso.
- **Cuándo usar / cuándo no:** límites y contexto.

## 1. Herramientas de captura

### airodump-ng
- **Enlace:** https://www.aircrack-ng.org/
- **Caso de uso:** Captura de tramas 802.11 con filtrado por canal, BSSID y ESSID.
- **Comando de ejemplo:** `airodump-ng --write captures/session-20260327 --output-format csv,pcap wlan0mon`
- **Notas útiles:** Guarda canal/ESSID y usa `--write-interval` para segmentar capturas largas.
- **Recomendaciones:** Fija el canal con `-c` para capturas focalizadas; exporta siempre en CSV y PCAP.
- **Cuándo usarlo:** Captura inicial de beacons, handshakes y tráfico de red inalámbrica en laboratorio.
- **Cuándo no:** En redes ajenas sin autorización explícita; la captura de tráfico inalámbrico tiene implicaciones legales.

### tcpdump
- **Enlace:** https://www.tcpdump.org/
- **Caso de uso:** Captura general de tráfico en modo monitor o interfaz normal.
- **Comando de ejemplo:** `tcpdump -i wlan0 -w captures/raw-20260327.pcap`
- **Notas útiles:** Aplica filtros `port 80` o `wlan host` para reducir volumen de captura.
- **Recomendaciones:** Usa filtros BPF para reducir ruido; rota archivos con `-C` en capturas largas.
- **Cuándo usarlo:** Captura rápida de tráfico con filtros precisos o cuando Wireshark no está disponible.
- **Cuándo no:** Análisis visual interactivo; para eso Wireshark es más eficiente.

### hcxdumptool
- **Enlace:** https://github.com/ZerBea/hcxdumptool
- **Caso de uso:** Captura especializada de PMKID y handshakes WPA para análisis offline.
- **Comando de ejemplo:** `hcxdumptool -i wlan0mon -o captures/pmkid.pcapng --enable_status=1`
- **Notas útiles:** Usa `--enable_status=1` y comprueba handshake con `hcxpcaptool` tras la captura.
- **Recomendaciones:** Verifica siempre la captura con `hcxpcaptool --summary`; documenta la red objetivo.
- **Cuándo usarlo:** Captura de PMKID o handshakes en laboratorio para análisis de contraseñas WPA.
- **Cuándo no:** Captura general de tráfico; airodump-ng o tcpdump son más apropiados para ese caso.

### Wireshark
- **Enlace:** https://www.wireshark.org/
- **Caso de uso:** Visualización y análisis interactivo de capturas de tráfico.
- **Comando de ejemplo:** `wireshark -r captures/session-20260327.pcap`
- **Notas útiles:** Marca anomalías con colores y exporta a JSON para reportes automatizados.
- **Recomendaciones:** Guarda filtros de display útiles como perfiles; usa "Follow Stream" para reconstruir sesiones.
- **Cuándo usarlo:** Análisis detallado de capturas existentes con navegación visual y filtros avanzados.
- **Cuándo no:** Captura en producción con alto volumen; Dumpcap o tcpdump son más eficientes para eso.

### Dumpcap
- **Enlace:** https://www.wireshark.org/docs/man-pages/dumpcap.html
- **Caso de uso:** Captura headless de alto rendimiento sin interfaz gráfica.
- **Comando de ejemplo:** `dumpcap -P -w captures/headless.pcap -b filesize:100000`
- **Notas útiles:** Usa `-P` para formato pcap y rota archivos por tamaño con `-b filesize`.
- **Recomendaciones:** Combina con análisis posterior en Wireshark; ideal para capturas largas automatizadas.
- **Cuándo usarlo:** Capturas largas o automatizadas en sistemas sin entorno gráfico.
- **Cuándo no:** Análisis en tiempo real interactivo; para eso Wireshark directamente es mejor.

### Airgraph-ng
- **Enlace:** https://github.com/aircrack-ng/airgraph-ng
- **Caso de uso:** Generación de diagramas de topología WiFi a partir de CSV de airodump-ng.
- **Comando de ejemplo:** `airgraph-ng -i captures/session-20260327.csv -o graphs/topology.png -g CAPR`
- **Notas útiles:** Genera diagramas SSID↔MAC a partir de CSV de airodump; bueno para documentar topología.
- **Recomendaciones:** Guarda los gráficos por sesión; usa `-g CAPR` para clientes y `-g CPG` para redes.
- **Cuándo usarlo:** Documentación visual de la topología WiFi detectada durante una sesión de captura.
- **Cuándo no:** Análisis de tráfico o contraseñas; es exclusivamente una herramienta de visualización.

## Comandos utilizados
- `airodump-ng --write captures/session-20260327 --output-format csv,pcap wlan0mon`.
- `tcpdump -i wlan0 -w captures/raw-20260327.pcap`.

## Técnicas aplicadas
- Filtro por canal y export de CSV para Airgraph.
- Análisis de ruido y beacon para calibrar la antena.

## Recomendaciones personales
- Mantén un inventario de `captures/` por fecha.
- Limpia capturas sensibles al terminar: `rm captures/tmp-*`.
