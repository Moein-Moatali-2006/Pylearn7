import cv2
import numpy as np

image_1=cv2.imread("d1.bmp")
image_2=cv2.imread("d2.bmp")

image_1=cv2.cvtColor(image_1,cv2.COLOR_BGR2GRAY)
image_2=cv2.cvtColor(image_2,cv2.COLOR_BGR2GRAY)

result = image_1 - image_2

cv2.imwrite("output/result.jpg",result)