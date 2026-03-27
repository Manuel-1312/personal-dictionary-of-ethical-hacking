# Toolkit - WiFi 🛰️

Libro de jugadas para auditorías inalámbricas. Cada herramienta sigue la plantilla (enlace, caso de uso, comando de ejemplo, notas, recomendaciones, cuándo usar/no usar) y documenta adaptador, canal y salidas para mantener reproducibilidad.

## Plantilla inalámbrica
- **Enlace:** referencia oficial.
- **Caso de uso:** qué cubre dentro de la auditoría WiFi.
- **Comando de ejemplo:** flags completos.
- **Notas útiles:** capturas, directorios, drivers.
- **Recomendaciones:** precauciones en entorno real.
- **Cuándo usar / cuándo no:** límites de aplicación.

## 1. Capturas y mapeo pasivo

### Kismet
- **Enlace:** https://www.kismetwireless.net/
- **Caso de uso:** detección pasiva de AP/estaciones y análisis de canales.
- **Comando de ejemplo:** `kismet -n -c wlan0mon --log-prefix captures/kismet/session-20260327`
- **Notas útiles:** exporto CSV/PCAP/GPS para Airgraph y anoto ruido/RSSI en `wifi/notes/kismet-<fecha>.md`.
- **Recomendaciones:** usa `--netxml` y filtra `signal>-80` para enfocarte en APs cercanos.
- **Cuándo usarlo:** al inicio para identificar redes y canales.
- **Cuándo no:** si necesitas lanzar ataques inmediatamente (usa `airodump`).

### Airodump-ng
- **Enlace:** https://github.com/aircrack-ng/aircrack-ng
- **Caso de uso:** capturar handshakes, beacon frames y asociar MAC/AP.
- **Comando de ejemplo:** `airodump-ng --write captures/session-20260327 --output-format csv,pcap wlan0mon`
- **Notas útiles:** aplico `--channel`/`--bssid` y guardo handshakes en `captures/handshakes-01.cap`.
- **Recomendaciones:** activa `--essid` para no perder sesión si hay roaming.
- **Cuándo usarlo:** siempre que necesites evidencia de handshake.
- **Cuándo no:** si solo haces reconocimiento pasivo (usa Kismet).

### hcxdumptool + hcxpcaptool
- **Enlace:** https://github.com/ZerBea/hcxdumptool
- **Caso de uso:** captura avanzada de handshakes, PMKID y 802.11r.
- **Comando de ejemplo:** `hcxdumptool -o captures/pmkid-20260327.pcapng -i wlan0mon --enable_status=1 --filterlist=targets/hcxdumptool-filterlist.txt`
- **Notas útiles:** convierto con `hcxpcaptool -z outputs/hashcat/pmkid.hc22000 captures/pmkid-*.pcapng`.
- **Recomendaciones:** usa `--filterlist` para evitar redes externas.
- **Cuándo usarlo:** cuando el objetivo soporta WPA2/3 con PMKID.
- **Cuándo no:** si el entorno es muy ruidoso y prefieres `airodump`.

## 2. Cracking y fuerza bruta

### Aircrack-ng
- **Enlace:** https://github.com/aircrack-ng/aircrack-ng
- **Caso de uso:** recuperar claves WPA/WPA2 con handshake.
- **Comando de ejemplo:** `aircrack-ng -w wordlists/rockyou.txt -b 00:11:22:33:44:55 captures/handshake-01.cap`
- **Notas útiles:** tengo wordlists propias en `wifi/wordlists/` y documento resultados en `reports/wifi/aircrack-results.md`.
- **Recomendaciones:** usa `--pke`/`--hccapx` para exportar a Hashcat.
- **Cuándo usarlo:** cuando hay handshake válido.
- **Cuándo no:** si la red usa WPA3 o PMKID-only (usa Hashcat).

