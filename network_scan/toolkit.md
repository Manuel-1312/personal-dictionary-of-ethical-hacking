# Toolkit - Network Scan 📡

Cada entrada esta basada en un escaneo real. Guardo comandos, la red puntual y el resultado más útil para que otros puedan repetirlo sin adivinar flags.

| Herramienta | Comando típico | Categoria | Resultado/nota |
| --- | --- | --- | --- |
| nmap | `nmap -T3 -sC -sV -oA reports/network/nmap-lab 10.0.0.0/24` | Escaneo completo | Exporto XML para alimentar reportes y uso `vulscan` para obtener CVEs. |
| Masscan | `masscan 10.0.0.0/20 --rate=1000 -p0-65535 -oG reports/network/masscan.gnmap` | Edge discovery | Sirve para saber qué IPs responderán antes del nmap. Ajusta `--rate` para evitar saturar el switch. |
| RustScan | `rustscan -a 10.0.1.50 -- -A -sV` | Escaneo rápido | Lo uso como preludio a nmap; guarda la lista de puertos abiertos en `reports/network/rustscan.txt`. |
| ZMap | `zmap -p 80 10.0.0.0/16 -o reports/network/zmap-http.csv` | Escaneo a escala | Solo sobre rangos autorizados y siempre con router de laboratorio. |
| Netdiscover | `netdiscover -i eth0 -r 10.0.0.0/24` | Descubrimiento ARP | Documenta MACs nuevas y la relación con VLAN y equipos reales. |
| Nping | `nping --tcp -p 443 10.0.0.5 --rate 10` | Generador de paquetes | Lo uso para probar filtros IDS/IPS y medir latencia; guardo los ICMP RTT. |
| Vulscan | `nmap --script vulscan --script-args vulscandb=scipag https://10.0.0.5` | Correlación CVE | Complementa los resultados de nmap con identificadores de vulnerabilidad. |
