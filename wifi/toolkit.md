# Toolkit - WiFi 🛰️

Este es mi inventario de herramientas inalámbricas. Cada vez que uso una, apunto el comando exacto, la interfaz (`wlan0`, `wlan1mon`), el canal y cómo terminé el experimento.

| Herramienta | Enlace | Categoría | Notas prácticas |
| --- | --- | --- | --- |
| Aircrack-ng | https://github.com/aircrack-ng/aircrack-ng | Suite completa | Para WPA2 uso `airodump-ng --write handshakes --channel 6 wlan0mon` y luego `aircrack-ng -w rockyou.txt handshakes-01.cap`. Guardo los archivos en `outputs/aircrack` con la fecha.
| Kismet | https://www.kismetwireless.net/ | Detección pasiva | Lo lanzo con `kismet -c wlan0mon` y exporto CSV/PCAP para comparar señales. Anoto el ruido, la potencia y si detectó redes ocultas.
| Bettercap | https://github.com/bettercap/bettercap | MITM e inyección | Uso `bettercap -iface wlan0mon -eval ...` en VMs aisladas; siempre detallo qué paquetes edité para reportarlo correctamente.
| Wifite2 | https://github.com/derv82/wifite2 | Auditoría automatizada | Ideal para QA. Lanzo `wifite --wps --handshake` y dejo el log en `wifite/logs`. Miro cuál antena responde mejor.
| Airgraph-ng | https://github.com/aircrack-ng/airgraph-ng | Visualización | Genero mapas de relaciones SSID↔MAC y los pego en el README de la sesión. Así veo si apareció un MAC nuevo.
| Wireshark | https://www.wireshark.org/ | Análisis de tramas | Archivo `.pcap` en `/captures`, filtro `wlan.fc.type_subtype == 0x08` para beacons y `encryption` para handshake.
| MDK4 | https://github.com/aircrack-ng/mdk4 | Stress testing | Solo en laboratorio: `mdk4 wlan0mon d` para ataques DDoS controlados. Anoto cuánto tardó el AP en recuperarse y cuál fue la latencia.

## Comandos utilizados recientemente
- `airodump-ng --write captures/session-20260327 --output-format csv,pcap wlan0mon` → Captura multi-formato para cargar en Airgraph.
- `hcxdumptool --enable_status=1 --pmkid=1 --output captures/pmkid-20260327.pcapng wlan0mon` → Sirve para estudiar PMKID recientes.
- `bettercap -iface wlan0mon -eval "net.probe on; wifi.assoc on"` → Pruebo mitm en redes de laboratorio sin exponer la red de casa.

## Técnicas aplicadas
- Captura prolongada (10 min) sin atacar para mapear APs, calcular ruido/overlap y ajustar `channel`.
- Monitorización de beacon/probe con Wireshark para detectar nuevas SSID, luego replico la topología en Airgraph.
- Pruebas de resiliencia WPA: `aircrack-ng` + `hashcat` contra `roster` y `rockyou` con un `mask` personalizado.

## Recomendaciones personales
- Mantén carpetas separadas para cada sesión (`captures/2026-03-27/`) y no mezcles handshakes, facilita la revisión.
- Documenta qué adaptador y versión de driver usaste: algunos chips Realtek necesitan `dkms` y se rompen con actualizaciones.
- Si `wifite` se cuelga, revisa la potencia y cambia a un canal menos concurrido antes de volver a correr los ataques automáticos.
