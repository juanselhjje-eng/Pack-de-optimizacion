# Diagnóstico de red de solo lectura.
$ErrorActionPreference = "Continue"
Write-Host "=== ADAPTADORES ==="
Get-NetAdapter | Format-Table -AutoSize
Write-Host "=== CONFIGURACION IP ==="
ipconfig /all
Write-Host "=== RUTA ==="
tracert -d 1.1.1.1
Write-Host "=== DNS ==="
nslookup example.com
Write-Host "=== LATENCIA ICMP ==="
ping -n 10 1.1.1.1
