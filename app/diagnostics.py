import platform
import subprocess
from datetime import datetime

try:
    import psutil
except ImportError:
    psutil = None

def _powershell(command):
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command", command],
            capture_output=True, text=True, timeout=20
        )
        return result.stdout.strip() if result.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None

def build_report():
    vm = psutil.virtual_memory() if psutil else None
    cpu_percent = psutil.cpu_percent(interval=1) if psutil else None
    disks = {}
    if psutil:
        for part in psutil.disk_partitions(all=False):
            try:
                usage = psutil.disk_usage(part.mountpoint)
                disks[part.mountpoint] = {
                    "total_gb": round(usage.total / 1024**3, 2),
                    "free_gb": round(usage.free / 1024**3, 2),
                    "used_percent": usage.percent
                }
            except (PermissionError, OSError):
                continue
    return {
        "generated_at": datetime.now().astimezone().isoformat(),
        "system": {
            "platform": platform.platform(),
            "windows_version": platform.version(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "computer_name": platform.node()
        },
        "cpu": {
            "physical_cores": psutil.cpu_count(logical=False) if psutil else None,
            "logical_cores": psutil.cpu_count(logical=True) if psutil else None,
            "usage_percent": cpu_percent
        },
        "memory": {
            "total_gb": round(vm.total / 1024**3, 2) if vm else None,
            "available_gb": round(vm.available / 1024**3, 2) if vm else None,
            "used_percent": vm.percent if vm else None
        },
        "disks": disks,
        "gpu": _powershell("Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"),
        "physical_disks": _powershell("Get-PhysicalDisk | Select-Object FriendlyName,MediaType,HealthStatus,OperationalStatus,Size | ConvertTo-Json -Compress"),
        "network_adapters": _powershell("Get-NetAdapter | Select-Object Name,InterfaceDescription,Status,LinkSpeed | ConvertTo-Json -Compress"),
        "battery": _powershell("Get-CimInstance Win32_Battery | Select-Object EstimatedChargeRemaining,BatteryStatus | ConvertTo-Json -Compress"),
        "python_version": platform.python_version(),
        "limitations": [
            "La temperatura depende de sensores y controladores compatibles.",
            "La información de GPU puede no incluir telemetría en tiempo real.",
            "El ping ICMP no equivale al ping dentro de un juego."
        ]
    }

def format_report(report):
    import json
    return "INFORME DEL EQUIPO\\n\\n" + json.dumps(report, indent=2, ensure_ascii=False)
