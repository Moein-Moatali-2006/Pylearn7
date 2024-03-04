from PySide6.QtWidgets import QWidget,QPushButton
from ui_widget import Ui_widget

class Widget(QWidget,Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Moein Calculator")
        self.setGeometry(200,455,300,450)
        self.setMaximumHeight(450)
        self.setMaximumWidth(300)
        self.setMinimumHeight(450)
        self.setMinimumWidth(300)

        self.button_0.clicked.connect(self.on_button_click)
        self.button_1.clicked.connect(self.on_button_click)
        self.button_2.clicked.connect(self.on_button_click)
        self.button_3.clicked.connect(self.on_button_click)
        self.button_4.clicked.connect(self.on_button_click)
        self.button_5.clicked.connect(self.on_button_click)
        self.button_6.clicked.connect(self.on_button_click)
        self.button_7.clicked.connect(self.on_button_click)
        self.button_8.clicked.connect(self.on_button_click)
        self.button_9.clicked.connect(self.on_button_click)
        self.button_c.clicked.connect(self.on_button_click)
        self.button_decimal.clicked.connect(self.on_button_click)
        self.button_plus.clicked.connect(self.on_button_click)
        self.button_minus.clicked.connect(self.on_button_click)
        self.button_division.clicked.connect(self.on_button_click)
        self.button_multiply.connect(self.on_button_click)
        self.button_equals.clicked.connect(self.on_button_click)

    def on_button_click(self):
        button = self.sender()
        current_text = self.main_label.text()

        if current_text == "0":
            current_text = ""
        
        if button.text() == "=":
            try:
                result=str(eval(current_text))
                self.main_label.setText(result)
                self.main_label_2.setText(current_text + button.text())
            except ZeroDivisionError:
                self.main_label.setText("Error: Division by zero")
            except Exception as e:
                self.main_label.setText("Error: Invalid expression")
        else:
            self.main_label.setText(current_text + button.text())
            self.main_label_2.setText(current_text + button.text())

        if button.text() == "C":
            self.main_label.setText("0")
            self.main_label_2.setText("")

        



        
