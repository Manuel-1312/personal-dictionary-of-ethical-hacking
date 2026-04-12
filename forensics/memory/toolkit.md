# Toolkit - Memoria 🧠

Documenta tus capturas y análisis de RAM; incluye versiones del sistema, scripts usados y hallazgos.

## Plantilla base
- **Enlace:** referencia oficial.
- **Caso de uso:** propósito de la herramienta.
- **Comando de ejemplo:** comando representativo.
- **Notas útiles:** observaciones clave.
- **Recomendaciones:** consejos de uso.
- **Cuándo usar / cuándo no:** límites y contexto.

## 1. Herramientas de captura y análisis de memoria

### LiME
- **Enlace:** https://github.com/504ensicsLabs/LiME
- **Caso de uso:** Captura de memoria RAM en sistemas Linux mediante módulo del kernel.
- **Comando de ejemplo:** `insmod lime-$(uname -r).ko "path=forensics/memory/mem-$(date +%Y%m%d).raw format=raw"`
- **Notas útiles:** Guarda offsets, rutas y el método de extracción; requiere compilar el módulo para el kernel objetivo.
- **Recomendaciones:** Compila LiME en un sistema idéntico al objetivo para evitar incompatibilidades de kernel.
- **Cuándo usarlo:** Captura forense de RAM en sistemas Linux en caliente con mínima alteración del estado.
- **Cuándo no:** Sistemas Windows; usa DumpIt o Magnet RAM Capture para esos entornos.

### DumpIt
- **Enlace:** https://www.moonsols.com/
- **Caso de uso:** Captura de memoria RAM en sistemas Windows con un solo ejecutable.
- **Comando de ejemplo:** `DumpIt.exe /OUTPUT mem-20260327.dmp`
- **Notas útiles:** Indica la versión del SO y si fue en caliente o en frío; portable y sin instalación.
- **Recomendaciones:** Ejecuta desde USB forense; documenta fecha, hora y estado del sistema al momento de la captura.
- **Cuándo usarlo:** Captura rápida de RAM en Windows durante respuesta a incidentes.
- **Cuándo no:** Sistemas Linux; usa LiME en esos casos.

### Volatility 3
- **Enlace:** https://github.com/volatilityfoundation/volatility3
- **Caso de uso:** Análisis forense de volcados de memoria con plugins específicos por SO.
- **Comando de ejemplo:** `volatility3 -f forensics/memory/mem-20260327.raw windows.pslist`
- **Notas útiles:** Lista plugins ejecutados y resultados clave (`pslist`, `malfind`, `netscan`); documentar todo.
- **Recomendaciones:** Ejecuta siempre `windows.info` o `linux.banner` primero para confirmar el perfil; guarda outputs por plugin.
- **Cuándo usarlo:** Análisis post-captura de procesos, conexiones, DLLs y artefactos de memoria.
- **Cuándo no:** Capturas de memoria sin el perfil correcto identificado; los resultados serán poco fiables.

### Rekall
- **Enlace:** https://github.com/google/rekall
- **Caso de uso:** Framework alternativo de análisis forense de memoria con soporte multiplataforma.
- **Comando de ejemplo:** `rekall -f forensics/memory/mem-20260327.raw pslist`
- **Notas útiles:** Usa para doble verificación y registra comparativas con Volatility 3.
- **Recomendaciones:** Úsalo como segunda opinión cuando Volatility produce resultados inesperados.
- **Cuándo usarlo:** Validación cruzada de hallazgos de Volatility 3 o cuando un plugin específico no existe en Volatility.
- **Cuándo no:** Como herramienta principal; el desarrollo de Rekall está menos activo que Volatility 3.

### Belkasoft RAM Capturer
- **Enlace:** https://belkasoft.com/
- **Caso de uso:** Captura de memoria RAM en Windows con soporte para sistemas protegidos.
- **Comando de ejemplo:** interfaz gráfica con selección de destino de captura
- **Notas útiles:** Documenta hash y contexto (por ejemplo UEFI/Legacy); soporta sistemas con protección de kernel.
- **Recomendaciones:** Verifica el hash de la captura inmediatamente; guarda el resultado en medio forense certificado.
- **Cuándo usarlo:** Sistemas Windows donde DumpIt falla por protecciones del kernel o antivirus.
- **Cuándo no:** Sistemas Linux; LiME es la opción adecuada para esos entornos.

### Magnet RAM Capture
- **Enlace:** https://www.magnetforensics.com/
- **Caso de uso:** Captura forense de RAM en Windows con interfaz sencilla y verificación de integridad.
- **Comando de ejemplo:** interfaz gráfica con exportación a archivo RAW
- **Notas útiles:** Guarda el archivo y documenta qué artefactos analizaste; incluye verificación de hash integrada.
- **Recomendaciones:** Exporta siempre con hash verificado; documenta el estado del sistema y procesos activos al capturar.
- **Cuándo usarlo:** Captura inicial rápida en Windows con verificación de integridad inmediata.
- **Cuándo no:** Sistemas Linux o cuando se necesita captura silenciosa sin interfaz gráfica.

## Comandos utilizados
- `insmod lime.ko "path=forensics/memory/mem-20260327.raw format=raw"`.
- `DumpIt.exe mem-20260327.dmp`.
- `volatility3 -f forensics/memory/mem-20260327.raw windows.pslist`.

## Técnicas aplicadas
- Use LiME para capturas en caliente de Linux y DumpIt para Windows.
- Corro Volatility y Rekall en paralelo para validar hallazgos.

## Recomendaciones personales
- Guarda hashes en `reports/forensics/memory-hashes.txt`.
- Documenta qué aviso o alerta motivó cada captura en `forensics/memory/cases/`.
