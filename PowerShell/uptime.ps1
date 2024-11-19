<#will take as input, services from a user, then check connectivity over a given time interval until stopped#>

$raw_services = read-host("please enter the IPv4 addresses of services you would like to monitor, separated by a comma ")

$services = $raw_services -split (",")

while ($true){
	for ($i = 0; $i -lt $services.Length; $i++){
		$currentService = $services[$i]
		[string]$response = ping $currentService
		if ($response -match "Destination host unreachable"){
			write-host "$currentService appears to be down"
			write-host "Press enter to dismiss alarm"
			while($true){
				if ([Console]::KeyAvailable){
					$key = [Console]::ReadKey($true)
					if ($key.Key -eq "Enter"){
						break
					}
				}
				[console]::Beep(1000,500)
			}
			write-host "Alarm dismissed, please fix issue in order to prevent alarm from triggering again"
		}

		else{
			write-host "$currentService is up"
		}
	}
	Start-Sleep -Seconds 10	
}

