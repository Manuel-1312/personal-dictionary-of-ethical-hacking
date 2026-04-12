# Toolkit - Contención 🧱

Registro de acciones que aplico para aislar un incidente y preservar evidencia.

## Plantilla base
- **Enlace:** referencia oficial de la herramienta.
- **Caso de uso:** qué acción de contención realiza (aislamiento, bloqueo, detención de proceso).
- **Comando de ejemplo:** comando o script de contención típico.
- **Notas útiles:** detalles de implementación y evidencia generada.
- **Recomendaciones:** cómo documentar y revertir la contención.
- **Cuándo usar / cuándo no:** solo con autorización; documenta el revert para restaurar el servicio.

## 1. Herramientas de contención

### Velociraptor
- **Enlace:** https://github.com/Velocidex/velociraptor
- **Caso de uso:** Aislamiento de procesos maliciosos en endpoints mediante queries VQL de terminación controlada.
- **Comando de ejemplo:** `SELECT * FROM execve(argv=["pkill", "-f", "malware_pattern"]) FROM scope()`
- **Notas útiles:** Query `processes{command_line =~ /evil/}` para pausar tareas y guarda `output.lock`.
- **Recomendaciones:** Verifica el proceso antes de detenerlo; guarda el listado de procesos antes y después de la acción.
- **Cuándo usarlo:** Para aislar procesos maliciosos de forma remota en endpoints con el agente instalado.
- **Cuándo no:** Sin confirmar que el proceso objetivo es realmente malicioso; un falso positivo puede tumbar servicios críticos.

### Sysinternals
- **Enlace:** https://learn.microsoft.com/en-us/sysinternals/
- **Caso de uso:** Terminación y suspensión de procesos sospechosos en Windows desde scripts de respuesta.
- **Comando de ejemplo:** `PsSuspend.exe <pid> && PsList.exe > process-snapshot.txt`
- **Notas útiles:** Uso `PsKill` y `PsSuspend` desde scripts para detener servicios sospechosos; guarda el output.
- **Recomendaciones:** Incluye `PsList` antes de detener para documentar el árbol de procesos; guarda el output en el caso.
- **Cuándo usarlo:** Para contención rápida en hosts Windows cuando necesitas detener un proceso específico.
- **Cuándo no:** Sin documentar el PID y el proceso; siempre verifica antes de ejecutar.

### Cisco ACL / pfSense
- **Enlace:** https://developer.cisco.com/
- **Caso de uso:** Segmentación de red mediante ACLs temporales para aislar VLANs o hosts comprometidos.
- **Comando de ejemplo:** `access-list 100 deny ip 192.168.10.0 0.0.0.255 any` (Cisco IOS)
- **Notas útiles:** Aplico ACL temporales que bloquean VLAN 10 y documento los comandos con timestamp.
- **Recomendaciones:** Documenta exactamente qué ACL se aplicó, en qué interfaz y a qué hora; planifica el revert antes de aplicar.
- **Cuándo usarlo:** Para aislar segmentos de red afectados cuando el compromiso puede propagarse lateralmente.
- **Cuándo no:** Sin coordinación con el equipo de red; una ACL mal aplicada puede causar una interrupción de servicio mayor.

### CrowdStrike Falcon
- **Enlace:** https://www.crowdstrike.com/
- **Caso de uso:** Contención de endpoint mediante aislamiento de red desde la consola de Falcon.
- **Comando de ejemplo:** Falcon Console → Hosts → selecciona host → Network Containment → Contain.
- **Notas útiles:** Capturo eventos de host y documento qué sensores se activaron antes y después de la contención.
- **Recomendaciones:** Documenta el estado del sensor (versión, política) en el momento de la contención; anota qué host se aisló y por qué.
- **Cuándo usarlo:** Para aislar endpoints de forma inmediata cuando el agente Falcon está desplegado.
- **Cuándo no:** Si el host tiene servicios críticos sin alternativa; coordina con el propietario del sistema antes.

### Firewall scripts
- **Enlace:** (tus scripts locales)
- **Caso de uso:** Aplicación de reglas ACL temporales mediante scripts para bloquear IPs o puertos específicos.
- **Comando de ejemplo:** `bash firewall-contain.sh <IP-maliciosa> <case-id>`
- **Notas útiles:** `firewall-contain.sh` añade reglas y las elimina automáticamente al cerrar el caso.
- **Recomendaciones:** El script debe incluir un mecanismo de revert automático; versiona los scripts en `defense/incident_response/scripts/`.
- **Cuándo usarlo:** Para bloqueos rápidos de IPs o puertos cuando no tienes acceso directo a la consola del firewall.
- **Cuándo no:** Sin probar el script en lab primero; un error en producción puede bloquear tráfico legítimo.

### Playbooks
- **Enlace:** (tu playbook local)
- **Caso de uso:** Checklist estructurado de pasos de contención con verificación y procedimiento de revert.
- **Comando de ejemplo:** Consulta `playbooks/containment.md` → sigue los pasos en orden → marca cada paso completado.
- **Notas útiles:** `playbooks/containment.md` describe pasos y verificación de revert; actualiza tras cada incidente.
- **Recomendaciones:** Revisa y actualiza el playbook después de cada incidente con lecciones aprendidas.
- **Cuándo usarlo:** Siempre; un playbook reduce errores humanos y asegura que no se omiten pasos críticos.
- **Cuándo no:** No hay caso en el que no debas seguir un playbook; si no existe, créalo antes del próximo incidente.

## 2. Flujos y documentación
- Documenta cada acción de contención con timestamp, herramienta usada y resultado observado.
- Guarda el procedimiento de revert junto a cada acción; la restauración del servicio es parte del proceso.
- Coordina con el propietario del sistema antes de aplicar contenciones que puedan interrumpir servicios.
