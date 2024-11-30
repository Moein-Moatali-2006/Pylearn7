import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

# تعریف کلاس اصلی
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # تنظیمات اولیه پنجره
        self.setWindowTitle(" Image Encryption and Decryption 🔐 ")
        self.setGeometry(100, 100, 900, 400)

        # ویجت مرکزی
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # لایه‌بندی افقی برای نمایش تصاویر
        layout = QHBoxLayout()

        # QLabel برای نمایش تصاویر
        self.input_image_label = QLabel("Input Image", self)
        self.input_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.input_image_label)

        self.encrypted_image_label = QLabel("Encrypted Image", self)
        self.encrypted_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.encrypted_image_label)

        self.decrypted_image_label = QLabel("Decrypted Image", self)
        self.decrypted_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.decrypted_image_label)

        # تنظیم لایه‌بندی برای ویجت مرکزی
        central_widget.setLayout(layout)

        # بارگذاری تصاویر خود شما
        self.load_images()

    def load_images(self):
        # بارگذاری تصاویر از مسیرهای مشخص‌شده (لطفاً مسیر صحیح را وارد کنید)
        input_image_path = "input.jpg"
        encrypted_image_path = "image_encrypted.bmp"
        decrypted_image_path = "decrypted_image.jpg"

        # بارگذاری تصاویر به صورت QPixmap
        input_pixmap = QPixmap(input_image_path)
        encrypted_pixmap = QPixmap(encrypted_image_path)
        decrypted_pixmap = QPixmap(decrypted_image_path)

        # تنظیم اندازه تصویر بدون تغییر کیفیت
        self.input_image_label.setPixmap(input_pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.encrypted_image_label.setPixmap(encrypted_pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.decrypted_image_label.setPixmap(decrypted_pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

# اجرای برنامه
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
