# Toolkit - Reconocimiento 🧭

Catálogo de herramientas para mapear dominios, infraestructura y artefactos pasivos. Cada bloque tiene enlace, comandos reproducibles y notas de campo para explicar cuándo le aportó valor a una hipótesis concreta.

## 1. Descubrimiento de dominios y subdominios

### Amass
- **Enlace:** https://github.com/OWASP/Amass
- **Caso de uso:** cobertura exhaustiva de DNS públicos y privados mediante enumeración + inteligencia externa.
- **Comando de ejemplo:** `amass enum -d example.lab -config recon/amass.conf -ip -o outputs/recon/amass-example.json`
- **Notas útiles:** uso el archivo `recon/amass.conf` para combinar API keys (SecurityTrails, VirusTotal, etc.) y comparo el JSON con las salidas de `assetfinder`. También guardo los hosts nuevos en `recon/archive/amass-<fecha>.txt`.
- **Recomendaciones:** ejecuta primero con `-src` para ver la fuente de cada entry y decide si vale la pena investigar.
- **Cuándo usarlo:** al inicio de la fase de footprinting.
- **Cuándo no:** cuando quieres solo los hosts activos y ya tienes un listado limpio (usa `httpx` + `assetfinder` para eso).

### Assetfinder
- **Enlace:** https://github.com/tomnomnom/assetfinder
- **Caso de uso:** lista rápida de subdominios filtrados de certificados públicos.
- **Comando de ejemplo:** `assetfinder --subs-only example.lab > outputs/recon/assetfinder.txt`.
- **Notas útiles:** guardo los resultados en `recon/assetfinder/archive`, paso la lista a `httpx` y actualizo `recon/targets/live.txt`.
- **Recomendaciones:** combínalo con `dnsx` para validar resolución.
- **Cuándo usarlo:** después de `amass` para reptil. 
- **Cuándo no:** si necesitas insumos de pago como SecurityTrails en la misma pasada.

### Subfinder
- **Enlace:** https://github.com/projectdiscovery/subfinder
- **Caso de uso:** fuentes adicionales con API keys (Crowd, PassiveTotal, AlienVault) para cerrar huecos.
- **Comando de ejemplo:** `subfinder -d example.lab -o outputs/recon/subfinder.txt -silent`.
- **Notas útiles:** sincronizo con `subfinder -silent -d example.lab -config recon/subfinder.yaml` y lo guardo en `recon/subfig/`.
- **Recomendaciones:** útil para replicar hallazgos cuando `amass` no devuelve subdominios antiguos.
- **Cuándo usarlo:** en paralelo con `assetfinder`.
- **Cuándo no:** en entornos con pocos hosts, porque genera ruido sin valor.

## 2. Infraestructura y OSINT profundo

### dnsx
- **Enlace:** https://github.com/projectdiscovery/dnsx
- **Caso de uso:** validación masiva de DNS + conversión a IPs para posteriores escaneos.
- **Comando de ejemplo:** `dnsx -l recon/targets/all-domains.txt -a -ptr -resp -o reports/recon/dnsx.txt`.
- **Notas útiles:** guardo los resultados en JSON y uso `jq` para clasificar por TTL, respuesta y tipo de registro.
- **Recomendaciones:** aplica `-r` para reducir replicaciones en zonas wildcard antes de meter hosts a `naabu`.
- **Cuándo usarlo:** tras generar dominios con `Assetfinder/Subfinder`.
- **Cuándo no:** si necesitas solo hosts vivos (usa `httpx`).

### theHarvester
- **Enlace:** https://github.com/laramies/theHarvester
- **Caso de uso:** recolección de correos y subdominios desde fuentes como Google, LinkedIn y GitHub.
- **Comando de ejemplo:** `theHarvester -d example.lab -b all -l 100 -f outputs/recon/harvester.xml`
- **Notas útiles:** convierto el XML en CSV con `harvester-to-csv.py` y lo subo a la hoja `recon/osint`.
- **Recomendaciones:** limita la búsqueda (`-l 100`) para evitar bloqueos y aprovecha `-b searchsploit` para ver si aparecen exploits.
- **Cuándo usarlo:** cuando buscas perfiles de empleados o correos para campañas de ingeniería.
- **Cuándo no:** si requieres discovery exclusivamente técnico.

