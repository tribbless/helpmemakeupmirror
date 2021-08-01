## face_shape_make_h5 돌린 것 --> my_face_Shape_model1.h5

## 정확도 52.50%

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

#import tensorflow as tf
#from tensorflow.python.client import device_lib
#print(device_lib.list_local_devices())

def main(image_path):
    #classifier = load_model('face_shape/my_face_shape_model1.h5') # self 동작 - jetson nano/window 용
    classifier = load_model('models/my_model_10') # windeow server에서 동작
    #classifier = load_model('my_face_shape_model1.h5')
    test_image = image.load_img(image_path, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)
    np.around(result)
    result = result.argmax()
    ###print(training_set.class_indices)
    if result == 0:
        prediction = 'oblong'
    elif result == 1:
        prediction = 'round'
    else:
        prediction = 'square'
    print('{}의 얼굴형은 {}입니다.'.format(image_path, prediction))
    return prediction
'''
## test할 때 쓰는 코드
image_path = '../ex_0.png'

classifier = load_model('my_face_shape_model1.h5')
#classifier.summary()

test_image = image.load_img(image_path, target_size = (64, 64))
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
'''