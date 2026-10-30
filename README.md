# Ultimate PC Optimizer

Aplicación de escritorio para diagnosticar Windows y revisar el rendimiento en uso general, programación, multitarea y videojuegos.

## Funciones actuales
- Interfaz gráfica con pestañas: resumen, procesos, programación, red, mantenimiento, inicio, rendimiento y perfiles.
- Inventario de Windows, CPU, RAM, discos físicos, volúmenes, GPU, batería y adaptadores de red.
- Procesos ordenados por memoria, con estado e hilos.
- Detección de Python, Git, Node.js, npm, VS Code y Cursor.
- Prueba ICMP con estadísticas de latencia y pérdida cuando Windows informa el dato.
- Revisión de archivos temporales sin borrarlos.
- Inventario de ubicaciones de inicio sin desactivar programas.
- Consulta del plan de energía actual.
- Consulta de telemetría NVIDIA mediante nvidia-smi, si está disponible.
- Consulta opcional de sensores térmicos mediante LibreHardwareMonitor u OpenHardwareMonitor.
- Microprueba corta de CPU y almacenamiento temporal.
- Recomendaciones basadas en uso de CPU, RAM y espacio libre.
- Perfiles informativos: equilibrado, programación, gaming y máximo rendimiento.
- Exportación JSON del informe ampliado.

## Requisitos
- Windows 10/11 de 64 bits.
- Python 3.10 o superior.
- PowerShell.
- Controlador NVIDIA compatible para consultar nvidia-smi.

## Ejecutar
Doble clic en run.bat. El script crea un entorno virtual local e instala las dependencias. También puedes ejecutar:

~~~powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe main.py
~~~

## Pruebas
~~~powershell
python -m unittest discover -s tests -v
~~~

GitHub Actions ejecuta pruebas en Windows con Python 3.12 cuando se activa el flujo de trabajo.

## Seguridad y límites
Esta versión prioriza diagnóstico. No cambia registro, plan de energía, servicios, firewall, Defender, Windows Update ni aplicaciones de inicio. No borra archivos. Las micropruebas son orientativas y no equivalen a benchmarks profesionales. No se garantizan aumentos fijos de FPS ni reducciones de ping.

Consulta docs/OPTIMIZATION_POLICY.md antes de añadir cualquier función que modifique Windows. Los cambios futuros deberán mostrar impacto y riesgos, solicitar confirmación y ofrecer reversión.

## Hardware de referencia
ASUS TUF Gaming F15 FX506HC, Intel Core i5-11400H, NVIDIA RTX 3050 Laptop, 16 GB DDR4-3200, SSD Micron 512 GB y pantalla 1920x1080 a 144 Hz. El programa detecta el equipo en el que se ejecuta; no fuerza estos valores.
