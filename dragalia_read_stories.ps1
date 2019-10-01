function GetValues() {
    "1"
    "2"
}

foreach ($_ in GetValues) {
    Write-Host "s: " $_
}


$device = 'd1f0ad9e'
$sleepTime = 2
$repeatInterval = 120+20

function doubleTap($x, $y) {
    adb -s $device shell input tap $x $y
    adb -s $device shell input tap $x $y
}

function singleTap($x, $y) {
    adb -s $device shell input tap $x $y
}

function Cycle() {
    SingleTap 520 623 #Tap on top-most person
    Start-Sleep -Seconds 11

    # This step seems unecessary
    #SingleTap 530 875 #Tap to skip initial load
    #Start-Sleep -Seconds 2

    SingleTap 968 1810 #Press skip button
    Start-Sleep -Seconds 2
    SingleTap 800 1286 #Press confirm button
    Start-Sleep -Seconds 10
    SingleTap 550 1280 #Close item reward menu
    SingleTap 550 1500 #Close item reward menu
    Start-Sleep -Seconds 2
    SingleTap 290 1250 #Cancel next episode
}

function Repeat($repeatCount, $repeatInterval) {
    For ($i=1; $i -le $repeatCount; $i++) {
        Write-Host "Repeat Count:" $i
        Cycle
        Write-Host "Cycle finished..." 
    }
}


Repeat 500 1




