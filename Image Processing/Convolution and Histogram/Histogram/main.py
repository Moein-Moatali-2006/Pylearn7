import cv2
import numpy as np
import matplotlib.pyplot as plt

# بارگذاری تصویر به صورت خاکستری (grayscale)
image = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)

# تابع برای محاسبه هیستوگرام تصویر
def histogram_calculate(image):
    # ایجاد لیستی برای نگهداری مقادیر هیستوگرام (256 مقدار برای سطوح خاکستری)
    histogram = [0 for i in range(256)]
    
    # پیمایش در تمامی پیکسل‌های تصویر
    for i in range(image.shape[0]):  # حلقه برای سطرهای تصویر (ارتفاع)
        for j in range(image.shape[1]):  # حلقه برای ستون‌های تصویر (عرض)
            # دریافت مقدار شدت روشنایی پیکسل (بین 0 تا 255)
            number = image[i][j]
            # افزایش مقدار هیستوگرام برای مقدار روشنایی پیکسل
            histogram[number] += 1 
    
    return histogram

# محاسبه هیستوگرام تصویر با استفاده از تابع
hist = histogram_calculate(image)

# نمایش هیستوگرام با استفاده از matplotlib
# plt.hist(hist)
# plt.plot(hist)
# plt.bar(range(256),hist)
plt.title("Histogram")
plt.show()
