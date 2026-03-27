# Toolkit - Host Discovery 🔎

Enumera herramientas para mapear hosts antes de escanearpuertos. Añade comandos y notas claras.

| Herramienta | Enlace | Uso | Notas |
| --- | --- | --- | --- |
| arp-scan | https://github.com/royhills/arp-scan | Descubrimiento ARP | `arp-scan -I eth0 -l 10.0.0.0/24` → Guardar MACs nuevos en `hosts/arp.csv`.
| nbtscan | https://github.com/claudiokuenzler/nbtscan | NetBIOS | `nbtscan -v 10.0.0.0/24` → Export `hosts/nbtscan.csv`.
| fping | https://fping.org/ | Ping masivo | `fping -a -g 10.0.1.0/24` para validar disponibilidad.
| hping3 | https://github.com/antirez/hping | TCP/UDP craft | Prueba filtros con `hping3 --syn -p 443 10.0.0.1`.
| masscan (ping) | https://github.com/robertdavidgraham/masscan | Ping masivo | `masscan --ping-only` para bloquear hosts activos.
| ZMap (ICMP) | https://github.com/zmap/zmap | Escaneo ICMP | Documenta rangos y proxies usados.

## Comandos utilizados recientemente
- `arp-scan -I eth0 -l 10.0.0.0/24` para mapear nuestra VLAN de pruebas.
- `nbtscan -v 10.0.1.0/24` para relacionar nombres de equipo con IPs.
- `fping -a -g 10.0.2.0/24` guardando resultados en `hosts/fping-20260327.txt`.

## Técnicas aplicadas
- Repetición de discovery por la mañana y la tarde para ver qué hosts aparecen nuevos.
- Validación de VLANs cambiadas con `masscan` segmentado y comparaciones con la tabla principal.

## Recomendaciones personales
- Guarda los archivos `hosts/*.csv` en Git para comparar cuándo se sumó un equipo.
- Automatiza la limpieza de hosts offline (`hosts/cleanup.sh`).
- Si un host desaparece, vuelve a escanearlo con `nmap -Pn` para confirmar que no recorta firewalls.