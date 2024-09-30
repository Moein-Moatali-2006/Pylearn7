import cv2
import numpy as np


image_1 = cv2.imread("image_1.jpg")
image_lion = cv2.imread("lion.jpg")

# image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
# image_lion = cv2.cvtColor(image_lion, cv2.COLOR_BGR2GRAY)

image_1 = cv2.resize(image_1, (450, 450))
image_lion = cv2.resize(image_lion, (450, 450))

image_1 = image_1.astype(np.float32)
image_lion = image_lion.astype(np.float32)

result = (image_1 * 3/4 + image_lion * 2/4)

result = result.astype(np.uint8)

cv2.imwrite("output_3.jpg", result)
