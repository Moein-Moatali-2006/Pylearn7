# import Libraries
import cv2

# Load images 
face_sticker = cv2.imread("input\image_lion.png")
lips_sticker = cv2.imread("input\image_lips.png")
sunglasses_sticker = cv2.imread("input\image_sunglasses.png")

# Load Models
face_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
lips_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
eye_detect_right = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_righteye_2splits.xml')
eye_detect_left = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_lefteye_2splits.xml')

# connect to webcam
cap = cv2.VideoCapture(0)

# Filters active
face_sticker_active = False
eyes_lips_sticker_active = False
blur_face_active = False
mirror_frame_active = False 

# Start work with frames
while True:
    _, frame = cap.read()
    if not _:
        break

    # convert frame to gray
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
        eye_left =eye_detect_left.detectMultiScale(gray, 1.3,15,minSize=[30,30],maxSize=[80,80])
        eye_right =eye_detect_right.detectMultiScale(gray, 1.3,15,minSize=[30,30],maxSize=[80,80])
    
        for e_left in eye_left:
            x,y,w,h=e_left
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),-1)

        for e_right in eye_right:
            x,y,w,h=e_right
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),-1)
    
    # Blur face
    if blur_face_active:
        faces=face_detect.detectMultiScale(gray,1.3)
        for face in faces:
            x,y,w,h = face
            my_face=frame[y:y+h,x:x+w]
            face_resized_small=cv2.resize(my_face,[10,10])
            face_resized_big=cv2.resize(face_resized_small,[w,h],interpolation=cv2.INTER_NEAREST)
            frame[y:y+h,x:x+w]=face_resized_big
    
    # Mirror
    if mirror_frame_active:
        mirror_1=cv2.flip(frame,1)
        mirror_2=cv2.flip(mirror_1,1)
        frame = cv2.hconcat([mirror_1,mirror_2])
       
    # show frame
    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF

    # Check the keyboard entries
    if key == ord('1'):
        mirror_frame_active = False
        blur_face_active = False
        eyes_lips_sticker_active =False
        face_sticker_active = True
    elif key == ord('2'):
        mirror_frame_active = False
        blur_face_active = False
        face_sticker_active = False
        eyes_lips_sticker_active = True
    elif key == ord('3'):
        mirror_frame_active = False
        face_sticker_active = False
        eyes_lips_sticker_active = False
        blur_face_active = True
    elif key == ord('4'):
        face_sticker_active = False
        eyes_lips_sticker_active = False
        blur_face_active = False
        mirror_frame_active = True
    elif key == ord('q'):
        break

# Release of resources
cap.release()
cv2.destroyAllWindows()