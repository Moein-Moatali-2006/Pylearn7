import cv2 as cv 


img=cv.imread("black_tape\img.png")
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.line(img,(150,0),(0,150),(0,0,0),45)

cv.imwrite("black_tape\output.png",img)
cv.waitKey(0)
cv.destroyAllWindows()