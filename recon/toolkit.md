# Toolkit - Reconocimiento 🧭

Lista herramientas de reconocimiento pasivo y activo con foco en trazabilidad: qué sacaste, de dónde vino y cómo se conecta luego con `network_scan/`, `web/` u `osint/`.

| Herramienta | Enlace | Tipo | Comando / uso típico | Nota de campo |
| --- | --- | --- | --- | --- |
| Amass | https://github.com/OWASP/Amass | DNS / attack surface | `amass enum -d example.lab -o outputs/recon/amass.txt` | Muy bueno para subdominios y relaciones; si el scope es grande, guarda config y seeds. |
| Sublist3r | https://github.com/aboul3la/Sublist3r | Subdominios | `sublist3r -d example.lab -o outputs/recon/sublist3r.txt` | Sencillo para una primera pasada rápida y comparar luego con Amass. |
| assetfinder | https://github.com/tomnomnom/assetfinder | Pasivo | `assetfinder --subs-only example.lab` | Ligero y rápido; ideal como fuente secundaria. |
| theHarvester | https://github.com/laramies/theHarvester | Correos / hosts | `theHarvester -d example.lab -b all` | Útil para dominios, emails, hosts y algo de OSINT básico sin demasiada ceremonia. |
| SpiderFoot | https://github.com/smicallef/spiderfoot | Correlación OSINT | `sf.py -s example.lab -o json > outputs/recon/spiderfoot.json` | Bueno para juntar piezas y sacar relaciones que luego investigas manualmente. |
| Recon-ng | https://github.com/lanmaster53/recon-ng | Framework | `recon-ng -r workspace.rc` | Práctico si quieres automatizar módulos y guardar resultados más estructurados. |
| Shodan CLI | https://help.shodan.io/the-shodan-command-line-client | Servicios expuestos | `shodan host 10.0.1.5` | Muy útil para banners históricos y contexto externo si el alcance lo permite. |
| dnsx | https://github.com/projectdiscovery/dnsx | Resolución masiva | `dnsx -l subs.txt -resp -a -aaaa -cname` | Ideal para limpiar listas y ver qué subdominios resuelven de verdad. |
| httpx | https://github.com/projectdiscovery/httpx | Validación HTTP | `httpx -l subs.txt -title -tech-detect -status-code` | Te dice rápido qué subdominios tienen web útil antes de pasar a `web/`. |
| gau | https://github.com/lc/gau | URLs históricas | `gau example.lab > outputs/recon/gau.txt` | Útil para sacar rutas viejas y endpoints olvidados. |
| waybackurls | https://github.com/tomnomnom/waybackurls | URLs históricas | `waybackurls example.lab > outputs/recon/wayback.txt` | Ligero y perfecto para complementar a `gau`. |
| naabu | https://github.com/projectdiscovery/naabu | Puertos rápidos | `naabu -host example.lab -top-ports 100` | Buen puente entre recon y network scanning cuando quieres una primera foto de puertos. |

## Comandos utilizados
- `amass enum -d example.lab -o outputs/recon/amass.txt`.
- `sublist3r -d example.lab -o outputs/recon/sublist3r.txt`.
- `assetfinder --subs-only example.lab > outputs/recon/assetfinder.txt`.
- `dnsx -l outputs/recon/subdomains.txt -resp -a -cname > outputs/recon/dnsx.txt`.
- `gau example.lab > outputs/recon/gau.txt`.

## Técnicas aplicadas
- Comparo siempre varias fuentes de subdominios antes de dar una lista por buena.
- Valido qué resuelve de verdad con `dnsx` y qué responde por HTTP con `httpx` para no arrastrar ruido.
- Si sale algo interesante, lo enlazo con `network_scan/` o `web/` para que el flujo del repo tenga continuidad.

## Recomendaciones personales
- Guarda los outputs con fecha cuando repitas un reconocimiento; así luego puedes usar diffs y ver qué ha cambiado.
- Documenta si un hallazgo vino de una fuente pasiva, de histórico o de una validación activa: eso ahorra muchas dudas más tarde.
- No mezcles automáticamente OSINT abierto con activos internos sin anotar bien el contexto; si no, luego el inventario se contamina rápido.
