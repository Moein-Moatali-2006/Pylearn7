import numpy as np
import cv2
import tensorflow as tf
from functools import partial
from TFLiteFaceAlignment import CoordinateAlignmentModel
from TFLiteFaceDetector import UltraLightFaceDetecion


print("Loading ... ")
# خواندن تصاویر ورودی (چهره انسان )
image_face = cv2.imread("Biger_eyes_lips\input\img.jpg")

# ایندکس نقاط مختلف صورت
lips = [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64, 65]
eye_left = [41, 40, 42, 39, 37, 33, 36, 35]
eye_right = [89, 90, 87, 91, 93, 96, 94, 95]

def snapchat_filters(parameter):
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
        mask = np.zeros(image_face.shape, dtype=np.uint8) + 255
        cv2.drawContours(mask, [landmarks], -1, (255, 255, 255), -1)
        mask = mask // 255

        # اعمال ماسک روی تصویر و برش قسمت مورد نظر
        result = cv2.multiply(image_face, mask)
        result = result[y:y+h, x:x+w]
        result_big=cv2.resize(result,(0,0),fx=2,fy=2)

        # اعمال قسمت برش‌خورده روی تصویر میوه
        image_face[y:(y+h)*2, x:(x+w)*2] = result_big

    # ذخیره تصویر نهایی
    cv2.imwrite("Biger_eyes_lips\output\output.jpg", image_face)

# اعمال فیلترها برای لب‌ها، چشم چپ و چشم راست
snapchat_filters(lips)
snapchat_filters(eye_left)
snapchat_filters(eye_right)

print("finished")