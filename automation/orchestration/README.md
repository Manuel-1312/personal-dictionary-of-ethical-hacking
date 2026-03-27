# Orquestación

Esta carpeta guarda los playbooks y scripts que coordinan mis laboratorios: desde levantar `kali-base` hasta ejecutar `nmap`/`zap` y limpiar los snapshots.

- `orchestration/playbooks/`: Ansible, PowerShell o Bash que preparo para automatizar despliegues. Ejemplo: `deploy-lab.yml` instala Kali, ZAP, Burp y actualiza el hosts de `lab.local`.
- `snapshots/`: detalles de cómo tomo snapshots (`VBoxManage snapshot lab-master take` o `docker commit`) y scripts que los restauran.
- `snapshots/README.md` explica cómo crear snapshots y qué etiquetas uso.

Cada vez que lanzo un playbook hago un `runlog` (por ejemplo `orchestration/logs/run-2026-03-27.log`) y lo enlazo desde aquí para que el siguiente que lo ejecute entienda qué variables cambió.

## Comandos utilizados
- `ansible-playbook -i automation/orchestration/inventory deploy-lab.yml` para desplegar el stack completo.
- `bash automation/orchestration/scripts/reset-env.sh` tras cada sesión para limpiar snapshots.

## Técnicas aplicadas
- Uso de inventarios por grupo (web, wifi, defense) y etiquetas para ejecutar roles selectivos.
- Captura de logs (`orchestration/logs/run-*.log`) para auditar qué hosts cambiaron.

## Recomendaciones personales
- Documenta en el mismo playbook qué variables dinámicas esperas (por ejemplo `target_host`).
- Guarda los runlogs y vincúlalos desde el README para facilidad de replicación.