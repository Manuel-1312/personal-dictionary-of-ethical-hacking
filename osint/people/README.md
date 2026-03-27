# OSINT - Personas

Aquí dejo archivos que explican cómo rastreo perfiles públicos de manera ética: las fuentes consultadas, los términos de uso y qué datos sí puedo guardar.

Cada carpeta tiene:
- Lista de consultas (Google Dorks, Twitter search, LinkedIn) y por qué se ejecutaron.
- Notas sobre qué filtré (solo información pública, sin credenciales ni datos sensibles).
- Capturas o JSON exportados que luego referencio en `lab-notes.md`.

Si ves un perfil en `osint/people/` y decides archivarlo, deja un comentario diciendo quién aprobó la sesión y por qué la información era relevante; eso evita malentendidos en el futuro.

## Comandos utilizados
- `maltego /import /path/to/pat.pat` y exporto el gráfico en `osint/people/maltego/20260327.png`.
- `python osint/scripts/google-dork.py "site:linkedin.com "Manuel"" -o outputs/osint/people/linkedin.json`.

## Técnicas aplicadas
- Análisis de relaciones con Maltego y enriquecimiento con APIs públicas.
- Google Dorking y exportes en CSV para mantener referencias.

## Recomendaciones personales
- Documenta qué términos de uso aplicaste y agrega la fecha de consulta.
- Mantén un registro de consentimientos o aprobaciones internas cuando lo requiera la política.