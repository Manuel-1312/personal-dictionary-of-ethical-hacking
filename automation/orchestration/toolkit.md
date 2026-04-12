# Toolkit - Orquestación 🧩

Cada herramienta corresponde a un script o playbook que ejecuté para montar el laboratorio. Anoto qué tareas encadené, qué variables usé y qué logs quedaron en `automation/orchestration/logs/`.

## Plantilla base
- **Enlace:** referencia oficial de la herramienta.
- **Caso de uso:** qué rol cumple en la orquestación del laboratorio.
- **Comando de ejemplo:** comando típico con opciones relevantes.
- **Notas útiles:** qué inventarios, logs y artefactos genera.
- **Recomendaciones:** cómo organizar los archivos generados.
- **Cuándo usar / cuándo no:** documenta siempre el estado del lab antes y después de ejecutar.

## 1. Herramientas de orquestación

### Ansible
- **Enlace:** https://www.ansible.com/
- **Caso de uso:** Orquestación completa del laboratorio mediante playbooks declarativos idempotentes.
- **Comando de ejemplo:** `ansible-playbook -i automation/orchestration/inventory/hosts lab.yml`
- **Notas útiles:** Guarda inventarios en `automation/orchestration/inventory/` y snapshots en `automation/orchestration/snapshots/`.
- **Recomendaciones:** Versiona los playbooks en Git; usa `--check` para dry-run antes de aplicar cambios en el lab.
- **Cuándo usarlo:** Para provisionar y configurar múltiples VMs del laboratorio de forma reproducible.
- **Cuándo no:** Para tareas únicas de un solo host; un script Bash es más simple en esos casos.

### PowerShell DSC
- **Enlace:** https://learn.microsoft.com/en-us/powershell/scripting/dsc/
- **Caso de uso:** Configuración declarativa de hosts Windows del laboratorio mediante Desired State Configuration.
- **Comando de ejemplo:** `Start-DscConfiguration -Path DSC -Wait -Verbose`
- **Notas útiles:** Adjunta el MOF generado y la salida `dsc.log` en `automation/orchestration/logs/`.
- **Recomendaciones:** Guarda el MOF compilado junto al script DSC fuente; documenta las dependencias de módulos DSC usados.
- **Cuándo usarlo:** Para configurar hosts Windows del lab de forma declarativa y reproducible.
- **Cuándo no:** En hosts Linux; usa Ansible para gestión multiplataforma.

### Make / Invoke
- **Enlace:** https://www.gnu.org/software/make/
- **Caso de uso:** Targets simples para encadenar tareas del laboratorio (levantar lab, ejecutar scans, limpiar).
- **Comando de ejemplo:** `make lab-up`
- **Notas útiles:** `make lab-up` lanza `docker-compose up`; guarda el output en `automation/orchestration/logs/make-lab-up.log`.
- **Recomendaciones:** Define un target `make help` que liste todos los targets disponibles con su descripción.
- **Cuándo usarlo:** Para encadenar pasos comunes del lab de forma simple sin necesidad de recordar comandos complejos.
- **Cuándo no:** Para orquestación compleja con dependencias; usa Ansible para flujos más elaborados.

### Bash / Python scripts
- **Enlace:** (local)
- **Caso de uso:** Pasos secuenciales de automatización específicos del laboratorio que no justifican un playbook completo.
- **Comando de ejemplo:** `bash scripts/run-scan.sh`
- **Notas útiles:** `scripts/run-scan.sh` lanza `nmap` + `zap` y copia los resultados a `automation/reporting/results/`.
- **Recomendaciones:** Añade un encabezado con descripción, autor y fecha; usa `set -euo pipefail` en scripts Bash.
- **Cuándo usarlo:** Para automatizar pasos repetitivos simples que se ejecutan en secuencia fija.
- **Cuándo no:** Para flujos complejos con manejo de errores; en ese caso usa Ansible o Python estructurado.

### GitHub Actions
- **Enlace:** https://docs.github.com/actions
- **Caso de uso:** Validación automática de que las plantillas y scripts del repositorio siguen la estructura esperada.
- **Comando de ejemplo:** `gh workflow run ci.yml`
- **Notas útiles:** `ci.yml` lanza tests para asegurar que las plantillas siguen la estructura; guarda artefactos con logs.
- **Recomendaciones:** Guarda los artefactos de cada run como evidencia de las validaciones; añade un badge de estado al README.
- **Cuándo usarlo:** Para validación continua de la estructura del repositorio en cada push o PR.
- **Cuándo no:** Para tareas que requieren acceso a recursos del lab local; usa scripts locales en esos casos.

## 2. Flujos y documentación
- Guarda los logs de cada ejecución en `automation/orchestration/logs/<herramienta>-<fecha>.log`.
- Antes de ejecutar un playbook en el lab, crea un snapshot del estado actual.
- Documenta las variables de entorno y el inventario usado para que la ejecución sea reproducible.
