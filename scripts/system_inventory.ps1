# Inventario de solo lectura. No modifica la configuración.
$ErrorActionPreference = "SilentlyContinue"
Write-Host "=== SISTEMA ==="
Get-CimInstance Win32_ComputerSystem | Select-Object Manufacturer, Model, TotalPhysicalMemory
Write-Host "=== CPU ==="
Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed
Write-Host "=== MEMORIA ==="
Get-CimInstance Win32_PhysicalMemory | Select-Object Manufacturer, Capacity, Speed
Write-Host "=== GPU ==="
Get-CimInstance Win32_VideoController | Select-Object Name, DriverVersion, AdapterRAM
Write-Host "=== DISCOS ==="
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, OperationalStatus, Size
Write-Host "=== RED ==="
Get-NetAdapter | Select-Object Name, InterfaceDescription, Status, LinkSpeed
