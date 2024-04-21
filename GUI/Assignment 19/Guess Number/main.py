import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication,QMainWindow
from main_ui import Ui_MainWindow


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.number=random.randint(1,100)
        self.ui.btn_check.clicked.connect(partial(self.play))

    def play(self):
        user_number=int(self.ui.text_box.text())
        if user_number > self.number:
            self.ui.label_2.setText("go down👇🏼")
        elif user_number <  self.number :
            self.ui.label_2.setText("go up👆🏼")
        elif user_number == self.number:
            self.ui.label_2.setText("Great 😍 🤩")


if __name__ == "__main__":
    app=QApplication(sys.argv)
    main_window=Main_Window()
    main_window.show()
    app.exec()