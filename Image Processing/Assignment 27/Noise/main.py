import cv2 as cv
import numpy as np


img=cv.imread("Noise\TV.png")
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
out=cv.VideoWriter("Noise\out_noise.avi",cv.VideoWriter_fourcc(*'XVID'),
               25,(img.shape[1],img.shape[0]),False)
while True:
    img_noise=np.random.random((243,444)) * 255
    img_noise=np.array(img_noise,dtype=np.uint8)
    
    x, y = 18, 14 
    img[y:y+243, x:x+444] = img_noise

    cv.imshow("result",img)
    out.write(img)
    if cv.waitKey(25) & 0xFF == ord('q'):
      break


