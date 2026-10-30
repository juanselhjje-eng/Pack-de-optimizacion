# Consulta los planes de energía; no cambia el plan activo.
Write-Host "=== PLANES DISPONIBLES ==="
powercfg /list
Write-Host "=== PLAN ACTIVO ==="
powercfg /getactivescheme
Write-Host "=== INFORME DE BATERIA ==="
$report = Join-Path $env:TEMP "ultimate-pc-battery-report.html"
powercfg /batteryreport /output $report
Write-Host "Informe generado en: $report"
