write-host 'Hello World'

$scriptPath = $MyInvocation.MyCommand.Path

$newContent = "write-host 'hack the planet'"

Set-Content -Path $scriptPath -Value $newContent