### Hashcat
- **Enlace:** https://hashcat.net/hashcat/
- **Caso de uso:** ataques GPU sobre handshakes/PMKID.
- **Comando de ejemplo:** `hashcat -m 2500 outputs/hashcat/handshake.hccapx -a 3 '?d?d?d?d?d?d?d?d' --session wifi-session`
- **Notas útiles:** guardo estado en `wifi/hashcat/wifi-session.hccap` y cracks en `wifi/hashcat/cracked.txt`.
- **Recomendaciones:** habilita `--restore` y `--status`.
- **Cuándo usarlo:** redes que requieren GPU o mask attacks.
- **Cuándo no:** laboratorios sin GPU (usa Aircrack-ng con wordlists ligeros).

## 3. MITM y manipulación activa

### Bettercap
- **Enlace:** https://github.com/bettercap/bettercap
- **Caso de uso:** inyección de paquetes, interceptación y manipulación HTTP.
- **Comando de ejemplo:** `bettercap -iface wlan0mon -eval 'net.probe on; wifi.assoc on; http.proxy on'`
- **Notas útiles:** configuro módulos por víctima y guardo logs en `wifi/bettercap/`.
- **Recomendaciones:** solo en laboratorios con autorización.
- **Cuándo usarlo:** cuando demuestras cómo un atacante interceptaría tráfico.
- **Cuándo no:** redes de producción sin permiso.

### Wifite2
- **Enlace:** https://github.com/derv82/wifite2
- **Caso de uso:** ataques automáticos (WPA, WPS, PMKID).
- **Comando de ejemplo:** `wifite --wps --handshake --dict wordlists/wifite-roster.txt --output=wifite/logs/session-20260327`
- **Notas útiles:** reviso logs (`timee.log`) para ver qué handshake se guardó.
- **Recomendaciones:** define `--essid` y `--exclude`.
- **Cuándo usarlo:** cuando hay muchas redes y quieres automatizar.
- **Cuándo no:** si necesitas control fino.

## 4. Análisis y visualización

### Wireshark
- **Enlace:** https://www.wireshark.org/
- **Caso de uso:** inspección de tramas, beacon/probe y autenticación.
- **Comando de ejemplo:** `wireshark -r captures/session-20260327.pcapng -Y 'wlan.fc.type_subtype == 0x08'`
- **Notas útiles:** filtro beacons y deauth, exporto snapshots a `reports/wifi/wireshark-sesiones.md`.
- **Recomendaciones:** usa `tshark` para extraer listas con `-T fields`.
- **Cuándo usarlo:** cuando necesitas evidencia visual del tráfico.
- **Cuándo no:** si solo necesitas metadata (usa Kismet o Airodump).

### Airgraph-ng
- **Enlace:** https://github.com/aircrack-ng/airgraph-ng
- **Caso de uso:** mapear relaciones SSID↔BSSID.
- **Comando de ejemplo:** `airgraph-ng -i captures/session-20260327-01.csv -o wifi/airgraph/graph.svg -g netxml`
- **Notas útiles:** convierto la salida en SVG y lo incluyo en reportes.
- **Recomendaciones:** usa `--min-quality 20`.
- **Cuándo usarlo:** para explicar cobertura a un cliente.
- **Cuándo no:** si ya tienes mapas generados.

## 5. Flujos y documentación
- Cada captura va a `captures/<fecha>/`, handshakes a `captures/handshakes/` y se registran en `reports/wifi/sessions.md` con adaptador, driver, canal y potencia.
- Usa `scripts/wifi/session-summary.sh` para generar CSV con `start_time`, `AP`, `clients`, `hit`, `handshake_found`.
- Mantén `wifi/drivers.md` con notas sobre chips Realtek/Qualcomm y `airmon-ng check kill`.
- Documenta tiempos de recuperación tras ataques en `reports/wifi/resilience.md`.
- Guarda MACs y ESSIDs ficticios en `reports/wifi/imsis.md` para reproducir sesiones.
- Respeta la legalidad: ninguna acción sin autorización expresa del propietario de la red.
