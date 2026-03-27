# Reconocimiento

Mis ejercicios de recon van documentados aquí. Para cada objetivo guardo la hipótesis, la lista de comandos empleados y qué fuentes consulté.

- `passive/` contiene datos que no tocan el objetivo (DNS públicos, certificados, redes sociales). Guardaré CSV y pantallazos para cada sesión.
- `active/` reúne los escaneos legítimos (nmap, nbtscan) que tocan IPs autorizadas.

Cuando termino un ciclo completo copio los hallazgos a `lab-notes.md` y hago referencia a los archivos `passive/` o `active/` correspondientes. Si la hipótesis cambia (por ejemplo, descubro subdominios nuevos), actualizo la sección `Recon / Reconceptos` con la fecha y la razón del cambio.

## Comandos utilizados
- `amass enum -d example.lab -config recon/amass.conf -o outputs/recon/amass.json` para captar nuevos subdominios.
- `shodan host 10.0.1.5` y guardo el banner en `outputs/recon/shodan-host10.0.1.5.json`.
- `nmap -sS -Pn -oA outputs/recon/active-target 10.0.1.5` como primer escaneo autorizado.

## Técnicas aplicadas
- Combino OSINT pasivo (Amass, PassiveTotal) con escaneos activos (nmap, RustScan) para validar cada host.
- Documentación de hypotheses: cada cambio en la hipótesis queda registrado en `recon/log.md`.

## Recomendaciones personales
- Usa `outputs/recon/reports/` para guardar JSON/CSV y enlázalos desde `lab-notes.md`.
- Si encuentras un subdominio nuevo, documenta la fuente y la fecha para poder rastrear quién lo añadió.
- Mantén el enfoque ético: copia solo datos públicos y evita bombardear servicios con demasiadas peticiones.