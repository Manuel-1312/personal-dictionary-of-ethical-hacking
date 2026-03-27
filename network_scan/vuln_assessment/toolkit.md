# Toolkit - Evaluación de Vulnerabilidades ⚠️

Catálogo de herramientas para la fase de validación. Cada fila añade comando típico, output y lo que hice personalmente con ese hallazgo.

| Herramienta | Enlace | Objetivo | Notas reales |
| --- | --- | --- | --- |
| nmap + Vulscan | https://github.com/scipag/vulscan | CVE detection | Conservo XML en `reports/network/vulscan/` y documento los IDs encontrados.
| Greenbone/OpenVAS | https://www.greenbone.net/ | Escaneo profundo | Uso una política `light` y anoto cuántos falsos positivos fueron descartados.
| Nikto + Gobuster | https://github.com/sullo/nikto | Cabeceras/dirs | Los logs van a `reports/network/nikto/`, memorizo qué cabeceras inseguros aparecieron.
| Lynis | https://github.com/CISOfy/lynis | Auditoría host | `lynis audit system` y guardo `lynis-report.dat` para comparar con sesiones futuras.
| VulnWhisperer | https://github.com/whisperer/VulnWhisperer | Centralización | Agrupa las salidas y genera dashboards; guardo la configuración en `automation/reporting/templates/`.
| Metasploit auxiliary | https://github.com/rapid7/metasploit-framework | Verificación | Uso módulos `scanner/` para validar vectores detectados.

## Comandos utilizados
- `nmap --script vulscan --script-args vulscandb=scipag -oX reports/network/vulscan/nmap-vulscan.xml 10.0.0.0/24`.
- `omp --create-target --name 'lab-net' --hosts 10.0.0.0/24` seguido de `omp --start-task --target=ID --config=/etc/openvas/policies/light.xml`.
- `nikto -h http://10.0.0.5 -output reports/network/nikto/nikto-10.0.0.5.html`.

## Técnicas aplicadas
- Contraste de resultados: comparo `nmap` con `OpenVAS` y limpias mis scripts `scripts/network/compare-cves.py`.
- Detección de falsos: replico la petición con `curl` y `python requests` para ver si el servicio responde.

## Recomendaciones personales
- Anota en `reports/network/falsos.csv` por qué descartaste cada hallazgo y quién validó la decisión.
- Genera un PDF semanal con `reports/network/summary.pdf` usando Pandoc para entregar a tu equipo.
- No corras OpenVAS sobre subredes completas sin aislar: arranca el escaneo desde una VM `scanner-lab`.