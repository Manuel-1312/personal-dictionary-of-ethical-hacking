# Toolkit - Reconocimiento 🧭

Catálogo estructurado de herramientas pasivas/activas. La plantilla que sigo por herramienta incluye enlace, caso de uso, comando reproducible, notas, recomendaciones y cuándo usar/no usar, para no perder contexto entre sesiones.

## Plantilla por herramienta
- **Enlace:** referencia oficial.
- **Caso de uso:** aporte concreto al ciclo de reconocimiento.
- **Comando de ejemplo:** instrucción lista para copiar.
- **Notas útiles:** outputs, directorios, comparaciones con otros escaneos.
- **Recomendaciones:** consejos basados en experiencias previas.
- **Cuándo usarlo / cuándo no:** límites del instrumento.

## 1. Descubrimiento de dominios y subdominios

### Amass
- **Enlace:** https://github.com/OWASP/Amass
- **Caso de uso:** cobertura exhaustiva de DNS públicos/privados usando enumeración e inteligencia externa.
- **Comando de ejemplo:** `amass enum -d example.lab -config recon/amass.conf -ip -o outputs/recon/amass-example.json`
- **Notas útiles:** combino `amass.conf` con APIs (SecurityTrails, VirusTotal) y almaceno hosts nuevos en `recon/archive/amass-<fecha>.txt`.
- **Recomendaciones:** empieza con `-src` para saber la fuente de cada entry.
- **Cuándo usarlo:** al iniciar footprinting.
- **Cuándo no:** cuando sólo necesitas hosts activos (usa `httpx`).

### Assetfinder
- **Enlace:** https://github.com/tomnomnom/assetfinder
- **Caso de uso:** lista rápida de subdominios desde certificados públicos.
- **Comando de ejemplo:** `assetfinder --subs-only example.lab > outputs/recon/assetfinder.txt`.
- **Notas útiles:** paso la lista a `httpx`, la guardo en `recon/assetfinder/archive` y la sincronizo con `Subfinder`.
- **Recomendaciones:** úsalos en conjunto para cubrir huecos.
- **Cuándo usarlo:** tras Amass para validar dominios recientes.
- **Cuándo no:** si necesitas datos históricos profundos (usa `SecurityTrails`).

### Subfinder
- **Enlace:** https://github.com/projectdiscovery/subfinder
- **Caso de uso:** fuentes adicionales con claves de pago para completar hosts antiguos.
- **Comando de ejemplo:** `subfinder -d example.lab -o outputs/recon/subfinder.txt -silent`
- **Notas útiles:** sincroniza la salida con `assetfinder` y archiva en `recon/subfinder/`.
- **Recomendaciones:** usa `-config recon/subfinder.yaml` para centralizar API keys.
- **Cuándo usarlo:** al cruzar datos privados (Crowdstrike, PassiveTotal).
- **Cuándo no:** en dominios pequeños donde agrega ruido.

## 2. Validación e infraestructura

### dnsx
- **Enlace:** https://github.com/projectdiscovery/dnsx
- **Caso de uso:** validación masiva de DNS/IPv4/AAAA/CNAME/TXT.
- **Comando de ejemplo:** `dnsx -l recon/targets/all-domains.txt -a -aaaa -cname -ptr -o reports/recon/dnsx.txt`
- **Notas útiles:** filtro con `jq` por TTL y guardo en `osint/dns-cache/` para comparativas.
- **Recomendaciones:** aplica `-r` para evitar wildcards antes de pasar a `naabu`.
- **Cuándo usarlo:** antes de escaneos de infraestructura.
- **Cuándo no:** si sólo buscas correos (usa `theHarvester`).

### theHarvester
- **Enlace:** https://github.com/laramies/theHarvester
- **Caso de uso:** recolectar emails, subdominios y metadatos desde motores y OSINT.
- **Comando de ejemplo:** `theHarvester -d example.lab -b all -l 100 -f outputs/recon/harvester-example.html`
- **Notas útiles:** convierto HTML a CSV y guardo la fuente; valido correos con Hunter (con permiso).
- **Recomendaciones:** limita `-l 100` para evitar bloqueos y registra el user-agent.
- **Cuándo usarlo:** fase de perfilado humano.
- **Cuándo no:** si ya tienes el listado autorizado.

