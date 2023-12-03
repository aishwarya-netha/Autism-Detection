import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from keras.models import Sequential 
from keras.layers import Activation, Dense, Flatten, Dropout

x = base_model.output
x = Flatten()(x)
x = Dense(1024, activation="relu")(x)
x = Dropout(0.4)(x)


predictions = Dense(1, activation="sigmoid")(x)
model_final = tf.keras.Model(base_model.input, predictions)
model_final.summary()