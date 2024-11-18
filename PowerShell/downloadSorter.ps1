#$CurrentPath = Get-Location

#if ($CurrentPath -ne "C:\Users\$Env:UserName\Downloads"){
#    set-Location "C:\Users\$Env:UserName\Downloads"
#}
while ($true){
    Set-Location "$home\Downloads"
    Get-ChildItem | forEach-Object {
        if(($_).Extension -eq ('.jpg' -or '.png')){
            Move-Item $_ $home\Pictures
        }
        elseif (($_).Extension -eq ('.wav' -or '.mp4')){
            Move-Item $_ $home\Videos
        }
        elseif(($_).Extension -eq '.mp3'){
            Move-Item $_ $home\Music
        }
        else{
            Move-Item $_ $home\Documents
        }
    }
    Start-sleep -Seconds 5
}
#set-Location $CurrentPath
