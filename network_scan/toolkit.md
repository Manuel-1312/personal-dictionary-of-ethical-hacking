# Toolkit - Network Scan 📡

Inventario de escaneos de red que ejecuté en laboratorios y entornos controlados. Cada herramienta describe el propósito (host discovery, fingerprinting, scan masivo), el comando exacto y qué aprendí de los logs.

## Herramientas clave

### Nmap
- **Enlace:** https://nmap.org
- **Caso de uso:** escaneo completo con detección de versiones, scripts NSE y salidas en XML/grepeable para alimentar reportes.
- **Comando de ejemplo:** `nmap -T3 -sC -sV -oA reports/network/nmap-lab 10.0.0.0/24`
- **Notas útiles:** guardo `reports/network/nmap-lab.xml` y lo uso con `vulscan` para obtener CVEs (`nmap --script vuln --script-args=unsafe=1`). También ejecuto `nmap --script http-headers` para comprobar cabeceras HSTS/CSP.
- **Recomendaciones:** arranca con `-T3` y aumenta a `-T4` solo cuando sabes que la red lo aguanta.
- **Cuándo usarlo:** tras validar hosts con `naabu`/`httpx`.
- **Cuándo no:** cuando necesitas un barrido muy rápido de puertos (usa `masscan` o `RustScan`).

### Masscan
- **Enlace:** https://github.com/robertdavidgraham/masscan
- **Caso de uso:** escaneo a escala de rangos enormes antes de entrar a nmap.
- **Comando de ejemplo:** `masscan 10.0.0.0/20 --rate=1000 -p0-65535 -oL reports/network/masscan.gnmap`
- **Notas útiles:** convierte el output a `nmap` con `masscan2nmap` y luego filtra solo hosts con puertos abiertos reales.
- **Recomendaciones:** fija `--rate` en 1000 o menos si trabajas en infra con switches antiguos; usa `--router-mac` para saber qué equipo responde.
- **Cuándo usarlo:** cuando te dan un /16 y no podés esperar horas.
- **Cuándo no:** en redes pequeñas o cuando tengas pocos hosts autorizados.

### RustScan
- **Enlace:** https://github.com/RustScan/RustScan
- **Caso de uso:** escaneo híbrido que lanza `nmap` automáticamente sobre puertos abiertos.
- **Comando de ejemplo:** `rustscan -a 10.0.1.50 --ulimit 5000 -- -A -sV`
- **Notas útiles:** los logs van a `reports/network/rustscan.txt` y la opción `-- -sC -sV` dispara el nmap subsecuente; recomiendo aumentar `--ulimit` para evitar errores de sockets.
- **Recomendaciones:** ideal para hosts aislados antes de un pentest interno.
- **Cuándo usarlo:** cuando querés un escaneo rápido en un solo equipo.
- **Cuándo no:** en barridos masivos (usa `masscan`).

### ZMap
- **Enlace:** https://zmap.io
- **Caso de uso:** escaneo de alto volumen para medir la superficie expuesta (HTTP, SSH, FTP).
- **Comando de ejemplo:** `zmap -p 80 10.0.0.0/16 -o reports/network/zmap-http.csv`
- **Notas útiles:** siempre lo lanzo en rangos autorizados y lo complemento con `zgrab` para obtener banners.
- **Recomendaciones:** guarda `zmap` + `zgrab` outputs en CSV y importa en `reports/network/zmap-analysis.md`.
- **Cuándo usarlo:** en auditorías masivas o comparativas de benchmarks.
- **Cuándo no:** en redes compartidas donde no podés saturar el switch.

### Naabu (host discovery)
- **Enlace:** https://github.com/projectdiscovery/naabu
- **Caso de uso:** preludio de nmap para acotar hosts con puertos abiertos.
- **Comando de ejemplo:** `naabu -iL recon/targets/live.txt -o outputs/recon/naabu.txt -rate 800`
- **Notas útiles:** los resultados alimentan `reports/network/naabu-<fecha>.txt` y etiqueto cada IP (por ejemplo, `10.0.1.55:22/ssh`).
- **Recomendaciones:** usa `-exclude-ports 22,161` si el cliente tiene sistemas críticos.
- **Cuándo usarlo:** justo antes de ejecutar `nmap`.
- **Cuándo no:** cuando ya hiciste un escaneo con `RustScan` y necesitas mantenerlo simple.

### Netdiscover / arp-scan
- **Enlace:** https://github.com/alexxy/netdiscover / https://github.com/royhills/arp-scan
- **Caso de uso:** descubrimiento ARP en redes internas no documentadas.
- **Comando de ejemplo:** `netdiscover -i eth0 -r 10.0.0.0/24` / `arp-scan --interface=eth0 10.0.0.0/24`
- **Notas útiles:** guardo los MAC/IP en `reports/network/netdiscover.csv` para cruzar VLAN.
- **Recomendaciones:** ideal para mapear topologías antes de escanear.
- **Cuándo usarlo:** cuando estás en un laboratorio conectado directamente a la red.
- **Cuándo no:** en entornos aislados donde proveen DHCP estático.

### Nping
- **Enlace:** https://nmap.org/nping
- **Caso de uso:** generar tráfico (TCP/ICMP) controlado para probar IDS/IPS.
- **Comando de ejemplo:** `nping --tcp -p 443 10.0.0.5 --rate 10 --flags syn`
- **Notas útiles:** guardo RTT en `reports/network/nping-433.log` y lo uso para detectar filtrado a nivel L4.
- **Recomendaciones:** combina con Suricata para validar alertas.
- **Cuándo usarlo:** al validar reglas de detección.
- **Cuándo no:** en entornos de producción con latencias sensibles.

### Vulscan (Nmap NSE)
- **Enlace:** https://github.com/scipag/vulscan
- **Caso de uso:** adjuntar identificadores de CVE a los resultados de nmap.
- **Comando de ejemplo:** `nmap --script vulscan --script-args vulscandb=scipag --script-args safe=1 10.0.0.5`
- **Notas útiles:** actualizo `vulscan` semanalmente y guardo los CSV resultantes en `reports/network/vulscan.csv`.
- **Recomendaciones:** revisa manualmente los CVEs antes de incluirlos en reportes.
- **Cuándo usarlo:** en fases de enumeración de vulnerabilidades controladas.
- **Cuándo no:** si necesitas solo inventario y no quieres generar falsos positivos.

## Flujos y notas rápidas
- `masscan` → `naabu` → `nmap -sC -sV` → `vulscan` → `RustScan` (caso host) / `ZMap` (rango grande).
- `Netdiscover`/`arp-scan` para descubrir activos antes de meter `nmap`.
- `Nping` + `Suricata` para validar filtros y `nping --rate` para calibrar thresholds.
- Guarda cada CSV en `reports/network/<herramienta>/` con la fecha y el contexto de pruebas.
- Usa `scripts/scan-collector.sh` para convertir outputs en un solo dashboard (referencia: `network/utils/scan-collector.md`).
