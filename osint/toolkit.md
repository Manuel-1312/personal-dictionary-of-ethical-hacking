# Toolkit - OSINT 🔎

Colección activa de herramientas OSINT para enriquecer inteligencia sobre dominios, personas e infraestructura. Cada entrada sigue una plantilla fija (enlace, caso de uso, comando, notas, recomendaciones, cuándo usar/no usar) y se documenta junto con flujos y límites legales.

## Plantilla OSINT
- **Enlace:** referencia oficial.
- **Caso de uso:** aporte al perfilado.
- **Comando de ejemplo:** instrucción lista para usar.
- **Notas útiles:** outputs, paths, validaciones.
- **Recomendaciones:** buenas prácticas y respeto legal.
- **Cuándo usar / cuándo no:** cuándo aporta valor y cuándo evitarla.

## 1. Descubrimiento de dominios, correos y metadatos

### theHarvester
- **Enlace:** https://github.com/laramies/theHarvester
- **Caso de uso:** recolectar emails, subdominios y metadatos desde motores y redes sociales.
- **Comando de ejemplo:** `theHarvester -d example.com -b all -l 100 -f outputs/osint/harvester-example.html`
- **Notas útiles:** convierto el HTML a CSV y guardo la fuente; los correos se validan luego con `hunter.io` cuando hay permiso.
- **Recomendaciones:** limita la profundidad a `-l 100` para evitar bloqueos.
- **Cuándo usarlo:** al comenzar la fase de perfilado.
- **Cuándo no:** si ya tienes un listado autorizado.

### Subfinder
- **Enlace:** https://github.com/projectdiscovery/subfinder
- **Caso de uso:** enumerar subdominios con APIs públicas y privadas.
- **Comando de ejemplo:** `subfinder -d example.com -o outputs/osint/subfinder.txt -silent`
- **Notas útiles:** elimino duplicados con `sort -u` y archivo en `osint/domains/subfinder-<fecha>.txt`.
- **Recomendaciones:** usa `-config recon/subfinder.yaml` para centralizar API keys.
- **Cuándo usarlo:** cuando necesitas cerrar vacíos que Amass no cubre.
- **Cuándo no:** dominios muy pequeños donde solo genera ruido.

### Assetfinder
- **Enlace:** https://github.com/tomnomnom/assetfinder
- **Caso de uso:** listas rápidas de subdominios desde certificados públicos.
- **Comando de ejemplo:** `assetfinder --subs-only example.com > outputs/osint/assetfinder.txt`
- **Notas útiles:** combino con `httpx` para validar vivos y archivo en `osint/domains/assetfinder-<fecha>.txt`.
- **Recomendaciones:** úsalo al lado de Subfinder para una cobertura completa.
- **Cuándo usarlo:** tras TheHarvester para pasar a datos técnicos.
- **Cuándo no:** si necesitas solo correos (usa Hunter).

### dnsx
- **Enlace:** https://github.com/projectdiscovery/dnsx
- **Caso de uso:** validación masiva de registros DNS y conversión a IPs.
- **Comando de ejemplo:** `dnsx -l osint/domains/all.txt -a -aaaa -cname -ptr -o outputs/osint/dnsx-validation.txt`
- **Notas útiles:** filtro con `jq` por TTL y almaceno en `osint/dns-cache/`.
- **Recomendaciones:** evita `-mx` si solo buscas hosts.
- **Cuándo usarlo:** antes de escanear infraestructura.
- **Cuándo no:** cuando necesitas solo correos.

## 2. Correlación, visualización y automatización

### Recon-ng
- **Enlace:** https://github.com/lanmaster53/recon-ng
- **Caso de uso:** framework modular para combinar APIs y generar reportes.
- **Comando de ejemplo:** `recon-ng -r recon-ng/workspaces/example -m recon/domains-contacts -m recon/domains-hosts`
- **Notas útiles:** guardo workspaces en `osint/recon-ng/<target>.db` y exporto CSV para importarlos en TheHive o Maltego.
- **Recomendaciones:** define API keys en `recon-ng/api_keys.yml` y no las compartas.
- **Cuándo usarlo:** flujos estructurados con muchas fuentes.
- **Cuándo no:** búsquedas ad-hoc (usa curl o theHarvester).

### SpiderFoot
- **Enlace:** https://github.com/smicallef/spiderfoot
- **Caso de uso:** orquestación de recon pasivo con alertas.
- **Comando de ejemplo:** `sf.py -s example.com -m passive -o outputs/osint/spiderfoot-example.json`
- **Notas útiles:** exporto JSON/PDF a `reports/osint/spiderfoot/`.
- **Recomendaciones:** desactiva módulos con límites API (Shodan) si no hay cuota.
- **Cuándo usarlo:** para un informe integral.
- **Cuándo no:** cuando necesitas huella mínima.

### Maltego CE
- **Enlace:** https://www.maltego.com/
- **Caso de uso:** visualizar relaciones entre dominios, personas e infraestructuras.
- **Comando de ejemplo:** lanzo el transform `To Website [DNS]` y exporto a `outputs/osint/maltego-case01.mtz`.
- **Notas útiles:** guardo gráficos en `osint/maltego/` con notas sobre cada entidad.
- **Recomendaciones:** utiliza CE para pruebas y licencias premium para transforms avanzados.
- **Cuándo usarlo:** para presentaciones visuales.
- **Cuándo no:** en flujos 100 % automatizados.