### SpiderFoot
- **Enlace:** https://github.com/smicallef/spiderfoot
- **Caso de uso:** correlación automatizada de múltiples fuentes y alertas en caso de nuevos indicadores.
- **Comando de ejemplo:** `sf.py -s example.lab -m passive -o outputs/recon/spiderfoot.json`
- **Notas útiles:** guardo las tareas en `recon/spiderfoot/jobs/` y uso el PDF export para documentar en `reports/osint/infraestructura.pdf`.
- **Recomendaciones:** personaliza los módulos para evitar que caiga en limitaciones de API (desactiva `shodan` si no tienes cuota).
- **Cuándo usarlo:** para generar un informe integral sin escribir scripts propios.
- **Cuándo no:** en redes muy internas donde no hay datos públicos.

### Gau + Waybackurls
- **Enlaces:** https://github.com/lc/gau / https://github.com/tomnomnom/waybackurls
- **Caso de uso:** colección de URLs históricas y actuales para entender el footprint web.
- **Comando de ejemplo:** `gau --json example.lab | jq -r '.url' > recon/urls/gau.txt` y `waybackurls example.lab > recon/urls/wayback.txt`.
- **Notas útiles:** limpio duplicados con `sort -u` y los paso a `ffuf`/`dirsearch`.
- **Recomendaciones:** combina gau+wayback con `httpx -silent` para priorizar URLs activas.
- **Cuándo usarlo:** cuando quieres ver versiones antiguas y endpoints desactualizados.
- **Cuándo no:** si sólo necesitas subdominios frescos.

### SecurityTrails / DNSDumpster
- **Enlaces:** https://securitytrails.com / https://dnsdumpster.com
- **Caso de uso:** mapas gráficos de infraestructura y certificados.
- **Comando de ejemplo:** descarga manual o `curl https://securitytrails.com/list/apidoc` (si hay API key).
- **Notas útiles:** guardo los mapas PDF en `reports/recon/dnsmap-<fecha>.pdf` y enlace las IPs con los resultados de `naabu`.
- **Recomendaciones:** descarga el mapa antes de hacer `naabu` para tener contexto de red.
- **Cuándo usarlo:** cuando necesitas evidenciar la arquitectura ante un cliente.
- **Cuándo no:** si la empresa no permite compartir ese nivel de detalle públicamente.

### Naabu
- **Enlace:** https://github.com/projectdiscovery/naabu
- **Caso de uso:** escaneo de puertos como preludio de `nmap`.
- **Comando de ejemplo:** `naabu -iL recon/targets/live.txt -o outputs/recon/naabu.txt -rate 1000`
- **Notas útiles:** `naabu` alimenta a `nmap` y `httpx` con puertos filtrados; guardo en `recon/naabu/last.txt` para comparar con exploraciones futuras.
- **Recomendaciones:** usa `-exclude-ports` con hosts que sabés que no quieres tocar.
- **Cuándo usarlo:** antes de un pentest interno para no disparar escaneos demasiado largos.
- **Cuándo no:** en assets públicos donde ya tienes autorización para `nmap` sin límites.

## Comandos y combinaciones habituales
- `assetfinder + subfinder + dnsx` → `httpx` (validar vivos) → `naabu` (descubrir puertos) → `nmap`.
- `theHarvester` + `SpiderFoot` → identifico activos humanos (correos, IP, metadata) y luego confirmo con `shodan`.
- `gau/waybackurls` → `ffuf`/`feroxbuster` para revalidar endpoints desactualizados.
- `SecurityTrails` + `amass` → comparo con la lista histórica guardada en `recon/history.csv`.

## Notas de documentación
- Mantengo `recon/targets/README.md` con la fecha del último escaneo y el script exacto utilizado.
- Todos los outputs van a `outputs/recon/<herramienta>/` y los enlazo desde `reports/recon/index.md`.
- Si uso APIs con límites, coloco el token en `~/.config/recon/apikeys.yaml` y lo referencio en la configuración de cada herramienta.
