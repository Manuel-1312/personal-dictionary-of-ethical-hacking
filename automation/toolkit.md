# Toolkit - Automatización 🤖

Catálogo de herramientas y scripts que te ayudan a automatizar despliegues, pruebas y recopilación de datos dentro del laboratorio.

## Plantilla base
- **Enlace:** referencia oficial.
- **Caso de uso:** propósito de la herramienta.
- **Comando de ejemplo:** comando representativo.
- **Notas útiles:** observaciones clave.
- **Recomendaciones:** consejos de uso.
- **Cuándo usar / cuándo no:** límites y contexto.

## 1. Orquestación e infraestructura

### Ansible
- **Enlace:** https://www.ansible.com/
- **Caso de uso:** Orquestación de infraestructura mediante playbooks declarativos.
- **Comando de ejemplo:** `ansible-playbook -i inventory.yml playbooks/lab-setup.yml`
- **Notas útiles:** Usa playbooks para levantar Kali, ZAP y registros; guarda inventarios constantes en `automation/ansible/`.
- **Recomendaciones:** Versiona todos los playbooks e inventarios; documenta variables de entorno y vault secrets.
- **Cuándo usarlo:** Despliegue y configuración repetible de entornos de laboratorio.
- **Cuándo no:** Tareas puntuales de una sola vez donde un script bash es más rápido.

### AutoRecon
- **Enlace:** https://github.com/Tib3rius/AutoRecon
- **Caso de uso:** Automatización de reconocimiento combinando nmap, enum4linux y dirbuster.
- **Comando de ejemplo:** `autorecon 10.0.0.1 --output recon/autorecon/`
- **Notas útiles:** Combina nmap, enum4linux y dirbuster; documenta los flags usados por sesión.
- **Recomendaciones:** Revisa los resultados de cada subcarpeta generada; no sustituye el análisis manual.
- **Cuándo usarlo:** Reconocimiento inicial rápido y completo de un objetivo en laboratorio.
- **Cuándo no:** Targets que requieren control preciso del tráfico o cuando el ruido es un problema.

### Invoke-IR
- **Enlace:** https://github.com/fireeye/flare-vm/tree/master/Invoke-IR
- **Caso de uso:** Scripts PowerShell de respuesta a incidentes y recolección de artefactos.
- **Comando de ejemplo:** `Import-Module Invoke-IR; Get-Prefetch`
- **Notas útiles:** Ejecuta módulos mientras guardas logs y resultados en CSV para revisión posterior.
- **Recomendaciones:** Documenta qué módulos se ejecutaron y en qué estado estaba el sistema; guarda outputs en `automation/ir/`.
- **Cuándo usarlo:** Recolección rápida de artefactos Windows durante ejercicios de respuesta a incidentes.
- **Cuándo no:** Sistemas Linux; usa herramientas nativas o osquery para esos entornos.

### SaltStack
- **Enlace:** https://github.com/saltstack/salt
- **Caso de uso:** Gestión de configuración remota basada en estados y pilares.
- **Comando de ejemplo:** `salt '*' state.apply lab-config`
- **Notas útiles:** Documenta estados aplicados y cómo se depuran los registros de minion.
- **Recomendaciones:** Mantén estados en repositorio Git; documenta la versión del master y los minions del laboratorio.
- **Cuándo usarlo:** Gestión de configuración cuando tienes múltiples VMs de laboratorio que mantener homogéneas.
- **Cuándo no:** Entornos de una sola VM donde Ansible es más sencillo de configurar.

### Puppet
- **Enlace:** https://puppet.com/
- **Caso de uso:** Gestión declarativa de configuraciones con manifests y módulos.
- **Comando de ejemplo:** `puppet apply manifests/site.pp`
- **Notas útiles:** Usa manifests para mantener entornos homogéneos y guarda políticas revisadas en control de versiones.
- **Recomendaciones:** Versiona todos los manifests; documenta dependencias de módulos en `Puppetfile`.
- **Cuándo usarlo:** Gestión de configuración a largo plazo de entornos de laboratorio estables.
- **Cuándo no:** Despliegues puntuales o si ya usas Ansible; mezclar herramientas de configuración añade complejidad.

## 2. Pruebas y artefactos

### CyberChef
- **Enlace:** https://gchq.github.io/CyberChef/
- **Caso de uso:** Procesamiento y transformación de artefactos, encodings y datos.
- **Comando de ejemplo:** interfaz web o `node CyberChef.js --recipe recipe.json --input data.txt`
- **Notas útiles:** Guarda recetas (.json) para reproducir transformaciones de logs; muy útil para decoding rápido.
- **Recomendaciones:** Exporta recetas útiles en `automation/cyberchef/recipes/`; versiona las más reutilizables.
- **Cuándo usarlo:** Transformaciones rápidas de datos, decoding, encoding y análisis de artefactos.
- **Cuándo no:** Procesamiento masivo de ficheros grandes; usa scripts Python para eso.

### Playwright + Allure
- **Enlace:** https://playwright.dev/ + https://qameta.io/allure/
- **Caso de uso:** Pruebas automatizadas de aplicaciones web con reportes visuales detallados.
- **Comando de ejemplo:** `npx playwright test && allure generate allure-results -o allure-report`
- **Notas útiles:** Integra el runner de Playwright y exporta dashboards Allure para reportes interinos.
- **Recomendaciones:** Guarda los resultados de Allure por sesión; documenta qué escenarios se automatizaron.
- **Cuándo usarlo:** Validación automatizada de flujos web y regresión en aplicaciones de laboratorio.
- **Cuándo no:** Auditorías manuales donde la exploración libre es más valiosa que los tests automatizados.
