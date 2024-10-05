import cv2
import numpy as np


image_1=cv2.imread("image1.jpg")
image_2=cv2.imread("image2.jpg")
image_3=cv2.imread("image3.jpg")

image1=cv2.resize(image_1,(image_2.shape[1],image_2.shape[0]))

image = image_3 / 255.0 * image_2

image3 = 255 - image_3

image += image3 / 255.0 * image1

image = image.astype(np.uint8)

cv2.imwrite("output.jpg",image)
