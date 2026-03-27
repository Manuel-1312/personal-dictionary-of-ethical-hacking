# Toolkit - Evaluación de Vulnerabilidades ⚠️

Catálogo de herramientas para validar hallazgos de vulnerabilidades en laboratorios y entornos autorizados. Aquí lo importante no es solo detectar, sino poder justificar por qué confías —o no— en cada resultado.

| Herramienta | Enlace | Objetivo | Comando / uso típico | Notas reales |
| --- | --- | --- | --- | --- |
| Nmap + Vulscan | https://github.com/scipag/vulscan | CVE / banners | `nmap --script vulscan --script-args vulscandb=scipag -oX reports/network/vulscan.xml 10.0.0.0/24` | Muy útil para triage rápido, pero siempre pide validación manual después. |
| Greenbone / OpenVAS | https://www.greenbone.net/ | Escaneo profundo | `omp --create-target ...` + política ligera | Bueno para una pasada más pesada, pero conviene controlar mucho el ruido y los falsos positivos. |
| Nessus Essentials | https://www.tenable.com/products/nessus/nessus-essentials | Vulnerability scanner | `nessuscli managed link --key ...` | Muy cómodo para host scanning y reporting visual si lo tienes montado en lab. |
| Nikto | https://github.com/sullo/nikto | Web básica / cabeceras | `nikto -h http://10.0.0.5 -output reports/network/nikto-10.0.0.5.html` | Ligero, rápido y útil para sacar una idea general del frente web. |
| Gobuster | https://github.com/OJ/gobuster | Enumeración | `gobuster dir -u http://10.0.0.5 -w wordlists/common.txt` | Sirve para complementar la parte de paths antes de afirmar que una superficie es pequeña. |
| Lynis | https://github.com/CISOfy/lynis | Auditoría de host | `lynis audit system` | Muy útil para Linux hardening y para tener checklist comparables entre sesiones. |
| Metasploit auxiliary | https://github.com/rapid7/metasploit-framework | Verificación | `msfconsole -q` + módulos `scanner/` | Mejor como verificación controlada que como detector principal. |
| nuclei | https://github.com/projectdiscovery/nuclei | Plantillas de vulnerabilidad | `nuclei -l hosts.txt -severity low,medium,high` | Bueno para priorizar, no para cerrar un informe sin validar. |
| testssl.sh | https://github.com/drwetter/testssl.sh | TLS / SSL | `testssl.sh https://target.lab` | Muy práctico para revisar cifrados, suites y configuración HTTPS. |
| sslscan | https://github.com/rbsec/sslscan | TLS rápido | `sslscan target.lab:443` | Complemento ligero cuando no necesitas todo el detalle de testssl.sh. |
| enum4linux-ng | https://github.com/cddmp/enum4linux-ng | SMB / Windows | `enum4linux-ng -A 10.0.0.20` | Muy bueno para triage de shares, usuarios y SMB posture. |
| smbclient | https://www.samba.org/samba/docs/current/man-html/smbclient.1.html | SMB manual | `smbclient -L //10.0.0.20/ -N` | Ideal para contrastar lo que otros scanners dicen sobre shares y acceso. |

## Comandos utilizados
- `nmap --script vulscan --script-args vulscandb=scipag -oX reports/network/vulscan.xml 10.0.0.0/24`.
- `nikto -h http://10.0.0.5 -output reports/network/nikto-10.0.0.5.html`.
- `lynis audit system` y comparación posterior del `lynis-report.dat`.
- `testssl.sh https://10.0.0.5` para una revisión específica de TLS.

## Técnicas aplicadas
- Contrasto al menos dos fuentes antes de elevar un hallazgo importante a “vulnerabilidad real”.
- Si el hallazgo viene por banner o firma, intento reproducir con una petición manual, `curl`, `smbclient` o una prueba ligera.
- Mantengo una lista de falsos positivos y la razón del descarte para no repetir el mismo trabajo en futuras sesiones.

## Recomendaciones personales
- Si una herramienta escupe demasiadas alertas, no intentes arreglarlo con fe: recorta scope, cambia política o valida por capas.
- Cuando un hallazgo merezca seguirse, enlázalo con `exploitation/` o con una nota de mitigación para no dejarlo huérfano.
- Genera reportes exportables (XML, CSV, HTML) siempre que puedas; ayudan mucho más que una captura suelta o una nota improvisada.
