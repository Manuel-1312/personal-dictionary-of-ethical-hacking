# Reconocimiento Activo

Aquí se documentan herramientas que interaccionan con el objetivo: escaneos, fingerprinting, enumeración de servicios. Usa este espacio para guardar scripts, salidas de nmap y tiempos de escaneo.

## Comandos utilizados
- `nmap -sS -sV -oA recon/active/nmap-active 10.0.1.5`.
- `rustscan -a 10.0.1.5 -- -A -sV`.

## Técnicas aplicadas
- Escaneo SYN `-sS` seguido de `-sV`/`-sC` para detección rápida.
- Uso de scripts NSE para enumerar vulnerabilidades.

## Recomendaciones personales
- Guarda salidas `nmap` en `recon/active/reports/` para trazabilidad.
- Documenta los tiempos de escaneo y la ventana en que se hicieron (para evitar repetición intensa).
