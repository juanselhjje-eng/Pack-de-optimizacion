import subprocess

def thermal_status():
    commands = [
        ("LibreHardwareMonitor", "root/LibreHardwareMonitor"),
        ("OpenHardwareMonitor", "root/OpenHardwareMonitor")
    ]
    results = {}
    for name, namespace in commands:
        command = (
            f"Get-CimInstance -Namespace '{namespace}' -ClassName Sensor -ErrorAction Stop "
            "| Where-Object { $_.SensorType -eq 'Temperature' } "
            "| Select-Object Name,Value,Identifier | ConvertTo-Json -Compress"
        )
        try:
            p = subprocess.run(
                ["powershell", "-NoProfile", "-NonInteractive", "-Command", command],
                capture_output=True, text=True, timeout=8
            )
            if p.returncode == 0 and p.stdout.strip():
                results[name] = {"available": True, "sensors_json": p.stdout.strip()}
            else:
                results[name] = {"available": False, "reason": "No se encontraron sensores. Comprueba que el programa compatible esté abierto."}
        except (OSError, subprocess.TimeoutExpired) as exc:
            results[name] = {"available": False, "reason": str(exc)}
    return {
        "sources": results,
        "note": "La lectura depende del controlador y de una aplicación de sensores compatible. No se deben comparar sensores con nombres o ubicaciones distintas."
    }
