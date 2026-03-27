# Toolkit - WiFi 🛰️

Libro de jugadas para auditorías inalámbricas: capturas, cracking, MITM y análisis de señales. Cada herramienta explica el contexto de uso, el comando exacto, dónde guardo las salidas y qué tener en cuenta para no romper la sesión.

## 1. Capturas y mapeo pasivo

### Kismet
- **Enlace:** https://www.kismetwireless.net/
- **Caso de uso:** detección pasiva de AP/estaciones, análisis de canales, identificación de SSID ocultos.
- **Comando de ejemplo:** `kismet -n -c wlan0mon --log-prefix captures/kismet/session-20260327`
- **Notas útiles:** exporto CSV, PCAP y `gpsdump` para alimentar `Airgraph-ng`. Anoto el ruido `rssi` y los canales menos saturados en `wifi/notes/kismet-<fecha>.md`.
- **Recomendaciones:** usa `--netxml` para generar mapas automáticos y filtra por `signal>-80` para enfocarte en APs cercanos.
- **Cuándo usarlo:** al inicio para identificar qué redes conviene atacar y cuánto solapa cada canal.
- **Cuándo no:** si necesitas atacar inmediatamente y no quieres ruido de escuchas (usa `airodump` directo).

### Airodump-ng
- **Enlace:** https://github.com/aircrack-ng/aircrack-ng
- **Caso de uso:** capturar handshakes, beacon frames y asociar MAC/AP.
- **Comando de ejemplo:** `airodump-ng --write captures/session-20260327 --output-format csv,pcap wlan0mon`
- **Notas útiles:** uso `--channel` y `--bssid` para fijar al objetivo; los handshakes saltan a `captures/handshakes-01.cap` y los valido con `aircrack-ng captures/handshake`.
- **Recomendaciones:** activa `--essid` para no perder la sesión si hay roaming.
- **Cuándo usarlo:** en todas las auditorías donde necesitas evidencia del handshake.
- **Cuándo no:** si solo estás haciendo reconocimiento y no quieres interrumpir tráfico (usa Kismet pasivo).

### hcxdumptool + hcxpcaptool
- **Enlace:** https://github.com/ZerBea/hcxdumptool
- **Caso de uso:** captura avanzada de handshakes, PMKID y tokens 802.11r.
- **Comando de ejemplo:** `hcxdumptool -o captures/pmkid-20260327.pcapng -i wlan0mon --enable_status=1 --filterlist=targets/hcxdumptool-filterlist.txt`
- **Notas útiles:** luego convierto con `hcxpcaptool -z outputs/hashcat/pmkid.hc22000 captures/pmkid-*.pcapng` y lo paso a hashcat. Documenté las macros en `wifi/hcxdumptool/notes.md`.
- **Recomendaciones:** utiliza `--filterlist` para evitar capturar redes externas.
- **Cuándo usarlo:** cuando el target solo soporta WPA2/3 con PMKID.
- **Cuándo no:** si estás en un entorno muy ruidoso y prefieres `airodump` tradicional.

## 2. Cracking y fuerza bruta

### Aircrack-ng
- **Enlace:** https://github.com/aircrack-ng/aircrack-ng
- **Caso de uso:** recuperar claves WPA/WPA2 via handshake capturado.
- **Comando de ejemplo:** `aircrack-ng -w wordlists/rockyou.txt -b 00:11:22:33:44:55 captures/handshake-01.cap`
- **Notas útiles:** mantengo wordlists propias en `wifi/wordlists/` combinando `maskprocessor` y `crunch`. Los resultados se documentan en `reports/wifi/aircrack-results.md`.
- **Recomendaciones:** usa `--pke` y `--hccapx` para exportar a Hashcat si necesitas GPU.
- **Cuándo usarlo:** cuando tienes un handshake válido y quieres validar contra un diccionario.
- **Cuándo no:** si la red usa WPA3 o PMKID-only (usa Hashcat con `hc22000`).

### Hashcat (modo hccapx/pmkid)
- **Enlace:** https://hashcat.net/hashcat/
- **Caso de uso:** ataques GPU optimizados sobre handshakes o PMKID.
- **Comando de ejemplo:** `hashcat -m 2500 outputs/hashcat/handshake.hccapx -a 3 '?d?d?d?d?d?d?d?d' --session wifi-session`
- **Notas útiles:** guardo el estado en `wifi/hashcat/wifi-session.hccap` y exporto cracks exitosos a `wifi/hashcat/cracked.txt`.
- **Recomendaciones:** habilita `--restore` y `--status` para controlar el job.
- **Cuándo usarlo:** si la red requiere técnicas GPU o mask/rule attacks.
- **Cuándo no:** en tests de laboratorio sin GPU (usa `aircrack-ng` con wordlists ligeros).

