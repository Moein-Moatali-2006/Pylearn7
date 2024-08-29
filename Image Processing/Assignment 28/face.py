import cv2 

def chess_face(image):

    image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    faces=face_detector.detectMultiScale(image_gray)
    for face in faces:
        x,y,w,h=face
        face_image=image[y:y+h,x:x+w]
        face_image_small=cv2.resize(face_image,[10,10])
        face_image_big=cv2.resize(face_image_small,[w,h],interpolation=cv2.INTER_NEAREST)
        image[y:y+h,x:x+w] = face_image_big


cap=cv2.VideoCapture(0)
face_detector =cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    _,frame=cap.read()
    image= chess_face(frame)
    cv2.imshow("Result",frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
