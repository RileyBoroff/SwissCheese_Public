Write-Host "Enter a user:" -NoNewline
$user = Read-Host
Write-Host "Enter a password for the user" -NoNewline
$password = Read-Host -AsSecureString

$hideUser = Read-Host "Do you want to hide this user from the login screen?(Will disable nor rdp login) (Y/N)"

if ($hideUser -eq "Y" -or $hideUser -eq "y") {
    $description = "HIDDEN"
} else {
    $description = ""
}

# Create the user account with or without a description
New-LocalUser -Name "rdpuser" -Password $password -Description $description
try {
Add-LocalGroupMember -Group "Administrators" -Member "$user"
}
catch {
    Write-Host "An error occurred adding the account to the Administrators group: $_"
}
# Check if the user already exists in the group
$group = [ADSI]("WinNT://./Remote Desktop Users,group")
$members = $group.Invoke("Members") | ForEach-Object { $_.GetType().InvokeMember("Name", 'GetProperty', $null, $_, $null) }

if ($members -notcontains $user) {
    try {
        # Add the user to the Remote Desktop Users group
        $group.Add("WinNT://$user")
    } catch {
        Write-Host "An error occurred adding $user to the RDP users group: $_"
    }
}
