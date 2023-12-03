import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from keras.models import Sequential 
from keras.layers import Activation, Dense, Flatten, Dropout

x = Flatten()(base_model.output)
x = Dense(1024, activation='relu')(x)
x = Dropout(0.2)(x)

x = Dense(1, activation='sigmoid')(x)

model = tf.keras.models.Model(base_model.input, x)

model.compile(optimizer = RMSprop(learning_rate=0.0001), loss = 'binary_crossentropy', metrics = ['accuracy'])