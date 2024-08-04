import sys
from PySide6.QtWidgets import QApplication
from widget_1 import Widget


app=QApplication(sys.argv)


window = Widget()
window.show()


app.exec()