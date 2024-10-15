import cv2
import numpy as np
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


def face_obj(part_of_face_landmarks_index):
    part_of_face_landmarks = []
    for landmark in part_of_face_landmarks_index:
        part_of_face_landmarks.append(pred[landmark])
    part_of_face_landmarks = np.array(part_of_face_landmarks, np.int16)
    return part_of_face_landmarks


def align_face(image, left_eye, right_eye, lips):
    left_eye_center = np.mean(left_eye, axis=0).astype(int)
    right_eye_center = np.mean(right_eye, axis=0).astype(int)
    print("Left Eye Center:", left_eye_center)
    print("Right Eye Center:", right_eye_center)

    dy = right_eye_center[1] - left_eye_center[1]
    dx = right_eye_center[0] - left_eye_center[0]
    angle = np.degrees(np.arctan2(dy, dx)) - 180

    eyes_center = (int(right_eye_center[0]), int(right_eye_center[1]))
    print(eyes_center)
    rotation_matrix = cv2.getRotationMatrix2D(eyes_center, angle, scale=1)

    aligned_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]), flags=cv2.INTER_CUBIC)

    return aligned_image


image = cv2.imread("Align Face\input\img.jpg")

lips_landmarks_index = [52, 64, 63, 71, 67, 68, 61, 58, 59, 53, 56, 55]
left_eye_landmarks_index = [89, 90, 87, 91, 93, 96, 94, 95]
right_eye_landmarks_index = [39, 42, 40, 41, 35, 36, 33, 37]

fd = UltraLightFaceDetecion("Models\RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("Models/coor_2d106.tflite")

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    lips = face_obj(lips_landmarks_index)
    print(lips)
    right_eye = face_obj(right_eye_landmarks_index)
    left_eye = face_obj(left_eye_landmarks_index)

aligned_image = align_face(image, left_eye, right_eye, lips)

cv2.imwrite("Align Face\output\output.jpg", aligned_image)
