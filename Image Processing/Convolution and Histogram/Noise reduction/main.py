import cv2
import numpy as np

def noise_reduction(image, output_name):

    # ایجاد ماسک‌های خالی برای هر اندازه کرنل
    mask_3_3 = np.zeros(image.shape, dtype=np.uint8)
    mask_5_5 = np.zeros(image.shape, dtype=np.uint8)
    mask_15_15 = np.zeros(image.shape, dtype=np.uint8)

    # فیلتر \(3 \times 3\)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            pix_3_3 = image[i-1:i+2, j-1:j+2]  # استخراج زیرماتریس \(3 \times 3\)
            pix_averaged = np.mean(pix_3_3)  # محاسبه میانگین
            mask_3_3[i][j] = pix_averaged  # ذخیره میانگین در ماسک

    # ذخیره تصویر فیلتر شده \(3 \times 3\)
    cv2.imwrite(f"output/{output_name}_3_3.png", mask_3_3)

    # فیلتر \(5 \times 5\)
    for i in range(2, image.shape[0] - 2):
        for j in range(2, image.shape[1] - 2):
            pix_5_5 = image[i-2:i+3, j-2:j+3]  # استخراج زیرماتریس \(5 \times 5\)
            pix_averaged = np.mean(pix_5_5)  # محاسبه میانگین
            mask_5_5[i][j] = pix_averaged  # ذخیره میانگین در ماسک

    # ذخیره تصویر فیلتر شده \(5 \times 5\)
    cv2.imwrite(f"output/{output_name}_5_5.png", mask_5_5)

    # فیلتر \(15 \times 15\)
    for i in range(7, image.shape[0] - 7):  # اصلاح محدوده پیمایش
        for j in range(7, image.shape[1] - 7):
            pix_15_15 = image[i-7:i+8, j-7:j+8]  # استخراج زیرماتریس \(15 \times 15\)
            pix_averaged = np.mean(pix_15_15)  # محاسبه میانگین
            mask_15_15[i][j] = pix_averaged  # ذخیره میانگین در ماسک

    # ذخیره تصویر فیلتر شده \(15 \times 15\)
    cv2.imwrite(f"output/{output_name}_15_15.png", mask_15_15)

# بارگذاری تصاویر ورودی به صورت مقیاس خاکستری
image_1 = cv2.imread("input/ima_xray.png", cv2.IMREAD_GRAYSCALE)
image_2 = cv2.imread("input/img_board.png", cv2.IMREAD_GRAYSCALE)
image_3 = cv2.imread("input/img_noise.png", cv2.IMREAD_GRAYSCALE)

# اعمال کاهش نویز بر روی تصاویر
noise_reduction(image_1, "image_1")
noise_reduction(image_2, "image_2")
noise_reduction(image_3, "image_3")
