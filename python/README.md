# Python Tools

Esta carpeta colecciona tus scripts propios para acelerar tareas típicas de la biblioteca: parseo de logs, generación de reportes, wrappers para herramientas externas y pequeños helpers que complementan los toolkits.

Cada script tiene su mini README/nota, una breve descripción de qué hace, qué librerías necesita y qué salida produce. Por ahora incluyen:

- `log_parser.py`: parsea logs de Zeek/Suricata, extrae IPs + puertos y genera un CSV resumido.
- `inventory_builder.py`: combina salidas de `nmap`/`masscan` y las normaliza (próximamente, puedes añadir tu propia variante).

Haz `pip install -r python/requirements.txt` si los scripts lo requieren, y ejecuta los comandos listados en `toolkit.md` para ver resultados reproducibles.
