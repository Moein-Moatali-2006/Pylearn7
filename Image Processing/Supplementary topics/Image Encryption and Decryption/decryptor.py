from cryptography.fernet import Fernet

# 1. بازیابی کلید
with open("key.npy", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# 2. خواندن فایل رمزگذاری شده
with open("image_encrypted.bmp", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# 3. رمزگشایی داده‌ها
decrypted_data = cipher.decrypt(encrypted_data)

# 4. ذخیره تصویر رمزگشایی شده
with open("decrypted_image.jpg", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)
