import platform
import os
import shutil
import subprocess
from datetime import datetime

try:
    import psutil
except ImportError:
    psutil = None

def _run_powershell(command):
    try:
        completed = subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command],
            capture_output=True, text=True, timeout=15
        )
        return completed.stdout.strip() if completed.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None

def build_report():
    memory = {}
    cpu = {}
    disks = {}
    if psutil:
        vm = psutil.virtual_memory()
        memory = {"total_gb": round(vm.total / 1024**3, 2), "available_gb": round(vm.available / 1024**3, 2), "used_percent": vm.percent}
        cpu = {"logical_cores": psutil.cpu_count(), "physical_cores": psutil.cpu_count(logical=False), "usage_percent": psutil.cpu_percent(interval=1)}
        for part in psutil.disk_partitions(all=False):
            try:
                usage = psutil.disk_usage(part.mountpoint)
                disks[part.mountpoint] = {"total_gb": round(usage.total / 1024**3, 2), "free_gb": round(usage.free / 1024**3, 2), "used_percent": usage.percent}
            except PermissionError:
                pass
    return {
        "generated_at": datetime.now().astimezone().isoformat(),
        "system": {"platform": platform.platform(), "windows": platform.version(), "machine": platform.machine(), "processor": platform.processor(), "computer_name": platform.node()},
        "cpu": cpu,
        "memory": memory,
        "disks": disks,
        "gpu_names": _run_powershell("Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"),
        "battery": _run_powershell("(Get-CimInstance Win32_Battery | Select-Object -ExpandProperty EstimatedChargeRemaining) -join ', '"),
        "python": platform.python_version(),
        "notes": ["Las métricas de GPU y temperatura requieren soporte del fabricante o herramientas adicionales."]
    }

def format_report(report):
    import json
    return "INFORME DEL EQUIPO\n\n" + json.dumps(report, indent=2, ensure_ascii=False)
