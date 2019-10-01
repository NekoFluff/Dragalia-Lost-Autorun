import subprocess
subprocess.call(['adb', 'shell', 'screencap', '-p', '/sdcard/screencap.png'])
print('Screenshotted')

subprocess.call(
    ['adb', 'pull', './screenshots/screencap.png', './screenshots'])
print('Pulled screenshot')