## 3. Infraestructura, certificados y servicios expuestos

### crt.sh
- **Enlace:** https://crt.sh/
- **Caso de uso:** rastrear certificados TLS y detectar SAN.
- **Comando de ejemplo:** `curl "https://crt.sh/?q=%.example.com&output=json" > outputs/osint/crt-example.json`
- **Notas útiles:** extraigo `name_value` con `jq` y combino con Subfinder.
- **Recomendaciones:** conserva metadata (emisión, expiración) para detectar renovaciones sospechosas.
- **Cuándo usarlo:** footprinting y detección de dominios temporales.
- **Cuándo no:** redes internas sin certificados públicos.

### Censys
- **Enlace:** https://censys.io/
- **Caso de uso:** metadatos de servicios y comparativa de banners.
- **Comando de ejemplo:** `censys search --format json "services.service_name: HTTPS and parsed.extensions.subject_alt_name.dns: example.com"`
- **Notas útiles:** guardo los JSON en `reports/osint/censys-example.json`.
- **Recomendaciones:** combina con crt.sh para validar certificados.
- **Cuándo usarlo:** cuando el target está en IPv4 públicos.
- **Cuándo no:** si no hay conexión externa.

### Shodan
- **Enlace:** https://www.shodan.io/
- **Caso de uso:** enumerar hosts, banners y cambios.<br>
- **Comando de ejemplo:** `shodan search "org:Example Corp" --limit 50 --fields ip_str,port,product`
- **Notas útiles:** exporto `outputs/osint/shodan-example.csv` y lo comparo con escaneos internos.
- **Recomendaciones:** respeta limitaciones de tokens.
- **Cuándo usarlo:** detectar hosts nuevos.
- **Cuándo no:** objetivos sin exposición pública.

### SecurityTrails
- **Enlace:** https://securitytrails.com/
- **Caso de uso:** cambios históricos de infraestructura.
- **Comando de ejemplo:** `curl https://api.securitytrails.com/v1/history/bulk/example.com`
- **Notas útiles:** guardo la respuesta en `outputs/osint/securitytrails-domains.json`.
- **Recomendaciones:** respeta el uso responsable del token.
- **Cuándo usarlo:** análisis de evolución de infraestructura.
- **Cuándo no:** redes internas sin dominios públicos.

### SSLyze + wfuzz
- **Enlaces:** https://github.com/nabla-c0d3/sslyze / https://github.com/xmendez/wfuzz
- **Caso de uso:** comprobar TLS y potenciales vectores para `nuclei` o `testssl`.
- **Comando de ejemplo:** `sslyze --regular example.com:443 --json_out=outputs/osint/sslyze-example.json`
- **Notas útiles:** exporto `reports/osint/tls-profile.md` y priorizo `nuclei`/`testssl`.
- **Recomendaciones:** usa los hallazgos para dirigir escaneos.
- **Cuándo usarlo:** cuando analizas un dominio externo.
- **Cuándo no:** hosts sin TLS.

## 4. Personas y redes sociales

### LinkedInt (scripts)
- **Enlace:** https://github.com/tomnomnom/linkedin
- **Caso de uso:** rastrear perfiles públicos y relaciones.
- **Comando de ejemplo:** `python linkedin-scraper.py --company example --output outputs/osint/linkedin-example.csv`
- **Notas útiles:** correlaciono con `Hunter` y guardo en `osint/people/`.
- **Recomendaciones:** respeta políticas y usa proxies.
- **Cuándo usarlo:** antes de campañas de ingeniería social.
- **Cuándo no:** sin autorización para recolectar datos personales.

### Hunter.io
- **Enlace:** https://hunter.io/
- **Caso de uso:** validar emails y detectar patrones.
- **Comando de ejemplo:** `hunter domain-search example.com --format json > outputs/osint/hunter-emails.json`
- **Notas útiles:** paso salidas a `email-permutator` y las documento en `reports/osint/correspondence.md`.
- **Recomendaciones:** anota la tasa de verificación (`score >= 0.8`).
- **Cuándo usarlo:** cuando necesitas validar contactos antes de enviar un correo simulado.
- **Cuándo no:** si el alcance no incluye personas.

### EmailPermutator
- **Enlace:** https://github.com/stephenhutchings/email-permutator
- **Caso de uso:** generar combinaciones de emails.
- **Comando de ejemplo:** `python email-permutator.py example.com > outputs/osint/email-permutations.txt`
- **Notas útiles:** compara con Hunter y documenta patrones.
- **Recomendaciones:** usa reglas para evitar variaciones inválidas.
- **Cuándo usarlo:** cuando preparas campañas de phishing controlado.
- **Cuándo no:** si no tienes permiso para contactar personas.

## 5. Flujos y documentación
- Coordina `osint/targets/README.md` con comandos usados y fase de cada herramienta.
- Todos los outputs van a carpetas fechadas y se enlazan desde `reports/osint/index.md`.
- Usa `scripts/osint/merge-reports.py` para combinar CSV/JSON en dashboards (`osint/scripts/README.md`).
- Mantén `tracking.md` con fuente original, fecha y limitaciones legales. 
- Documenta los tokens/API en `osint/keys.yaml` y no los subas al repositorio.
