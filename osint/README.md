# OSINT

Esta carpeta reúne los recursos y políticas que sigo cuando hago inteligencia abierta. Cada sesión empieza con la pregunta: ¿estoy recabando solo datos públicos y respetando la privacidad?

- `people/`: recopilo perfiles sociales, correos o referencias públicas y anoto qué fuentes usé (Maltego, Google Dorks, etc.).
- `infrastructure/`: dibujo infraestructura pública (DNS, certificados, historical IPs) y guardo capturas de los mapas.

Cada sesión termina con un resumen en `lab-notes.md` y una copia de los artefactos (CSV, JSON, capturas). También registro qué comprobaciones legales hice (policy de la empresa, términos de uso de la fuente) para no saltarme nada.

## Comandos utilizados
- `amass enum -d example.lab -config osint/examples/amass.yml -o outputs/osint/amass.json`.
- `python osint/scripts/collect-shodan.py -i indicators.txt -o outputs/osint/shodan.json`.

## Técnicas aplicadas
- Recolección pasiva antes de tocar al objetivo: uso Amass/PassiveTotal para dibujar la superficie.
- Documentación de la fuente: cada resultado lleva URL, fecha y cómo se obtuvo para mantener la ética.

## Recomendaciones personales
- Guarda los artefactos en carpetas `outputs/osint/<fecha>/` y enlázalos desde `lab-notes.md`.
- Si usas APIs (Shodan, SecurityTrails), registra la API key (sin compartirla) y anota los límites de uso.