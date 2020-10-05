import cv2
import numpy as np
import copy 
import random
import sys

length, hight = 200, 200
currentMetrix = [[0 for i in range(length + 1)] for j in range(hight + 1)]
preMetrix = [[0 for i in range(length + 1)] for j in range(hight + 1)]

def getLifeValue(i,j):
    return preMetrix[i][j]

def checkAndUpdateLists():
   for i in range(0, length):
        for j in range(0, length):  
            num = 0
            num = num + getLifeValue(i-1,j-1)
            num = num + getLifeValue(i-1,j)
            num = num + getLifeValue(i-1,j+1)
            num = num + getLifeValue(i,j-1)
            num = num + getLifeValue(i,j+1)
            num = num + getLifeValue(i+1,j-1)
            num = num + getLifeValue(i+1,j)
            num = num + getLifeValue(i+1,j+1) 

            if (preMetrix[i][j] == 1 and (num == 2 or num ==3)) or (preMetrix[i][j] == 0 and num == 3):
                currentMetrix[i][j] = 1
                image[i,j] = (150,150,150)   
            else:
                currentMetrix[i][j] = 0
                image[i,j] = (0,0,0) 

def init():
    for i in range(0, length):
        for j in range(0, length):
            rand = random.randint(1, 100) 
            if rand > 94:
                image[i,j] = (150,150,150)  
                preMetrix[i][j] = 1

def resize(mul):
    if mul == 1:
        return image
    preMetrix = copy.deepcopy(currentMetrix)
    scale_percent = mul * 100 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    
image = np.zeros((hight,length,3), np.uint8)
init()
while(1):   
    checkAndUpdateLists()
    preMetrix = copy.deepcopy(currentMetrix)
    cv2.imshow('image',resize(2))
    k = cv2.waitKey(13)
    if k==27:
        sys.exit()