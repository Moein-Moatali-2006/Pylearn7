import cv2
import numpy as np


height, width = 600, 900
field = np.zeros((height, width, 3), dtype=np.uint8)


stripe_width = 100

for i in range(0, width, stripe_width):
    if (i // stripe_width) % 2 == 0:
        color = (0, 100, 0)
    else:
        color=(0, 80, 0)
    cv2.rectangle(field, (i, 0), (i + stripe_width, height), color, -1)

line_thickness = 3

cv2.rectangle(field, (50, 50), (width - 50, height - 50), (255, 255, 255), line_thickness)

cv2.line(field, (width // 2, 50), (width // 2, height - 50), (255, 255, 255), line_thickness)

cv2.circle(field, (width // 2, height // 2), 80, (255, 255, 255), line_thickness)

cv2.circle(field, (width // 2, height // 2), 10, (255, 255, 255), -1)

cv2.rectangle(field, (50, height // 2 - 100), (150, height // 2 + 100), (255, 255, 255), line_thickness)
cv2.rectangle(field, (width - 150, height // 2 - 100), (width - 50, height // 2 + 100), (255, 255, 255), line_thickness)

cv2.rectangle(field, (50, height // 2 - 50), (100, height // 2 + 50), (255, 255, 255), line_thickness)
cv2.rectangle(field, (width - 100, height // 2 - 50), (width - 50, height // 2 + 50), (255, 255, 255), line_thickness)

cv2.imwrite("football_pitch\output\output.jpg",field)
cv2.imshow('Football', field)
cv2.waitKey(0)
cv2.destroyAllWindows()
