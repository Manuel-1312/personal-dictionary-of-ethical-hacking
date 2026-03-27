param([string]$Text = 'LAB ACTIVE', [int]$Delay = 40)
foreach ($char in $Text.ToCharArray()) {
  Write-Host -NoNewline $char
  Start-Sleep -Milliseconds $Delay
}
Write-Host ''
