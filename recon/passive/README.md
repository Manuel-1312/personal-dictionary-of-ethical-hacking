# Reconocimiento Pasivo

Recopila datos sin interactuar directamente con el objetivo: registros DNS públicos, redes sociales, metadatos en certificados. Usa herramientas OSINT y documenta las fuentes y licencias de cada dato.

## Comandos utilizados
- `amass enum -d example.lab -passive`.
- `theHarvester -d example.lab -b google -l 200`.

## Técnicas aplicadas
- Recolección pasiva con APIs públicas antes de tocar el target.
- Exportación a CSV para comparar con resultados activos.

## Recomendaciones personales
- Mantén las fuentes publicadas y toma screenshots de cada consulta.
- Documenta los TOS revisados antes de usar un servicio.
