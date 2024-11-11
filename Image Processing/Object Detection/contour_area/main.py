import cv2
import numpy as np


def calculate_contour_area(contour):
    number = len(contour)
    area = 0

    for i in range(number):
        x_i, y_i = contour[i][0]
        x_next, y_next = contour[(i + 1) % number][0]
        area += x_i * y_next - x_next * y_i

    return abs(area) / 2


image = np.ones((500, 500), dtype=np.uint8) * 255

cv2.circle(image, (250, 250), 100, (0, 0, 0), -1)

contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) > 0:
    area = cv2.contourArea(contours[0])
    print("opencv contour area:", area)

    my_area = calculate_contour_area(contours[0])
    print("my contour area:", my_area)


