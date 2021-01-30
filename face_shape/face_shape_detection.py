import tensorflow
import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder
from pandas import get_dummies
from keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt
import keras.backend.tensorflow_backend as K
from PIL import Image
import os, glob, sys, numpy as np
from sklearn.model_selection import train_test_split
from keras.utils import np_utils

img_dir = './dataset/training_set'
categories = ['Oblong', 'Round','Square']
np_classes = len(categories)

image_w = 64
image_h = 64


pixel = image_h * image_w * 3

X = []
y = []

for idx, oblong in enumerate(categories):
    img_dir_detail = img_dir + "/" + oblong
    files = glob.glob(img_dir_detail+"/*.jpg")


    for i, f in enumerate(files):
        try:
            img = Image.open(f)
            img = img.convert("RGB")
            img = img.resize((image_w, image_h))
            data = np.asarray(img)
            #Y는 0 아니면 1이니까 idx값으로 넣는다.
            X.append(data)
            y.append(idx)
            if i % 300 == 0:
                print(oblong, " : ", f)
        except:
            print(oblong, str(i)+" 번째에서 에러 ")
X = np.array(X)
Y = np.array(y)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

xy = (X_train, X_test, Y_train, Y_test)
np.save("./binary_image_data.npy", xy)


## Create the CNN Model
X_train, X_test, y_train, y_test = np.load('./binary_image_data.npy')

image_w = 64
image_h = 64
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

# conv layers
with K.tf_ops.device('/device:GPU:0'):
    model = Sequential()
    model.add(Conv2D(2, (3, 3), input_shape=(150, 150, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(20, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(90, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

#  fully connected layers
    model.add(Flatten())

    model.add(Dense(activation='relu', units=64))
    model.add(Dense(activation='softmax', units=4))

    model.compile(loss='sparse_categorical_crossentropy',
                 optimizer='adam',
                  metrics=['accuracy'])
    model_dir = './model'
    if not os.path.exists(model_dir):
        os.mkdir(model_dir)
    model_path = model_dir + "/face_classify.model"

    checkpoint = ModelCheckpoint(filepath=model_path, monitor='val_loss', verbose=1, save_best_only=True)
    early_stopping = EarlyStopping(monitor='val_loss', patience=7)

'''
train_datagen = ImageDataGenerator(
        rescale=1./255,
       )
test_datagen = ImageDataGenerator(rescale=1./255)

## Import Data

#import dataset
train_set = train_datagen.flow_from_directory('./dataset/training_set',
                                            target_size=(64, 64),
                                            batch_size=6,
                                            class_mode='binary')
test_set = train_datagen.flow_from_directory('./dataset/test_set',
                                            target_size=(64, 64),
                                            batch_size=6,
                                            class_mode='binary')
#load dataset
(trainX, trainy) = train_set.load_data()
(testX, testy) = test_set.load_data()

# summarize loaded dataset
print('Train: X=%s, y=%s' % (trainX.shape, trainy.shape))
print('Test: X=%s, y=%s' % (testX.shape, testy.shape))

## Data Pre-processing

# reshape dataset to have a single channel
trainX = trainX.reshape((trainX.shape[0], 28, 28, 3))
testX = testX.reshape((testX.shape[0], 28, 28, 3))

# scale data to the range of [0, 1]
trainX = trainX.astype("float32") / 255.0
testX = testX.astype("float32") / 255.0

#One hot encoding
trainy = get_dummies(trainy)
trainy =trainy.values

testy = get_dummies(testy)
testy =testy.values
'''
## Train the Model
'''
model.fit(
    trainX,trainy, batch_size=100,
    epochs=10, verbose=1,
    validation_data=(testX,testy),
)'''
history = model.fit(X_train, y_train, batch_size=64, epochs=100,
                    validation_split=0.15,
                    callbacks=[checkpoint, early_stopping])
print("정확도 : %.2f " %(model.evaluate(X_test, y_test)[1]))

#### Predition

import cv2

## Import Data

## prediction of single new data
from keras.preprocessing import image
from keras.models import load_model

model = load_model('./model/face_classify.model')
test_image= image.load_img('./image/ex1.jpg'
                           ,target_size =(150,150))

test_image

## Pre-processing

## Convert image to array
test_image = image.img_to_array(test_image)
test_image.shape
test_image=test_image.reshape(1,150, 150, 3)

## Make Prediction

## For single prediction change the dimension using axis. To remove problem of batch
#test_image = np.expand_dims(test_image,axis = 0)
result = model.predict(test_image)
np.around(result)
result=result.argmax()
result
## Class label of garment

if result == 0:
    prediction = 'Oblong'
elif result == 1:
    prediction = 'Round'
elif result == 2:
    prediction = 'Square'

prediction
