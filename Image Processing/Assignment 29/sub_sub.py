import cv2
import numpy as np

image_1=cv2.imread("a.tif")
image_2=cv2.imread("b.tif")

image_1=cv2.cvtColor(image_1,cv2.COLOR_BGR2GRAY)
image_2=cv2.cvtColor(image_2,cv2.COLOR_BGR2GRAY)

# result = image_1 - image_2
result = cv2.subtract(image_1 , image_2)

result = 255 - result

cv2.imwrite("output/c.jpg",result)