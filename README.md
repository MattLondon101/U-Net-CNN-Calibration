# U-Net-Calibration
Code to quickly calibrate U-Net for your purposes.
Code was initially run in Spyder (Python 3.7) on ASUS ROG GU502GV laptop with a 9th Gen Intel® Core™ i7-9750H CPU @ 2.60GHz, 6 cores, 12 logical processors, 16 GB RAM, 2592 MHz max clock speed, and 141pixels per inch (ppi) display resolution. The training images for U-Net were grayscale images (pixel values 0-255 (black-white)).

Dependencies:
Python 3 (code has only been tested in Spyder (Python 3.7) in Anaconda 3) on PC

All other dependencies are easily installed and/or imported in import.py

Fiji/ImageJ:
Trace ROIs for use as train labels.
Overlay prediction images with corresponding ROI tracing. Measure number of pixels in prediction that are in ROI = True Positive (TP).
Use *Count_Non_Zero* to calculate all predicted pixels (Total).
Total - TP = False Positive (FP)

PPV determines accuracy of predictions.
Positive Predictive Value (PPV) = PPV = TP/(TP+FP)

*Count_Non_Zero* produces string of non-zero values for all image files in src path
src='Path/of/images/'
j=[]
for fileName in natsorted(os.listdir(src),alg=ns.PATH):
    filePath=os.path.join(src,fileName)
    if os.path.isfile(filePath):
        im=cv.imread(filePath,0)
        nonzero = cv.countNonZero(im)



