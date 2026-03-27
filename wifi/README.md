# WiFi Lab

Aquí guardo todo lo que uso para auditorías inalámbricas legales. En mi estación principal (WSL conectada a una Alpha AWUS036ACH y un TP-Link con drivers nuevos) siempre empiezo así:

1. Documento la tarjeta que voy a usar y la red de laboratorio (SSID, canal, BSSID) en `lab-notes.md`.
2. Lanzo `airmon-ng check kill` y luego `airmon-ng start wlan0` antes de capturar.
3. Capturo paquetes durante 5–10 minutos (.cap/.pcap) y los guardo con fecha. Después uso `Wireshark` para exportar los beacons más interesantes.

Este directorio tiene tres pilares:

- **Equipos**: tarjetas monitor-mode, antenas direccionales, adaptadores USB. Siempre anoto modelos y qué firmware estaba activo.
- **Captura**: traffic dumps (`airodump`, `hcxdumptool`, `dumpcap`), filtros por canal y notas sobre ruido o interferencias.
- **Atques controlados**: bruteforce WPA/WPA2, pruebas de WPS en laboratorio (con `reaver` y `bully`), tests de RADIUS y benchmarking de throughput.

Usa `toolkit.md` como índice y deja allí ejemplos reales de comandos o trampas que te funcionaron; si algo falló, apunta también la causa (drivers, interferencia, falta de permisos). La idea es que cualquier compañero pueda replicar tu práctica paso a paso.

## Comandos utilizados
- `sudo airmon-ng check kill && sudo airmon-ng start wlan0` para limpiar el entorno y entrar en monitor mode antes de cualquier captura.
- `airodump-ng --write captures/session-$(date +%Y%m%d) --output-format csv,pcap wlan0mon` para generar datos listos para Airgraph y para validar handshakes.
- `hcxdumptool -o captures/session-$(date +%Y%m%d).pcapng --enable_status=15 wlan0mon` cuando necesito recopilar PMKID y handshakes a nivel moderno.

## Técnicas aplicadas
- Captura pasiva durante 5 minutos antes de atacar: me sirve para catalogar dispositivos y calibrar filtros en Wireshark.
- Uso de `bettercap` en VLAN aisladas para probar inyección y ver cómo reaccionan los IDS/IPS ficticios conectados al laboratorio.
- Pruebas de resiliencia WPA/WPA2 con `aircrack-ng` y `hashcat` en un entorno offline para medir el impacto de wordlists personalizadas.

## Recomendaciones personales
- Siempre mantén un backup de los `.cap` y `.csv`; cuando los procesas con Airgraph, puedes volver a trazar la topología para sesiones futuras.
- Anota qué adaptador y qué drivers funcionaron: algunos chips (Realtek 8812au) requieren recompilar el módulo a mano.
- Si fallan los ataques con `wifite`, revisa la potencia y considera cambiar de canal para evitar interferencias de vecinos.
