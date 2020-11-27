# U-Net-Calibration
Code was initially run in Spyder (Python 3.7) on ASUS ROG GU502GV laptop with a 9th Gen Intel® Core™ i7-9750H CPU @ 2.60GHz, 6 cores, 12 logical processors, 16 GB RAM, 2592 MHz max clock speed, and 141pixels per inch (ppi) display resolution. The training images for U-Net were grayscale images (pixel values 0-255 (black-white)).

Dependencies:
Python 3 (code has only been tested in Spyder (Python 3.7) in Anaconda 3) on PC

Use Tensorflow 1 (e.g. Tensorflow 1.15.0)

All other dependencies found in import.py

Fiji/ImageJ:
Trace ROIs for use as train labels.
Overlay prediction images with corresponding ROI tracing. Measure number of pixels in prediction that are in ROI = True Positive (TP).
Use Count_Non_Zero in Calibration.py to calculate all predicted pixels (Total).
Total - TP = False Positive (FP)

PPV determines accuracy of predictions.
Positive Predictive Value (PPV) = PPV = TP/(TP+FP)

## **Calibration** 
With the settings of 40 steps-per-epoch and 60 epochs (in train_unet.py) and without updating the .hdf5 weights file, accuracy and reliability across subjects fluctuated from across runs. The pattern exhibited was PPV < 0.4 on the 1st and 3rd runs, PPV between 0.5 - 0.9 on the 2nd run, and PPV between 0.9-1.0 on the 4th run. PPV declined at a rate of -0.3/run after the 4th run. Thus, with an unchanged weights file/model, the 4th run is the most accurate and reliable for U-Net predictions.

