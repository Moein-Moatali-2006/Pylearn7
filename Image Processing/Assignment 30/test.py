import cv2
import numpy as np

image= np.zeros((300,400),dtype=np.uint8)

points= np.array(([3,40],
                  [140,7],
                  [40,40],
                  [250,120],),dtype=int)

cv2.drawContours(image,[points],-1,(255,255,255),-1)
cv2.imshow("result",image)
cv2.waitKey(0)