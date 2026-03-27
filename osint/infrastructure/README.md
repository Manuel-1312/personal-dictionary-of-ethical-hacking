# OSINT - Infraestructura

Documenta los descubrimientos sobre infraestructura pública: qué IPs están expuestas, qué proveedores aparecen en los Whois, qué certificados TLS se renovaron.

Incluye:
- Capturas de Shodan, crt.sh y SecurityTrails con fechas.
- Notas sobre dependencias externas (CDNs, proveedores de correo) y por qué son relevantes para el objetivo.
- Archivos `outputs/osint/infra/` con JSON/CSV que luego referencio en los reportes.

Si identificas cambios (por ejemplo, un nuevo certificado o un host moviéndose de proveedor), anota la fecha, la fuente y los pasos para replicar la observación.

## Comandos utilizados
- `shodan search org:"Example Inc" --fields ip_str,org,port` > `outputs/osint/infra/shodan-org.json`.
- `curl "https://crt.sh/?q=%25example.com"` y guardo el PDF en `outputs/osint/infra/crtsh-example.pdf`.
- `securitytrails domain example.com --fields dns` y guardo `outputs/osint/infra/securitytrails.json`.

## Técnicas aplicadas
- Correlación de IPs con CDN/proveedor y documentación en `outputs/osint/infra/history.csv`.
- Comparación de certificados TLS (crt.sh vs Censys) para detectar rotaciones.

## Recomendaciones personales
- Adjunta la fuente y fecha para cada dato (Shodan, crt.sh, etc.).
- Si detectas un cambio de proveedor, guarda whois y nota el contacto para futuras referencias.