# Threat Hunting

Acá guardo los casos de hunting. Cada vez que lanzo un query en Velociraptor o corro una regla Sigma lo registro: fecha, hipótesis, fuentes (Sysmon, Zeek, logs de red) y resultado final. Cuando ejecuto hunts con VQL los resultados van a `defense/threat_hunting/results/`.

Cuando un hunt genera un caso válido lo subo a The Hive y enlazo la ID en `CASE-XXXX.md`. Este directorio también sirve para documentar qué reglas hay que desactivar porque tiran falsos positivos recurrentes.