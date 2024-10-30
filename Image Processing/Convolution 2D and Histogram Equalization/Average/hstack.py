import cv2
import numpy as np


image_1 = cv2.imread("output\Avg_kernel3_3=0_04.png")
image_2 = cv2.imread("output\Avg_kernel3_3=1_0.png")
image_3 = cv2.imread("output\Avg_kernel3_3=5_0.png")
image_4 = cv2.imread("output\Avg_kernel5_5=0_04.png")
image_5 = cv2.imread("output\Avg_kernel5_5=1_0.png")
image_6 = cv2.imread("output\Avg_kernel5_5=5_0.png")


result = np.hstack((image_1,image_2,image_3,image_4,image_5,image_6))
cv2.imwrite("output\output.png",result) 