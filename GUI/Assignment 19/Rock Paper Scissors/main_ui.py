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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(299, 437)
        MainWindow.setStyleSheet(u"background-color:rgb(85, 170, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_computer = QLabel(self.centralwidget)
        self.label_computer.setObjectName(u"label_computer")
        self.label_computer.setGeometry(QRect(60, 10, 101, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_computer.setFont(font)
        self.label_computer.setStyleSheet(u"background-color:rgb(170, 0, 0);")
        self.computer_score = QLabel(self.centralwidget)
        self.computer_score.setObjectName(u"computer_score")
        self.computer_score.setGeometry(QRect(190, 120, 121, 20))
        self.computer_score.setStyleSheet(u"background-color:rgb(255, 255, 0);")
        self.player_score = QLabel(self.centralwidget)
        self.player_score.setObjectName(u"player_score")
        self.player_score.setGeometry(QRect(190, 150, 91, 20))
        self.player_score.setStyleSheet(u"background-color:rgb(255, 255, 0);")
        self.show_player = QLabel(self.centralwidget)
        self.show_player.setObjectName(u"show_player")
        self.show_player.setGeometry(QRect(60, 240, 101, 61))
        font1 = QFont()
        font1.setPointSize(15)
        self.show_player.setFont(font1)
        self.win = QLabel(self.centralwidget)
        self.win.setObjectName(u"win")
        self.win.setGeometry(QRect(20, 140, 161, 41))
        self.win.setFont(font1)
        self.show_computer = QLabel(self.centralwidget)
        self.show_computer.setObjectName(u"show_computer")
        self.show_computer.setGeometry(QRect(50, 50, 91, 61))
        self.show_computer.setFont(font1)
        self.label_player = QLabel(self.centralwidget)
        self.label_player.setObjectName(u"label_player")
        self.label_player.setGeometry(QRect(70, 190, 91, 31))
        self.label_player.setFont(font)
        self.btn_rock = QPushButton(self.centralwidget)
        self.btn_rock.setObjectName(u"btn_rock")
        self.btn_rock.setGeometry(QRect(20, 310, 71, 61))
        self.btn_rock.setFont(font1)
        self.btn_rock.setStyleSheet(u"background-color:rgb(170, 0, 127);")
        self.btn_paper = QPushButton(self.centralwidget)
        self.btn_paper.setObjectName(u"btn_paper")
        self.btn_paper.setGeometry(QRect(100, 310, 71, 61))
        self.btn_paper.setFont(font1)
        self.btn_paper.setStyleSheet(u"background-color:rgb(170, 0, 127);")
        self.btn_scissor = QPushButton(self.centralwidget)
        self.btn_scissor.setObjectName(u"btn_scissor")
        self.btn_scissor.setGeometry(QRect(180, 310, 71, 61))
        self.btn_scissor.setFont(font1)
        self.btn_scissor.setStyleSheet(u"background-color:rgb(170, 0, 127);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 299, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_computer.setText(QCoreApplication.translate("MainWindow", u"Computer", None))
        self.computer_score.setText(QCoreApplication.translate("MainWindow", u"computer_score:0", None))
        self.player_score.setText(QCoreApplication.translate("MainWindow", u"player_score:0", None))
        self.show_player.setText("")
        self.win.setText("")
        self.show_computer.setText("")
        self.label_player.setText(QCoreApplication.translate("MainWindow", u"Player", None))
        self.btn_rock.setText(QCoreApplication.translate("MainWindow", u"Rock", None))
        self.btn_paper.setText(QCoreApplication.translate("MainWindow", u"Paper", None))
        self.btn_scissor.setText(QCoreApplication.translate("MainWindow", u"scissor", None))
    # retranslateUi

