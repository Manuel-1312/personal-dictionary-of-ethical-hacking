# Toolkit - OSINT 🔎

Colección activa de técnicas y herramientas para enriquecer la inteligencia de fuentes abiertas. Cada herramienta incluye enlace, caso de uso, comando de ejemplo y notas para saber cuándo aporta valor y cuándo deja de ser útil.

## 1. Descubrimiento de dominios, correos y metadatos

### theHarvester
- **Enlace:** https://github.com/laramies/theHarvester
- **Caso de uso:** recolectar correos electrónicos, subdominios y metadatos públicos a partir de motores de búsqueda y redes sociales.
- **Comando de ejemplo:** `theHarvester -d example.com -b all -l 100 -f outputs/osint/harvester-example.html`
- **Notas útiles:** convierto el HTML en CSV con `harvester_to_csv.py` y guardo la fuente original; los correos se validan luego con `hunter.io` (solo si tengo permiso).
- **Recomendaciones:** limita la profundidad (`-l 100`) para evitar bloqueos y registra el user-agent en `osint/headers/harvester-ua.txt`.
- **Cuándo usarlo:** al arrancar la fase de perfilado de la empresa o de empleados.
- **Cuándo no:** si ya tienes un listado autorizado y no quieres generar ruido con requests adicionales.

### Subfinder + Assetfinder
- **Enlace:** https://github.com/projectdiscovery/subfinder / https://github.com/tomnomnom/assetfinder
- **Caso de uso:** enumeración rápida y cruzada de subdominios mediante APIs públicas y certificados.
- **Comando de ejemplo:** `subfinder -d example.com -o outputs/osint/subfinder.txt && assetfinder --subs-only example.com > outputs/osint/assetfinder.txt`
- **Notas útiles:** combino las listas y elimino duplicados con `sort -u` y luego paso el master a `httpx`.
- **Recomendaciones:** guarda las versiones con fecha en `osint/domains/` y añade la fuente (`subfinder`, `assetfinder`).
- **Cuándo usarlo:** luego de `theHarvester`, para tener una visión más técnica del espacio atacante.
- **Cuándo no:** cuando solo necesitas dominios internos sin exposición pública.

### dnsx
- **Enlace:** https://github.com/projectdiscovery/dnsx
- **Caso de uso:** validación de dominios y extracción de registros DNS (A, AAAA, CNAME, TXT, PTR) en lote.
- **Comando de ejemplo:** `dnsx -l osint/domains/all.txt -a -aaaa -cname -ptr -o outputs/osint/dnsx-validation.txt`
- **Notas útiles:** uso `-json` y luego filtro por TTL con `jq` para identificar activos recientes. Los resultados se almacenan en `osint/dns-cache/` para compararlos con exploraciones futuras.
- **Recomendaciones:** evita agregar `-mx` si tu objetivo es solo host discovery; deja eso para una fase posterior con `mxlookup`.
- **Cuándo usarlo:** antes de lanzar escaneos de infraestructura.
- **Cuándo no:** si solo buscas correos y ya tienes la lista en un repositorio controlado.

## 2. Correlación, visualización y automatización

### Recon-ng
- **Enlace:** https://github.com/lanmaster53/recon-ng
- **Caso de uso:** framework modular para combinar APIs, generar reportes y exportar CSV/JSON.
- **Comando de ejemplo:** `recon-ng -r recon-ng/workspaces/example -m recon/domains-contacts -m recon/domains-hosts`
- **Notas útiles:** guardo los workspaces en `osint/recon-ng/<target>.db` y exporto los resultados con `export csv` para importarlos en `TheHive` o en `Maltego`.
- **Recomendaciones:** define las API keys en `recon-ng/api_keys.yml` y no las subas al repositorio.
- **Cuándo usarlo:** cuando necesitas un flujo estructurado para muchas fuentes.
- **Cuándo no:** para búsquedas ad-hoc rápidas (usa `curl` o `theHarvester`).

### SpiderFoot
- **Enlace:** https://github.com/smicallef/spiderfoot
- **Caso de uso:** orquestación de recon pasivo y escaneo continuo con alertas.
- **Comando de ejemplo:** `sf.py -s example.com -m passive -o outputs/osint/spiderfoot-example.json`
- **Notas útiles:** exporto el JSON y lo subo a `reports/osint/spiderfoot/` y uso la interfaz web para generar un PDF con los hallazgos.
- **Recomendaciones:** desactiva módulos con límite de API (como Shodan) si no tienes cuota suficiente.
- **Cuándo usarlo:** para un reporte integral de OSINT que combine dominios, correos, personas y metadatos.
- **Cuándo no:** si necesitas la mínima huella posible (prefiere `theHarvester`).

