'''
Convolutional Neural Network

Installing Theano
pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

Installing Tensorflow
pip install tensorflow

Installing Keras
pip install --upgrade keras


##### 참고 사이트
https://github.com/VinitaSilaparasetty/face_shape_analyzer / CNN 얼굴모양구분
https://github.com/dsmlr/faceshape / 얼굴 데이터셋
https://becominghuman.ai/building-an-image-classifier-using-deep-learning-in-python-totally-from-a-beginners-perspective-be8dbaf22dd8
//CNN 개-고양이 구분
'''

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model
from keras.callbacks import ModelCheckpoint
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

'''
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
'''

classifier = Sequential()
#img_rows, img_cols = 64, 64
#input_shape = (None, img_rows, img_cols, 1)
#classifier = classifier.reshape(None, 64, 64, 3)

# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
#classifier.add(Conv2D(32, (3, 3), input_shape = input_shape, activation = 'relu'))


# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
#classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(Conv2D(20, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Conv2D(90, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))


# Step 3 - Flattening
classifier.add(Flatten())


# Step 4 - Full connection
#classifier.add(Dense(units = 128, activation = 'relu'))
#classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.add(Dense(activation='relu', units=64))
classifier.add(Dense(activation='softmax', units=4))

# Compiling the CNN
#classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
classifier.compile(loss='sparse_categorical_crossentropy',
                   optimizer='adam',
                   metrics=['accuracy'])


# Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 51,
                                                 class_mode = 'binary')
test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 8,
                                            class_mode = 'binary')

# 추가
import os
MODEL_DIR = './model'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

modelpath = "./model/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)
checkpoint_path = "./training_face_shape/cp-{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path,
    verbose=1,
    save_weights_only=True,
    period=5)

classifier.save_weights(checkpoint_path.format(epoch=0))

'''밑에 his 주석처리하면 바로 load해서 사용 가능'''

his = classifier.fit_generator(training_set,
                               steps_per_epoch=50,
                               epochs=50,
#                              verbose=1,
                               validation_data=test_set,
                               validation_steps=5, callbacks=[checkpointer])

# his = classifier.fit_generator(training_set,
#                         steps_per_epoch = 347,
#                         verbose=1,
#                         epochs = 50,
#                         validation_data = test_set,
#                         validation_steps=11, callbacks=[checkpointer])

classifier.save('./my_face_shape_model1.h5')
classifier = load_model('./my_face_shape_model1.h5')
classifier.summary()

print("-- Evaluate --")
scores = classifier.evaluate_generator(test_set, steps=5)

print("%s: %.2f%%" %(classifier.metrics_names[1], scores[1]*100))

'''
classifier.fit_generator(training_set,
                         steps_per_epoch = 100,
                         verbose=1,
                         epochs = 10,
                         validation_data = test_set)
'''

#output = classifier.predict_generator(test_image, steps=5)

# Part 3 - Making new predictions
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('../virtual_makeup/test_image/ex2.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
np.around(result)
result=result.argmax()
###print(training_set.class_indices)
if result == 0:
    prediction = 'Oblong'
elif result == 1:
    prediction = 'Round'
else:
    prediction = 'Square'

print(prediction)
print(result)
