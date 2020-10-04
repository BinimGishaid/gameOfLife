import cv2
import numpy as np
import copy 
import random

def getLifeValue(i,j, matrix):
    if i < 0 or j < 0 or i == length or j == length:
        return 0
    return matrix[i][j]


length, hight = 400, 400
  
currentMetrix = [ [ 0 for i in range(length) ] for j in range(hight) ]
preMetrix = [ [ 0 for i in range(length) ] for j in range(hight) ]

image = np.zeros((hight,length,3), np.uint8)


for i in range(0, len(preMetrix)):
        for j in range(0, len(preMetrix[i])):
                preMetrix[i][j] = random.choice([0, 1])
                if preMetrix[i][j] == 1:
                    image[i,j] = (150,30,200)


cv2.imshow('image',image)
cv2.waitKey(500)

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

    for i in range(0, len(preMetrix)):
        for j in range(0, len(preMetrix[i])):
            if i == 0 or i == length-1 or j == 0 or j == length -1: 
                num = 0
                num = num + getLifeValue(i-1,j-1, preMetrix)
                num = num + getLifeValue(i-1,j, preMetrix)
                num = num + getLifeValue(i-1,j+1, preMetrix)
                num = num + getLifeValue(i,j-1, preMetrix)
                num = num + getLifeValue(i,j+1, preMetrix)
                num = num + getLifeValue(i+1,j-1, preMetrix)
                num = num + getLifeValue(i+1,j, preMetrix)
                num = num + getLifeValue(i+1,j+1, preMetrix)

                currentMetrix[i][j] = 0
                if((preMetrix[i][j]) == 1 and num == 2) or ((preMetrix[i][j]) == 0 and num == 3):
                    currentMetrix[i][j] = 1
                    image[i,j] = (150,30,200)            
                else:
                    image[i,j] = (0,0,0)

    preMetrix = copy.deepcopy(currentMetrix)

    cv2.imshow('image',image)
    cv2.waitKey(100)


