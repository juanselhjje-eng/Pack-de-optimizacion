import shutil
import subprocess

def nvidia_status():
    executable = shutil.which("nvidia-smi")
    if not executable:
        return {
            "available": False,
            "reason": "No se encontró nvidia-smi. Puede faltar el controlador NVIDIA o no estar en PATH."
        }
    query = [
        executable,
        "--query-gpu=name,temperature.gpu,utilization.gpu,memory.total,memory.used,power.draw",
        "--format=csv,noheader,nounits"
    ]
    try:
        p = subprocess.run(query, capture_output=True, text=True, timeout=8)
        if p.returncode != 0:
            return {"available": False, "reason": p.stderr.strip() or "Consulta NVIDIA no disponible."}
        return {"available": True, "raw": p.stdout.strip(),
                "fields": ["name", "temperature_c", "utilization_percent", "memory_total_mb", "memory_used_mb", "power_w"]}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"available": False, "reason": str(exc)}
