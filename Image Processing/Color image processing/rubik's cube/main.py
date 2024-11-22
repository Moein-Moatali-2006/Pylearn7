import cv2
import numpy as np


image = cv2.imread("rubik_cube.png")

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        b,g,r = image[i,j]
        
        if 200<=b<=255 and 200<=r<=255 :
            image[i,j] = [0, 255, 0]

        if 200<=g<=255 and 200<=b<=255:
            image[i,j] = [0,0,255]

        if 200<=r<=255 and  200<=g<=255:
            image[i,j] = [255,0,0]
        
        if 200<=b<=255 and  200<=g<=255 and 200<=r<=255 :
            image[i,j] = [255,255,255]
    

cv2.imwrite("output.png",image)
