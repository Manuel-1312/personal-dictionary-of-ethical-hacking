# Toolkit - Recon Pasivo 🌍

Herramientas que solo consultan fuentes públicas; registra cada dato con fecha y URL.

## Plantilla base
- **Enlace:** referencia oficial de la herramienta.
- **Caso de uso:** qué fuente pública consulta y qué datos extrae.
- **Comando de ejemplo:** comando o URL de consulta típica.
- **Notas útiles:** qué registrar (fecha, fuente, formato).
- **Recomendaciones:** cómo organizar los resultados.
- **Cuándo usar / cuándo no:** solo fuentes públicas; nunca actives consultas directas al objetivo.

## 1. Fuentes públicas y OSINT pasivo

### Amass (passive)
- **Enlace:** https://github.com/OWASP/Amass
- **Caso de uso:** Footprinting DNS pasivo para descubrir subdominios sin contactar directamente el objetivo.
- **Comando de ejemplo:** `amass enum -passive -d example.com -o amass-passive.json`
- **Notas útiles:** Ejecuta con `-passive` y guarda JSON de subdominios.
- **Recomendaciones:** Complementa con otras fuentes (crt.sh, Shodan) para mayor cobertura; anota la fecha de ejecución.
- **Cuándo usarlo:** Fase inicial de reconocimiento para mapear la superficie de ataque sin alertar al objetivo.
- **Cuándo no:** Con `-active` en entornos no autorizados; el modo activo envía paquetes directamente.

### theHarvester
- **Enlace:** https://github.com/laramies/theHarvester
- **Caso de uso:** Recolección de correos electrónicos, nombres y subdominios desde múltiples fuentes públicas.
- **Comando de ejemplo:** `theHarvester -d example.com -b google,bing,linkedin -f results.html`
- **Notas útiles:** Usa múltiples APIs y documenta cada fuente consultada.
- **Recomendaciones:** Configura API keys para maximizar resultados; guarda el reporte HTML para evidencia.
- **Cuándo usarlo:** Cuando necesitas enumerar correos y subdominios en la fase de reconocimiento pasivo.
- **Cuándo no:** Sin configurar las API keys adecuadas; no usar en dominios ajenos sin autorización.

### SpiderFoot
- **Enlace:** https://github.com/smicallef/spiderfoot
- **Caso de uso:** Integración OSINT automatizada que agrega datos de decenas de fuentes públicas.
- **Comando de ejemplo:** `spiderfoot -s example.com -t INTERNET_NAME -o json -q`
- **Notas útiles:** Configura módulos pasivos con API keys; evita módulos activos en reconocimiento pasivo.
- **Recomendaciones:** Mantén un perfil de configuración con solo módulos pasivos habilitados; documenta qué módulos activaste.
- **Cuándo usarlo:** Cuando quieres una vista consolidada de múltiples fuentes OSINT en un solo workflow.
- **Cuándo no:** Con módulos activos habilitados o sin revisar qué datos están siendo consultados.

### Shodan (query)
- **Enlace:** https://www.shodan.io/
- **Caso de uso:** Búsqueda de servicios y dispositivos expuestos en internet mediante banners indexados.
- **Comando de ejemplo:** `shodan search 'org:"Example Corp" port:443'`
- **Notas útiles:** Exporta banners e indica los filtros usados (org, port, hostname, product).
- **Recomendaciones:** Guarda las queries en `recon/passive/queries/shodan.md`; exporta resultados en JSON para análisis.
- **Cuándo usarlo:** Para identificar servicios expuestos del objetivo sin enviar ningún paquete.
- **Cuándo no:** No reemplaza un escaneo activo autorizado; los datos pueden estar desactualizados.

### crt.sh
- **Enlace:** https://crt.sh/
- **Caso de uso:** Certificados TLS para descubrir subdominios mediante Subject Alternative Names (SAN).
- **Comando de ejemplo:** `curl -s 'https://crt.sh/?q=%.example.com&output=json' | jq '.[].name_value'`
- **Notas útiles:** Registra SAN y fechas de emisión; puede revelar subdominios internos expuestos por error.
- **Recomendaciones:** Filtra duplicados y ordena por fecha para identificar cambios recientes en la infraestructura.
- **Cuándo usarlo:** Siempre en la fase pasiva para complementar la enumeración de subdominios.
- **Cuándo no:** Como única fuente; combina con Amass y theHarvester para mayor cobertura.

## 2. Flujos y documentación
- Guarda cada resultado con fecha de ejecución en `recon/passive/results/<herramienta>-<fecha>.json`.
- Anota la URL o query exacta usada para que sea reproducible.
- Cruza subdominios de distintas fuentes para confirmar hallazgos antes de avanzar a reconocimiento activo.
