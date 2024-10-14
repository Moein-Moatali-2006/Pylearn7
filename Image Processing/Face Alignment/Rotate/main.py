import numpy as np
import cv2
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

# اندکس نقاط مختلف صورت
lips = [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64, 65]
eye_left = [41, 40, 42, 39, 37, 33, 36, 35]
eye_right = [89, 90, 87, 91, 93, 96, 94, 95]

# بارگذاری مدل‌ها
fd = UltraLightFaceDetecion("Models/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("Models/coor_2d106.tflite")

# بارگذاری تصویر اصلی
image_face = cv2.imread("Rotate/input/Face.jpg")
height, width = image_face.shape[:2]

# تشخیص چهره و یافتن نقاط
boxes, scores = fd.inference(image_face)
for pred in fa.get_landmarks(image_face, boxes):
    
    # گرفتن مختصات لب‌ها
    lips_landmarks = np.array([pred[i] for i in lips], dtype=np.int_)
    x_lips, y_lips, w_lips, h_lips = cv2.boundingRect(lips_landmarks)
    mask_lips = np.zeros(image_face.shape, dtype=np.uint8) +255
    cv2.drawContours(mask_lips, [lips_landmarks], -1, (255, 255, 255), -1)
    mask_lips = mask_lips // 255
    result_lips = image_face * mask_lips
    result_lips = result_lips[y_lips:y_lips + h_lips, x_lips:x_lips + w_lips]

    # گرفتن مختصات چشم چپ
    eye_left_landmarks = np.array([pred[i] for i in eye_left], dtype=np.int_)
    x_eye_left, y_eye_left, w_eye_left, h_eye_left = cv2.boundingRect(eye_left_landmarks)
    mask_eye_left = np.zeros(image_face.shape, dtype=np.uint8) +255
    cv2.drawContours(mask_eye_left, [eye_left_landmarks], -1, (255, 255, 255), -1)
    mask_eye_left = mask_eye_left // 255
    result_eye_left = image_face * mask_eye_left
    result_eye_left = result_eye_left[y_eye_left:y_eye_left + h_eye_left, x_eye_left:x_eye_left + w_eye_left]

    # گرفتن مختصات چشم راست
    eye_right_landmarks = np.array([pred[i] for i in eye_right], dtype=np.int_)
    x_eye_right, y_eye_right, w_eye_right, h_eye_right = cv2.boundingRect(eye_right_landmarks)
    mask_eye_right = np.zeros(image_face.shape, dtype=np.uint8) +255
    cv2.drawContours(mask_eye_right, [eye_right_landmarks], -1, (255, 255, 255), -1)
    mask_eye_right = mask_eye_right // 255
    result_eye_right = image_face * mask_eye_right
    result_eye_right = result_eye_right[y_eye_right:y_eye_right + h_eye_right, x_eye_right:x_eye_right + w_eye_right]

# چرخش تصویر اصلی به اندازه ۱۸۰ درجه
image_face_rotated = cv2.rotate(image_face, cv2.ROTATE_180)

# محاسبه مختصات جدید لب‌ها بعد از چرخش
rotated_lips_landmarks = np.array([(width - x, height - y) for (x, y) in lips_landmarks], dtype=np.int_)
x_rot_lips, y_rot_lips, w_rot_lips, h_rot_lips = cv2.boundingRect(rotated_lips_landmarks)
mask_rot_lips = np.zeros(image_face_rotated.shape, dtype=np.uint8) 
cv2.drawContours(mask_rot_lips, [rotated_lips_landmarks], -1, (255, 255, 255), -1)
mask_rot_lips = mask_rot_lips // 255
image_face_rotated[y_rot_lips:y_rot_lips + h_rot_lips, x_rot_lips:x_rot_lips + w_rot_lips] = result_lips

# محاسبه مختصات جدید چشم چپ بعد از چرخش
rotated_eye_left_landmarks = np.array([(width - x, height - y) for (x, y) in eye_left_landmarks], dtype=np.int_)
x_rot_eye_left, y_rot_eye_left, w_rot_eye_left, h_rot_eye_left = cv2.boundingRect(rotated_eye_left_landmarks)
mask_rot_eye_left = np.zeros(image_face_rotated.shape, dtype=np.uint8) 
cv2.drawContours(mask_rot_eye_left, [rotated_eye_left_landmarks], -1, (255, 255, 255), -1)
mask_rot_eye_left = mask_rot_eye_left // 255
image_face_rotated[y_rot_eye_left:y_rot_eye_left + h_rot_eye_left, x_rot_eye_left:x_rot_eye_left + w_rot_eye_left] = result_eye_left

# محاسبه مختصات جدید چشم راست بعد از چرخش
rotated_eye_right_landmarks = np.array([(width - x, height - y) for (x, y) in eye_right_landmarks], dtype=np.int_)
x_rot_eye_right, y_rot_eye_right, w_rot_eye_right, h_rot_eye_right = cv2.boundingRect(rotated_eye_right_landmarks)
mask_rot_eye_right = np.zeros(image_face_rotated.shape, dtype=np.uint8) 
cv2.drawContours(mask_rot_eye_right, [rotated_eye_right_landmarks], -1, (255, 255, 255), -1)
mask_rot_eye_right = mask_rot_eye_right // 255
image_face_rotated[y_rot_eye_right:y_rot_eye_right + h_rot_eye_right, x_rot_eye_right:x_rot_eye_right + w_rot_eye_right] = result_eye_right

# ذخیره تصویر نهایی
cv2.imwrite("Rotate/output/output_final.jpg", image_face_rotated)
