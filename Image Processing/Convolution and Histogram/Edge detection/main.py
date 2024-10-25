import cv2  # کتابخانه OpenCV برای پردازش تصویر
import numpy as np  # کتابخانه NumPy برای محاسبات عددی

# بارگذاری تصاویر به صورت مقادیر خاکستری
image_lion = cv2.imread("lion.png", cv2.IMREAD_GRAYSCALE)
image_spider = cv2.imread("spider.png", cv2.IMREAD_GRAYSCALE)

# تعریف هسته تشخیص لبه
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

def edge_detection(image, name):
    # ایجاد یک ماسک خالی برای ذخیره لبه‌ها
    mask = np.zeros(image.shape, dtype=np.uint8)

    # پیمایش در هر پیکسل تصویر (به جز مرزها)
    for i in range(1, image.shape[0]-1):
        for j in range(1, image.shape[1]-1):
            # استخراج ناحیه 3x3 حول پیکسل جاری
            pix_3_3 = image[i-1:i+2, j-1:j+2]
            # اعمال هسته و ذخیره نتیجه در ماسک
            mask[i][j] = np.abs(np.sum(pix_3_3 * kernel))

    # ذخیره تصویر خروجی
    cv2.imwrite(f"{name}.png", mask) 

# فراخوانی تابع برای هر تصویر
edge_detection(image_lion, "image_lion_output")
edge_detection(image_spider, "image_spider_output")
