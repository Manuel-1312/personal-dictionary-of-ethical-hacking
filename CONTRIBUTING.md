# 🤝 Guía de Contribución

Gracias por interesarte en hacer crecer esta biblioteca ética. 🎉

> [!NOTE]
> Antes de empezar, lee este documento completo para entender cómo mantener la calidad y coherencia del proyecto.

---

## 📋 Antes de contribuir

1. Lee el [Código de Conducta](CODE_OF_CONDUCT.md) y asegúrate de que tu participación sigue esos valores.
2. Familiarízate con la estructura: cada carpeta tiene su propio `toolkit.md`
   y hay recursos centrales en `conceptos/`, `CHEAT_SHEETS.md` y `CHEAT_SHEETS_EXT.md`.
3. Revisa el [CATALOG.md](CATALOG.md) para ver el estado actual de cada sección y dónde hacen más falta aportes.

---

## 🔄 Flujo de trabajo

1. **Fork** del repositorio y crea una rama descriptiva (`feature/web-toolkit`, `fix/link-roto`, `docs/forensics-update`).
2. Haz tus cambios en la rama, manteniendo commits pequeños y descriptivos.
3. Abre un **Pull Request** usando la plantilla de [PULL_REQUEST_TEMPLATE.md](PULL_REQUEST_TEMPLATE.md).
4. Espera la revisión. El CI ejecutará MarkdownLint y link check automáticamente.

> [!TIP]
> Usa ramas con prefijos claros: `feature/`, `fix/`, `docs/` para facilitar la revisión.

---

## 📝 Tipos de contribución

### 📝 Documentación

- Mejora o amplía los `toolkit.md` de cada carpeta.
- Añade definiciones al [diccionario de conceptos](conceptos/diccionario.md).
- Actualiza los cheat sheets con comandos útiles que hayas probado.

### 🐍 Scripts (Python / PowerShell)

- Añade scripts en la subcarpeta correcta (`python/parsers/`, `powershell/network/`, etc.).
- Incluye docstring/comentario con descripción, uso y ejemplo.
- Actualiza `CHEAT_SHEETS.md` si el script es de uso frecuente.
- Mantén las dependencias al mínimo; si necesitas una nueva, documéntala en `DEPENDENCIES.md`.

### 🐛 Reportar problemas

- Usa las plantillas de issue: [bug report](.github/ISSUE_TEMPLATE/bug_report.md) o feature request.
- Incluye pasos para reproducir, resultado esperado y contexto.

---

## 📏 Estándares de formato

### Markdown

- Usa Markdown plano y evita tabulaciones para listas.
- Longitud máxima de línea: 160 caracteres (configurado en `.markdownlint.json`).
- Documenta cada carpeta nueva con `toolkit.md` o `README.md`.

### Scripts

- **Python**: sigue PEP 8, incluye docstring en el módulo y funciones principales, usa `argparse` para CLI.
- **PowerShell**: documenta parámetros, usa `Format-Table` o export a CSV/JSON para outputs.
- Añade comentarios que expliquen el *por qué*, no solo el *qué*.

---

## ✅ Verificaciones antes de enviar el PR

- [ ] Los enlaces Markdown funcionan correctamente.
- [ ] Los scripts se ejecutan sin errores en un entorno limpio.
- [ ] No hay secretos, credenciales ni comandos destructivos sin contexto.
- [ ] El contenido es evergreen y no depende de URLs temporales.
- [ ] Has actualizado los documentos relacionados (cheat sheets, toolkit, dependencies).

---

## 💬 Comunicación

- Si el cambio afecta varias carpetas (por ejemplo, modificaciones en `app/` o en la estructura), explica el impacto en el PR.
- Cita el issue relacionado y enlaza recursos (CVE, docs oficiales, guías OWASP) que respalden tu aporte.
- Sé claro, conciso y respetuoso en las discusiones.

---

Gracias por mantener este proyecto ético y bien organizado 💜
