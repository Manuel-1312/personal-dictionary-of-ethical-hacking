# Toolkit - Fun Scripts 🎈

Colección de scripts ligeros para decorar terminales, generar artefactos ficticios y añadir algo de humor al laboratorio.

## Plantilla de scripts
- **Subcategoría:** carpeta a la que pertenece.
- **Descripción:** qué hace el script.
- **Comando de ejemplo:** cómo lanzarlo.
- **Notas:** dependencias o advertencias clave.

## 1. Scripts disponibles

### `ascii_banner_maker.py`
- **Descripción:** Genera banners ASCII personalizados para notas o intros rápidas.
- **Comando de ejemplo:** `python fun-scripts/ascii_banner_maker.py --text "LAB 01"`
- **Notas:** Bueno para notas o intros rápidas.

### `ascii_box_text.py`
- **Descripción:** Mete texto dentro de una caja ASCII; muy bueno para notas y pantallas.
- **Comando de ejemplo:** `python fun-scripts/ascii_box_text.py --text "Objetivo: web-lab"`
- **Notas:** Muy bueno para notas y pantallas.

### `ascii_tree_generator.py`
- **Descripción:** Genera un árbol ASCII de altura configurable.
- **Comando de ejemplo:** `python fun-scripts/ascii_tree_generator.py --height 6`
- **Notas:** Completamente innecesario y por eso simpático.

### `ascii_separator_generator.py`
- **Descripción:** Crea separadores ASCII con o sin etiqueta de sección.
- **Comando de ejemplo:** `python fun-scripts/ascii_separator_generator.py --label "SESSION START"`
- **Notas:** Útil en terminal y documentación.

### `ascii_skull.py`
- **Descripción:** Imprime una calavera ASCII mínima.
- **Comando de ejemplo:** `python fun-scripts/ascii_skull.py`
- **Notas:** Cero utilidad, bastante encanto.

### `ascii_lab_card.py`
- **Descripción:** Genera una tarjeta ASCII para un lab o caso; ideal para abrir notas con estilo.
- **Comando de ejemplo:** `python fun-scripts/ascii_lab_card.py --title "LAB 07" --subtitle "AD Playground"`
- **Notas:** Ideal para abrir notas con estilo.

### `ascii_network_map.py`
- **Descripción:** Dibuja un mini flujo de nodos en ASCII para demos rápidas o notas.
- **Comando de ejemplo:** `python fun-scripts/ascii_network_map.py router kali juice-shop`
- **Notas:** Bueno para demos rápidas o notas.

### `ascii_progress_bar.py`
- **Descripción:** Genera barras de progreso ASCII con porcentaje configurable.
- **Comando de ejemplo:** `python fun-scripts/ascii_progress_bar.py --percent 73`
- **Notas:** Sencillo, útil y visual.

### `ascii_terminal_frame.py`
- **Descripción:** Enmarca texto como si fuera una terminal vieja.
- **Comando de ejemplo:** `python fun-scripts/ascii_terminal_frame.py --title shell --text "access granted"`
- **Notas:** Queda bastante aparente.

### `ascii_badge_maker.py`
- **Descripción:** Crea un badge ASCII simple con etiqueta izquierda y derecha.
- **Comando de ejemplo:** `python fun-scripts/ascii_badge_maker.py --left LAB --right ACTIVE`
- **Notas:** Va bien para títulos o estados.

### `lab_quote_generator.py`
- **Descripción:** Saca frases aleatorias de laboratorio con humor ligero y tono hacker/seguridad.
- **Comando de ejemplo:** `python fun-scripts/lab_quote_generator.py`
- **Notas:** Humor ligero con tono hacker/seguridad.

### `fake_breach_report.py`
- **Descripción:** Genera un informe ficticio de incidente; útil para practicar reporting.
- **Comando de ejemplo:** `python fun-scripts/fake_breach_report.py --company Acme --output report.md`
- **Notas:** Útil para practicar reporting.

### `terminal_glitch_text.py`
- **Descripción:** Convierte texto en estilo glitch para efecto visual terminalero.
- **Comando de ejemplo:** `python fun-scripts/terminal_glitch_text.py --text "ACCESS GRANTED"`
- **Notas:** Puro postureo terminalero.

### `random_codenames.py`
- **Descripción:** Genera nombres de operación aleatorios para labs o casos.
- **Comando de ejemplo:** `python fun-scripts/random_codenames.py --count 5`
- **Notas:** Sirve para labs o casos.

### `phishing_subject_ideas.py`
- **Descripción:** Genera asuntos ficticios de awareness para simulaciones internas.
- **Comando de ejemplo:** `python fun-scripts/phishing_subject_ideas.py --count 10`
- **Notas:** Solo para simulaciones internas.

### `password_wordlist_mixer.py`
- **Descripción:** Crea mini wordlists mezclando piezas base con años para labs controlados.
- **Comando de ejemplo:** `python fun-scripts/password_wordlist_mixer.py --base manu lab cyber --years 2024 2025`
- **Notas:** Útil para labs controlados.

### `red_team_excuse_generator.py`
- **Descripción:** Genera excusas absurdas de red team; humor interno.
- **Comando de ejemplo:** `python fun-scripts/red_team_excuse_generator.py`
- **Notas:** Humor interno.

### `log_noise_generator.py`
- **Descripción:** Genera logs falsos para practicar análisis y detección.
- **Comando de ejemplo:** `python fun-scripts/log_noise_generator.py --count 50 --output fake.log`
- **Notas:** Divertido y útil.

### `retro_matrix_printer.py`
- **Descripción:** Imprime una animación tipo matrix en la terminal.
- **Comando de ejemplo:** `python fun-scripts/retro_matrix_printer.py --seconds 5`
- **Notas:** Para demos y estética.

## 2. Flujos y documentación
- Todos los scripts son independientes y no requieren instalación adicional salvo indicación en el script.
- Si un script crece o añade dependencias, muévelo a `python/` y documéntalo en su toolkit.
- Guarda ejemplos de output interesantes en `fun-scripts/examples/` para referencia rápida.
