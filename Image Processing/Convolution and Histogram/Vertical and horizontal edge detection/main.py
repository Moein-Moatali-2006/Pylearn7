import cv2
import numpy as np

# تعریف کرنل عمودی برای تشخیص لبه‌ها
kernel_vertical = np.array([[-1, -2, -1],
                             [0, 0, 0],
                             [1, 2, 1]])

# تعریف کرنل افقی برای تشخیص لبه‌ها
kernel_horizontal = np.array([[1, 0, -1],
                              [2, 0, -2],
                              [1, 0, -1]])

def Vertical_and_horizontal_edge_detection(image, kernel_type, output_name):
    """
    تشخیص لبه‌های عمودی و افقی با استفاده از کرنل‌های کانولوشن.

    پارامترها:
    - image: تصویر ورودی به صورت ماتریس NumPy
    - kernel_type: کرنل مورد استفاده برای تشخیص لبه
    - output_name: نام فایل خروجی برای ذخیره تصویر نتیجه
    """
    # ایجاد ماسک خالی برای ذخیره نتایج
    mask = np.zeros(image.shape, dtype=np.uint8)

    # پیمایش در پیکسل‌های تصویر به جز حاشیه‌ها
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            # استخراج زیرماتریس \(3 \times 3\) از تصویر
            pix_3_3 = image[i-1:i+2, j-1:j+2]
            # محاسبه شدت لبه با استفاده از کرنل
            mask[i][j] = np.abs(np.sum(pix_3_3 * kernel_type))

    # ذخیره تصویر نتیجه با نام مشخص
    cv2.imwrite(f"{output_name}.png", mask)

# بارگذاری تصویر به صورت مقیاس خاکستری
image = cv2.imread("House.png", cv2.IMREAD_GRAYSCALE)

# فراخوانی تابع تشخیص لبه با کرنل عمودی
Vertical_and_horizontal_edge_detection(image, kernel_vertical, "kernel_vertical")
# فراخوانی تابع تشخیص لبه با کرنل افقی
Vertical_and_horizontal_edge_detection(image, kernel_horizontal, "kernel_horizontal")
