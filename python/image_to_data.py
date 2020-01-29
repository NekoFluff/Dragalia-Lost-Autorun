import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import subprocess
from PIL import Image
import numpy as np
import os

image_data = np.array([])
image_labels = np.array([])
labeled_images = np.array([])

# Use this module to convert all pictures taken into viable training data

def what_is_it(image_path):
    imgplot = plt.imshow(mpimg.imread(image_path))
    plt.ion()
    plt.show()
    label = int(input("What is this?: "))
    plt.close()
    return label


def load_data():
    if os.path.exists('./data/already_labeled_images.npy'):
        global image_data
        global image_labels
        global labeled_images
        image_data = np.load('./data/image_data.npy')
        image_labels = np.load('./data/image_labels2.npy')
        labeled_images = np.load('./data/already_labeled_images.npy')
        # print(data)
        print('Data shape:', image_data.shape)
        print('Labels shape:', image_labels.shape)
        print('Labeled Images shape:', labeled_images.shape)
        print('Last 5 labels:', labeled_images[-5:])
        print('Last 5 label values:', image_labels[-5:])


def convert_image_to_data(full_path, suppress_log=False):
    if (suppress_log == False):
        print('Converting image {} to data'.format(full_path))

    im_frame = Image.open(full_path)
    np_frame = np.array(im_frame.getdata()).reshape((32, 32, 4))
    np_frame = np.delete(np_frame, 3, 2)
    np_frame = np_frame / 255.0
    np_frame = np.expand_dims(np_frame, axis=0)
    im_frame.close()
    # print(np_frame)
    # print(np_frame.shape)
    return np_frame


def add_training_data(full_path):
    load_data()
    global image_data
    global image_labels

    np_frame = convert_image_to_data(full_path)
    image_data = np.vstack((image_data, np_frame))

    label = int(what_is_it(full_path))
    image_labels = np.vstack((image_labels, [[label]]))

    np.save('./data/image_data.npy', image_data)
    np.save('./data/image_labels2.npy', image_labels)

# Attempts to convert ALL the images in the screenshots/resized folder
# If the file name was previously used, it would re-add it'
# Use the add_training_data method instead
def convert_all_images():
    load_data()

    folder_path = './screenshots/resized/'
    onlyfiles = [f for f in os.listdir(folder_path) if os.path.isfile(
        os.path.join(folder_path, f))]

    for filename in onlyfiles:
        global image_data
        global image_labels
        global labeled_images
        if filename[:-4] in labeled_images:
            continue

        full_path = folder_path + filename
        filename = filename[:-4]

        np_frame = convert_image_to_data(full_path)

        if image_data.size > 0:
            # print(image_data.shape)
            # print(np_frame.shape)
            image_data = np.vstack((image_data, np_frame))
        else:
            image_data = np_frame
        print(image_data.shape)

        label = int(what_is_it(full_path))
        image_labels = np.vstack((image_labels, [[label]]))

        np.save('./data/image_data.npy', image_data)
        np.save('./data/image_labels2.npy', image_labels)

        # Mark image as labeled
        labeled_images = np.append(labeled_images, [filename])
        np.save('./data/already_labeled_images.npy', labeled_images)


if __name__ == "__main__":
    # THIS IS THE MAIN METHOD 
    convert_all_images()

    # THIS WAS TEMPORARY TO ADD MORE DRAGON-READY DATA
    # for i in range(20):
    #     path = './screenshots/resized/_real-time-{}-dragon_ready.png'.format(i)
    #     if os.path.exists(path):
    #         add_training_data(path)

    # THIS WAS TEMPORARY TO ADD A CERTAIN TIME SKIP IMAGE TO TRAINING
    # path = './screenshots/resized/_real-time-skip.png'
    # add_training_data(path)
    