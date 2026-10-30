# Diagnóstico de almacenamiento. No borra archivos.
Write-Host "=== VOLUMENES ==="
Get-Volume | Select-Object DriveLetter, FileSystemLabel, FileSystem, HealthStatus, Size, SizeRemaining
Write-Host "=== DISCOS FISICOS ==="
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, OperationalStatus, Size
Write-Host "=== ESPACIO TEMPORAL ==="
$temp = $env:TEMP
Get-ChildItem $temp -Force -ErrorAction SilentlyContinue |
    Measure-Object -Property Length -Sum |
    Select-Object Count, Sum
