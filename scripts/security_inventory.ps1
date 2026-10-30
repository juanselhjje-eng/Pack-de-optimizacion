$ErrorActionPreference = 'SilentlyContinue'
Write-Host '=== MICROSOFT DEFENDER ==='
Get-MpComputerStatus | Select-Object AntivirusEnabled,RealTimeProtectionEnabled,AntispywareEnabled,AMServiceEnabled | Format-List
Write-Host '=== FIREWALL ==='
Get-NetFirewallProfile | Select-Object Name,Enabled | Format-Table -AutoSize
Write-Host '=== SERVICIOS IMPORTANTES ==='
Get-Service WinDefend,MpsSvc,wuauserv -ErrorAction SilentlyContinue | Select-Object Name,Status,StartType | Format-Table -AutoSize
Write-Host '=== VIRTUALIZACION ==='
Get-CimInstance Win32_ComputerSystem | Select-Object HypervisorPresent | Format-List
Write-Host '=== ARRANQUE SEGURO ==='
try { Confirm-SecureBootUEFI } catch { Write-Host 'No disponible en este equipo o firmware.' }
