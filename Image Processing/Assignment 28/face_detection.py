import random
import cv2 as cv


image=cv.imread("family.jpg")
image_gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

image_sticker_red =cv.imread("sticker_red.jpg")
image_sticker_sun =cv.imread("sticker_sungalsses.jpg")
image_sticker_z =cv.imread("sticker_z.jpg")
stickers=[image_sticker_red,image_sticker_sun,image_sticker_z]

# face_detector =cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
face_detector =cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
# faces=face_detector.detectMultiScale(image_gray,1.3)
faces=face_detector.detectMultiScale(image_gray)

for face in faces:
    x,y,w,h=face
    # cv.rectangle(image,[x,y],[x+w,y+h],(0,0,0),4)
    sticker=cv.resize(random.choice(stickers),[w,h])
    image[y:y+h,x:x+w]=sticker
    



cv.imshow("result",image)
cv.waitKey(0)
cv.destroyAllWindows()