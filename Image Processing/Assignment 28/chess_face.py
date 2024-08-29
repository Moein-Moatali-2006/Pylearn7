import cv2

image=cv2.imread("sajjad.jpg")
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face_detector =cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
faces=face_detector.detectMultiScale(image_gray)


for face in faces:
    x,y,w,h=face
    face_image=image[y:y+h,x:x+w]
    face_image_small=cv2.resize(face_image,[10,10])
    face_image_big=cv2.resize(face_image_small,[w,h],interpolation=cv2.INTER_NEAREST)

    image[y:y+h,x:x+w] = face_image_big
    



cv2.imshow("result",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
