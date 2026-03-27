# Toolkit - Contención 🧱

Registro de acciones que aplico para aislar un incidente y preservar evidencia.

| Herramienta | Enlace | Acción | Notas de implementación |
| --- | --- | --- | --- |
| Velociraptor | https://github.com/Velocidex/velociraptor | Aislamiento | Query `processes{command_line =~ /evil/}` para pausar tareas y guarda `output.lock`.
| Sysinternals | https://learn.microsoft.com/en-us/sysinternals/ | Kill / Ps | Uso `PsKill` y `PsSuspend` desde scripts para detener servicios sospechosos.
| Cisco ACL / pfSense | https://developer.cisco.com/ | Segmentación | Aplico ACL temporales que bloquean VLAN 10 y documento los comandos.
| CrowdStrike Falcon | https://www.crowdstrike.com/ | Contención endpoint | Capturo eventos de host y documenta qué sensores se activaron.
| Firewall scripts | (tus scripts) | ACL | `firewall-contain.sh` añade reglas y las elimina al cerrar el caso.
| Playbooks | (tu playbook) | Checklist | `playbooks/containment.md` describe pasos y verificación de revert.
