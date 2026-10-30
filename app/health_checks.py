import shutil
import platform

def run_health_checks():
    return {
        "python_version": platform.python_version(),
        "powershell_available": shutil.which("powershell") is not None,
        "nvidia_smi_available": shutil.which("nvidia-smi") is not None,
        "git_available": shutil.which("git") is not None,
        "winget_available": shutil.which("winget") is not None,
        "note": "Este módulo solo comprueba la disponibilidad de herramientas; no ejecuta reparaciones."
    }
