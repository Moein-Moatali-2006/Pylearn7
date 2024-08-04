# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(377, 450)
        widget.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(6)
        widget.setFont(font)
        widget.setStyleSheet(u"background-color:black;")
        self.main_label = QLabel(widget)
        self.main_label.setObjectName(u"main_label")
        self.main_label.setGeometry(QRect(20, 70, 341, 61))
        font1 = QFont()
        font1.setFamilies([u"Microsoft JhengHei UI"])
        font1.setPointSize(35)
        self.main_label.setFont(font1)
        self.main_label.setStyleSheet(u"color:white;")
        self.main_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.main_label_2 = QLabel(widget)
        self.main_label_2.setObjectName(u"main_label_2")
        self.main_label_2.setGeometry(QRect(20, 10, 351, 61))
        font2 = QFont()
        font2.setFamilies([u"Microsoft JhengHei UI"])
        font2.setPointSize(16)
        self.main_label_2.setFont(font2)
        self.main_label_2.setStyleSheet(u"color:white")
        self.main_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayoutWidget = QWidget(widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 140, 361, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_7 = QPushButton(self.gridLayoutWidget)
        self.button_7.setObjectName(u"button_7")
        font3 = QFont()
        font3.setPointSize(17)
        self.button_7.setFont(font3)
        self.button_7.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_7, 0, 0, 1, 1)

        self.button_multiply = QPushButton(self.gridLayoutWidget)
        self.button_multiply.setObjectName(u"button_multiply")
        self.button_multiply.setFont(font3)
        self.button_multiply.setStyleSheet(u"background-color:#EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_multiply, 2, 3, 1, 1)

        self.button_minus = QPushButton(self.gridLayoutWidget)
        self.button_minus.setObjectName(u"button_minus")
        self.button_minus.setFont(font3)
        self.button_minus.setStyleSheet(u"background-color:#EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_minus, 1, 3, 1, 1)

        self.button_4 = QPushButton(self.gridLayoutWidget)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setFont(font3)
        self.button_4.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_4, 1, 0, 1, 1)

        self.button_3 = QPushButton(self.gridLayoutWidget)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setFont(font3)
        self.button_3.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_3, 2, 2, 1, 1)

        self.button_sin = QPushButton(self.gridLayoutWidget)
        self.button_sin.setObjectName(u"button_sin")
        self.button_sin.setFont(font3)
        self.button_sin.setStyleSheet(u"background-color:rgb(255, 201, 8);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_sin, 0, 4, 1, 1)

        self.button_division = QPushButton(self.gridLayoutWidget)
        self.button_division.setObjectName(u"button_division")
        self.button_division.setFont(font3)
        self.button_division.setStyleSheet(u"background-color:#EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_division, 3, 3, 1, 1)

        self.button_sqrt = QPushButton(self.gridLayoutWidget)
        self.button_sqrt.setObjectName(u"button_sqrt")
        self.button_sqrt.setFont(font3)
        self.button_sqrt.setStyleSheet(u"background-color:rgb(255, 201, 8);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_sqrt, 4, 4, 1, 1)

        self.button_9 = QPushButton(self.gridLayoutWidget)
        self.button_9.setObjectName(u"button_9")
        self.button_9.setFont(font3)
        self.button_9.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_9, 0, 2, 1, 1)

        self.button_1 = QPushButton(self.gridLayoutWidget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setFont(font3)
        self.button_1.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_1, 2, 0, 1, 1)

        self.button_cot = QPushButton(self.gridLayoutWidget)
        self.button_cot.setObjectName(u"button_cot")
        self.button_cot.setFont(font3)
        self.button_cot.setStyleSheet(u"background-color:rgb(255, 201, 8);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_cot, 3, 4, 1, 1)

        self.button_cos = QPushButton(self.gridLayoutWidget)
        self.button_cos.setObjectName(u"button_cos")
        self.button_cos.setFont(font3)
        self.button_cos.setStyleSheet(u"background-color:rgb(255, 201, 8);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_cos, 1, 4, 1, 1)

        self.button_0 = QPushButton(self.gridLayoutWidget)
        self.button_0.setObjectName(u"button_0")
        self.button_0.setFont(font3)
        self.button_0.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_0, 3, 0, 1, 2)

        self.button_2 = QPushButton(self.gridLayoutWidget)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setFont(font3)
        self.button_2.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_2, 2, 1, 1, 1)

        self.button_plus = QPushButton(self.gridLayoutWidget)
        self.button_plus.setObjectName(u"button_plus")
        self.button_plus.setFont(font3)
        self.button_plus.setStyleSheet(u"background-color:#EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_plus, 0, 3, 1, 1)

        self.button_tan = QPushButton(self.gridLayoutWidget)
        self.button_tan.setObjectName(u"button_tan")
        self.button_tan.setFont(font3)
        self.button_tan.setStyleSheet(u"background-color:rgb(255, 201, 8);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_tan, 2, 4, 1, 1)

        self.button_5 = QPushButton(self.gridLayoutWidget)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setFont(font3)
        self.button_5.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_5, 1, 1, 1, 1)

        self.button_decimal = QPushButton(self.gridLayoutWidget)
        self.button_decimal.setObjectName(u"button_decimal")
        self.button_decimal.setFont(font3)
        self.button_decimal.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_decimal, 3, 2, 1, 1)

        self.button_8 = QPushButton(self.gridLayoutWidget)
        self.button_8.setObjectName(u"button_8")
        self.button_8.setFont(font3)
        self.button_8.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_8, 0, 1, 1, 1)

        self.button_6 = QPushButton(self.gridLayoutWidget)
        self.button_6.setObjectName(u"button_6")
        self.button_6.setFont(font3)
        self.button_6.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_6, 1, 2, 1, 1)

        self.button_c = QPushButton(self.gridLayoutWidget)
        self.button_c.setObjectName(u"button_c")
        self.button_c.setFont(font3)
        self.button_c.setStyleSheet(u"background-color:white;\n"
"color:black;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_c, 4, 0, 1, 1)

        self.button_equals = QPushButton(self.gridLayoutWidget)
        self.button_equals.setObjectName(u"button_equals")
        self.button_equals.setFont(font3)
        self.button_equals.setStyleSheet(u"background-color:white;\n"
"color:black;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_equals, 4, 1, 1, 2)

        self.button_log = QPushButton(self.gridLayoutWidget)
        self.button_log.setObjectName(u"button_log")
        self.button_log.setFont(font3)
        self.button_log.setStyleSheet(u"background-color:rgb(255, 201, 8);\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_log, 4, 3, 1, 1)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.main_label.setText(QCoreApplication.translate("widget", u"0", None))
        self.main_label_2.setText(QCoreApplication.translate("widget", u"0", None))
        self.button_7.setText(QCoreApplication.translate("widget", u"7", None))
        self.button_multiply.setText(QCoreApplication.translate("widget", u"*", None))
        self.button_minus.setText(QCoreApplication.translate("widget", u"-", None))
        self.button_4.setText(QCoreApplication.translate("widget", u"4", None))
        self.button_3.setText(QCoreApplication.translate("widget", u"3", None))
        self.button_sin.setText(QCoreApplication.translate("widget", u"sin", None))
        self.button_division.setText(QCoreApplication.translate("widget", u"/", None))
        self.button_sqrt.setText(QCoreApplication.translate("widget", u"sqrt", None))
        self.button_9.setText(QCoreApplication.translate("widget", u"9", None))
        self.button_1.setText(QCoreApplication.translate("widget", u"1", None))
        self.button_cot.setText(QCoreApplication.translate("widget", u"cot", None))
        self.button_cos.setText(QCoreApplication.translate("widget", u"cos", None))
        self.button_0.setText(QCoreApplication.translate("widget", u"0", None))
        self.button_2.setText(QCoreApplication.translate("widget", u"2", None))
        self.button_plus.setText(QCoreApplication.translate("widget", u"+", None))
        self.button_tan.setText(QCoreApplication.translate("widget", u"tan", None))
        self.button_5.setText(QCoreApplication.translate("widget", u"5", None))
        self.button_decimal.setText(QCoreApplication.translate("widget", u".", None))
        self.button_8.setText(QCoreApplication.translate("widget", u"8", None))
        self.button_6.setText(QCoreApplication.translate("widget", u"6", None))
        self.button_c.setText(QCoreApplication.translate("widget", u"C", None))
        self.button_equals.setText(QCoreApplication.translate("widget", u"=", None))
        self.button_log.setText(QCoreApplication.translate("widget", u"log", None))
    # retranslateUi

