try {
    # Check if Remote Desktop is enabled
    $rdpEnabled = Get-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections"

    if ($rdpEnabled.fDenyTSConnections -eq 0) {
        Write-Host "Remote Desktop is already enabled."
    } else {
        # Enable Remote Desktop
        Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0
        Write-Host "Remote Desktop has been enabled."
    }
}
catch {
    Write-Host "An error occurred: $_"
}


