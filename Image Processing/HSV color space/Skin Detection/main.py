import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)
lower_skin = np.array([0, 20, 70])
upper_skin = np.array([20, 255, 255])

while True:
    ret , frame = cap.read()
    frame = cv2.flip(frame,1)

    frame_HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame_HSV,lower_skin,upper_skin)

    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Skin detection",result)
    if cv2.waitKey(25) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()