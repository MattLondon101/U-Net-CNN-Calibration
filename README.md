# U-Net-Calibration
Code to quickly calibrate U-Net for your purposes.
Code was initially run in Spyder (Python 3.7) on ASUS ROG GU502GV laptop with a 9th Gen Intel® Core™ i7-9750H CPU @ 2.60GHz, 6 cores, 12 logical processors, 16 GB RAM, 2592 MHz max clock speed, and 141pixels per inch (ppi) display resolution. The training images for U-Net were grayscale images (pixel values 0-255 (black-white)).

Dependencies:
Python 3 (code has only been tested in Spyder (Python 3.7) in Anaconda 3) on PC

All other dependencies are easily installed and/or imported in import.py

Fiji/ImageJ:
Trace ROIs for use as train labels.
Overlay prediction images with corresponding ROI tracing. Measure number of pixels in prediction that are in ROI = True Positive (TP).
Use Count_Non_Zero in Calibration.py to calculate all predicted pixels (Total).
Total - TP = False Positive (FP)

PPV determines accuracy of predictions.
Positive Predictive Value (PPV) = PPV = TP/(TP+FP)

**Calibration**
With the settings of 40 steps-per-epoch and 60 epochs (in train_unet.py) accuracy and reliability across subjects is nearly 100% on 4th run. There is a particular cycle that accuracy and reliability follows before and after the 4th run. Yet, the data regarding this is still being prepared for publication and will not be made public until at least 2021. But, each run only takes no more than an hour. So see what you can find!


