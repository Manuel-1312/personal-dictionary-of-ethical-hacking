# Toolkit - Orquestación 🧩

Cada fila corresponde a un script o playbook que ejecuté para montar el laboratorio. Anoto qué tareas encadené, qué variables usé y qué logs quedaron en `automation/orchestration/logs/`.

| Herramienta | Enlace | Rol | Notas reales |
| --- | --- | --- | --- |
| Ansible | https://www.ansible.com/ | Orquestación completa | `ansible-playbook -i hosts lab.yml`; guarda inventarios en `automation/orchestration/inventory/` y snapshots en `automation/orchestration/snapshots/`.
| PowerShell DSC | https://learn.microsoft.com/en-us/powershell/scripting/dsc/ | Configuración Windows | `Start-DscConfiguration -Path DSC` en los hosts Windows; adjunto el MOF y la salida `dsc.log`.
| Make / Invoke | https://www.gnu.org/software/make/ | Targets simples | `make lab-up` lanza `docker-compose up`; guardo el output en `automation/orchestration/logs/make-lab-up.log`.
| Bash / Python scripts | (local) | Pasos secuenciales | `scripts/run-scan.sh` lanza `nmap` + `zap` y copia los resultados a `automation/reporting/results/`.
| GitHub Actions | https://docs.github.com/actions | Validación | `ci.yml` lanza tests para asegurar que las plantillas siguen la estructura; guarda artefactos con logs.
