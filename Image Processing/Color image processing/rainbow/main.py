import cv2
import numpy as np


image = np.zeros((600,600,3),dtype=np.uint8) + 255

cv2.circle(image,[300,300],50,(255,0,255),25)
cv2.circle(image,[300,300],75,(255,0,0),25)
cv2.circle(image,[300,300],100,(255,255,0),25)
cv2.circle(image,[300,300],125,(0,255,0),25)
cv2.circle(image,[300,300],150,(0,255,255),25)
cv2.circle(image,[300,300],175,(0,125,255),25)
cv2.circle(image,[300,300],200,(0,0,255),25)

result = image[0:300,0:600]

cv2.imwrite("rainbow.jpg",result)