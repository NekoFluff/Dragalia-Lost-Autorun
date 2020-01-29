from PIL import Image
import os

# This module has functions to crop and resize the photos in the screenshots folder

# Always crop() before calling resize()
# TODO: Make values of box_locations an array. Such that they can exist in multiple locations
box_locations = {
    'next': (750, 1750, 900, 1900),
    'skip': (900, 1750, 1050, 1900),
    'close': (450, 1175, 600, 1325),
    'home': (25, 1750, 175, 1900),
    'upgrade': (375, 1750, 525, 1900),
    'teams': (550, 1750, 700, 1900),
    'castle': (725, 1750, 875, 1900),
    'summon': (900, 1750, 1050, 1900)
    'dragon_ready': (25, 1400, 225, 1600),
    'auto_enabled': (925, 365, 1075, 515),
    #'more': (a,b,c,d),
    'repeat': (115, 1750, 265, 1900),
    'stamina': (700, 1350, 900, 1550),
    'ticket': (300, 1350, 500, 1550),
    'confirm': (700, 1200, 850, 1350),
    'quests': (200, 1750, 350, 1900), # no data
}

index_to_label = {
    0: 'invalid',
    1: 'next',
    2: 'skip',
    3: 'close',
    4: 'home',
    5: 'upgrade',
    6: 'teams',
    7: 'castle',
    8: 'summon',
    9: 'dragon_ready',
    10: 'dragon_not_ready',
    11: 'auto_enabled',
    12: 'auto_disabled',
    13: 'more',
    14: 'repeat',
    15: 'stamina',
    16: 'ticket',
    17: 'confirm',
    18: 'quests',
}

label_to_index = {v: k for k, v in index_to_label.items()}


def crop(filename, box):
    im = Image.open("./screenshots/" + filename + ".png")
    cropped_im = im.crop(box_locations[box])
    cropped_im.save("./screenshots/cropped/" +
                    filename + "-" + box + ".png", "PNG")
    # print('Cropped to size:', cropped_im.size)
    im.close()


def resize(filename, box, size):
    im = Image.open("./screenshots/cropped/" + filename + "-" + box + ".png")
    im_resized = im.resize(size, Image.ANTIALIAS)
    final_path = "./screenshots/resized/" + filename + "-" + box + ".png"
    im_resized.save(final_path, "PNG")
    im.close()
    return final_path


def crop_and_resize(filename, box, new_size):
    crop(filename, box)
    return resize(filename, box, new_size)


def run():
    screenshots_path = './screenshots/'
    onlyfiles = [f for f in os.listdir(screenshots_path) if os.path.isfile(
        os.path.join(screenshots_path, f))]

    for filename in onlyfiles:
        print('Cropping pieces from screenshot:', filename)
        filename = filename[:-4]
        for box in box_locations.keys():
            crop_and_resize(filename, box, (32, 32))


def test():
    filename = 'screencap-26'
    crop_and_resize(filename, 'confirm', (32, 32))


if __name__ == "__main__":
    # test()
    run()
