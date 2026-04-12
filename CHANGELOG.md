# 📋 Changelog

Todos los cambios notables de este proyecto se documentan en este archivo. 📝

El formato sigue las convenciones de [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
Las versiones se organizan por *Faces* (fases) del proyecto. 🔖

## 🚧 [Sin versión] - En desarrollo

### ✅ Añadido

- **CHANGELOG.md**: registro formal de cambios del proyecto.
- **Tests unitarios** para los scripts Python (`tests/`): parsers, forensics, reporting y recon.
- **CI workflow mejorado**: paso de tests Python integrado en el pipeline de calidad.
- **Diccionario ampliado**: nuevos términos en `conceptos/diccionario.md` (Exfiltración, Pivoting, Lateral Movement, etc.).

### 🔄 Cambiado

- **README.md** reescrito: estructura más clara, ejemplos de uso, diagrama del repositorio y navegación rápida.
- **CONTRIBUTING.md** ampliado: flujo de trabajo detallado, estándares por tipo de contribución y checklist de verificación.
- **CI workflow** (`face3-quality.yml`): corregido el import roto de `markdown_it_py` → `markdown_it`, mejorada la extracción de enlaces y añadida deduplicación.
- **log_parser.py**: refactorizado para cumplir PEP 8 (espaciado, docstrings, constantes extraídas).
- **inventory_builder.py**: refactorizado con docstrings, tipado, PEP 8 y lógica de origen mejorada (detecta hosts presentes en ambas herramientas).
- **Comentarios humanizados** en scripts clave: explicaciones del *por qué* además del *qué*.

### 🐛 Corregido

- Import roto en el CI link-check (`import markdown_it_py` → `from markdown_it import MarkdownIt`).
- Extracción de enlaces en CI: ahora busca en tokens inline/children en vez de solo tokens raíz.
- `inventory_builder.py`: el campo Origin ahora detecta correctamente hosts encontrados por ambas herramientas (`both`).

## 🎯 [Face 4] - Anterior a este changelog

### ✅ Añadido

- Scripts de conversión: `masscan_to_csv.py`, `web_screenshot_manifest.py`, `csv_to_markdown_table.py`.
- `chain_of_custody_builder.py` para plantillas de cadena de custodia.
- Launcher de escritorio (`app/`) con GUI Tkinter.
- `CHEAT_SHEETS_EXT.md` como guía extendida.
- `COMMUNITY.md` con estrategia de difusión.
- Scripts fun: ASCII generators, fake breach reports, lab utilities.

### 🔄 Cambiado

- Organización de `python/` en subcategorías (`parsers/`, `web/`, `forensics/`, `recon/`, `reporting/`, `ad/`).
- PowerShell organizado en `system/`, `files/`, `network/`, `reporting/`, `fun/`.
- `exploitation/` expandido con subcategorías completas y plantillas.

## ⚙️ [Face 3] - Calidad automatizada

### ✅ Añadido

- GitHub Actions workflow (`face3-quality.yml`) con MarkdownLint y link check.
- `.markdownlint.json` con reglas de formato.
- `pcap_summary.py`, `evidence_indexer.py`, `ioc_enricher.py`.
- `SECURITY.md` con política de divulgación responsable.

## 📦 [Face 2] - Expansión de scripts

### ✅ Añadido

- Subcategorías de Python: `recon/`, `reporting/`, `ad/`.
- `subdomain_diff.py`, `nmap_xml_to_markdown.py`, `markdown_case_bundler.py`.
- `ad_notes_builder.py` para documentación de laboratorios AD.
- `python/ROADMAP.md` y `python/DEPENDENCIES.md`.

## 🏗️ [Face 1] - Estructura base

### ✅ Añadido

- Estructura inicial del repositorio con todas las carpetas principales.
- `README.md`, `CODE_OF_CONDUCT.md`, `LICENSE` (MIT).
- `conceptos/diccionario.md` con definiciones base.
- `CHEAT_SHEETS.md` con comandos por categoría.
- `CATALOG.md` como índice del proyecto.
- Toolkits (`toolkit.md`) en cada carpeta.

---

> [!TIP]
> Cada vez que hagas un cambio relevante, documéntalo aquí antes de hacer merge.
> Un changelog bien mantenido es la memoria del proyecto. 🧠
