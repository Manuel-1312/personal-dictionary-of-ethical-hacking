# Toolkit - Infraestructura 🏗️

Herramientas para mapear infraestructura pública; añaden detalles sobre IPs, DNS y certificados.

## Plantilla base
- **Enlace:** referencia oficial de la herramienta.
- **Caso de uso:** qué aspecto de la infraestructura mapea.
- **Comando de ejemplo:** comando o query típica.
- **Notas útiles:** qué registrar (filtros, banners, registros DNS).
- **Recomendaciones:** cómo organizar y exportar los datos.
- **Cuándo usar / cuándo no:** solo fuentes públicas; documenta cada consulta con fecha.

## 1. Herramientas de infraestructura pública

### Shodan CLI
- **Enlace:** https://help.shodan.io/the-shodan-command-line-client
- **Caso de uso:** Búsqueda de hosts y servicios expuestos mediante filtros avanzados (org, port, product).
- **Comando de ejemplo:** `shodan search 'org:"Example" port:22' --fields ip_str,port,org`
- **Notas útiles:** Registra filtros (org, port) y banners relevantes; exporta en JSON para reproducibilidad.
- **Recomendaciones:** Guarda las queries en un archivo de referencia; usa `shodan download` para exportar resultados grandes.
- **Cuándo usarlo:** Para identificar servicios expuestos y banners sin enviar paquetes al objetivo.
- **Cuándo no:** Como sustituto de un escaneo activo autorizado; los datos indexados pueden estar desactualizados.

### crt.sh
- **Enlace:** https://crt.sh/
- **Caso de uso:** Certificados TLS para descubrir subdominios y SAN sin contactar el objetivo.
- **Comando de ejemplo:** `curl -s 'https://crt.sh/?q=%.example.com&output=json' | jq '.[].name_value' | sort -u`
- **Notas útiles:** Documenta SAN y fechas; guarda capturas de pantalla si lo necesitas.
- **Recomendaciones:** Filtra duplicados y ordena por fecha para detectar cambios de infraestructura recientes.
- **Cuándo usarlo:** Siempre en la fase de reconocimiento pasivo para enumeración de subdominios.
- **Cuándo no:** Como única fuente; combina con DNS y Shodan para mayor cobertura.

### SecurityTrails
- **Enlace:** https://securitytrails.com/
- **Caso de uso:** DNS/WHOIS histórico y actual para mapear registros A/AAAA, MX y cambios de infraestructura.
- **Comando de ejemplo:** `curl -H 'APIKEY: <key>' 'https://api.securitytrails.com/v1/domain/example.com/dns/history/a'`
- **Notas útiles:** Guarda registros A/AAAA, MX y TTL usados; útil para detectar IPs históricas.
- **Recomendaciones:** Exporta en JSON y guarda en `osint/infrastructure/results/securitytrails/`; anota la fecha de consulta.
- **Cuándo usarlo:** Para ver el historial DNS y descubrir IPs anteriores que puedan estar activas.
- **Cuándo no:** Sin API key válida los datos son limitados; no almacenes información personal de terceros.

### PassiveTotal
- **Enlace:** https://www.riskiq.com/
- **Caso de uso:** Historial de infraestructura: IPs anteriores, cambios de resolución DNS y contexto de amenazas.
- **Comando de ejemplo:** `curl -u 'user:key' 'https://api.passivetotal.org/v2/dns/passive?query=example.com'`
- **Notas útiles:** Anota IPs detectadas anteriormente y cambios; útil para correlacionar con IOCs.
- **Recomendaciones:** Combina con SecurityTrails para cubrir más fuentes históricas; documenta los cambios con fechas.
- **Cuándo usarlo:** Cuando necesitas contexto histórico de una IP o dominio para una investigación.
- **Cuándo no:** Para datos en tiempo real; combina con Shodan para banners actuales.

### Censys
- **Enlace:** https://censys.io/
- **Caso de uso:** Búsqueda de hosts y certificados con queries avanzadas y exportación JSON.
- **Comando de ejemplo:** `censys search 'parsed.subject_dn: example.com' --index-type certificates`
- **Notas útiles:** Especifica queries y exporta JSON para reproducibilidad; cubre IPv4 e IPv6.
- **Recomendaciones:** Guarda la query exacta junto al resultado para que sea reproducible; exporta en JSON.
- **Cuándo usarlo:** Para profundizar en certificados y configuraciones TLS de hosts específicos.
- **Cuándo no:** Sin API key los resultados son muy limitados; no sustituye un escaneo activo autorizado.

### DNSDumpster
- **Enlace:** https://dnsdumpster.com/
- **Caso de uso:** Mapas de zona DNS con visualización de relaciones entre hosts y dominios.
- **Comando de ejemplo:** Consulta web en https://dnsdumpster.com/ con el dominio objetivo.
- **Notas útiles:** Captura mapas en PDF y destaca dependencias externas (CDN, MX providers).
- **Recomendaciones:** Exporta el mapa visual en PDF y el CSV de hosts para análisis offline.
- **Cuándo usarlo:** Para obtener una vista gráfica rápida de la estructura DNS de un dominio.
- **Cuándo no:** Como única fuente DNS; complementa con SecurityTrails y crt.sh para mayor profundidad.

## 2. Flujos y documentación
- Guarda cada resultado en `osint/infrastructure/results/<herramienta>-<fecha>/` con la query usada.
- Cruza IPs de Shodan/Censys con historial de SecurityTrails/PassiveTotal para validar hallazgos.
- Documenta dependencias externas (CDN, proveedores MX) detectadas en los mapas de zona.
