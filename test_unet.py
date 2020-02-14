import PIL
import tensorflow as tf
tf.__version__
import time
start_time=time.time()
from model3D import *
from data import *

# test model and save predicted results
testGene = testGenerator("Path/to/test/images")
model = unet()
model.load_weights('Path/to/WeightsFile/from/train_unet_py.hdf5')
results = model.predict_generator(testGene,20,verbose=1)
saveResult("Path/to/directory/to/save/prediction/images",results)
