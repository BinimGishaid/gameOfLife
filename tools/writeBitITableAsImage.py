import cv2
import numpy as np
import copy 
import random

length, hight = 250, 250


  
currentMetrix = [ [ 0 for i in range(length) ] for j in range(hight) ]
preMetrix = [ [ 0 for i in range(length) ] for j in range(hight) ]



image = np.zeros((hight,length,3), np.uint8)


for i in range(2, len(preMetrix)-2):
        for j in range(2, len(preMetrix[i])-2):
                preMetrix[i][j] = random.choice([0, 1])
                if preMetrix[i][j] == 1:
                    image[i,j] = (200,200,200)

cv2.imshow('image',image)
cv2.waitKey(500)

for x in range(0, 400):
    for i in range(2, len(preMetrix)-2):
        for j in range(2, len(preMetrix[i])-2):
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
            if((preMetrix[i][j]) == 1 and num == 2) or (preMetrix[i][j] == 0 and num == 3):
                currentMetrix[i][j] = 1
                image[i,j] = (200,20,200)
            else:
                image[i,j] = (0,0,0)

    preMetrix = copy.deepcopy(currentMetrix)

    cv2.imshow('image',image)
    cv2.waitKey(2)

    #just wanna see how to publish new branch


