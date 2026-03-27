# Automatización y Orquestación

Aquí guardo los scripts que me permiten reproducir un laboratorio: desde levantar VMs hasta lanzar escaneos y ensamblar reportes. Cada vez que lanzo un playbook (por ejemplo `ansible-playbook lab.yml`) incluyo en `automation/orchestration/` la salida `logs/` para que otros vean qué cambió.

- `orchestration/`: playbooks y scripts que arrancan/disponen entornos, aplican snapshots y preparan herramientas.
- `reporting/`: plantillas, scripts y ejemplos de dashboards que convierten datos crudos en informes legibles.

Si automatizas un pipeline, guarda aquí la descripción, el script y el resultado (`automation/reporting/results/`). También detalla qué partes ejecutas manualmente para evitar que alguien piense que todo el proceso es totalmente automático.

## Comandos utilizados
- `ansible-playbook -i automation/orchestration/inventory lab.yml --tags web` para desplegar Kali + Juice Shop.
- `bash automation/orchestration/scripts/deploy.sh && bash automation/orchestration/scripts/cleanup.sh` para controlar el ciclo.
- `python automation/reporting/scripts/render.py --template automation/reporting/templates/standard.md` para generar PDF.

## Técnicas aplicadas
- Uso de IDs de playbook en GitHub Actions para versionar y replicar cada ejecución.
- Snapshot + playbook: tomo snapshot antes del playbook y lo empleo después para resets rápidos.

## Recomendaciones personales
- Mantén comentarios dentro de los scripts para saber qué variables cambiaste la última vez.
- Guarda versiones de templates en `automation/reporting/templates/` y anota qué datos dinámicos reemplaza cada variable.