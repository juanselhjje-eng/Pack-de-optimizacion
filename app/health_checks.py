import shutil
import subprocess
import platform

def run_health_checks():
    checks = {
        "python": platform.python_version(),
        "powershell": shutil.which("powershell"),
        "nvidia_smi": shutil.which("nvidia-smi"),
        "git": shutil.which("git"),
        "winget": shutil.which("winget")
    }
    try:
        p = subprocess.run(["sfc", "/verifyonly"], capture_output=True, text=True, timeout=2)
        checks["system_file_checker"] = {
            "started": False,
            "note": "No se ejecutó el análisis porque SFC puede tardar y requiere una acción separada."
        }
    except (OSError, subprocess.TimeoutExpired):
        checks["system_file_checker"] = {"started": False}
    return checks
