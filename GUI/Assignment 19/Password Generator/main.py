import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication,QMainWindow,QButtonGroup
from main_ui import Ui_MainWindow


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.easy_list=["1","2","3","4","5","6","7","8","9","0"]
        self.hard_list=["1","2","3","4","5","6","7","8","9","0",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.difficult_list=["1","2","3","4","5","6","7","8","9","0",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',"!","@","#","$","%","^","&","*","(",")","+"]

        self.buttonGroup=QButtonGroup()
        self.buttonGroup.addButton(self.ui.radio_easy)
        self.buttonGroup.addButton(self.ui.radio_hard)
        self.buttonGroup.addButton(self.ui.radio_difficult)

        self.ui.radio_easy.toggled.connect(self.easy)
        self.ui.radio_hard.toggled.connect(self.hard)
        self.ui.radio_difficult.toggled.connect(self.difficult)

    def easy(self,check):
        if check:
            self.ui.btn_creat.clicked.connect(partial(self.x))
    
    def x(self):
        output=""
        random.shuffle(self.easy_list)
        for item in range(8):
            output+= self.easy_list[item]
        self.ui.text_box.setText(output)

    def hard(self,check):
        if check:
            self.ui.btn_creat.clicked.connect(partial(self.a))

    def a(self):
        output=""
        random.shuffle(self.hard_list)
        for item in range(8):
            output+= self.hard_list[item]
        self.ui.text_box.setText(output)

    def difficult(self,check):
        if check:
            self.ui.btn_creat.clicked.connect(partial(self.f))

    def f(self):
        output=""
        random.shuffle(self.difficult_list)
        for item in range(8):
            output+= self.difficult_list[item]
        self.ui.text_box.setText(output)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    main_window=Main_Window()
    main_window.show()
    app.exec()