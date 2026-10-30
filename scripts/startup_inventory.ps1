# Lista de ubicaciones comunes de inicio. Solo lectura.
Write-Host "=== INICIO: REGISTRO DEL USUARIO ==="
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" | Format-List
Write-Host "=== INICIO: REGISTRO DEL EQUIPO ==="
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" | Format-List
Write-Host "=== CARPETA DE INICIO DEL USUARIO ==="
Get-ChildItem "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup" -Force |
    Select-Object Name, FullName, Length
Write-Host "=== CARPETA DE INICIO GLOBAL ==="
Get-ChildItem "$env:ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp" -Force |
    Select-Object Name, FullName, Length
