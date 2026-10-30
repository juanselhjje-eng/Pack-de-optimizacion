import subprocess

def _ps(command):
    try:
        p = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", command],
            capture_output=True, text=True, timeout=20)
        return p.stdout.strip() if p.returncode == 0 else p.stderr.strip()
    except (OSError, subprocess.TimeoutExpired) as exc:
        return str(exc)

def scan_startup_entries():
    commands = {
        "current_user_run": "Get-ItemProperty 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run' | Select-Object * -ExcludeProperty PS* | ConvertTo-Json -Compress",
        "local_machine_run": "Get-ItemProperty 'HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run' | Select-Object * -ExcludeProperty PS* | ConvertTo-Json -Compress",
        "user_startup_folder": "Get-ChildItem (Join-Path $env:APPDATA 'Microsoft\\Windows\\Start Menu\\Programs\\Startup') -Force | Select-Object Name,FullName | ConvertTo-Json -Compress",
        "common_startup_folder": "Get-ChildItem (Join-Path $env:ProgramData 'Microsoft\\Windows\\Start Menu\\Programs\\StartUp') -Force | Select-Object Name,FullName | ConvertTo-Json -Compress"
    }
    return {
        "entries": {name: _ps(command) for name, command in commands.items()},
        "changed": False,
        "note": "Inventario de solo lectura. No deshabilita programas."
    }
