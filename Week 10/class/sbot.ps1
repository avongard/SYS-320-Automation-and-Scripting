# Send an email using Powershell

$toSend = @('michael.portegello@mymail.champlain.edu','')

# Message body
$msg = "Hello"
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