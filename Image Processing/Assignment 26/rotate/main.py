import cv2 as cv


img=cv.imread("rotate\img.jpg")
img=cv.rotate(img,cv.ROTATE_180)

cv.imwrite("rotate\output.jpg",img)

cv.waitKey(0)
cv.destroyAllWindows()