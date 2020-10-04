import cv2
import numpy as np
import copy 
import random
from scipy.ndimage import zoom

length, hight = 160, 160

currentMetrix = [[0 for i in range(length)] for j in range(hight)]
preMetrix = [[0 for i in range(length)] for j in range(hight)]

edgeList = []

def getLifeValueEdge(i,j):
    if i < 0 or j < 0 or i == length or j == length:
        return 0
    return preMetrix[i][j]

j = 0
for i in range(0, len(preMetrix)):
    edgeList.append([i, j])

j = length - 1
for i in range(0, len(preMetrix)):
    edgeList.append([i, j])

i = 0
for j in range(0, len(preMetrix)):
    edgeList.append([i, j])

i = length -1
for j in range(0, len(preMetrix)):
    edgeList.append([i, j])

image = np.zeros((hight,length,3), np.uint8)

for i in range(0, len(preMetrix)):
    for j in range(0, len(preMetrix[i])):
        rand = random.randint(1, 100) 
        if rand  > 35:
            image[i,j] = (150,30,200)
            preMetrix[i][j] = 1


for x in range(0, 500):
    for i in range(1, len(preMetrix)-1):
        for j in range(1, len(preMetrix[i])-1):
            num = 0
            if(preMetrix[i-1][j-1]) == 1:
               num = num +1
            if(preMetrix[i-1][j]) == 1:
                num = num +1   
            if(preMetrix[i-1][j+1]) == 1:
                num = num +1
            if(preMetrix[i][j-1]) == 1:
                num = num +1      
            if(preMetrix[i][j+1]) == 1:
                num = num +1   
            if(preMetrix[i+1][j-1]) == 1:
                num = num +1
            if(preMetrix[i+1][j]) == 1:
                num = num +1     
            if(preMetrix[i+1][j+1]) == 1:
                num = num +1

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

        if preMetrix[i][j] == 1 and (num == 2 or num ==3):
            currentMetrix[i][j] = 1
            image[i,j] = (150,30,200)   
        elif preMetrix[i][j] == 0 and num == 3:        
            currentMetrix[i][j] = 1
            image[i,j] = (150,30,200)   
        else:
            currentMetrix[i][j] = 0
            image[i,j] = (0,0,0) 

    preMetrix = copy.deepcopy(currentMetrix)

    scale_percent = 400 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)


    cv2.imshow('image',resized)

    #cv2.imshow('image',image)

    cv2.waitKey(10)


