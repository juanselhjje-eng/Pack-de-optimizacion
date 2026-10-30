# Control térmico y prevención del recalentamiento

La aplicación recopila temperaturas cuando los sensores están disponibles. Consulta LibreHardwareMonitor u OpenHardwareMonitor mediante WMI y también intenta leer la temperatura de NVIDIA con `nvidia-smi`.

## Interpretación

Los avisos orientativos empiezan en CPU 90 °C (alto desde 95 °C) y GPU 85 °C (alto desde 90 °C). No son límites oficiales para todos los modelos. Los portátiles pueden tener sensores y límites térmicos específicos del fabricante. Una lectura aislada no demuestra una avería.

## Qué hacer si se calienta

1. Reduce temporalmente las tareas exigentes si aparece una alerta alta.
2. Usa el portátil sobre una superficie firme, sin bloquear rejillas.
3. Comprueba procesos con alto uso de CPU/GPU.
4. Si el problema se repite, pide revisar ventiladores, disipadores y mantenimiento interno.
5. Vuelve a medir bajo condiciones similares.

No se controla directamente la velocidad de los ventiladores ni se cambia voltaje, overclock o límites térmicos. Esas acciones dependen del firmware y del fabricante y pueden causar daños si se fuerzan.

## Sobre usar el 100% de recursos

No es recomendable mantener CPU, GPU o RAM al 100% permanentemente. La RAM ocupada no equivale a rendimiento, y el uso máximo continuo genera calor y consumo. El objetivo es permitir que las aplicaciones aprovechen los recursos disponibles cuando los necesitan, sin desactivar protecciones ni provocar recalentamiento.

Los umbrales de esta herramienta son avisos orientativos y no sustituyen las especificaciones térmicas de ASUS o Intel/NVIDIA.
