import cv2
import numpy as np

image_main = cv2.imread("SuperMan.jpg")
image = cv2.imread("city.jpg")

image = cv2.resize(image, (image_main.shape[1], image_main.shape[0]))

image_main_HSV = cv2.cvtColor(image_main, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 50, 50])  
upper_green = np.array([85, 255, 255])  

mask = cv2.inRange(image_main_HSV, lower_green, upper_green)

mask_inv = cv2.bitwise_not(mask)

main_no_green = cv2.bitwise_and(image_main, image_main, mask=mask_inv)

background_green = cv2.bitwise_and(image, image, mask=mask)

result = cv2.add(main_no_green, background_green)

cv2.imwrite("result.jpg", result)