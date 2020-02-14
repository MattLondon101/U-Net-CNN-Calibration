# Positive Predictive Value (PPV) is used to determine accuracy of predictions
# PPV = TP/(TP+FP)
# TP = True Positive
# FP = False Positive

# Count non-zero pixels to determine total prediction pixels in image
src='Path/to/images/'
j=[]
for fileName in natsorted(os.listdir(src),alg=ns.PATH):
    filePath=os.path.join(src,fileName)
    if os.path.isfile(filePath):
        im=cv.imread(filePath,0)
        nonzero = cv.countNonZero(im)
        
# Calibration may involve further experimentation with these parameters
