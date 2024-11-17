import cv2
import numpy as np


image = cv2.imread("rubik_cube.png")

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        b,g,r = image[i,j]
        if b==255 and r==255 :
            image[i,j] = [0, 255, 0]

        if g==255 and b==255:
            image[i,j] = [0,0,255]

        if r==255 and g==255:
            image[i,j] = [255,0,0]
        
        if b==255 and  g==255 and r==255 :
            image[i,j] = [255,255,255]
    

cv2.imwrite("output.png",image)