## 3. MITM y manipulación activa

### Bettercap
- **Enlace:** https://github.com/bettercap/bettercap
- **Caso de uso:** inyección de paquetes, captura de credenciales HTTP y manipulación de trazas.
- **Comando de ejemplo:** `bettercap -iface wlan0mon -eval 'net.probe on; wifi.assoc on; http.proxy on'`
- **Notas útiles:** configuro `bettercap/caps` por víctima y guardo los logs en `wifi/bettercap/`. Documenté qué módulos (`wifi.deauth`, `http.proxy.script`) se activaron en `reports/wifi/bettercap.md`.
- **Recomendaciones:** úsalo únicamente en entornos de laboratorio o con autorización explícita.
- **Cuándo usarlo:** cuando necesitas evidenciar cómo un atacante podría interceptar tráfico o inyectar scripts.
- **Cuándo no:** en redes de producción sin permiso (riesgo legal elevado).

### Wifite2
- **Enlace:** https://github.com/derv82/wifite2
- **Caso de uso:** orquestar ataques automáticos (WPA handshakes, WPS, PMKID) sobre múltiples redes.
- **Comando de ejemplo:** `wifite --wps --handshake --dict wordlists/wifite-roster.txt --output=wifite/logs/session-20260327`
- **Notas útiles:** reviso el log `wifite/logs/session-20260327/timee.log` para saber qué redes responderán y qué handshake se guardó. Lo uso como respaldo cuando manualmente no encuentro handshakes.
- **Recomendaciones:** define `--essid` y `--exclude` para no tocar redes vecinas.
- **Cuándo usarlo:** cuando hay muchas redes y quieres automatizar pruebas.
- **Cuándo no:** si necesitas un control fino y no quieres que la herramienta cambie canales constantemente.

## 4. Análisis y visualización

### Wireshark
- **Enlace:** https://www.wireshark.org/
- **Caso de uso:** inspección detallada de tramas, beacon/probe y autenticación 802.11.
- **Comando de ejemplo:** `wireshark -r captures/session-20260327.pcapng -Y 'wlan.fc.type_subtype == 0x08'`
- **Notas útiles:** filtro `wlan.fc.type_subtype == 0x08` para beacons y `wlan.fc.type_subtype == 0x0a` para Deauth. Exporto gráficos a `wifi/wireshark/` y añado snapshots a `reports/wifi/wireshark-sesiones.md`.
- **Recomendaciones:** usa `tshark` para extraer rápidamente listas con `-T fields -e wlan.sa -e wlan.da`.
- **Cuándo usarlo:** cuando necesitas evidencia visual del tráfico o construir un caso técnico para el cliente.
- **Cuándo no:** si solo necesitas metadata (usa `kismet` o `airodump`).

### Airgraph-ng
- **Enlace:** https://github.com/aircrack-ng/airgraph-ng
- **Caso de uso:** mapear relaciones SSID↔BSSID y visualizar drones.
- **Comando de ejemplo:** `airgraph-ng -i captures/session-20260327-01.csv -o wifi/airgraph/graph.svg -g netxml`
- **Notas útiles:** convierto la salida a SVG y lo incluyo en los reportes para mostrar roaming o clones.
- **Recomendaciones:** añade `--min-quality 20` para omitir APs muy débiles.
- **Cuándo usarlo:** al entregar el informe para explicar a un cliente la cobertura de su red.
- **Cuándo no:** si ya tienes mapas generados con Kismet y no quieres duplicar esfuerzo.

## 5. Flujos, documentación y recomendaciones
- Cada captura va a `captures/<fecha>/` y los handshakes a `captures/handshakes/`; luego los registramos en `reports/wifi/sessions.md` con metadata de adaptador, driver, canal y potencia.
- Usa `scripts/wifi/session-summary.sh` para generar CSV con `start_time`, `AP`, `clients`, `hit`, `handshake_found`.
- Mantén un `wifi/drivers.md` con notas sobre qué chips Realtek/Qualcomm se caen tras actualizar o requieren `airmon-ng check kill`.
- Cuando la red se cae por ataques, anota el tiempo de recuperación en `reports/wifi/resilience.md` para comparar distintas técnicas.
- Documenta siempre los `MAC`s ficticios y `ESSID`s temporales usados durante las pruebas para poder reproducirlas en sesiones futuras.
