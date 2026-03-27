# Roadmap de utilidades Python

Esta hoja de ruta recoge ideas de scripts que encajan bien con la biblioteca. La idea no es meter herramientas por meter, sino ampliar `python/` con piezas pequeñas, útiles y fáciles de mantener. Cada propuesta está pensada para complementar otras áreas del repo como `network_scan/`, `web/`, `defense/`, `forensics/` y `exploitation/`.

La carpeta `python/` ya está organizada por subcategorías (`parsers/`, `web/`, `forensics/`) para que este crecimiento sea ordenado desde el principio.

## 10 utilidades candidatas

### 1. `nmap_xml_to_markdown.py`
**Qué haría**
- Convertiría resultados XML de Nmap en un informe Markdown limpio, legible y reutilizable.

**Por qué merece la pena**
- Te ahorra leer XML a pelo.
- Encaja muy bien con reporting y documentación de sesiones.

**Dónde viviría mejor**
- `network_scan/`
- `automation/reporting/`

---
### 2. `masscan_to_csv.py`
**Qué haría**
- Normalizaría salidas de Masscan o GNMAP a un CSV ordenado por host, puerto y servicio.

**Por qué merece la pena**
- Hace más fácil comparar descubrimiento rápido con escaneos posteriores.
- Muy útil para inventarios y diff entre sesiones.

**Dónde viviría mejor**
- `network_scan/`
- `python/`

---
### 3. `web_screenshot_manifest.py`
**Qué haría**
- Tomaría una lista de URLs y generaría un manifiesto de capturas, títulos, códigos de estado y notas rápidas.

**Por qué merece la pena**
- Da contexto visual a auditorías web.
- Muy bueno para laboratorios con muchas apps o paneles.

**Dónde viviría mejor**
- `web/`
- `exploitation/web_exploitation/`

---
### 4. `subdomain_diff.py`
**Qué haría**
- Compararía dos listas de subdominios y marcaría qué apareció, qué desapareció y qué se mantiene.

**Por qué merece la pena**
- Ideal para seguimiento OSINT o cambios en superficie expuesta.
- Sencillo, útil y fácil de mantener.

**Dónde viviría mejor**
- `recon/`
- `osint/`

---
### 5. `dir_bruteforce_report.py`
**Qué haría**
- Convertiría salidas de `ffuf` o `dirsearch` en un resumen claro con rutas relevantes, códigos y observaciones.

**Por qué merece la pena**
- Evita perder hallazgos entre JSON, TXT y logs dispersos.
- Muy útil para `web_exploitation/`.

**Dónde viviría mejor**
- `web/`
- `exploitation/web_exploitation/`

---
### 6. `ioc_enricher.py`
**Qué haría**
- Tomaría IOCs ya extraídos y los clasificaría mejor: tipo, contexto, frecuencia, origen o formato.

**Por qué merece la pena**
- Le da más valor al extractor básico que ya tienes.
- Útil para triage, defensa y forense.

**Dónde viviría mejor**
- `defense/`
- `forensics/`
- `python/`

---
### 7. `pcap_summary.py`
**Qué haría**
- Sacaría un resumen rápido de un PCAP: IPs, puertos, protocolos, top talkers y ventana temporal.

**Por qué merece la pena**
- Muy práctico para revisar tráfico sin abrir Wireshark en cada caso.
- Tiene mucho valor en labs, IR y análisis rápido.

**Dónde viviría mejor**
- `defense/`
- `forensics/`
- `network_scan/`

---
### 8. `ad_notes_builder.py`
**Qué haría**
- Convertiría hallazgos de Active Directory en una nota Markdown estructurada con host, usuario, permisos, rutas y mitigación.

**Por qué merece la pena**
- Haría más consistente la documentación de sesiones AD.
- Muy alineado con la nueva carpeta `exploitation/active_directory/`.

**Dónde viviría mejor**
- `exploitation/active_directory/`

---
### 9. `evidence_indexer.py`
**Qué haría**
- Recorrería una carpeta de evidencias y generaría un índice con hashes, tamaños, fechas y rutas.

**Por qué merece la pena**
- Encaja perfecto con notas de caso, forense y cadena de custodia ligera.
- Te ayuda a no perder artefactos entre carpetas.

**Dónde viviría mejor**
- `exploitation/notes/`
- `forensics/`
- `python/`

---
### 10. `markdown_case_bundler.py`
**Qué haría**
- Uniría varias notas Markdown (`hallazgo`, `evidencia`, `timeline`, `mitigación`) en un informe final.

**Por qué merece la pena**
- Muy bueno para cerrar sesiones y generar entregables rápidos.
- Te da continuidad entre explotación, defensa y reporting.

**Dónde viviría mejor**
- `automation/reporting/`
- `exploitation/notes/`
- `python/`

---
## Mi recomendación honesta
Si quieres crecer con cabeza, yo empezaría por estos cinco:

1. `nmap_xml_to_markdown.py`
2. `subdomain_diff.py`
3. `pcap_summary.py`
4. `evidence_indexer.py`
5. `markdown_case_bundler.py`

Ese pack da bastante valor real y cubre:
- reporting
- recon
- análisis de red
- evidencias
- cierre de casos

## Cómo elegir sin meter ruido
Para cada script nuevo, yo miraría:
- si resuelve un dolor real del flujo
- si genera salida reutilizable (CSV/Markdown/JSON)
- si puede mantenerse sin volverse un monstruo
- si conecta bien con otras carpetas del repo

Si luego quieres, podemos convertir esta hoja de ruta en una tanda de implementación por fases:
- **Fase 1:** reporting + inventario
- **Fase 2:** recon + web
- **Fase 3:** forense + evidencias
- **Fase 4:** Active Directory y casos complejos
