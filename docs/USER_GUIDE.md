# Guía de uso

## Primer inicio
1. Ejecuta \`run.bat\`.
2. Espera a que termine el análisis inicial.
3. Abre Resumen y revisa los datos detectados.
4. Revisa Procesos para identificar qué aplicaciones consumen memoria.
5. Abre Programación para comprobar herramientas instaladas.
6. Abre Red y ejecuta una prueba ICMP.
7. Usa Mantenimiento para revisar temporales; no borra nada.
8. Usa Inicio de Windows para consultar entradas de arranque.
9. En Rendimiento consulta NVIDIA, el plan de energía y la microprueba.
10. Exporta el informe JSON si necesitas compartir el diagnóstico.

## Interpretación
- CPU alta: revisa qué proceso la está usando y si la carga es temporal.
- RAM disponible baja: identifica aplicaciones y pestañas abiertas antes de cerrar nada.
- Disco casi lleno: revisa manualmente archivos grandes y copias de seguridad.
- Ping alto o pérdida: repite en varios momentos y compara Ethernet y Wi-Fi. El proveedor, la ruta y el servidor influyen.
- Temperatura: esta versión no ofrece todavía lectura universal y fiable de sensores CPU/GPU.

## Antes de cambiar Windows
No uses opciones de optimización de terceros sin conocer exactamente qué cambian. Mantén copias de seguridad y evita desactivar la seguridad del sistema.
