# Toolkit - Recon Activo 🎯

Documenta cada herramienta que envía paquetes directamente al objetivo; anota autorización, criterios y resultados.

## Plantilla base
- **Enlace:** referencia oficial de la herramienta.
- **Caso de uso:** qué tipo de escaneo activo realiza.
- **Comando de ejemplo:** comando típico con opciones relevantes.
- **Notas útiles:** qué registrar (scripts, versiones, flags).
- **Recomendaciones:** cómo documentar los hallazgos.
- **Cuándo usar / cuándo no:** solo con autorización explícita; nunca en producción sin permiso.

## 1. Herramientas de escaneo activo

### nmap
- **Enlace:** https://nmap.org/
- **Caso de uso:** Escaneo TCP/UDP de puertos, detección de versiones y OS.
- **Comando de ejemplo:** `nmap -sV -sC -oN output.txt <target>`
- **Notas útiles:** Registra scripts NSE y versiones detectadas.
- **Recomendaciones:** Guarda siempre la salida con `-oN`/`-oX`; anota la versión de nmap usada.
- **Cuándo usarlo:** Cuando necesitas un inventario detallado de servicios en un rango de IPs autorizado.
- **Cuándo no:** En redes de producción sin ventana de mantenimiento o permiso escrito.

### Masscan
- **Enlace:** https://github.com/robertdavidgraham/masscan
- **Caso de uso:** Syn scan masivo para detectar IPs y puertos abiertos a alta velocidad.
- **Comando de ejemplo:** `masscan -p1-65535 <target> --rate=1000 -oL masscan.txt`
- **Notas útiles:** Usa para detectar IPs rápidamente; documenta `--rate`.
- **Recomendaciones:** Calibra `--rate` según el ancho de banda disponible para no saturar el enlace.
- **Cuándo usarlo:** Descubrimiento inicial de hosts activos en rangos grandes de red autorizada.
- **Cuándo no:** En redes con IDS sensibles o sin autorización; el volumen de paquetes es muy visible.

### RustScan
- **Enlace:** https://github.com/RustScan/RustScan
- **Caso de uso:** Escaneo rápido de puertos que luego delega en nmap para análisis profundo.
- **Comando de ejemplo:** `rustscan -a <target> -- -sV -sC`
- **Notas útiles:** Integra con nmap y guarda listas pulidas.
- **Recomendaciones:** Usa la bandera `--ulimit` para ajustar los descriptores de archivo y evitar falsos negativos.
- **Cuándo usarlo:** Cuando quieres velocidad de Masscan combinada con la profundidad de nmap.
- **Cuándo no:** En entornos donde la velocidad del escaneo puede disparar alertas de seguridad.

### Nmap NSE
- **Enlace:** https://nmap.org/book/nse.html
- **Caso de uso:** Scripts especiales para enumeración, detección de vulns y explotación controlada.
- **Comando de ejemplo:** `nmap --script=vuln,safe -p 80,443 <target>`
- **Notas útiles:** Detalla scripts usados y hallazgos; anota la categoría del script (safe, intrusive).
- **Recomendaciones:** Limita a categorías `safe` o `default` en el primer pase; guarda el output con `--script-trace` si necesitas debug.
- **Cuándo usarlo:** Después del escaneo de puertos inicial para profundizar en servicios específicos.
- **Cuándo no:** Scripts de categoría `exploit` o `brute` sin autorización explícita.

### nbtscan
- **Enlace:** https://github.com/gbin/nbtscan
- **Caso de uso:** Escáner NetBIOS para inventariar hosts Windows y nombres compartidos.
- **Comando de ejemplo:** `nbtscan -r 192.168.1.0/24`
- **Notas útiles:** Inventaria hosts Windows y nombres compartidos en la red local.
- **Recomendaciones:** Cruza resultados con nmap para confirmar hostnames; documenta nombres de dominio encontrados.
- **Cuándo usarlo:** En redes Windows para mapear recursos compartidos y nombres de equipo rápidamente.
- **Cuándo no:** En redes donde NetBIOS está bloqueado por política o fuera de rango autorizado.

### SNMPWalk
- **Enlace:** https://www.net-snmp.org/
- **Caso de uso:** Consulta SNMP para enumerar variables de configuración y estado de dispositivos.
- **Comando de ejemplo:** `snmpwalk -v2c -c public <target> 1.3.6.1.2.1`
- **Notas útiles:** Registra variables accesibles y contacta al propietario si encuentras community strings por defecto.
- **Recomendaciones:** Documenta la community string usada y los OIDs relevantes; exporta a texto para análisis posterior.
- **Cuándo usarlo:** Cuando dispositivos de red exponen SNMP y quieres enumerar su configuración en lab.
- **Cuándo no:** En producción sin coordinación con el equipo de red; una community string `public` accesible es ya un hallazgo.

## 2. Flujos y documentación
- Antes de ejecutar cualquier herramienta, confirma que tienes autorización escrita y anota el alcance.
- Guarda outputs en `recon/active/results/` con nombre `<herramienta>-<fecha>-<target>.txt`.
- Cruza los resultados de diferentes herramientas para validar hallazgos antes de documentarlos.
