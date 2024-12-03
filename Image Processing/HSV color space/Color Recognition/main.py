import cv2
import numpy as np


cap = cv2.VideoCapture(0)
text_color = "Unknown"
font = cv2.FONT_HERSHEY_DUPLEX
color=(0,0,0)

while True:
    ret , frame = cap.read()
    frame=cv2.flip(frame,1)

    blurred_frame = cv2.GaussianBlur(frame, (51, 51), 0)
    x1, y1 = 100, 100
    x2, y2 = 300, 300
    blurred_frame[y1:y2, x1:x2] = frame[y1:y2, x1:x2]



    cv2.rectangle(blurred_frame,[100,100],[300,300],0,2)
    mask = frame[y1:y2, x1:x2]
    
    mask_HSV = cv2.cvtColor(mask,cv2.COLOR_BGR2HSV)

    H,S,V = cv2.split(mask_HSV)
    H_mean = np.mean(H)
    
    if 0 < H_mean < 20 or 170 < H_mean < 180:
        text_color = "Red"
        color = (0,0,255)
    elif 15 < H_mean < 25:
        text_color = "Orange"
        color = (0,165,255)
    elif 25 < H_mean < 35:
        text_color = "Yellow"
        color = (0,255,255)
    elif 35 < H_mean < 80:
        text_color = "Green"
        color = (0,255,0)
    elif 80 < H_mean < 125:
        text_color = "Blue"
        color = (255,0,0)
    elif 125 < H_mean < 160:
        text_color = "Purple"
        color = (128,0,128)
    
    if np.mean(S) < 20 and np.mean(V) > 200:
        text_color = "White"
        color = (255, 255, 255)

    cv2.putText(blurred_frame,text_color,[50,50],font,1,color)
    cv2.imshow("Webcam",blurred_frame)
    if cv2.waitKey(25) == ord("q"):
        break

cap.release()
