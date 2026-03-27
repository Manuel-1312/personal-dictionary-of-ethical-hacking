param([int]$Seconds = 5)
for ($i = $Seconds; $i -ge 1; $i--) {
  Write-Host "Iniciando lab en $i..." -ForegroundColor Cyan
  Start-Sleep -Seconds 1
}
Write-Host 'Go.' -ForegroundColor Green
