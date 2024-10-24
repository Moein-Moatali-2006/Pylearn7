import cv2 
import numpy as np


image_1=cv2.imread("image_1.png")
image_2=cv2.imread("image_2.png")

image_1=image_1.astype(np.float32)
image_2=image_2.astype(np.float32)

result_1 = np.add(image_1 , image_2)
result_2 = (image_1*3/4 + image_2*1/4) 
result_3 = (image_1*1/4 + image_2*3/4)

result_1.astype(np.uint8)
result_2.astype(np.uint8)
result_3.astype(np.uint8)

results=np.concatenate((image_1,result_2,result_1,result_3,image_2),axis=1)
cv2.imwrite("output2.png",results)