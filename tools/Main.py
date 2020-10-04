import cv2
import numpy as np
import copy 
import random
import sys
from scipy.ndimage import zoom

length, hight = 200, 200
edgeList = []
insideList = []
currentMetrix = [[0 for i in range(length)] for j in range(hight)]
preMetrix = [[0 for i in range(length)] for j in range(hight)]

def getLifeValueEdge(i,j):
    if i < 0 or j < 0 or i == length or j == length:
        return 0
    return preMetrix[i][j]
def getLifeValue(i,j):
    return preMetrix[i][j]
def checkAndUpdateLists():
    for index in insideList:
        i = index[0]
        j = index[1]  
        num = 0
        num = num + getLifeValue(i-1,j-1)
        num = num + getLifeValue(i-1,j)
        num = num + getLifeValue(i-1,j+1)
        num = num + getLifeValue(i,j-1)
        num = num + getLifeValue(i,j+1)
        num = num + getLifeValue(i+1,j-1)
        num = num + getLifeValue(i+1,j)
        num = num + getLifeValue(i+1,j+1) 

        i = index[0]
        j = index[1]
        if preMetrix[i][j] == 1 and (num == 2 or num ==3):
            currentMetrix[i][j] = 1
            image[i,j] = (150,30,200)   
        elif preMetrix[i][j] == 0 and num == 3:        
            currentMetrix[i][j] = 1
            image[i,j] = (150,30,200)   
        else:
            currentMetrix[i][j] = 0
            image[i,j] = (0,0,0) 

    for index in edgeList:
        i = index[0]
        j = index[1]  
        num = 0
        num = num + getLifeValueEdge(i-1,j-1)
        num = num + getLifeValueEdge(i-1,j)
        num = num + getLifeValueEdge(i-1,j+1)
        num = num + getLifeValueEdge(i,j-1)
        num = num + getLifeValueEdge(i,j+1)
        num = num + getLifeValueEdge(i+1,j-1)
        num = num + getLifeValueEdge(i+1,j)
        num = num + getLifeValueEdge(i+1,j+1) 

        i = index[0]
        j = index[1]
        if preMetrix[i][j] == 1 and (num == 2 or num ==3):
            currentMetrix[i][j] = 1
            image[i,j] = (150,30,200)   
        elif preMetrix[i][j] == 0 and num == 3:        
            currentMetrix[i][j] = 1
            image[i,j] = (150,30,200)   
        else:
            currentMetrix[i][j] = 0
            image[i,j] = (0,0,0)         
def init():
    for i in range(0, length):
        edgeList.append([i, 0])
        edgeList.append([0, i])
        edgeList.append([i, length -1])
        edgeList.append([length -1, i])

    for i in range(1, length-1):
        for j in range(1, length-1):
            insideList.append([i,j])

    for i in range(0, length):
        for j in range(0, length):
            rand = random.randint(1, 100) 
            if rand  > 24:
                image[i,j] = (15,30,200)
                preMetrix[i][j] = 1
def resize(mul):
    preMetrix = copy.deepcopy(currentMetrix)
    scale_percent = mul * 100 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    
image = np.zeros((hight,length,3), np.uint8)
init()

for x in range(0, 500):    
    checkAndUpdateLists()
    checkAndUpdateLists()
    preMetrix = copy.deepcopy(currentMetrix)
    cv2.imshow('image',resize(2))
    k = cv2.waitKey(33)
    if k==27:
        sys.exit()
