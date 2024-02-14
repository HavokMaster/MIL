import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import pickle

def loadImages(imageDir = 'images', size=False, serialize=False, bgr2rgb=False, dumpName="images", maxSize=2000, normalize=False):
    classes = os.listdir(imageDir)
    images = []
    labels = []
    
    print(f"{len(classes)} Total class/classes detected!")
    for idx, classLabel in enumerate(classes):
        imgNo = 0
        for img in os.listdir(f'{imageDir}/{classLabel}'):
            if imgNo >= maxSize: break
            image = cv2.imread(f'{imageDir}/{classLabel}/'+img)
            if bgr2rgb: image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            if size != False: image = cv2.resize(image, size)
            images.append(image)
            labels.append(idx)
            imgNo += 1
        if imgNo == 0: print(f"No images loaded from {classLabel}")
        else: print(f"Loaded {imgNo} image(s) from {classLabel}")
    if serialize:
        with open(f'{dumpName}.pkl', 'wb') as file:
            pickle.dump({"Images":images, "Labels":labels}, file)
    images = np.array(images)
    labels = np.array(labels)
    if normalize: images = images.astype('float32')/255.0
    return [images, labels]

def loadFromDump(dumpName='images.pkl'):
    with open(dumpName, 'rb') as file:
        data = pickle.load(file)
    return data

def getClasses(imageDir='images'):
    classes = os.listdir(imageDir)
    return classes
