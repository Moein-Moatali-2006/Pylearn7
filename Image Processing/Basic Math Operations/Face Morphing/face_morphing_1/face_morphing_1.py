import cv2
import numpy as np

image_1=cv2.imread("image_1.jpg")
image_2=cv2.imread("image_2.jpg")

new_size = (800, 600)
image_1 = cv2.resize(image_1,new_size)
image_2 = cv2.resize(image_2,new_size)

image_1.astype(np.float32)
image_2.astype(np.float32)

result = cv2.add(image_1 , image_2)
result.astype(np.uint8)

results=np.concatenate((image_1,result,image_2),axis=1)

cv2.imwrite("output_1.jpg",results)
cv2.waitKey(0)
cv2.destroyAllWindows()