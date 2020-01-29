import subprocess
import os

# This module will take screenshots for you!
# If you run this module it will take a screenshot whenever you press enter.
def screenshot(savePath):
    subprocess.call(['adb', 'shell', 'screencap',
                     '-p', '/sdcard/screencap.png'])
    print('Screenshotted')

    subprocess.call(
        ['adb', 'pull', '/sdcard/screencap.png', savePath])
    print('Pulled screenshot')


if __name__ == "__main__":
    index = 0
    savePath = './screenshots/screencap-{}.png'.format(index)

    while(True):
        while (os.path.exists(savePath)):
            index += 1
            savePath = './screenshots/screencap-{}.png'.format(index)

        input('Press enter when ready.')
        screenshot(savePath)
