# Toolkit - Evasión 🕶️

Registra frameworks y técnicas que usas para comprender y documentar cómo se detectan acciones adversas.

## Plantilla base
- **Enlace:** referencia oficial.
- **Caso de uso:** propósito de la herramienta.
- **Comando de ejemplo:** comando representativo.
- **Notas útiles:** observaciones clave.
- **Recomendaciones:** consejos de uso.
- **Cuándo usar / cuándo no:** límites y contexto.

## 1. Simulación y frameworks

### Veil-Framework
- **Enlace:** https://github.com/Veil-Framework/Veil
- **Caso de uso:** Generación de payloads ofuscados para evasión de detección por firmas.
- **Comando de ejemplo:** `veil --list-payloads`
- **Notas útiles:** Compara detecciones de firmas antes y después de aplicar ofuscación con VirusTotal o sandbox local.
- **Recomendaciones:** Documenta siempre el hash del payload original y el ofuscado; anota qué AV lo detecta y cuál no.
- **Cuándo usarlo:** Laboratorio de análisis de detección por firmas para entender cómo los AV identifican amenazas.
- **Cuándo no:** Fuera del laboratorio controlado; estos payloads activan defensas reales y tienen implicaciones legales.

### MITRE CALDERA
- **Enlace:** https://github.com/mitre/caldera
- **Caso de uso:** Simulación de adversarios con técnicas ATT&CK automatizadas.
- **Comando de ejemplo:** `python server.py --insecure`
- **Notas útiles:** Documenta qué técnicas ATT&CK se emulan y cuál fue el impacto; mapea con el framework.
- **Recomendaciones:** Usa operaciones controladas y documenta cada fase; enlaza los resultados con las detecciones generadas.
- **Cuándo usarlo:** Emulación de adversarios para validar cobertura de detección en laboratorio.
- **Cuándo no:** Sin un equipo de detección o monitorización activa; la simulación pierde valor sin defender.

### Sliver
- **Enlace:** https://github.com/BishopFox/sliver
- **Caso de uso:** Framework C2 moderno con capacidades de evasión y persistencia.
- **Comando de ejemplo:** `sliver-server`
- **Notas útiles:** Guarda módulos usados y monitorea cómo se detecta la persistencia en el laboratorio.
- **Recomendaciones:** Documenta canales de comunicación usados (HTTP, DNS, mTLS) y las alertas generadas por cada uno.
- **Cuándo usarlo:** Laboratorio de C2 para estudiar detección de comunicaciones y persistencia.
- **Cuándo no:** Sin entorno de monitorización activa; el valor educativo requiere observar las detecciones.

### MITRE ATT&CK tools
- **Enlace:** https://github.com/mitre/mitre-attack
- **Caso de uso:** Navegación, mapeo y documentación de técnicas del framework ATT&CK.
- **Comando de ejemplo:** consultas en la matriz ATT&CK Navigator
- **Notas útiles:** Mapea cada experimento con la técnica del framework; mantén una capa Navigator por sesión.
- **Recomendaciones:** Guarda capas Navigator (.json) por laboratorio para documentar qué técnicas se cubrieron.
- **Cuándo usarlo:** Mapeo y documentación de técnicas adversarias en cualquier fase del laboratorio.
- **Cuándo no:** Como guía exclusiva de ataque; el framework es referencia, no prescripción.

### Empire
- **Enlace:** https://github.com/BC-SECURITY/Empire
- **Caso de uso:** Framework de post-explotación basado en PowerShell y Python.
- **Comando de ejemplo:** `python empire.py`
- **Notas útiles:** Registra scripts ejecutados y alertas generadas en el laboratorio; documenta listeners usados.
- **Recomendaciones:** Usa en entornos Windows de laboratorio aislados; documenta cada módulo y las detecciones activadas.
- **Cuándo usarlo:** Post-explotación en laboratorio Windows para estudiar detección de PowerShell ofuscado.
- **Cuándo no:** Sin monitorización activa de PowerShell; las alertas son el objetivo del ejercicio.

### Shellter
- **Enlace:** https://www.shellterproject.com/
- **Caso de uso:** Inyección y ofuscación de shellcode en binarios PE legítimos.
- **Comando de ejemplo:** `shellter` (interfaz interactiva)
- **Notas útiles:** Documenta hashes, firmas y cómo se comporta el antivirus ante el binario resultante.
- **Recomendaciones:** Registra antes y después de la inyección con hashes y resultados de sandbox; compara detecciones.
- **Cuándo usarlo:** Laboratorio de análisis de evasión de AV mediante inyección en binarios legítimos.
- **Cuándo no:** Binarios de producción o entornos sin sandbox controlado; el riesgo es elevado.

## 2. Flujos y documentación relacionada
- Enlaza cada experimento con una técnica ATT&CK concreta y documenta el resultado en `evasion/notes/`.
- Compara detecciones antes y después de cada técnica de ofuscación con sandbox local o VirusTotal.
- Mantén un registro de qué herramientas activan alertas en tu SIEM/EDR de laboratorio.
