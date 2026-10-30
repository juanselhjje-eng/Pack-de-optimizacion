# Ultimate PC Optimizer

Herramienta local para diagnosticar y mejorar el mantenimiento de Windows 10/11. Diseñada para uso general, programación, multitarea y videojuegos.

## Principios
- Diagnóstico antes de modificar.
- Ningún ajuste del sistema se aplica sin confirmación.
- Las operaciones destructivas se excluyen de la primera versión.
- Registro local de acciones y copias de seguridad cuando corresponda.
- No se prometen aumentos fijos de FPS ni reducciones garantizadas de ping.

## Requisitos
- Windows 10/11 de 64 bits.
- Python 3.10 o superior.
- PowerShell disponible.
- Algunas consultas avanzadas pueden requerir permisos de administrador.

## Instalación
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

Si PowerShell bloquea la activación, ejecuta `\.venv\Scripts\python.exe -m pip install -r requirements.txt` y luego `\.venv\Scripts\python.exe main.py`.

## Módulos
- Resumen de hardware y sistema.
- CPU, RAM, GPU, almacenamiento y procesos.
- Diagnóstico de latencia y pérdida de paquetes.
- Revisión de espacio temporal.
- Perfiles informativos: General, Programación y Gaming.
- Exportación de informes JSON.
- Registro de acciones.

## Seguridad
La versión inicial es principalmente diagnóstica. No desactiva Defender, Windows Update, firewall, servicios esenciales ni modifica el registro automáticamente. No incluye "limpiadores de RAM" agresivos, overclocking ni cambios de TCP universales.

Antes de implementar una optimización nueva, documenta su efecto, riesgos, compatibilidad, método de comprobación y reversión. Prueba cada cambio en el hardware objetivo.

## Hardware de desarrollo de referencia
ASUS TUF Gaming F15 FX506HC, Intel Core i5-11400H, NVIDIA RTX 3050 Laptop, 16 GB DDR4-3200, SSD Micron 512 GB, pantalla 1920x1080 a 144 Hz. La detección se ejecuta localmente; estos datos solo sirven como referencia.

## Estado
Prototipo inicial. Algunas métricas dependen de controladores y herramientas del fabricante.
