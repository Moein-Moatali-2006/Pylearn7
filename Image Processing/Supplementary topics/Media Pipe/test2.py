import cv2
import mediapipe as mp


mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # پردازش تصویر برای تشخیص حالت بدن
    results = pose.process(frame_rgb)

    # اگر نقاط کلیدی شناسایی شدند، آنها را رسم کن
    if results.pose_landmarks:
        # رسم نقاط کلیدی و اتصالات روی تصویر
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow("Pose Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# آزاد کردن منابع
cap.release()
cv2.destroyAllWindows()
