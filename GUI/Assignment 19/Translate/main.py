import sys
import gtts
from os import path
from functools import partial
from gtts import gTTS 
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QMainWindow, QWidget,QMessageBox,QRadioButton,QButtonGroup
from main_ui import Ui_MainWindow


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.read_from_file()
        self.buttonGroup =QButtonGroup()
        self.buttonGroup.addButton(self.ui.radio_EP)
        self.buttonGroup.addButton(self.ui.radio_PE)
        self.ui.radio_EP.toggled.connect(self.onRadioButton1Clicked)
        self.ui.radio_PE.toggled.connect(self.onRadioButton2Clicked)
        self.make_sound()

    def onRadioButton1Clicked(self,checked):
        if checked:
            self.ui.btn_translate.clicked.connect(partial(self.translate_english_to_persian))

    def onRadioButton2Clicked(self,checked):
        if checked:
            self.ui.btn_translate.clicked.connect(partial(self.translate_persian_to_english))

    def read_from_file(self):
            if path.exists("data_base_words.txt"):
                global words_bank
                f=open("data_base_words.txt","r")
                temp=f.read().split("\n")
                words_bank=[]
                for i in range(0,len(temp),2):
                    my_dict={"en":temp[i],"fa":temp[i+1]}
                    words_bank.append(my_dict)

                f.close()
            else:
                msg_box=QMessageBox()
                msg_box.setText("database not found")
                msg_box.exec()

    def translate_english_to_persian(self):
            user_text=self.ui.lineEdit.text()
            list_user_word=user_text.split(" ")
            output=""
            for word in list_user_word:
                for item in words_bank:
                    if word == item["en"]:
                        output=output+item["fa"]+" "
                        break
                else:
                    output=output+word+" "
            
            self.ui.lineEdit_2.setText(output)

    def translate_persian_to_english(self):
            user_text=self.ui.lineEdit.text()
            list_user_word=user_text.split(" ")
            output=""
            for word in list_user_word:
                for item in words_bank:
                    if word == item["fa"]:
                        output=output+item["en"]+" "
                        break
                else:
                    output=output+word+" "
            
            self.ui.lineEdit_2.setText(output)

    def make_sound(self):
        self.ui.btn_sound.clicked.connect(partial(self.speak))

    def speak(self):
            voice=gTTS(self.ui.lineEdit_2.text(),lang="en")
            voice.save("voice.mp3")
   

if __name__ == "__main__":
    app=QApplication(sys.argv)
    main_window=Main_Window()
    main_window.show()
    app.exec()

