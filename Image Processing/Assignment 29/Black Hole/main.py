import os
import cv2
import numpy as np


def noise_reduction(folder_path=""):
    images_path=os.listdir(folder_path)
    images=[]
    for image_path in images_path:
        image = cv2.imread(folder_path+f"\{image_path}")
        image = image.astype(np.float32)
        images.append(image)

    result = np.zeros(image.shape)

    for image in images:
        result += image 

    result = result / len(images)
    result.astype(np.uint8)

    return result

result_1=noise_reduction("1")
result_2=noise_reduction("2")
result_3=noise_reduction("3")
result_4=noise_reduction("4")

final_1 = np.concatenate((result_1,result_2),axis=1)
final_2 = np.concatenate((result_3,result_4),axis=1)

result = np.concatenate((final_1,final_2),axis=0)

cv2.imwrite("output.jpg",result)