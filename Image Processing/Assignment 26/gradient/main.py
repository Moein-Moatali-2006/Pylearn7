import cv2
import numpy as np

width, height = 512, 512
gradient = np.zeros((height, width))

for y in range(height):
    gradient[y, :] = 255 - (y * 255 // height)


cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('gradient\output.png', gradient)
