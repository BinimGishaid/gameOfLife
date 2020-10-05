import cv2, copy, random, sys, numpy as np

length, hight = 200, 200
currentMetrix = [[0 for i in range(length + 1)] for j in range(hight + 1)]
preMetrix = [[0 for i in range(length + 1)] for j in range(hight + 1)]

def checkAndUpdateLists():
   for i in range(0, length):
        for j in range(0, length):  
            num = 0
            num = num + preMetrix[i-1][j-1]
            num = num + preMetrix[i-1][j]
            num = num + preMetrix[i-1][j+1]
            num = num + preMetrix[i][j-1]
            num = num + preMetrix[i][j+1]
            num = num + preMetrix[i+1][j-1]
            num = num + preMetrix[i+1][j]
            num = num + preMetrix[i+1][j+1] 

            if num == 3 or (preMetrix[i][j] == 1 and num == 2):
                currentMetrix[i][j] = 1
                image[i,j] = (150,200,100)   
            else:
                currentMetrix[i][j] = 0
                image[i,j] = (0,0,0) 

def init():
    for i in range(0, length):
        for j in range(0, length):
            preMetrix[i][j] = 1 if random.randint(1, 100) > 95 else 0

def resize(mul):
    if mul == 1:
        return image
    preMetrix = copy.deepcopy(currentMetrix)
    scale_percent = mul * 100 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

#main
image = np.zeros((hight,length,3), np.uint8)
init()
while(1):   
    checkAndUpdateLists()
    preMetrix = copy.deepcopy(currentMetrix)
    cv2.imshow('image',resize(2))
    if cv2.waitKey(13)==27:
        sys.exit()