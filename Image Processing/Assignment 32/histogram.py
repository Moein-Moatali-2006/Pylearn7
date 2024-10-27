import cv2
import matplotlib.pyplot as plt


image = cv2.imread("input\Lion.jpg",cv2.IMREAD_GRAYSCALE)
hist=cv2.calcHist([image],[0],None,[256],[0,256])

# print(hist.astype(int))
plt.plot(hist)
plt.show()
