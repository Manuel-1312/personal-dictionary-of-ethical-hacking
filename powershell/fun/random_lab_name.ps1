param([int]$Count = 3)
$adjectives = 'Silent','Ghost','Velvet','Crimson','Midnight','Dusty'
$nouns = 'Router','Falcon','Signal','Mantis','Circuit','Lantern'
1..$Count | ForEach-Object {
    "$($adjectives | Get-Random) $($nouns | Get-Random)"
}
