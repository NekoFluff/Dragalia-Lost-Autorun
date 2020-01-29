import os
import numpy as np

# THIS IS A FILE TO FIX RECENTLY MISLABELED DATA
# NO LONGER IN USE

image_data = None
image_labels = None
labeled_images = None


def load_data():
    if os.path.exists('./data/already_labeled_images.npy'):
        global image_data
        global image_labels
        global labeled_images
        image_data = np.load('./data/image_data.npy')
        image_labels = np.load('./data/image_labels.npy')
        labeled_images = np.load('./data/already_labeled_images.npy')
        # print(data)
        print('Data shape:', image_data.shape)
        print('Labels shape:', image_labels.shape)
        print('Labeled Images shape:', labeled_images.shape)
        print('Last 5 labels:', labeled_images[-5:])
        print('Last 5 label values:', image_labels[-5:])


load_data()

print(image_labels[-1])
print(image_labels[-2])
print(image_labels[-3])
print(image_labels[-4])
print(image_labels[-5])
print(image_labels[-6])
print(image_labels[-7])
print(image_labels[-8])
print(image_labels[-9])
print(image_labels[-10])

# USE THIS LINE TO FIX MISLABELED DATA
# image_labels[-6] = 11
new_labels = []
for x in image_labels:
    y = np.array([int(x)])
    new_labels.append(y)

print(new_labels)
np.save('./data/image_labels2.npy', new_labels)
