import cv2
import numpy as np
import copy 
import random
from scipy.ndimage import zoom

length, hight = 250, 250

currentMetrix = [ [ 0 for i in range(length) ] for j in range(hight) ]
preMetrix = [ [ 0 for i in range(length) ] for j in range(hight) ]

def getLifeValueEdge(i,j):
    if i < 0 or j < 0 or i == length or j == length:
        return 0
    return preMetrix[i][j]

image = np.zeros((hight,length,3), np.uint8)

for i in range(0, len(preMetrix)):
        for j in range(0, len(preMetrix[i])):
                rand = random.randint(1, 10) 
                if rand < 2:
                    image[i,j] = (150,30,200)
                    preMetrix[i][j] = 1


for x in range(0, 50):
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

            currentMetrix[i][j] = 0
            if((preMetrix[i][j]) == 1 and num == 2) or ((preMetrix[i][j]) == 0 and num == 3):
                currentMetrix[i][j] = 1
                image[i,j] = (150,30,200)            
            else:
                image[i,j] = (0,0,0)

    edgeList = []
    j = 1
    for i in range(1, len(preMetrix)-1):
        edgeList.append(j, i)
        #num = 0
        #num = num + getLifeValueEdge(i-1,j-1)
        #num = num + getLifeValueEdge(i-1,j)
        #num = num + getLifeValueEdge(i-1,j+1)
        #num = num + getLifeValueEdge(i,j-1)
        #num = num + getLifeValueEdge(i,j+1)
        #num = num + getLifeValueEdge(i+1,j-1)
        #num = num + getLifeValueEdge(i+1,j)
        #num = num + getLifeValueEdge(i+1,j+1)

        currentMetrix[i][j] = 0
        if((preMetrix[i][j]) == 1 and num == 2) or ((preMetrix[i][j]) == 0 and num == 3):
            currentMetrix[i][j] = 1
            image[i,j] = (150,30,200)            
        else:
            image[i,j] = (0,0,0)

    j = length - 1
    for i in range(1, len(preMetrix)-1):
        edgeList.append(j, i)
        #num = 0
        #num = num + getLifeValueEdge(i-1,j-1)
        #num = num + getLifeValueEdge(i-1,j)
        #num = num + getLifeValueEdge(i-1,j+1)
        #num = num + getLifeValueEdge(i,j-1)
        #num = num + getLifeValueEdge(i,j+1)
        #num = num + getLifeValueEdge(i+1,j-1)
        #num = num + getLifeValueEdge(i+1,j)
        #num = num + getLifeValueEdge(i+1,j+1)


        currentMetrix[i][j] = 0
        if((preMetrix[i][j]) == 1 and num == 2) or ((preMetrix[i][j]) == 0 and num == 3):
            currentMetrix[i][j] = 1
            image[i,j] = (150,30,200)            
        else:
            image[i,j] = (0,0,0)
    
    i = 0
    for j in range(1, len(preMetrix)-1):
        edgeList.append(j, i)
        #num = 0
        #num = num + getLifeValueEdge(i-1,j-1)
        #num = num + getLifeValueEdge(i-1,j)
        #num = num + getLifeValueEdge(i-1,j+1)
        #num = num + getLifeValueEdge(i,j-1)
        #num = num + getLifeValueEdge(i,j+1)
        #num = num + getLifeValueEdge(i+1,j-1)
        #num = num + getLifeValueEdge(i+1,j)
        #num = num + getLifeValueEdge(i+1,j+1)


        currentMetrix[i][j] = 0
        if((preMetrix[i][j]) == 1 and num == 2) or ((preMetrix[i][j]) == 0 and num == 3):
            currentMetrix[i][j] = 1
            image[i,j] = (150,30,200)            
        else:
            image[i,j] = (0,0,0)

    i = length -1
    for j in range(1, len(preMetrix)-1):
        edgeList.append(j, i)
        #num = 0
        #num = num + getLifeValueEdge(i-1,j-1)
        #num = num + getLifeValueEdge(i-1,j)
        #num = num + getLifeValueEdge(i-1,j+1)
        #num = num + getLifeValueEdge(i,j-1)
        #num = num + getLifeValueEdge(i,j+1)
        #num = num + getLifeValueEdge(i+1,j-1)
        #num = num + getLifeValueEdge(i+1,j)
        #num = num + getLifeValueEdge(i+1,j+1)


        currentMetrix[i][j] = 0
        if((preMetrix[i][j]) == 1 and num == 2) or ((preMetrix[i][j]) == 0 and num == 3):
            currentMetrix[i][j] = 1
            image[i,j] = (150,30,200)            
        else:
            image[i,j] = (0,0,0)

    preMetrix = copy.deepcopy(currentMetrix)

    scale_percent = 220 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)


    #image = clipped_zoom(image, 2)
    cv2.imshow('image',resized)
    cv2.waitKey(50)


