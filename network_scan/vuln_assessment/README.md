# Evaluación de Vulnerabilidades

Aquí dejo todo el proceso de validación: qué herramientas de escaneo profundo utilicé, qué resultados comparé y qué scripts ejecuté para verificar si un hallazgo era válido.

Flujo típico:
1. Cargo el resultado de `nmap` con `vulscan`, exporto el XML y las entradas con CVEs, y las convierto en un ticket dentro de `reports/network/cves.md`.
2. Ejecuto Greenbone/OpenVAS con una política ligera para no saturar la red y subo los reportes PDF a `reports/network/openvas/`.
3. Complemento con `Nikto` y `Gobuster` para ver cabeceras y directorios inseguros; cada comando termina en un `.log` que guardo en `reports/network/nikto/`.

Si un resultado parece falso positivo, lo añado a `reports/network/falsos.csv` junto con la evidencia que lo contradice. Así cualquiera puede revisar qué detección fue real y qué se descartó.

## Comandos utilizados
- `nmap --script vulscan --script-args vulscandb=scipag -oA reports/network/nmap-vulscan 10.0.0.5` para listar CVEs con referencias.
- `openvas-cli --target 10.0.2.5 --config /etc/openvas/policies/light.xml --output reports/network/openvas/scan-20260327.xml` para no arrastrar escaneos pesados.
- `nikto -h http://10.0.0.5 -output reports/network/nikto/nikto-10.0.0.5.html` y `gobuster dir -u http://10.0.0.5 -w /usr/share/wordlists/raft-large.txt -o reports/network/gobuster-lab.txt`.

## Técnicas aplicadas
- Escaneo escalonado: `masscan` para identificar hosts, luego `nmap`+NSE y finalmente `OpenVAS` para validar CVEs.
- Validación manual de falsos positivos: corro `curl -I` sobre cada puerto y verifico que la respuesta existe antes de catalogar la vulnerabilidad.
- Uso de `vulnwhisperer` para centralizar resultados y compararlos con hallazgos previos.

## Recomendaciones personales
- Guarda los XML/HTML en `reports/network/<fecha>/` y crea una pequeña entrada en `reports/network/index.md` con un resumen.
- Si un CVE aparece repetido, compara la versión del software vs. la base de datos local, a veces el hallazgo se debe a un banner falso.
- Automatiza la firma de hallazgos con `scripts/network/build-ticket.sh` para actualizar `reports/network/cves.md`.