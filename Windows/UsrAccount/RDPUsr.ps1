Write-Host "Enter a password for the RDPUser:" -NoNewline
$password = Read-Host -AsSecureString

$hideUser = Read-Host "Do you want to hide this user from the login screen?(Will disable nor rdp login) (Y/N)"

if ($hideUser -eq "Y" -or $hideUser -eq "y") {
    $description = "HIDDEN"
} else {
    $description = ""
}
New-LocalUser -Name "rdpuser" -Password $password -Description $description
try {
Add-LocalGroupMember -Group "Administrators" -Member "rdpuser"
}
catch {
    Write-Host "An error occurred adding the account to the Administrators group: $_"
}
# Check if the user already exists in the Remote Desktop Users group
$group = [ADSI]("WinNT://./Remote Desktop Users,group")
$members = $group.Invoke("Members") | ForEach-Object { $_.GetType().InvokeMember("Name", 'GetProperty', $null, $_, $null) }

if ($members -notcontains "rdpuser") {
    try {
        # Add the user to the Remote Desktop Users group
        $group.Add("WinNT://rdpuser")
    } 
    catch {
        Write-Host "An error occurred adding the account to the Remote Desktop Users group: $_"
    }
}