### Maltego CE
- **Enlace:** https://www.maltego.com/
- **Caso de uso:** visualización de relaciones (dominios, certificados, personas, infrastructure).
- **Comando de ejemplo:** en la GUI arranco un transform `To Website [DNS]` y exporto el gráfico a `outputs/osint/maltego-case01.mtz`
- **Notas útiles:** guardo los gráficos en la carpeta `osint/maltego/` y los acompaño con notas de cada entidad.
- **Recomendaciones:** usa la versión CE para pruebas y solicita licencias privadas si necesitas transforms premium.
- **Cuándo usarlo:** para presentaciones a clientes que valoran una visión gráfica.
- **Cuándo no:** para tareas 100 % automatizadas sin intervención humana.

## 3. Infraestructura, certificados y servicios expuestos

### crt.sh y Censys
- **Enlace:** https://crt.sh/ / https://censys.io/
- **Caso de uso:** trazado de certificados TLS y detección de nombres alternos.
- **Comando de ejemplo:** `curl "https://crt.sh/?q=%.example.com&output=json" > outputs/osint/crt-example.json` y luego `censys search --format json "services.service_name: HTTPS and parsed.extensions.subject_alt_name.dns: example.com"`
- **Notas útiles:** filtro el JSON con `jq -r '.[].name_value' | sort -u` y los combino con las listas de `Subfinder`.
- **Recomendaciones:** conserva la metadata del certificado ( emisión, expiración ) para detectar renewals sospechosos.
- **Cuándo usarlo:** en capacidades de footprinting y para detectar dominios temporales.
- **Cuándo no:** cuando el objetivo es una red interna privada sin certificados públicos.

### Shodan y SecurityTrails
- **Enlace:** https://www.shodan.io/ / https://securitytrails.com/
- **Caso de uso:** enumerar hosts, banners, servicios y cambios de infraestructura.
- **Comando de ejemplo:** `shodan search "org:Example Corp" --limit 50 --fields ip_str,port,product` + `curl https://api.securitytrails.com/v1/history/bulk/example.com`
- **Notas útiles:** guardo la salida en `outputs/osint/shodan-example.csv` y en `osint/securitytrails/domains.json` para tener histórica.
- **Recomendaciones:** respeta los límites y no automatices con tokens personales en scripts públicos.
- **Cuándo usarlo:** para detectar hosts nuevos y comparar con escaneos internos.
- **Cuándo no:** si el objetivo no aparece en IPv4 públicos (usa recon interno).

### SSLyze + wfuzz (analizar TLS)
- **Enlace:** https://github.com/nabla-c0d3/sslyze / https://github.com/xmendez/wfuzz
- **Caso de uso:** comprobar configuraciones TLS, cipher suites y fallback.
- **Comando de ejemplo:** `sslyze --regular example.com:443 --json_out=outputs/osint/sslyze-example.json`
- **Notas útiles:** exporto los hallazgos a `reports/osint/tls-profile.md` y decides si es un vector de recon (ciphers débiles, NPN obsoleto).
- **Recomendaciones:** los resultados me ayudan a priorizar `nuclei` y `testssl`.
- **Cuándo usarlo:** cuando verificas un dominio externo o detectas un cambio reciente en certificados.
- **Cuándo no:** si trabajas con hosts que no exponen TLS (usa `nmap` o `naabu` en su lugar).

## 4. Enfocado en personas y redes sociales

### LinkedInt (scripts + exportadores)
- **Enlace:** https://github.com/tomnomnom/linkedin
- **Caso de uso:** rastrear perfiles públicos, cargos y relaciones dentro de una empresa.
- **Comando de ejemplo:** `python linkedin-scraper.py --company example --output outputs/osint/linkedin-example.csv`
- **Notas útiles:** guardo los CSV en `osint/people/` y los correlaciono con `electrum`/`Hunter` para emails.
- **Recomendaciones:** respeta las políticas de la red y usa proxies dedicados para evitar bloqueos.
- **Cuándo usarlo:** cuando necesitas contexto humano para un pentest con ingeniería social.
- **Cuándo no:** si no tienes autorización para recolectar datos personales sensibles.

### Hunter.io + EmailPermutator
- **Enlace:** https://hunter.io/ / https://github.com/stephenhutchings/email-permutator
- **Caso de uso:** validar emails, descubrir patrones y prepararlos para campañas de phishing controlado.
- **Comando de ejemplo:** `hunter domain-search example.com --format json > outputs/osint/hunter-emails.json`
- **Notas útiles:** paso las salidas a `email-permutator` para generar combinaciones y las presento en `reports/osint/correspondence.md`.
- **Recomendaciones:** siempre anota la tasa de verificación (`score >= 0.8`) y guarda las fuentes.
- **Cuándo usarlo:** cuando necesitas validar contactos antes de enviar un correo simulado.
- **Cuándo no:** si el alcance del engagement no incluye personas (usa recon técnico en su lugar).

## 5. Flujos y documentación
- Coordino `osint/targets/README.md` con los comandos usados y el paso donde se empleó cada herramienta.
- Todos los outputs van a carpetas fechadas y se enlazan desde `reports/osint/index.md`.
- Uso `scripts/osint/merge-reports.py` para unificar CSV/JSON en dashboards (referencia en `osint/scripts/README.md`).
- Mantengo un `tracking.md` con la fuente original (nombre del portal, API, fecha) y las limitaciones legales asociadas.
