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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTimeEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(405, 543)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_add_task = QLabel(self.centralwidget)
        self.lbl_add_task.setObjectName(u"lbl_add_task")
        self.lbl_add_task.setGeometry(QRect(10, 310, 75, 16))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 327, 371, 164))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_priority = QLabel(self.gridLayoutWidget)
        self.lbl_priority.setObjectName(u"lbl_priority")

        self.gridLayout.addWidget(self.lbl_priority, 2, 0, 1, 1)

        self.btn_creat = QPushButton(self.gridLayoutWidget)
        self.btn_creat.setObjectName(u"btn_creat")

        self.gridLayout.addWidget(self.btn_creat, 5, 3, 1, 1)

        self.lbl_title = QLabel(self.gridLayoutWidget)
        self.lbl_title.setObjectName(u"lbl_title")

        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 1)

        self.date = QDateEdit(self.gridLayoutWidget)
        self.date.setObjectName(u"date")
        self.date.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))

        self.gridLayout.addWidget(self.date, 3, 3, 1, 1)

        self.lbl_time = QLabel(self.gridLayoutWidget)
        self.lbl_time.setObjectName(u"lbl_time")

        self.gridLayout.addWidget(self.lbl_time, 4, 0, 1, 1)

        self.txt_title = QLineEdit(self.gridLayoutWidget)
        self.txt_title.setObjectName(u"txt_title")

        self.gridLayout.addWidget(self.txt_title, 0, 3, 1, 1)

        self.lbl_date = QLabel(self.gridLayoutWidget)
        self.lbl_date.setObjectName(u"lbl_date")

        self.gridLayout.addWidget(self.lbl_date, 3, 0, 1, 1)

        self.time = QTimeEdit(self.gridLayoutWidget)
        self.time.setObjectName(u"time")

        self.gridLayout.addWidget(self.time, 4, 3, 1, 1)

        self.check_priority = QCheckBox(self.gridLayoutWidget)
        self.check_priority.setObjectName(u"check_priority")

        self.gridLayout.addWidget(self.check_priority, 2, 3, 1, 1)

        self.lbl_description = QLabel(self.gridLayoutWidget)
        self.lbl_description.setObjectName(u"lbl_description")

        self.gridLayout.addWidget(self.lbl_description, 1, 0, 1, 1)

        self.txt_description = QLineEdit(self.gridLayoutWidget)
        self.txt_description.setObjectName(u"txt_description")

        self.gridLayout.addWidget(self.txt_description, 1, 3, 1, 1)

        self.lbl_done = QLabel(self.centralwidget)
        self.lbl_done.setObjectName(u"lbl_done")
        self.lbl_done.setGeometry(QRect(10, 190, 62, 16))
        self.lbl_my_tasks = QLabel(self.centralwidget)
        self.lbl_my_tasks.setObjectName(u"lbl_my_tasks")
        self.lbl_my_tasks.setGeometry(QRect(10, 0, 71, 16))
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 110, 381, 81))
        self.show_tasks = QGridLayout(self.gridLayoutWidget_2)
        self.show_tasks.setObjectName(u"show_tasks")
        self.show_tasks.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 210, 381, 101))
        self.show_done = QGridLayout(self.gridLayoutWidget_3)
        self.show_done.setObjectName(u"show_done")
        self.show_done.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_4 = QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 20, 381, 81))
        self.show_tasks_important = QGridLayout(self.gridLayoutWidget_4)
        self.show_tasks_important.setObjectName(u"show_tasks_important")
        self.show_tasks_important.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 405, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_add_task.setText(QCoreApplication.translate("MainWindow", u"add new task :", None))
        self.lbl_priority.setText(QCoreApplication.translate("MainWindow", u"priority :", None))
        self.btn_creat.setText(QCoreApplication.translate("MainWindow", u"create", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"title :", None))
        self.lbl_time.setText(QCoreApplication.translate("MainWindow", u"Time :", None))
        self.lbl_date.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.check_priority.setText(QCoreApplication.translate("MainWindow", u"True", None))
        self.lbl_description.setText(QCoreApplication.translate("MainWindow", u"description :", None))
        self.lbl_done.setText(QCoreApplication.translate("MainWindow", u"tasks done :", None))
        self.lbl_my_tasks.setText(QCoreApplication.translate("MainWindow", u"your tasks :", None))
    # retranslateUi

