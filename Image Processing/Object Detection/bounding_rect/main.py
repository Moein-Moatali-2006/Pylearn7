
import cv2
import numpy as np

def my_bounding_rect(contour):
    x_min = contour[0][0]
    y_min = contour[0][1]
    x_max = contour[0][0]
    y_max = contour[0][1]
    
    for list in contour:
        
        if x_min < list[0]:
            x_min = x_min
        else:
            x_min = list[0]

        if y_min < list[1]:
            y_min = y_min
        else:
            y_min = list[1]

        if x_max > list[0]:
            x_max = x_max
        else:
            x_max = list[0]

        if y_max > list[1]:
            y_max = y_max
        else :
            y_max = list[1]
    
    w = x_max - x_min
    h = y_max - y_min

    return x_min,y_min,w+1,h+1


contour = np.array([(100, 150), (150, 200), (200, 150), (150, 100), (250, 200), (220, 200)])

print("my function [my_bounding_rect]:")
x,y,w,h = my_bounding_rect(contour)
print(f"x:{x}")
print(f"y:{y}")
print(f"w:{w}")
print(f"h:{h}")


print("opencv function [cv2.boundingRect]:")
x, y, w, h = cv2.boundingRect(contour)
print(f"x: {x}")
print(f"y: {y}")
print(f"w: {w}")
print(f"h: {h}") 

