from tensorflow.keras.preprocessing.image import load_img
from matplotlib.pyplot import imread
from matplotlib.pyplot import imshow
import numpy as np

img_path ="C:\\Users\\Akshay\\Desktop\\aishu_project\\base_data\\testing\\Autistic\\Autistic.2.jpg"
image = load_img(img_path,target_size=(224,224))
my_image = imread(img_path)
imshow(my_image)
img = np.array(image)3
img = img/255.0
img = img.reshape(1,224,224,3)
label = model_final.predict(img)
print(label[0])
if(label[0] < 0.5):
    print("Our model says he/she is Autistic")
else:
    print("Our model says he/she is Non-Autistic")