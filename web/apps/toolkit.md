# Toolkit - Apps Vulnerables 🧪

Documenta cada aplicación vulnerable, su stack y qué retos completaste en el laboratorio.

| Aplicación | Enlace | Categoría | Notas |
| --- | --- | --- | --- |
| OWASP Juice Shop | https://github.com/juice-shop/juice-shop | Node.js/Express | Mantén un `score.json` y restauraciones por container.
| WebGoat | https://github.com/WebGoat/WebGoat | Java/Spring | Documenta módulos completados y configuraciones de seguridad.
| DVWA | https://github.com/digininja/DVWA | PHP/MySQL | Usa niveles (`low/medium/high`) y guarda scripts de reset.
| Mutillidae II | https://github.com/webpwnized/mutillidae | PHP | Mantén scripts para restaurar DB y módulos explorados.
| OWASP Broken Web Apps | https://github.com/OWASP/OWASPBrokenWebApplications | Multi | Anota apps desplegadas y dependencias.
| Juice Shop CTF | https://owasp.org/www-project-juice-shop/ | Node.js | Documenta retos resueltos y vectores usados.

## Comandos utilizados
- `docker run -d --name juice-shop -p 3000:3000 bkimminich/juice-shop`.
- `docker-compose -f web/apps/webgoat-compose.yml up -d`.
- `python3 web/apps/reset-dvwa.py`.

## Técnicas aplicadas
- Restauración periódica de contenedores para evitar persistencias.
- Anotación de retos y payloads en `web/apps/notes.md`.

## Recomendaciones personales
- Mantén un archivo `web/apps/state.md` con la versión y lecciones pendientes.
- Incluye los comandos de despliegue para cada app en su README correspondiente.