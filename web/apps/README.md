# Aplicaciones Web Vulnerables

Esta carpeta contiene notas sobre aplicaciones que usas para practicar (Juice Shop, DVWA, WebGoat, OWASP Mutillidae). Añade scripts de despliegue, versiones y cómo restauras el estado antes/depués de cada sesión.

## Comandos utilizados
- `docker run -d --name juice-shop -p 3000:3000 bkimminich/juice-shop`.
- `docker-compose up webgoat` y luego `docker-compose down`.
- `python3 web/apps/reset-dvwa.py` para limpiar la base de datos.

## Técnicas aplicadas
- Uso de contenedores aislados y restauración completa tras cada sesión.
- Scripting de retos completados y payloads usados para reproducir fallos.

## Recomendaciones personales
- Mantén un archivo `web/apps/state.md` con la versión y lecciones pendientes.
- Anota los comandos de despliegue (`docker run`, `npm start`) para que otros puedan recrear el entorno exacto.
