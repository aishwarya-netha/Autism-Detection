import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
nrows = 4
ncols = 4

fig = plt.gcf()
fig.set_size_inches(ncols*4, nrows*4)
pic_index = 100
train_autistic_fnames = os.listdir( train_autistic_dir )
train_nonautistic_fnames = os.listdir( train_nonautistic_dir )


next_autistic_pix = [os.path.join(train_autistic_dir, fname) 
                for fname in train_autistic_fnames[ pic_index-8:pic_index] 
               ]

next_nonautistic_pix = [os.path.join(train_nonautistic_dir, fname) 
                for fname in train_nonautistic_fnames[ pic_index-8:pic_index]
               ]

for i, img_path in enumerate(next_autistic_pix+next_nonautistic_pix):
  sp = plt.subplot(nrows, ncols, i + 1)
  sp.axis('Off') 

  img = mpimg.imread(img_path)
  plt.imshow(img)

plt.show()