from __future__ import absolute_import, division, print_function, unicode_literals

import os
import tensorflow as tf
import numpy as np
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt


def split(x, y, train_ratio=0.9):
    x_size = x.shape[0]
    train_size = int(x_size * train_ratio)
    test_size = x_size - train_size
    train_indices = np.random.choice(x_size, size=train_size, replace=False)
    mask = np.zeros(x_size, dtype=bool)
    mask[train_indices] = True
    x_train, y_train = x[mask], y[mask]
    x_test, y_test = x[~mask], y[~mask]
    return (x_train, y_train), (x_test, y_test)

# VERIFY DATA


def verify():
    class_names = [
        'invalid',
        'next',
        'skip',
        'close',
        'home',
        'upgrade',
        'teams',
        'castle',
        'summon',
        'dragon_ready',
        'dragon_not_ready',
        'auto_enabled',
        'auto_disabled',
        'more',
        'repeat',
        'stamina',
        'ticket',
        'confirm'
    ]

    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        # The CIFAR labels happen to be arrays,
        # which is why we need the extra index
        plt.xlabel(class_names[train_labels[i][0]])
    plt.show()


# CREATE CNN
def create_model():
    model = models.Sequential()
    model.add(layers.Conv2D(
        32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(18, activation='softmax'))

    # Compile and train
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model


def evaluate():
    # Evaluate the model
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0.5, 1])
    plt.legend(loc='lower right')
    # plt.show()

    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

    # result = model.predict(test_images)
    # for idx, val in enumerate(result):
    #     if np.argmax(val) != test_labels[idx][0]:
    #         print('Diff at index:', idx, 'Prediction:',
    #               np.argmax(val), 'Actual:', test_labels[idx][0])


def create_checkpoint(model):
    model.save_weights('./checkpoints/my_checkpoint')


def laod_checkpoint(model):
    model.load_weights('./checkpoints/my_checkpoint')


# create_checkpoint(model)


# -------------------
# print("Test")

# model = create_model()
# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
# laod_checkpoint(model)
# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# ---------------------
# print("Save full model")


def save_model(model):
    model.save('./models/dragalia_model.h5')


def load_model():
    # Recreate the exact same model, including its weights and the optimizer
    return tf.keras.models.load_model('./models/dragalia_model.h5')


# save_model(model)
# model = load_model()
# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

if __name__ == "__main__":

    # GET DATA
    train_images = np.load('./data/image_data.npy')
    train_labels = np.load('./data/image_labels2.npy')
    test_images = train_images
    test_labels = train_labels

    # (train_images, train_labels), (test_images, test_labels) = split(
    #     train_images, train_labels)

    print('First 5 train labels:', train_labels[:5])

    model = None
    if os.path.exists('./models/dragalia_model.h5'):
        model = load_model()
    else:
        model = create_model()
    model.summary()

    history = model.fit(train_images, train_labels, epochs=50,
                        validation_data=(test_images, test_labels))
    save_model(model)
