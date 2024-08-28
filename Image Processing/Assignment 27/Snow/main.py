import cv2
import random

snow_frame=cv2.imread("Snow\snow.png")
snow_frame=cv2.cvtColor(snow_frame,cv2.COLOR_BGR2GRAY)

height, width = snow_frame.shape

num_snowflakes = 1000
snowflakes = []

for _ in range(num_snowflakes):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    snowflakes.append([x, y])

cap=cv2.VideoWriter("Snow\out_snow.avi",cv2.VideoWriter_fourcc(*'XVID'),
               25,(snow_frame.shape[1],snow_frame.shape[0]),False)

while True: 
    frame = snow_frame.copy()
    for snowflake in snowflakes:
        x, y = snowflake
        cv2.circle(frame, (x, y), 2, 255, -1)

    for snowflake in snowflakes:
        snowflake[1] += random.randint(1, 3)

        if snowflake[1] > height:
            snowflake[0] = random.randint(0, width - 1)
            snowflake[1] = 0

    cv2.imshow('Snow', frame)
    cap.write(frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
