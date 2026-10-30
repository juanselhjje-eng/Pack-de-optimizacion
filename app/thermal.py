import json
import shutil
import subprocess


def _run_powershell(command):
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command", command],
            capture_output=True, text=True, timeout=8
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        pass
    return None


def _load_sensor_data(raw):
    if not raw:
        return []
    try:
        data = json.loads(raw)
    except (TypeError, ValueError):
        return []
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        return []
    sensors = []
    for item in data:
        if not isinstance(item, dict):
            continue
        try:
            value = float(item.get("Value"))
        except (TypeError, ValueError):
            continue
        name = str(item.get("Name") or item.get("Identifier") or "Sensor")
        sensors.append({"name": name, "celsius": round(value, 1)})
    return sensors


def _nvidia_temperature():
    if not shutil.which("nvidia-smi"):
        return None
    try:
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode != 0:
            return None
        value = float(result.stdout.strip().splitlines()[0])
        return {"name": "NVIDIA GPU", "celsius": round(value, 1)}
    except (OSError, ValueError, IndexError, subprocess.TimeoutExpired):
        return None


def _classify(sensor):
    name = sensor["name"].lower()
    value = sensor["celsius"]
    if "gpu" in name or "nvidia" in name:
        kind, warning, high = "GPU", 85, 90
    elif any(word in name for word in ("cpu", "core", "package", "tctl", "tdie")):
        kind, warning, high = "CPU", 90, 95
    else:
        kind, warning, high = "Otro", 60, 70
    level = "alto" if value >= high else "precaucion" if value >= warning else "normal"
    return {**sensor, "component": kind, "level": level}


def thermal_status():
    sources = {}
    all_sensors = []
    for name, namespace in (
        ("LibreHardwareMonitor", "root/LibreHardwareMonitor"),
        ("OpenHardwareMonitor", "root/OpenHardwareMonitor")
    ):
        command = (
            "Get-CimInstance -Namespace '" + namespace + "' -ClassName Sensor -ErrorAction Stop "
            "| Where-Object { $_.SensorType -eq 'Temperature' } "
            "| Select-Object Name,Value,Identifier | ConvertTo-Json -Compress"
        )
        sensors = _load_sensor_data(_run_powershell(command))
        sources[name] = {"available": bool(sensors), "sensor_count": len(sensors)}
        all_sensors.extend(sensors)

    nvidia = _nvidia_temperature()
    if nvidia:
        all_sensors.append(nvidia)
    classified = [_classify(sensor) for sensor in all_sensors]
    alerts = [sensor for sensor in classified if sensor["level"] != "normal"]
    status = "sin_datos" if not classified else (
        "alto" if any(item["level"] == "alto" for item in classified)
        else "precaucion" if alerts else "normal"
    )
    return {
        "sensors": classified,
        "alerts": alerts,
        "sources": sources,
        "nvidia_cli_available": nvidia is not None,
        "status": status,
        "note": "Umbrales orientativos, no límites oficiales. Los nombres de sensores varían; compara el mismo sensor."
    }


def thermal_recommendations(status):
    level = status.get("status")
    if level == "sin_datos":
        return [
            "No hay lecturas térmicas disponibles. Abre LibreHardwareMonitor para habilitar sensores compatibles.",
            "No se debe asumir que el equipo está frío cuando faltan datos."
        ]
    if level == "alto":
        return [
            "Reduce temporalmente la carga exigente y deja que el equipo se enfríe.",
            "Comprueba que las rejillas estén despejadas y usa el portátil sobre una superficie firme.",
            "Si ocurre repetidamente, solicita revisar ventiladores, disipadores y mantenimiento interno."
        ]
    if level == "precaucion":
        return [
            "Revisa procesos con alto uso de CPU o GPU y cierra solo los que no necesites.",
            "Mejora el flujo de aire y vuelve a medir después de unos minutos.",
            "Evita overclock y cambios de voltaje mientras investigas la temperatura."
        ]
    return [
        "No se detectan alertas en los sensores disponibles en esta medición.",
        "Mantén libres las entradas y salidas de aire y revisa las temperaturas bajo cargas prolongadas."
    ]
