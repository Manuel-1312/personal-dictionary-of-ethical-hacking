# Guía de contribución

Gracias por ayudar a crecer esta biblioteca ética. Antes de comenzar:

1. Lee `CODE_OF_CONDUCT.md` y asegúrate de que tu participación siga esos valores.
2. Comprende la estructura básica: cada carpeta tiene su propio `toolkit.md`, y hay recursos específicos en `conceptos/`, `CHEAT_SHEETS.md` y `CHEAT_SHEETS_EXT.md`.
3. Trabaja sobre un fork, crea una rama descriptiva (`face2-contributing`, `feature/web-toolkit`, etc.) y empuja tus cambios ahí.

## Cómo contribuir

1. **Reporta problemas claros** usando `ISSUE_TEMPLATE/bug_report.md` o propone ideas con `ISSUE_TEMPLATE/feature_request.md`. Incluye pasos para reproducir o el valor esperado.
2. **Haz los cambios** en tu rama. Mantén un formato consistente (`toolkit`, documentación, scripts). Usa Markdown simple y explica cada término nuevo.
3. **Prepara un pull request** explicando qué hiciste y por qué. Usa `PULL_REQUEST_TEMPLATE.md` para cubrir checklist, pruebas (si hay) y dependencias.
4. **Incluye pruebas cuando sea viable**: si añades scripts, describe cómo ejecutarlos (por ejemplo `python create_conceptos.py`). Si modificas docs, revisa que los enlaces internos sean correctos y que los ressources referenciados existan.

## Estándares de formato

- Usa Markdown plano y evita tabulaciones para listas.
- Documenta cada carpeta con `toolkit.md` o `README.md` si introduces subdirectorios nuevos.
- Para scripts, agrega comentarios y actualiza `CHEAT_SHEETS.MD`/`CHEAT_SHEETS_EXT.MD` si es necesario.

## Verificaciones mínimas

- Revisa que los enlaces Markdown funcionen (por ejemplo, abre `README.md` y prueba los enlaces principales tras un cambio).
- Confirma que los archivos sea evergreen (no incluyas secretos ni comandos destructivos sin contexto).

## Comunicación

- Si el cambio requiere coordinación (por ejemplo modificaciones en `app/`, `vision`), deja un comentario en el PR explicando los pasos y el impacto en otras carpetas.
- Cita el issue relacionado (si existe) y vincula recursos (CVE, docs oficiales, guías OWASP) que respalden tus aportes.

Gracias por mantener este proyecto ético y bien organizado 💜
