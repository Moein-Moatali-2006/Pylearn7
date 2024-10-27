import cv2
import numpy as np


image = cv2.imread("input\Bear.jpg")
# sharpening filer
# kernel = np.array([[0,-1,0],
#                    [-1,5,-1],
#                    [0,-1,0]])

#emboss filter
# kernel = np.array([[-2,-1,0],
#                    [-1,1,1],
#                    [0,1,2]])

#edge detection filter
# kernel = np.array([[-1,0,1],
#                    [-2,0,2],
#                    [-1,0,1]])

# kernel = np.ones((3,3)) /9
# result=cv2.filter2D(image,-1,kernel)

result = cv2.blur(image,[15,15])
cv2.imwrite("output/result5.jpg",result)
