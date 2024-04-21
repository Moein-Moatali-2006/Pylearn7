import sys
from PySide6 import QtWidgets, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Remove Line Breaks')

        self.inputLineEdit = QtWidgets.QLineEdit(self)
        self.removeButton = QtWidgets.QPushButton('Remove Line Breaks', self)
        self.outputTextEdit = QtWidgets.QTextEdit(self)

        self.removeButton.clicked.connect(self.removeLineBreaks)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.inputLineEdit)
        layout.addWidget(self.removeButton)
        layout.addWidget(self.outputTextEdit)

        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        self.show()

    def removeLineBreaks(self):
        text = self.inputLineEdit.text()
        text_without_line_breaks = text.replace('\n', '')
        self.outputTextEdit.setText(text_without_line_breaks)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
