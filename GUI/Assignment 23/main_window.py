# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(506, 557)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 40, 481, 461))
        self.grid_Layout = QGridLayout(self.gridLayoutWidget)
        self.grid_Layout.setObjectName(u"grid_Layout")
        self.grid_Layout.setContentsMargins(0, 0, 0, 0)
        self.btn_new_game = QPushButton(self.centralwidget)
        self.btn_new_game.setObjectName(u"btn_new_game")
        self.btn_new_game.setGeometry(QRect(10, 10, 75, 24))
        self.btn_open_file = QPushButton(self.centralwidget)
        self.btn_open_file.setObjectName(u"btn_open_file")
        self.btn_open_file.setGeometry(QRect(100, 10, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 506, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SudoKu Game", None))
        self.btn_new_game.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.btn_open_file.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
    # retranslateUi