### SpiderFoot
- **Enlace:** https://github.com/smicallef/spiderfoot
- **Caso de uso:** correlación automatizada de señales OSINT con alertas.
- **Comando de ejemplo:** `sf.py -s example.lab -m passive -o outputs/recon/spiderfoot-example.json`
- **Notas útiles:** exporto JSON a `reports/osint/spiderfoot/` y saco PDFs para stakeholders.
- **Recomendaciones:** desactiva módulos con límites de API si no tienes cuota (Shodan, Censys).
- **Cuándo usarlo:** para reportes integrales.
- **Cuándo no:** cuando sólo necesitas una búsqueda ligera.

### SecurityTrails / DNSDumpster
- **Enlaces:** https://securitytrails.com / https://dnsdumpster.com
- **Caso de uso:** mapas gráficos de infraestructura y certificados.
- **Comando de ejemplo:** descarga manual o `curl` a la API (según permisos) y guarda PDF en `reports/recon/dnsmap-<fecha>.pdf`.
- **Notas útiles:** enlaza IPs con los resultados de `naabu` y `nmap`.
- **Recomendaciones:** descarga mapas antes de escanear para entender la arquitectura.
- **Cuándo usarlo:** para evidenciar cobertura ante clientes.
- **Cuándo no:** si no puedes compartir ese nivel de detalle públicamente.

### Naabu
- **Enlace:** https://github.com/projectdiscovery/naabu
- **Caso de uso:** escaneo rápido de puertos antes de `nmap`.
- **Comando de ejemplo:** `naabu -iL recon/targets/live.txt -o outputs/recon/naabu.txt -rate 1000`
- **Notas útiles:** etiqueta IPs en `recon/naabu/last.txt` y las pasa a `nmap`.
- **Recomendaciones:** excluye puertos sensibles con `-exclude-ports`.
- **Cuándo usarlo:** justo antes de un pentest interno.
- **Cuándo no:** cuando ya hiciste un `RustScan` y quieres mantener baja la huella.

## 3. Recon activo y API de servicios

### Shodan CLI
- **Enlace:** https://help.shodan.io/the-shodan-command-line-client
- **Caso de uso:** confirmar servicios descubiertos y comparar banners.
- **Comando de ejemplo:** `shodan host 10.0.1.5` y guardo `outputs/recon/shodan-host10.0.1.5.json`.
- **Notas útiles:** agrego los servicios en `reports/recon/shodan-history.md`.
- **Recomendaciones:** usa campos `--fields` para reducir ruido.
- **Cuándo usarlo:** cuando el host ya está en Internet.
- **Cuándo no:** en redes privadas sin salida.

### SecurityTrails (API) + Censys
- **Caso de uso:** complementan el footprint gráfico con metadatos.
- **Comando de ejemplo:** `curl https://api.securitytrails.com/v1/history/bulk/example.com` y `censys search ...`.
- **Notas útiles:** guardo la metadata en `outputs/recon/securitytrails.json` y `reports/recon/censys.csv`.
- **Recomendaciones:** respetar límites y tokens en `recon/keys.yaml`.
- **Cuándo usarlo:** para historial de dominios.
- **Cuándo no:** en sandbox que no permiten conexión externa.

## 4. Flujos y documentación relacionada
- `assetfinder + subfinder + dnsx` → `httpx` → `naabu` → `nmap` → `vulscan` (compare con `reports/recon/flow.md`).
- `theHarvester` + `SpiderFoot` + `Shodan` → `reports/recon/people.md` para campañas de ingeniería.
- `SecurityTrails` + `amass` → archiva en `recon/history.csv` y actualiza `recon/targets/README.md`.
- Todos los outputs van a `outputs/recon/<herramienta>/` y se enlazan desde `reports/recon/index.md`.
