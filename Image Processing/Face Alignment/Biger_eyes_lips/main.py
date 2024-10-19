import numpy as np
import cv2
from TFLiteFaceAlignment import CoordinateAlignmentModel
from TFLiteFaceDetector import UltraLightFaceDetecion

print("Loading ... ")
# خواندن تصویر ورودی (چهره انسان)
image_face = cv2.imread("Biger_eyes_lips/input/img.jpg")

# ایندکس نقاط مختلف صورت
lips = [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64, 65]
eye_left = [41, 40, 42, 39, 37, 33, 36, 35]
eye_right = [89, 90, 87, 91, 93, 96, 94, 95]

def snapchat_filters(parameter, scale_factor=2):
    # بارگذاری مدل‌های تشخیص چهره و هم‌راستاسازی نقاط صورت
    fd = UltraLightFaceDetecion("Models/RFB-320.tflite", conf_threshold=0.88)
    fa = CoordinateAlignmentModel("Models/coor_2d106.tflite")

    # انجام عملیات تشخیص چهره روی تصویر ورودی
    boxes, scores = fd.inference(image_face)

    for pred in fa.get_landmarks(image_face, boxes):
        # دریافت نقاط انتخابی از ویژگی‌های صورت
        landmarks = [pred[i] for i in parameter]
        landmarks = np.array(landmarks, dtype=np.int_)

        # ایجاد ماسک برای محدوده انتخاب شده (لب یا چشم‌ها)
        x, y, w, h = cv2.boundingRect(landmarks)
        mask = np.zeros(image_face.shape[:2], dtype=np.uint8) +255 # ماسک سیاه و سفید
        cv2.fillPoly(mask, [landmarks], 255)

        # استخراج قسمت انتخابی
        roi = cv2.bitwise_and(image_face, image_face, mask=mask)

        # برش قسمت انتخابی از چهره
        roi_cropped = roi[y:y+h, x:x+w]

        # بزرگ‌نمایی قسمت برش‌خورده
        result_big = cv2.resize(roi_cropped, (0, 0), fx=scale_factor, fy=scale_factor)

        # جایگذاری قسمت بزرگ شده روی چهره
        new_w, new_h = result_big.shape[1], result_big.shape[0]

        # محاسبه مختصات جدید برای قرار دادن تصویر بزرگ‌شده در مکان صحیح
        center_x, center_y = np.mean(landmarks[:, 0]), np.mean(landmarks[:, 1])
        top_left_x = int(center_x - new_w // 2)
        top_left_y = int(center_y - new_h // 2)

        # قرار دادن قسمت بزرگ‌شده روی تصویر اصلی
        image_face[top_left_y:top_left_y+new_h, top_left_x:top_left_x+new_w] = result_big

    # ذخیره تصویر نهایی
    cv2.imwrite("Biger_eyes_lips/output/output.jpg", image_face)

# اعمال فیلترها برای لب‌ها، چشم چپ و چشم راست
snapchat_filters(lips)
snapchat_filters(eye_left)
snapchat_filters(eye_right)

print("Finished")
