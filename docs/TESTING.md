# Pruebas

Desde la raíz del proyecto:

\`\`\`powershell
python -m unittest discover -s tests -v
\`\`\`

Pruebas manuales recomendadas:
1. Ejecutar sin permisos de administrador.
2. Ejecutar en Windows 10 y Windows 11.
3. Probar sin NVIDIA, sin Git y sin conexión a internet.
4. Revisar que los diagnósticos no cambien configuraciones.
5. Exportar y abrir un informe JSON.
6. Confirmar que los errores de permisos se muestran sin cerrar la aplicación.
7. Comparar benchmarks solo bajo condiciones similares.

No declarar compatibilidad completa hasta ejecutar estas pruebas en los equipos objetivo.
