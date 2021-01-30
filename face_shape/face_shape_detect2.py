## face_shape_detect_ljh.ipynb 돌린 것 --> my_face_Shape_model.h5

## 정확도 47.50%
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

image_path = '../virtual_makeup/test_image/ex2.jpg'

classifier = load_model('./my_face_shape_model2.h5')
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