import cv2

image_1=cv2.imread("image_1.png")
image_2=cv2.imread("image_2.png")

image_1 = cv2.cvtColor(image_1,cv2.COLOR_BGR2GRAY)
image_2 = cv2.cvtColor(image_2,cv2.COLOR_BGR2GRAY)

image_1 = 255 - image_1
image_2 = 255 - image_2

result = image_1 - image_2
cv2.imwrite("output5.jpg",result)