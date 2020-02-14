import tensorflow as tf
tf.__version__
import time
start_time=time.time()
from model3D import *
from data import *

#if you don't want to do data augmentation, set data_gen_args as an empty dict.
data_gen_args = dict()
"""
data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')
"""
# Training Images: 20 512*512 grayscale images
# Training Labels: 20 512*512 binary (black and white (0,1)) images
myGene = trainGenerator(20,'Path/to/train/images/and/labels','ImageDir','LabelDir',data_gen_args,save_to_dir = None)
model = unet()
model_checkpoint = ModelCheckpoint('WeightsFile.hdf5', monitor='loss',verbose=1, save_best_only=True)
model.fit_generator(myGene,steps_per_epoch=40,epochs=6,callbacks=[model_checkpoint])

# prints total training time at end
print('Training tool {} seconds'.format(time.time()-start_time))
