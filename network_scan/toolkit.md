# Toolkit - Network Scan 📡

Inventario de escaneos de red ejecutados en laboratorios controlados. Cada herramienta sigue la plantilla estándar (enlace, caso de uso, comando, notas, recomendaciones y cuándo usar/no usar) y enlaza con reportes para facilitar la reproducibilidad.

## Plantilla base
- **Enlace:** página oficial.
- **Caso de uso:** propósito dentro del ciclo de escaneo.
- **Comando de ejemplo:** flaglist reproducible.
- **Notas útiles:** logs, CSV, transformaciones.
- **Recomendaciones:** cómo evitar saturar la red.
- **Cuándo usar / cuándo no:** límites de aplicación.

## Herramientas clave

### Nmap
- **Enlace:** https://nmap.org
- **Caso de uso:** escaneo completo con detección de versiones, NSE y salidas para reportes.
- **Comando de ejemplo:** `nmap -T3 -sC -sV -oA reports/network/nmap-lab 10.0.0.0/24`
- **Notas útiles:** exporto `reports/network/nmap-lab.xml` y lo paso a `vulscan` (`nmap --script vuln --script-args=unsafe=1`). También uso `http-headers` para comprobar HSTS/CSP.
- **Recomendaciones:** arranca en `-T3` y sube a `-T4` solo si la red lo tolera.
- **Cuándo usarlo:** tras validar hosts con `naabu`/`httpx`.
- **Cuándo no:** cuando buscas un barrido ultrarrápido (usa `masscan`).

### Masscan
- **Enlace:** https://github.com/robertdavidgraham/masscan
- **Caso de uso:** escaneo a escala de rangos grandes antes de entrar a `nmap`.
- **Comando de ejemplo:** `masscan 10.0.0.0/20 --rate=1000 -p0-65535 -oL reports/network/masscan.gnmap`
- **Notas útiles:** convierto la salida con `masscan2nmap` y filtro hosts con puertos abiertos.
- **Recomendaciones:** ajusta `--rate` (≤1000) si trabajas con switches antiguos y añade `--router-mac` para saber qué responde.
- **Cuándo usarlo:** con /16s.
- **Cuándo no:** redes pequeñas o autorizaciones limitadas.

### RustScan
- **Enlace:** https://github.com/RustScan/RustScan
- **Caso de uso:** escaneo híbrido que lanza `nmap` automáticamente sobre puertos abiertos.
- **Comando de ejemplo:** `rustscan -a 10.0.1.50 --ulimit 5000 -- -A -sV`
- **Notas útiles:** guarda logs en `reports/network/rustscan.txt`. Recomiendo aumentar `--ulimit` para evitar errores de sockets.
- **Recomendaciones:** ideal para escanear hosts aislados antes de un pentest interno.
- **Cuándo usarlo:** cuando necesitas un único host rápido.
- **Cuándo no:** barridos masivos (usa `masscan`).

### ZMap
- **Enlace:** https://zmap.io
- **Caso de uso:** escaneo a gran escala (HTTP, SSH, FTP) en rangos autorizados.
- **Comando de ejemplo:** `zmap -p 80 10.0.0.0/16 -o reports/network/zmap-http.csv`
- **Notas útiles:** complemento con `zgrab` para obtener banners y guardar CSV en `reports/network/zmap-analysis.md`.
- **Recomendaciones:** convierte outputs y carga en dashboards para análisis comparativos.
- **Cuándo usarlo:** auditorías masivas o benchmarks.
- **Cuándo no:** redes compartidas donde no puedes saturar el switch.

### Naabu
- **Enlace:** https://github.com/projectdiscovery/naabu
- **Caso de uso:** preludio rápido de `nmap` para enfocar hosts con puertos abiertos.
- **Comando de ejemplo:** `naabu -iL recon/targets/live.txt -o outputs/recon/naabu.txt -rate 800`
- **Notas útiles:** etiqueta cada IP en `reports/network/naabu-<fecha>.txt` y alimenta `nmap` con la lista.
- **Recomendaciones:** usa `-exclude-ports` para evitar sistemas críticos.
- **Cuándo usarlo:** justo antes de `nmap`.
- **Cuándo no:** si ya hiciste `RustScan` y quieres mantener el proceso simple.

### Netdiscover / arp-scan
- **Enlaces:** https://github.com/alexxy/netdiscover / https://github.com/royhills/arp-scan
- **Caso de uso:** descubrimiento ARP en redes internas sin documentación.
- **Comando de ejemplo:** `netdiscover -i eth0 -r 10.0.0.0/24` / `arp-scan --interface=eth0 10.0.0.0/24`
- **Notas útiles:** guardo MAC/IP en `reports/network/netdiscover.csv` para vincular VLAN.
- **Recomendaciones:** mapear topologías antes de escanear puertos.
- **Cuándo usarlo:** cuando tienes acceso a la red.
- **Cuándo no:** entornos aislados con DHCP estático.

### Nping
- **Enlace:** https://nmap.org/nping
- **Caso de uso:** generación controlada de tráfico para probar IDS/IPS.
- **Comando de ejemplo:** `nping --tcp -p 443 10.0.0.5 --rate 10 --flags syn`
- **Notas útiles:** guardo RTT en `reports/network/nping-433.log` y lo uso para detectar filtrado L4.
- **Recomendaciones:** combínalo con Suricata para validar alertas.
- **Cuándo usarlo:** al validar reglas de detección.
- **Cuándo no:** redes sensibles a latencia.

### Vulscan (Nmap NSE)
- **Enlace:** https://github.com/scipag/vulscan
- **Caso de uso:** añadir CVEs a resultados de `nmap`.
- **Comando de ejemplo:** `nmap --script vulscan --script-args vulscandb=scipag --script-args safe=1 10.0.0.5`
- **Notas útiles:** actualizo `vulscan` semanalmente y guardo CSV en `reports/network/vulscan.csv`.
- **Recomendaciones:** revisa manualmente los CVEs antes de reportarlos.
- **Cuándo usarlo:** fase controlada de enumeración de vulnerabilidades.
- **Cuándo no:** cuando sólo quieres inventario y no necesitas CVEs.

## Flujos y documentación relacionada
- Flujo típico: `masscan` → `naabu` → `nmap -sC -sV` → `vulscan` → `RustScan` (host) / `ZMap` (rango grande).
- Usa `Netdiscover`/`arp-scan` para mapear activos antes de `nmap` y documenta en `network/utils/scan-collector.md`.
- `Nping` + `Suricata` sirve para calibrar thresholds (`reports/network/nping-suricata.md`).
- Todos los CSV/outputs van a `reports/network/<herramienta>/` con contexto y se enlazan desde `reports/network/README.md`.
