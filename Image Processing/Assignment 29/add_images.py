import cv2
import numpy as np

image_human=cv2.imread("human.jpg")
image_horse=cv2.imread("horse.jpg")

image_human=cv2.cvtColor(image_human,cv2.COLOR_BGR2GRAY)
image_horse=cv2.cvtColor(image_horse,cv2.COLOR_BGR2GRAY)

#1
# result = image_human + image_horse

#2
# result = cv2.add(image_human , image_horse)

#3
# result = np.add(image_human , image_horse)

#4 # important
# image_human = image_human.astype(np.float32) # یک روش
# image_horse = image_horse.astype("float32") # یک روش 

# result = image_human + image_horse
# result = result.astype("uint8")

cv2.imwrite("output/result.jpg",result)