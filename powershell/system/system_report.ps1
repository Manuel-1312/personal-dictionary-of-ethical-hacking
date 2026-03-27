param()
$os = Get-CimInstance Win32_OperatingSystem
$cs = Get-CimInstance Win32_ComputerSystem
$bios = Get-CimInstance Win32_BIOS
[pscustomobject]@{
    ComputerName = $env:COMPUTERNAME
    UserName     = $env:USERNAME
    OS           = $os.Caption
    Version      = $os.Version
    Build        = $os.BuildNumber
    Manufacturer = $cs.Manufacturer
    Model        = $cs.Model
    MemoryGB     = [math]::Round($cs.TotalPhysicalMemory / 1GB, 2)
    BIOS         = $bios.SMBIOSBIOSVersion
    LastBoot     = $os.LastBootUpTime
} | Format-List
