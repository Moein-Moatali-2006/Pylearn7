import cv2 as cv


cap=cv.VideoCapture(0)

face_detector=cv.CascadeClassifier("Filters\models\haarcascade_frontalface_alt.xml")
img_lion=cv.imread("Filters\input\lion.jpg")

while True:
    _,frame=cap.read()
    key=cv.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('1'):
        ...         
    elif key == ord('2'):
        ...
    elif key == ord('3'):
        ...
    elif key == ord('4'):
        ...
    
    cv.imshow("result",frame)

cap.release()
cv.destroyAllWindows()