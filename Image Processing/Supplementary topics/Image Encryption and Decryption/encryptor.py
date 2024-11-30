from cryptography.fernet import Fernet

# 1. تولید کلید رمزنگاری
key = Fernet.generate_key()
cipher = Fernet(key)

# 2. خواندن تصویر به‌صورت باینری
with open("input.jpg", "rb") as file:
    image_data = file.read()

# 3. رمزگذاری تصویر
encrypted_data = cipher.encrypt(image_data)

# 4. ذخیره فایل رمزگذاری شده
with open("image_encrypted.bmp", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

# ذخیره کلید (برای رمزگشایی نیاز است)
with open("key.npy", "wb") as key_file:
    key_file.write(key)
