import cv2
import numpy as np


image = np.zeros((300,600,3),dtype=np.uint8) + 115
#Red
cv2.rectangle(image,[100,100],[150,150],[0,70,220],-1)
#Yellow
cv2.rectangle(image,[150,150],[200,200],[0,180,215],-1)
#Green
cv2.rectangle(image,[150,100],[200,150],[0,190,130],-1)
#Blue
cv2.rectangle(image,[100,150],[150,200],[225,150,0],-1)

cv2.line(image,[150,100],[150,200],(115,115,115),2)
cv2.line(image,[100,150],[200,150],(115,115,115),2)

cv2.putText(image,"Microsoft",[220,180],cv2.FONT_HERSHEY_DUPLEX,2,(255,255,255),2)

cv2.imwrite("output.png",image)
