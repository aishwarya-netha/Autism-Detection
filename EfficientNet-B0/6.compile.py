from tensorflow.keras.optimizers import RMSprop

model_final.compile(optimizer = tf.keras.optimizers.legacy.RMSprop(learning_rate=0.0001, decay=1e-6), loss = 'binary_crossentropy',metrics = ['accuracy'])