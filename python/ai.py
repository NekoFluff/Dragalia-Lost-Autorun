# This is the main file that is run to automate dragalie

import tensorflow as tf
import numpy as np
from tensorflow.keras import datasets, layers, models
from python.screenshotter import screenshot
from python.image_to_data import convert_image_to_data
from python.pillow_image_compression import crop_and_resize, index_to_label, label_to_index
import time
import subprocess

model = tf.keras.models.load_model('./models/dragalia_model.h5')
real_time_image_path = './screenshots/_real-time.png'


def check_if_exists(label, filename, alternate_value=0):
    # Crop & resize a section of the screenshot
    new_file_path = crop_and_resize(filename, label, (32, 32))

    # Convert cropped & resized image into data
    np_frame = convert_image_to_data(new_file_path, suppress_log=True)

    # Perform a prediction and act on it.
    prediction = model.predict(np_frame)
    val = np.argmax(prediction[0])
    matched = val == label_to_index[label] if alternate_value == 0 else val == alternate_value
    if (matched):
        print('AI RESULT:', val, 'a.k.a', index_to_label[val], ' | Result matched?:', val == label_to_index[label])
    return matched

def auto_pic():
    index = 0
    while(True):
        # label = input('\nWhat would you like to check for the existence of?\n')

        # TODO: Remove or comment out
        time.sleep(3)
        label = 'dragon_ready'
        real_time_image_path = './screenshots/_real-time-{}.png'.format(index)

        screenshot(real_time_image_path)
        check_if_exists(label, '_real-time-{}'.format(index))

        index += 1


# IDEA: Store check_if_exist results and reset after every screenshot
def auto_run_dungeon(times):
    real_time_image_path = './screenshots/_real-time.png'
    index = 0
    while(times > 0):
        time.sleep(2.5)
        screenshot(real_time_image_path)
        # press_next_if_ready()
        press_skip_if_ready()
        press_close_if_ready()
        # press_home_if_ready()
        # press_upgrade_if_ready()
        # press_teams_if_ready()
        # press_castle_if_ready()
        # press_summon_if_ready()
        press_dragon_if_ready()
        press_auto_enable_if_disabled()
        # press_more_if_ready()
        if not check_if_exists('stamina', '_real-time') and not check_if_exists('confirm', '_real-time') and100press_repeat_if_ready():
            times -= 1
        press_stamina_if_ready()

        # press_ticket_if_ready()
        press_confirm_if_ready()


def tap_at_point(x, y):
    subprocess.call(['adb', 'shell', 'input',
                         'tap', x, y])
    print('Tapped at', (x,y))
    time.sleep(1.25)

def press_next_if_ready():
    if check_if_exists('next', '_real-time'):
        tap_at_point('900', '1845')
        return True

def press_skip_if_ready():
    if check_if_exists('skip', '_real-time'):
        tap_at_point('968', '1810')
        return True

def press_close_if_ready():
    if check_if_exists('close', '_real-time'):
        tap_at_point('550', '1280')
        return True

def press_home_if_ready():
    if check_if_exists('home', '_real-time'):
        tap_at_point('100', '1825')
        return True

def press_upgrade_if_ready():
    if check_if_exists('upgrade', '_real-time'):
        tap_at_point('275', '1825')
        return True

def press_teams_if_ready():
    if check_if_exists('teams', '_real-time'):
        tap_at_point('450', '1825')
        return True

def press_castle_if_ready():
    if check_if_exists('castle', '_real-time'):
        tap_at_point('625', '1825')
        return True

def press_summon_if_ready():
    if check_if_exists('summon', '_real-time'):
        tap_at_point('800', '1825')
        return True

def press_dragon_if_ready():
    if check_if_exists('dragon_ready', '_real-time'):
        tap_at_point('150', '1520')
        return True

def press_auto_enable_if_disabled():
    if check_if_exists('auto_enabled', '_real-time', 12):
        tap_at_point('1000', '440')
        return True

def press_more_if_ready():
    # if check_if_exists('more', '_real-time'):
    #     tap_at_point('1000', '440')
    #     return True
    return False

def press_repeat_if_ready():
    if check_if_exists('repeat', '_real-time'):
        tap_at_point('190', '1825')
        return True

def press_stamina_if_ready():
    if check_if_exists('stamina', '_real-time'):
        tap_at_point('800', '1450')
        return True

def press_ticket_if_ready():
    if check_if_exists('ticket', '_real-time'):
        tap_at_point('400', '1450')
        return True

def press_confirm_if_ready():
    if check_if_exists('confirm', '_real-time'):
        tap_at_point('775', '1275')
        return True

if __name__ == "__main__":
    # auto_pic()
    while (True):
        user_input = input('\nHow many times do you want to run this dungeon?\n')
        auto_run_dungeon(int(user_input))
