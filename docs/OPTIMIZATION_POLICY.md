# Política para futuras optimizaciones

Toda optimización que modifique Windows debe pasar por este proceso:

1. Identificar un problema medible y reproducible.
2. Mostrar el valor actual y explicar el cambio propuesto.
3. Identificar riesgos, requisitos y efectos secundarios.
4. Crear respaldo del estado anterior cuando sea posible.
5. Solicitar confirmación específica del usuario.
6. Aplicar un solo cambio por vez.
7. Medir el resultado con las mismas condiciones.
8. Permitir restaurar el estado anterior y verificar la reversión.

## Cambios que no deben automatizarse
- Desactivar Microsoft Defender, firewall o Windows Update.
- Desactivar servicios de Windows en bloque.
- Eliminar claves de registro sin diagnóstico.
- Deshabilitar archivo de paginación.
- Vaciar standby list o ejecutar limpiadores de RAM.
- Aplicar comandos TCP universales para reducir ping.
- Eliminar carpetas de caché de Python, Node, IDE o navegadores sin selección.
- Cambiar voltajes, límites térmicos u overclock automáticamente.

## Perfiles
Los perfiles deben modificar únicamente preferencias explícitas y documentadas. "Máximo rendimiento" no debe ignorar temperatura, batería ni límites del fabricante.
