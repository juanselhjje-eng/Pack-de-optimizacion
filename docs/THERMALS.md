# Temperaturas y sensores

Windows no ofrece una API universal que entregue todas las temperaturas de CPU y GPU en cada portátil.

La aplicación consulta:
- NVIDIA nvidia-smi para telemetría compatible de la GPU NVIDIA.
- LibreHardwareMonitor o OpenHardwareMonitor mediante WMI si uno de esos programas está instalado y abierto.

Si no hay sensores disponibles, la aplicación debe indicarlo; no debe inventar valores ni mostrar cero como si fuera una temperatura real.

En portátiles, los sensores pueden tener nombres distintos y algunos valores pueden no estar expuestos. Compara siempre el mismo sensor bajo condiciones parecidas. No uses una temperatura aislada como único criterio para modificar ventiladores, voltajes o límites térmicos.
