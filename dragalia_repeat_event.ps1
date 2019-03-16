function GetValues() {
    "1"
    "2"
}

foreach ($_ in GetValues) {
    Write-Host "s: " $_
}

$sleepTime = 2
$repeatInterval = 120+20

function doubleTap($x, $y) {
    adb shell input tap $x $y
    adb shell input tap $x $y
}

function singleTap($x, $y) {
    adb shell input tap $x $y
}

function TapRepeat() {
    SingleTap 214 1843
    Start-Sleep -Seconds $sleepTime
}


function TapWithStamina() {
    SingleTap 754 1447
    Start-Sleep -Seconds $sleepTime
}

function TapConfirm() {
    SingleTap 773 1280
    Start-Sleep -Seconds $sleepTime
}


function tapEvents() {
    SingleTap 167 1532
    Start-Sleep -Seconds $sleepTime
}

function scrollToPower() {
    adb shell input swipe 550 1400 550 400 4000 # scroll down
    Start-Sleep -Seconds $sleepTime
}

function tapAvenueToPower() {
    SingleTap 550 958
    Start-Sleep -Seconds $sleepTime
}

function tapMasterDifficulty() {
    SingleTap 550 838
    Start-Sleep -Seconds $sleepTime
}

function tapFirstAdventurer() {
    SingleTap 550 979 
    Start-Sleep -Seconds $sleepTime
}

function tapBeginQuest() {
    DoubleTap 835 1620  
    Start-Sleep -Seconds $sleepTime
}

function tapAvenueToFortune() {
    DoubleTap 550 1245
    Start-Sleep -Seconds $sleepTime
}

function tapElementalRuins() {
    DoubleTap 550 1453
    Start-Sleep -Seconds $sleepTime
}

function TapBack() {
    DoubleTap 157 1645
    Start-Sleep -Seconds $sleepTime
}

function tapNext() {
    DoubleTap 900 1845
    Start-Sleep -Seconds $sleepTime
    Start-Sleep -Seconds 5
}

function closeDailyBonus() {
    DoubleTap 550 1400
    DoubleTap 550 1240
    DoubleTap 550 1533
    DoubleTap 550 1400
    DoubleTap 550 1240
    Start-Sleep -Seconds $sleepTime
}

function activateDragon() {
    SingleTap 84 1450
    Start-Sleep -Seconds 2
}

function activateSkill1() {
    SingleTap 390 1800
    Start-Sleep -Seconds 1
}

function sleepAndActivateDragon($repeatInterval) {
    $tapTimeInterval = 2
    For ($time=1; $time -lt $repeatInterval; $time += $tapTimeInterval) {
        Start-Sleep -Seconds $tapTimeInterval
        activateDragon
        activateSkill1
        Write-Host "Time:" $time
        #tapRepeat
        $time += $sleepTime + 2 + 1
    }
}


function Repeat($repeatCount, $repeatInterval) {
    For ($i=1; $i -le $repeatCount; $i++) {
        Write-Host "Repeat Count:" $i

        cancelFriendRequest
        tapNext # Next... (after quest completion)
        Start-Sleep -Seconds 1
        tapNext # Rewards
        Start-Sleep -Seconds 1
        tapNext # Tap to Proceed

        SingleTap 500 1700 # Claim rewards

        tapRepeat
        tapWithStamina
        tapConfirm
        Write-Host "Sleeping" 
        sleepAndActivateDragon $repeatInterval
        closeDailyBonus
    }
}

function cancelFriendRequest() {
    SingleTap 300 1300
    Start-Sleep -Seconds $sleepTime
}



sleepAndActivateDragon 100
Repeat 5 100


