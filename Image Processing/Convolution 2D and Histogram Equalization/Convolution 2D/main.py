import cv2
import numpy as np


# 1. Edge detection filter
kernel_edge = np.array([[-1 , -1 , -1],
                   [-1 ,  8 , -1],
                   [-1 , -1 , -1]])

# 2. Sharpening filter
kernel_Sharpening = np.array([[0  , -1 ,  0],
                   [-1 ,  5 , -1],
                   [0  , -1 ,  0]])

# 3. Emboss filter
kernel_emboss = np.array([[-2 , -1 ,  0],
                   [-1 ,  1 ,  1],
                   [0  ,  1 ,  2]])

# 4. Identity filter
kernel_identity = np.array([[0  ,  0 ,  0],
                   [0  ,  1 ,  0],
                   [0  ,  0 ,  0]])

# 5. My filter
kernel_my = np.array([[2  ,  0 ,  -1],
                   [2  ,  0 ,  -1],
                   [2  ,  0 ,  -1]])


image = cv2.imread("lion.png",cv2.IMREAD_GRAYSCALE)


result_1 = cv2.filter2D(image , -1 , kernel_edge)
result_2 = cv2.filter2D(image , -1 , kernel_Sharpening)
result_3 = cv2.filter2D(image , -1 , kernel_emboss)
result_4 = cv2.filter2D(image , -1 , kernel_identity)
result_5 = cv2.filter2D(image , -1 , kernel_my)

cv2.imwrite("output/result_1.png",result_1)
cv2.imwrite("output/result_2.png",result_2)
cv2.imwrite("output/result_3.png",result_3)
cv2.imwrite("output/result_4.png",result_4)
cv2.imwrite("output/result_5.png",result_5)

result = np.hstack((image,result_1,result_2,result_3,result_4,result_5))
cv2.imwrite("output/result.png",result)