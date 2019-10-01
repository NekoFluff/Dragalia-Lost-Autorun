from PIL import Image


def resize(filename, size):
    # size = 270, 480
    # size = 135, 240
    # size = 27, 48
    # size = 54, 96
    im = Image.open(filename + ".png")
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save(filename + "-cropped.png", "PNG")


def crop(filename):
    im = Image.open(filename + ".png")
    box = (550, 1750, 1080, 1900)
    cropped_im = im.crop(box)
    cropped_im.save(filename + "-cropped.png", "PNG")
    print(cropped_im.size)


crop("./screenshots/screencap")
resize('./screenshots/screencap-cropped', (106, 30))
