from tensorflow.keras.applications.vgg16 import VGG16

base_model = VGG16(input_shape = (224, 224, 3),
include_top = False,
weights = 'imagenet')