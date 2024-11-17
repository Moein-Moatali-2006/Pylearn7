import cv2
import numpy as np


image = cv2.imread("watermelon.png")
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

R,G,B=cv2.split(image)

Z = R
R = G
G = Z

result=cv2.merge([B,G,R])
cv2.imwrite("materwelon.png",result)