import cv2
import numpy as np


cap = cv2.VideoCapture(0)
text = "Place an object"
color=(0,0,0)

while True:
    ret , frame = cap.read()
    frame = cv2.flip(frame,1)

    cv2.putText(frame,text,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
    cv2.rectangle(frame,[100,100],[500,400],(0,0,0),3)

    mask = frame[100:400,100:500]
    b,g,r = cv2.split(mask)

    b = int(np.mean(b))
    g = int(np.mean(g))
    r = int(np.mean(r))
    
    if r>b and r>g:
        text="Red"
        color=(0,0,255)
    elif g>r and g>b:
        text="Green"
        color=(0,255,0)
    elif b>r and b>g:
        text="Blue"
        color=(255,0,0)
    elif r > b and r > g and g > b:
        text = "Orange"
        color = (0, 165, 255)
    else:
        text = "Unknown"
        color = (0, 0, 0)

    cv2.putText(frame,f"B:{b} G:{g} R:{r}",(150,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)

    cv2.imshow("result",frame)
    if cv2.waitKey(25) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





