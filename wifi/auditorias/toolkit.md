# Toolkit - Auditorías WiFi 🔍

Documenta el flujo completo: escaneo, captura, análisis y mitigación durante una auditoría inalámbrica.

## Plantilla base
- **Enlace:** referencia oficial.
- **Caso de uso:** propósito de la herramienta.
- **Comando de ejemplo:** comando representativo.
- **Notas útiles:** observaciones clave.
- **Recomendaciones:** consejos de uso.
- **Cuándo usar / cuándo no:** límites y contexto.

## 1. Herramientas de auditoría

### airmon-ng
- **Enlace:** https://www.aircrack-ng.org/
- **Caso de uso:** Activación de modo monitor en interfaces inalámbricas.
- **Comando de ejemplo:** `airmon-ng start wlan0`
- **Notas útiles:** Activa monitor mode, documenta interfaces usadas y drivers; usa `airmon-ng check kill` para evitar conflictos.
- **Recomendaciones:** Verifica el driver con `airmon-ng` antes de iniciar; documenta la interfaz resultante (`wlan0mon`).
- **Cuándo usarlo:** Preparación de la interfaz antes de cualquier captura o inyección en laboratorio WiFi.
- **Cuándo no:** En interfaces que no soportan modo monitor; verifica compatibilidad del chipset primero.

### aireplay-ng
- **Enlace:** https://www.aircrack-ng.org/
- **Caso de uso:** Inyección de tramas: desautenticaciones, fake auth y ataques de replay.
- **Comando de ejemplo:** `aireplay-ng --deauth 10 -a <BSSID> wlan0mon`
- **Notas útiles:** Prueba desautenticaciones controladas y documenta la respuesta; úsalo solo en redes propias.
- **Recomendaciones:** Limita el número de paquetes con `--deauth N`; registra el resultado en `wifi/auditorias/logs/`.
- **Cuándo usarlo:** Forzar captura de handshake en laboratorio controlado para análisis de contraseña.
- **Cuándo no:** En redes ajenas o de producción; la desautenticación interrumpe conectividad de usuarios.

### reaver
- **Enlace:** https://github.com/t6x/reaver
- **Caso de uso:** Ataque de fuerza bruta al PIN WPS de puntos de acceso.
- **Comando de ejemplo:** `reaver -i wlan0mon -b <BSSID> -vv --no-nacks`
- **Notas útiles:** Solo en laboratorios con WPS habilitado; guarda tiempos y tasa de intentos por sesión.
- **Recomendaciones:** Usa `--no-nacks` para evitar bloqueos; documenta si el AP tiene rate limiting o lockout.
- **Cuándo usarlo:** Laboratorios con AP que tiene WPS habilitado para demostrar el riesgo del protocolo.
- **Cuándo no:** APs con WPS deshabilitado o con lockout activo; el ataque será inefectivo o causará bloqueo.

### bully
- **Enlace:** https://github.com/wiire-a/bully
- **Caso de uso:** Alternativa a reaver para bruteforce de WPS con mejor manejo de errores.
- **Comando de ejemplo:** `bully -b <BSSID> -c 6 --timeout 10`
- **Notas útiles:** Alternativa a reaver; registra handshake y compara detecciones entre ambas herramientas.
- **Recomendaciones:** Compara resultados con reaver en el mismo AP; documenta qué herramienta tiene mejor tasa de éxito.
- **Cuándo usarlo:** Cuando reaver falla o el AP responde mejor a la implementación de bully.
- **Cuándo no:** APs sin WPS o con protecciones anti-bruteforce; el resultado será el mismo que con reaver.

### wifite2
- **Enlace:** https://github.com/derv82/wifite2
- **Caso de uso:** Auditoría WiFi automatizada con secuencias de ataques configurables.
- **Comando de ejemplo:** `wifite --wpa --dict wordlists/rockyou.txt`
- **Notas útiles:** Usa secuencias de retries con logs; ideal para QA y documentación de sesiones completas.
- **Recomendaciones:** Revisa las opciones de targeting para no atacar redes fuera del alcance del laboratorio.
- **Cuándo usarlo:** Auditorías rápidas que cubren múltiples vectores (WPS, WPA handshake) en laboratorio.
- **Cuándo no:** Análisis manual detallado donde prefieres controlar cada paso de la auditoría.

### hostapd
- **Enlace:** https://w1.fi/hostapd/
- **Caso de uso:** Creación de puntos de acceso simulados para pruebas de detección y cliente.
- **Comando de ejemplo:** `hostapd /etc/hostapd/hostapd.conf`
- **Notas útiles:** Lanza redes falsas o simuladas para pruebas de detección; documenta la configuración usada.
- **Recomendaciones:** Usa en red aislada; documenta SSID, canal y tipo de autenticación de la red simulada.
- **Cuándo usarlo:** Simulación de redes maliciosas para pruebas de detección o validación de clientes.
- **Cuándo no:** Entornos con usuarios reales conectados; puede causar confusión o interrupciones.

## Comandos utilizados
- `aireplay-ng --deauth 10 -a <BSSID> wlan0mon`.
- `reaver -i wlan0mon -b <BSSID> -vv --no-nacks`.
- `bully -b <BSSID> -c 6 --timeout 10`.

## Técnicas aplicadas
- Automatización de bruteforce con wifite2 y logging de resultados.
- Comparativa de detecciones entre reaver y bully.

## Recomendaciones personales
- Documenta cómo revertir los cambios en la red y cuándo detener los ataques.
- Guarda logs en `wifi/auditorias/logs/` y resúmelos en `wifi/auditorias/reportes.md`.
