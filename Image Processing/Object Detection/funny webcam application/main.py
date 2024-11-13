import cv2

# img = cv2.imread('donald.jpg')
img = cv2.imread('harris.jpg')
# img = cv2.imread('elon.jpg')
img = cv2.resize(img, (800, 650))

overlay_x, overlay_y, overlay_w, overlay_h = 270, 380, 250, 100  

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    display_image = img.copy()

    h, w, _ = frame.shape

    center_x, center_y = w // 2, h // 2
    half_w, half_h = overlay_w // 2, overlay_h // 2
    cropped_frame = frame[center_y - half_h:center_y + half_h, center_x - half_w:center_x + half_w]
    display_image[overlay_y:overlay_y + overlay_h, overlay_x:overlay_x + overlay_w] = cropped_frame
    cv2.imshow('Camera Overlay', display_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
