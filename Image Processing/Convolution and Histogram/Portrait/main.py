import cv2
import numpy as np


image = cv2.imread("image.png",cv2.IMREAD_GRAYSCALE)
mask = cv2.GaussianBlur(image, (55, 55), 0)

threshold = 127

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        pix = image[i][j]
        if pix > threshold:
            mask[i][j] = pix

cv2.imwrite("blurred_image.png", mask)
