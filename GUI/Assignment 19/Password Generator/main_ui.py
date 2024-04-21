# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(412, 160)
        MainWindow.setStyleSheet(u"background-color:rgb(72, 72, 72);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.radio_easy = QRadioButton(self.centralwidget)
        self.radio_easy.setObjectName(u"radio_easy")
        self.radio_easy.setGeometry(QRect(10, 10, 89, 20))
        self.radio_easy.setStyleSheet(u"background-color:rgb(0, 255, 0);")
        self.radio_hard = QRadioButton(self.centralwidget)
        self.radio_hard.setObjectName(u"radio_hard")
        self.radio_hard.setGeometry(QRect(10, 40, 89, 20))
        self.radio_hard.setStyleSheet(u"background-color:rgb(0, 170, 0);")
        self.radio_difficult = QRadioButton(self.centralwidget)
        self.radio_difficult.setObjectName(u"radio_difficult")
        self.radio_difficult.setGeometry(QRect(10, 70, 89, 20))
        self.radio_difficult.setStyleSheet(u"background-color:rgb(0, 85, 0);")
        self.btn_creat = QPushButton(self.centralwidget)
        self.btn_creat.setObjectName(u"btn_creat")
        self.btn_creat.setGeometry(QRect(114, 30, 71, 41))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.btn_creat.setFont(font)
        self.btn_creat.setStyleSheet(u"background-color:rgb(156, 78, 0);")
        self.text_box = QLineEdit(self.centralwidget)
        self.text_box.setObjectName(u"text_box")
        self.text_box.setGeometry(QRect(200, 40, 181, 21))
        self.text_box.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 412, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radio_easy.setText(QCoreApplication.translate("MainWindow", u"Easy", None))
        self.radio_hard.setText(QCoreApplication.translate("MainWindow", u"Hard", None))
        self.radio_difficult.setText(QCoreApplication.translate("MainWindow", u"Difficult", None))
        self.btn_creat.setText(QCoreApplication.translate("MainWindow", u"Creat", None))
        self.text_box.setText("")
    # retranslateUi

