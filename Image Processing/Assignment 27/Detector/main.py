import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)
_ ,frame=cap.read()
a=frame.shape[0]
b=frame.shape[1]

out=cv.VideoWriter("Detector\output.avi",cv.VideoWriter_fourcc(*'XVID'),30,(b,a),isColor=False)

while True:
    _ ,frame=cap.read()
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    frame_blur = cv.GaussianBlur(frame,(51,51),0)

    h, w = frame.shape[:2]
    square_size=50
    x_center = w // 2
    y_center = h // 2
    x1 = x_center - square_size // 2
    y1 = y_center - square_size // 2
    x2 = x_center + square_size // 2
    y2 = y_center + square_size // 2
    mask = np.zeros_like(frame)
    mask[y1:y2, x1:x2] = 255

    result=np.where(mask==255,frame,frame_blur)
    cv.rectangle(result,(x1,y1),(x2,y2),0,3)
    
    mean_val = cv.mean(frame, mask=mask)
    
    if mean_val[0] < 20:
        cv.putText(result,"Black",(20,50),cv.FONT_HERSHEY_COMPLEX,2,255)
    elif 50 < mean_val[0] < 100 :
        cv.putText(result,"White",(20,50),cv.FONT_HERSHEY_COMPLEX,2,255)
    else:
        cv.putText(result,"Gray",(20,50),cv.FONT_HERSHEY_COMPLEX,2,255)
    
    cv.imshow("result",result)
    out.write(result)
    if cv.waitKey(25) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv.destroyAllWindows()