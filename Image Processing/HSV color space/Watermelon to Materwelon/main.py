import cv2
import numpy as np


image = cv2.imread("watermelon.png")
image_HSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

H,S,V = cv2.split(image_HSV)

H_new = H.copy()

# for i in range(H.shape[0]):
#     for j in range(H.shape[1]):
#         if 30< H[i,j] <80:
#             H_new[i,j]=170

#         if 0< H[i,j] <15 or 165< H[i,j] <180:
#             H_new[i,j]=70

#         print("Processing...!")


H_new[(30 < H) & (H < 80)] = 170
H_new[(0 < H) & (H < 15)] = 65
H_new[(165 < H) & (H < 180)] = 65

new_image = cv2.merge((H_new,S,V))
new_image = cv2.cvtColor(new_image,cv2.COLOR_HSV2BGR)

cv2.imwrite("output.png",new_image)
