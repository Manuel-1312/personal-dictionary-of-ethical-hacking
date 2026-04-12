# Toolkit - Host Discovery 🔎

Enumera herramientas para mapear hosts antes de escanear puertos. Añade comandos y notas claras.

## Plantilla base
- **Enlace:** referencia oficial.
- **Caso de uso:** propósito de la herramienta.
- **Comando de ejemplo:** comando representativo.
- **Notas útiles:** observaciones clave.
- **Recomendaciones:** consejos de uso.
- **Cuándo usar / cuándo no:** límites y contexto.

## 1. Herramientas de descubrimiento

### arp-scan
- **Enlace:** https://github.com/royhills/arp-scan
- **Caso de uso:** Descubrimiento ARP en red local.
- **Comando de ejemplo:** `arp-scan -I eth0 -l 10.0.0.0/24`
- **Notas útiles:** Guardar MACs nuevos en `hosts/arp.csv`.
- **Recomendaciones:** Usa `-l` con la interfaz correcta; útil para detectar hosts ocultos a ICMP.
- **Cuándo usarlo:** Primera pasada en red local donde controlas la interfaz.
- **Cuándo no:** En redes con muchos hosts virtuales; puede generar ruido ARP notable.

### nbtscan
- **Enlace:** https://github.com/claudiokuenzler/nbtscan
- **Caso de uso:** Descubrimiento NetBIOS / resolución de nombres en redes Windows.
- **Comando de ejemplo:** `nbtscan -v 10.0.0.0/24`
- **Notas útiles:** Export `hosts/nbtscan.csv`; útil para correlacionar nombres de equipo con IPs.
- **Recomendaciones:** Combinar con arp-scan para tener MAC + nombre NetBIOS.
- **Cuándo usarlo:** Entornos mixtos con Windows o Active Directory en laboratorio.
- **Cuándo no:** Redes donde NetBIOS está deshabilitado o bloqueado por firewall.

### fping
- **Enlace:** https://fping.org/
- **Caso de uso:** Ping sweep masivo para validar disponibilidad de hosts.
- **Comando de ejemplo:** `fping -a -g 10.0.1.0/24`
- **Notas útiles:** `-a` muestra solo los vivos; redirige a fichero para inventario rápido.
- **Recomendaciones:** Ajusta el timeout con `-t` si la red tiene latencia alta.
- **Cuándo usarlo:** Validación rápida de qué hosts responden antes de un escaneo de puertos.
- **Cuándo no:** Si ICMP está bloqueado globalmente; combinar con hping3 en ese caso.

### hping3
- **Enlace:** https://github.com/antirez/hping
- **Caso de uso:** Crafting TCP/UDP/ICMP para probar filtros y firewalls.
- **Comando de ejemplo:** `hping3 --syn -p 443 10.0.0.1`
- **Notas útiles:** Prueba filtros con SYN en puertos específicos; documenta respuestas (RST, timeout).
- **Recomendaciones:** Usa con cuidado en entornos monitorizados; genera tráfico anómalo fácilmente detectable.
- **Cuándo usarlo:** Cuando ICMP está bloqueado y necesitas confirmar si un host está vivo vía TCP/UDP.
- **Cuándo no:** En producción sin autorización explícita; cada paquete crafteado es potencialmente alerta.

### masscan (ping)
- **Enlace:** https://github.com/robertdavidgraham/masscan
- **Caso de uso:** Ping sweep a gran escala sobre rangos amplios.
- **Comando de ejemplo:** `masscan --ping-only 10.0.0.0/24`
- **Notas útiles:** Ajusta `--rate` para no saturar la red; guarda resultados con `-oJ`.
- **Recomendaciones:** Limitar siempre el rate en laboratorio; comparar con resultado de arp-scan.
- **Cuándo usarlo:** Redes grandes donde fping tarda demasiado.
- **Cuándo no:** En redes donde el flood ICMP puede causar problemas o levantar alertas IDS.

### ZMap (ICMP)
- **Enlace:** https://github.com/zmap/zmap
- **Caso de uso:** Escaneo ICMP de alta velocidad sobre subredes grandes.
- **Comando de ejemplo:** `zmap -p 0 10.0.0.0/16 --probe-module=icmp_echoscan`
- **Notas útiles:** Documenta rangos y proxies usados; exporta con `--output-file`.
- **Recomendaciones:** Úsalo solo en laboratorio o con permiso explícito; es extremadamente rápido.
- **Cuándo usarlo:** Discovery a escala de /16 o mayor donde masscan con ping es insuficiente.
- **Cuándo no:** Redes de producción o entornos sensibles; su velocidad puede saturar switches.

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
