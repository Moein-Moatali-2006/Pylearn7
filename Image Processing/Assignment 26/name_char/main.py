import cv2 as cv
import numpy as np

img = np.zeros((600,600))

img[20:550,70:100] = 255
img[20:550,500:530] = 255
cv.line(img,(84,27),(280,180),(255,255,255),30)
cv.line(img,(515,27),(290,180),(255,255,255),30)

cv.imwrite("name_char\output_char.png",img)
cv.waitKey(0)
cv.destroyAllWindows()


