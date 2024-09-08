import cv2
import numpy as np

face_sticker = cv2.imread("input\image_lion.png")
lips_sticker = cv2.imread("input\image_lips.png")
sunglasses_sticker = cv2.imread("input\image_sunglasses.png")

face_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
lips_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
eyes_detect = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_righteye_2splits.xml')


cap = cv2.VideoCapture(0)

face_sticker_active = False
eyes_lips_sticker_active = False

while True:
    _, frame = cap.read()
    if not _:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Face active
    if face_sticker_active:
        faces = face_detect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            resized_sticker = cv2.resize(face_sticker, (w, h))

            for i in range(resized_sticker.shape[0]):
                for j in range(resized_sticker.shape[1]):
                    if all(resized_sticker[i, j] != 0):
                        frame[y + i, x + j] = resized_sticker[i, j]
    
    
    
    # eyes lips active
    if eyes_lips_sticker_active:
        #lips
        lips = lips_detect.detectMultiScale(gray, 1.01,190,minSize=[30,30],maxSize=[80,80])
        for lip in lips:
            x,y,w,h=lip
            lips_resized=cv2.resize(lips_sticker,[w,h],interpolation=cv2.INTER_CUBIC)
            for i in range(lips_resized.shape[0]):
                for j in range(lips_resized.shape[1]):
                    if all(lips_resized[i, j] != 0):
                        frame[y + i, x + j] = lips_resized[i, j]
            
            
        #eyes
        # eyes =eyes_detect.detectMultiScale(gray, 1.3,15,minSize=[30,30],maxSize=[80,80])
        # print(eyes)
        # for eye in eyes:
        #     x,y,w,h=eye
            
        #     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
        


    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        eyes_lips_sticker_active =False
        face_sticker_active = True
    elif key == ord('2'):
        face_sticker_active = False
        eyes_lips_sticker_active = True
    elif key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()