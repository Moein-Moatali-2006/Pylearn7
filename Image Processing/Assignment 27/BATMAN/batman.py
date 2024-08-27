import cv2 as cv 


img=cv.imread("BATMAN\input_batman.png")
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

threshold=int(255/2)
_ , image =cv.threshold(img,threshold,255,cv.THRESH_BINARY_INV)


cv.putText(image,"BATMAN",(320,450),cv.FONT_HERSHEY_DUPLEX,2,255)

cv.imwrite("BATMAN\output_batman.png",image)
cv.waitKey(0)
cv.destroyAllWindows()