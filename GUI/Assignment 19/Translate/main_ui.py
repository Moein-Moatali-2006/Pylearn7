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
        MainWindow.resize(440, 248)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.radio_PE = QRadioButton(self.centralwidget)
        self.radio_PE.setObjectName(u"radio_PE")
        self.radio_PE.setGeometry(QRect(10, 10, 116, 20))
        self.radio_EP = QRadioButton(self.centralwidget)
        self.radio_EP.setObjectName(u"radio_EP")
        self.radio_EP.setGeometry(QRect(10, 30, 116, 20))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 50, 211, 111))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(240, 50, 181, 111))
        self.btn_sound = QPushButton(self.centralwidget)
        self.btn_sound.setObjectName(u"btn_sound")
        self.btn_sound.setGeometry(QRect(270, 170, 75, 24))
        self.btn_translate = QPushButton(self.centralwidget)
        self.btn_translate.setObjectName(u"btn_translate")
        self.btn_translate.setGeometry(QRect(120, 170, 141, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 440, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radio_PE.setText(QCoreApplication.translate("MainWindow", u"Persian to English", None))
        self.radio_EP.setText(QCoreApplication.translate("MainWindow", u"English to Persian", None))
        self.btn_sound.setText(QCoreApplication.translate("MainWindow", u"make sound", None))
        self.btn_translate.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
    # retranslateUi

