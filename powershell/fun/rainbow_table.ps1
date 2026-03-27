param([string]$Text = 'LAB ACTIVE')
$colors = 'Red','Yellow','Green','Cyan','Blue','Magenta'
$i = 0
foreach ($char in $Text.ToCharArray()) {
  Write-Host -NoNewline $char -ForegroundColor $colors[$i % $colors.Count]
  $i++
}
Write-Host ''
