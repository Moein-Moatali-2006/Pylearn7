import cv2

image = cv2.imread("output.png")
image = cv2.cvtColor(image,cv2.COLOR_BGR2BGRA)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        b,g,r,a = image[i,j]
        if b==115 and g==115 and r==115:
            image[i,j,3]=0

cv2.imwrite("output_Alpha.png",image)