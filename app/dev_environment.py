import shutil
import subprocess

TOOLS = {
    "Python": ["python", "--version"],
    "Python Launcher": ["py", "--version"],
    "Git": ["git", "--version"],
    "Node.js": ["node", "--version"],
    "npm": ["npm", "--version"],
    "VS Code": ["code", "--version"],
    "Cursor": ["cursor", "--version"]
}

def scan_development_tools():
    results = {}
    for name, command in TOOLS.items():
        executable = shutil.which(command[0])
        if not executable:
            results[name] = {"installed": False, "path": None, "version": None}
            continue
        try:
            completed = subprocess.run(command, capture_output=True, text=True, timeout=8)
            version = (completed.stdout or completed.stderr).strip().splitlines()
            results[name] = {
                "installed": True,
                "path": executable,
                "version": version[0] if version else "Versión no disponible"
            }
        except (OSError, subprocess.TimeoutExpired):
            results[name] = {"installed": True, "path": executable, "version": "No se pudo consultar"}
    return results
