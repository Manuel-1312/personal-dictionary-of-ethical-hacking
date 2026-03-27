# Snapshots

Aquí detallo mis snapshots: cuándo los tomo, qué nombre tienen y qué parte del laboratorio guardan. Por ejemplo, `VBoxManage snapshot lab-base take pre-web` captura el estado antes de instalar Juice Shop.

Apunto también qué snapshots RESTORE para volver al punto limpio (`VBoxManage snapshot lab-base restore pre-web`). Si uso Docker, documento `docker commit --change` + `docker save` en `automation/orchestration/snapshots/docker-save/`.

Guarda los scripts que deben ejecutarse antes/después del snapshot (`scripts/snapshot-cleanup.sh`) para no arrastrar configuraciones temporales.

## Comandos utilizados
- `VBoxManage snapshot lab-base take pre-web` antes del despliegue de servicios.
- `VBoxManage snapshot lab-base restore pre-web` para volver al estado base.
- `docker commit lab-web lab-web:clean && docker save lab-web:clean -o automation/orchestration/snapshots/docker/lab-web-clean.tar`.

## Técnicas aplicadas
- Etiquetado con fechas y etiquetas: `pre-web`, `post-scan`, etc.
- Uso de `scripts/snapshot-cleanup.sh` para eliminar logs temporales antes de tomar el snapshot.

## Recomendaciones personales
- Archiva los snapshots más importantes en `automation/orchestration/snapshots/notes.md` con una descripción breve.
- No guardes snapshots con secretos (cambia contraseñas o usa placeholders antes de tomar la imagen).
