#$CurrentPath = Get-Location

#if ($CurrentPath -ne "C:\Users\$Env:UserName\Downloads"){
#    set-Location "C:\Users\$Env:UserName\Downloads"
#}
while ($true){
    Set-Location "C:\Users\ianms\Downloads"
    Get-ChildItem | forEach-Object {
        if(($_).Extension -eq ('.jpg' -or '.png')){
            Move-Item $_ C:\Users\ianms\Pictures
        }
        elseif (($_).Extension -eq ('.wav' -or '.mp4')){
            Move-Item $_ C:\Users\ianms\Videos
        }
        elseif(($_).Extension -eq '.mp3'){
            Move-Item $_ C:\Users\ianms\Music
        }
        else{
            Move-Item $_ C:\Users\ianms\Documents
        }
    }
    Start-sleep -Seconds 5
}
#set-Location $CurrentPath