import cv2


face_sticker = cv2.imread("input\image_lion.png")


face_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

face_sticker_active = False

while True:
    _, frame = cap.read()
    if not _:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    if face_sticker_active:
        for (x, y, w, h) in faces:
            resized_sticker = cv2.resize(face_sticker, (w, h))

            for i in range(resized_sticker.shape[0]):
                for j in range(resized_sticker.shape[1]):
                    if all(resized_sticker[i, j] != 0):
                        frame[y + i, x + j] = resized_sticker[i, j]

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        face_sticker_active = True
    elif key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
