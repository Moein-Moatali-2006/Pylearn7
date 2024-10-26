import cv2
import numpy as np

# بارگذاری تصویر به صورت مقیاس خاکستری
image = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)

# اعمال فیلتر GaussianBlur برای کاهش نویز تصویر
mask = cv2.GaussianBlur(image, (55, 55), 0)

# تعیین آستانه برای تفکیک پیکسل‌های روشن از تاریک
threshold = 127

# پیمایش در تمامی پیکسل‌های تصویر
for i in range(image.shape[0]):  # پیمایش سطرها
    for j in range(image.shape[1]):  # پیمایش ستون‌ها
        pix = image[i][j]  # گرفتن مقدار پیکسل در موقعیت (i, j)
        
        # اگر مقدار پیکسل بیشتر از آستانه باشد، آن را در ماسک ذخیره کن
        if pix > threshold:
            mask[i][j] = pix

# ذخیره تصویر نهایی با نام 'blurred_image.png'
cv2.imwrite("blurred_image.png", mask)
