# Toolkit - Personas 🧍

Herramientas que usas para recolectar información de perfiles públicos y mantener el respeto por la privacidad.

## Plantilla base
- **Enlace:** referencia oficial de la herramienta.
- **Caso de uso:** qué tipo de información de personas recopila.
- **Comando de ejemplo:** comando o consulta típica.
- **Notas útiles:** qué registrar (fuentes, contexto ético, fechas).
- **Recomendaciones:** buenas prácticas de privacidad y documentación.
- **Cuándo usar / cuándo no:** solo información pública; nunca almacenes datos privados o credenciales.

## 1. Herramientas para perfiles y personas

### Maltego CE
- **Enlace:** https://www.maltego.com/
- **Caso de uso:** Visualización de relaciones entre entidades (personas, dominios, IPs, organizaciones).
- **Comando de ejemplo:** Abre Maltego CE → New Graph → Add Entity (Domain) → Run transforms.
- **Notas útiles:** Documenta qué entidades enlazas y qué fuentes públicas usas; exporta el grafo en PNG/CSV.
- **Recomendaciones:** Limita los transforms a fuentes públicas; guarda el proyecto `.mtgx` en `osint/people/results/`.
- **Cuándo usarlo:** Para visualizar conexiones complejas entre personas, dominios y organizaciones.
- **Cuándo no:** Con transforms de pago sin autorización o cuando los datos podrían violar la privacidad.

### OSINT Framework
- **Enlace:** https://osintframework.com/
- **Caso de uso:** Mapa interactivo de recursos OSINT organizados por categoría y tipo de objetivo.
- **Comando de ejemplo:** Navega a https://osintframework.com/ y selecciona la categoría relevante.
- **Notas útiles:** Sigue los sectores y guarda enlaces actualizados en `osint/people/resources.md`.
- **Recomendaciones:** Úsalo como punto de partida para descubrir herramientas especializadas; revisa periódicamente si los enlaces siguen activos.
- **Cuándo usarlo:** Al inicio de una investigación para identificar qué fuentes son relevantes para el objetivo.
- **Cuándo no:** Como fuente directa de datos; es un directorio de herramientas, no una herramienta de recolección.

### SpiderFoot
- **Enlace:** https://github.com/smicallef/spiderfoot
- **Caso de uso:** Recolección automática de información de personas desde múltiples fuentes públicas.
- **Comando de ejemplo:** `spiderfoot -s "nombre@ejemplo.com" -t EMAILADDR -o json -q`
- **Notas útiles:** Mantén API keys y logs por sesión; evita datos privados; usa solo módulos pasivos.
- **Recomendaciones:** Configura un perfil de módulos pasivos; guarda logs en `osint/people/results/spiderfoot/`.
- **Cuándo usarlo:** Para agregación automática de datos públicos de un correo, nombre o dominio.
- **Cuándo no:** Con módulos activos o cuando el sujeto no es parte del alcance autorizado.

### Google Dorking
- **Enlace:** https://www.exploit-db.com/google-hacking-database
- **Caso de uso:** Búsqueda avanzada en Google para encontrar información expuesta públicamente.
- **Comando de ejemplo:** `site:example.com filetype:pdf "confidential"` en Google Search.
- **Notas útiles:** Documenta queries y resultados con contexto ético; guarda las URLs encontradas con fecha.
- **Recomendaciones:** Usa la Google Hacking Database como referencia; anota qué dorks generaron resultados relevantes.
- **Cuándo usarlo:** Para encontrar documentos, directorios o páginas expuestos involuntariamente.
- **Cuándo no:** Para acceder a información protegida; documentar siempre el hallazgo con su contexto ético.

### LinkedIn (uso manual)
- **Enlace:** https://www.linkedin.com/
- **Caso de uso:** Reconocimiento manual de perfiles profesionales, estructura organizacional y tecnologías usadas.
- **Comando de ejemplo:** Búsqueda manual en LinkedIn: `"Example Corp" AND "security engineer"`.
- **Notas útiles:** Usa sólo versiones públicas o APIs oficiales; no almacenes credenciales ni datos privados.
- **Recomendaciones:** Documenta solo lo que es visible públicamente; no crees perfiles falsos para recopilar datos.
- **Cuándo usarlo:** Para mapear la estructura del equipo de seguridad o identificar tecnologías mencionadas en perfiles.
- **Cuándo no:** Para recopilar datos personales detallados o cuando viola los términos de servicio de LinkedIn.

### theHarvester
- **Enlace:** https://github.com/laramies/theHarvester
- **Caso de uso:** Recolección de correos electrónicos, nombres y dominios desde múltiples fuentes públicas.
- **Comando de ejemplo:** `theHarvester -d example.com -b linkedin,google,bing -f people-results.html`
- **Notas útiles:** Aplica filtros de responsabilidad y guarda las fuentes usadas; documenta cada API consultada.
- **Recomendaciones:** Usa `-b all` con precaución; filtra resultados irrelevantes antes de documentar.
- **Cuándo usarlo:** Para recopilar correos corporativos y nombres de empleados en la fase de reconocimiento pasivo.
- **Cuándo no:** Para investigaciones personales fuera del alcance autorizado o sin propósito de seguridad claro.

## 2. Flujos y documentación
- Documenta siempre el propósito ético de la investigación antes de iniciar la recolección.
- Guarda resultados en `osint/people/results/<herramienta>-<fecha>/` con la fuente y fecha de cada dato.
- Revisa los hallazgos para asegurarte de que no incluyes información privada fuera del alcance.
