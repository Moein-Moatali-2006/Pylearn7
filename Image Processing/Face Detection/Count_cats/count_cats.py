import random
import cv2


img=cv2.imread("Count_cats\input\cats.jpg")

face_detector=cv2.CascadeClassifier("Count_cats\haarcascade_frontalcatface.xml")
faces=face_detector.detectMultiScale(img)

colors_list=[(188,143,143),(210,105,30),(255,20,147),(128,0,128),(75,0,130),(72,209,204),(85,107,47),(218,165,32),(255,69,0),(128,128,128)]

for face in faces:
    x,y,w,h=face
    cv2.rectangle(img,(x,y),(x+w,y+h),random.choice(colors_list),4)

cv2.putText(img,f"output:{len(faces)}",(10,45),cv2.FONT_HERSHEY_COMPLEX,1,0,1)
cv2.imshow("result",img)
cv2.imwrite("Count_cats\output\output.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()