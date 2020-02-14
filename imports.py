# Not all imports are used for U-Net, yet are used in preparation and analysis
import subprocess
# Use subprocess to install packages, E.g.:
subprocess.check_call(["python",'-m','pip','install','opencv-python'])
import cv2 as cv
import os
import sys
import pip
import glob
import keras
from natsort import natsorted,ns
import csv
import math
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
from numpy import int32
from os import listdir
from os.path import isfile, join
from os import walk
import pandas as pd
from PIL import Image
from PIL import ImageStat
import PIL.ImageOps
from resizeimage import resizeimage
import scipy
import skimage
from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data
from skimage.color import rgb2gray
from skimage.color import label2rgb
from skimage import io, color
from skimage.util.shape import view_as_windows as vaw
import statistics as stats
from scipy import signal
from scipy import ndimage

# function for image visualization
def imsh(img,nrows=1,ncols=1,cmap='gray'):
    fig,ax=plt.subplots(nrows=nrows,ncols=ncols,
    figsize=(5,5))
    ax.imshow(img,cmap='gray')
    ax.axis('off')
    return fig,ax
