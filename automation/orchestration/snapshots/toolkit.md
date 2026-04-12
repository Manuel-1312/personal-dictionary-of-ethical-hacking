# Toolkit - Snapshots 💾

Referencia rápida de cómo creo snapshots para cada laboratorio: herramienta, comando y qué guardo en `snapshots/`.

## Plantilla base
- **Enlace:** referencia oficial de la herramienta.
- **Caso de uso:** qué tipo de snapshot o imagen crea (VM, contenedor, box, imagen).
- **Comando de ejemplo:** comando de creación de snapshot.
- **Notas útiles:** dónde se guarda y qué metadatos anotar.
- **Recomendaciones:** convención de nombres y gestión de almacenamiento.
- **Cuándo usar / cuándo no:** siempre antes de cambios significativos en el lab; limpia snapshots antiguos regularmente.

## 1. Herramientas de snapshots

### VirtualBox
- **Enlace:** https://www.virtualbox.org/
- **Caso de uso:** Snapshots de VMs completas para guardar estados del laboratorio antes de pruebas destructivas.
- **Comando de ejemplo:** `VBoxManage snapshot lab-base take pre-web --description "Estado antes de test web"`
- **Notas útiles:** Guarda la descripción del snapshot en `snapshots/notes.md` con fecha y propósito.
- **Recomendaciones:** Usa nombres descriptivos con prefijo de fecha (`YYYYMMDD-pre-<fase>`); documenta el estado del lab en `snapshots/notes.md`.
- **Cuándo usarlo:** Antes de cualquier fase de explotación o cambio de configuración significativo en VMs de VirtualBox.
- **Cuándo no:** Como única estrategia de backup; los snapshots de VirtualBox crecen rápido y degradan el rendimiento.

### VMware Workstation
- **Enlace:** https://www.vmware.com/
- **Caso de uso:** Snapshots de VMs Windows para preservar estados intermedios del laboratorio.
- **Comando de ejemplo:** `vmrun snapshot "path/to/lab-win.vmx" pre-scan`
- **Notas útiles:** Anota el estado de los agentes (AV, EDR) en `snapshots/vmware/` al momento del snapshot.
- **Recomendaciones:** Documenta qué agentes/herramientas estaban activos en el momento del snapshot; usa nombres consistentes.
- **Cuándo usarlo:** Antes de pruebas en VMs Windows donde necesitas poder revertir rápidamente.
- **Cuándo no:** Con demasiados snapshots encadenados; más de 3-4 snapshots por VM degradan el rendimiento.

### Docker
- **Enlace:** https://www.docker.com/
- **Caso de uso:** Snapshots de contenedores mediante commit e imágenes exportadas para reproducibilidad.
- **Comando de ejemplo:** `docker commit lab-web lab-web:v1 && docker save lab-web:v1 -o snapshots/docker/lab-web.tar`
- **Notas útiles:** Guarda el `.tar` en `snapshots/docker/` para poder restaurar sin necesidad de reconstruir.
- **Recomendaciones:** Etiqueta las imágenes con versión semántica y fecha (`lab-web:v1-20260101`); documenta los cambios en un CHANGELOG del lab.
- **Cuándo usarlo:** Para preservar el estado de contenedores de laboratorio antes de pruebas que puedan modificar el sistema de archivos.
- **Cuándo no:** Para aplicaciones de producción; usa un registro de contenedores en lugar de archivos `.tar`.

### Vagrant
- **Enlace:** https://www.vagrantup.com/
- **Caso de uso:** Snapshots de boxes Vagrant para preservar estados del laboratorio con gestión de versiones integrada.
- **Comando de ejemplo:** `vagrant snapshot save lab before-scan`
- **Notas útiles:** Guarda el directorio `.vagrant/` en la carpeta del proyecto para preservar el estado de los snapshots.
- **Recomendaciones:** Usa nombres descriptivos para los snapshots; documenta en `Vagrantfile` qué estado representa cada uno.
- **Cuándo usarlo:** Para labs basados en Vagrant donde necesitas rollback rápido a un estado limpio conocido.
- **Cuándo no:** Para VMs con estado persistente importante fuera del Vagrantfile; usa VirtualBox/VMware en esos casos.

### Packer
- **Enlace:** https://www.packer.io/
- **Caso de uso:** Creación de imágenes base reproducibles para el laboratorio a partir de definiciones declarativas.
- **Comando de ejemplo:** `packer build lab.json`
- **Notas útiles:** Mantén los builds en `snapshots/packer/`; versiona el `lab.json` en Git para reproducibilidad total.
- **Recomendaciones:** Añade checksums a las imágenes generadas; documenta qué provisioners se usaron y qué instalan.
- **Cuándo usarlo:** Para crear imágenes base del laboratorio que necesitan ser reproducibles desde cero.
- **Cuándo no:** Para snapshots de estado intermedio; Packer es para construir imágenes base, no para preservar estados.

## 2. Flujos y documentación
- Crea un snapshot antes de cada fase del laboratorio con nombre `YYYYMMDD-pre-<fase>`.
- Documenta en `snapshots/notes.md` el propósito de cada snapshot y cómo revertir.
- Limpia snapshots antiguos regularmente para no degradar el rendimiento del hypervisor.
