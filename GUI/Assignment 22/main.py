import sys
from functools import partial
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow
from database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.db=Database()
        self.ui.btn_creat.clicked.connect(partial(self.db.add_to_database,self.ui.txt_title,self.ui.check_priority,self.ui.date.text(),self.ui.time.text(),self.ui.txt_description))
        self.check()

    def show_list_tasks_important(self):
        tasks=self.db.get_tasks_important()
        for item in range(len(tasks)):
            btn_info=QPushButton()
            btn_info.setText("info")
            btn_info.clicked.connect(partial(self.db.info,tasks[item][0]))
            btn_delete=QPushButton()
            btn_delete.setText("❌")
            btn_delete.clicked.connect(partial(self.db.remove_from_database,tasks[item][0]))
            btn_tike=QPushButton()
            btn_tike.setText("✅")
            btn_tike.clicked.connect(partial(self.db.update_database,tasks[item][0]))
            lbl=QLabel()
            lbl.setText(tasks[item][1])
            lbl_important=QLabel()
            lbl_important.setText("⚠️ Important ⚠️")

            self.ui.show_tasks_important.addWidget(btn_info,item,0)
            self.ui.show_tasks_important.addWidget(btn_delete,item,1)
            self.ui.show_tasks_important.addWidget(btn_tike,item,2)
            self.ui.show_tasks_important.addWidget(lbl,item,3)
            self.ui.show_tasks_important.addWidget(lbl_important,item,4)
                
    def show_list_tasks(self):
        tasks=self.db.get_tasks()
        for item in range(len(tasks)):
            btn_info=QPushButton()
            btn_info.setText("info")
            btn_info.clicked.connect(partial(self.db.info,tasks[item][0]))
            btn_delete=QPushButton()
            btn_delete.setText("❌")
            btn_delete.clicked.connect(partial(self.db.remove_from_database,tasks[item][0]))
            btn_tike=QPushButton()
            btn_tike.setText("✅")
            btn_tike.clicked.connect(partial(self.db.update_database,tasks[item][0]))
            lbl=QLabel()
            lbl.setText(tasks[item][1])

            self.ui.show_tasks.addWidget(btn_info,item,0)
            self.ui.show_tasks.addWidget(btn_delete,item,1)
            self.ui.show_tasks.addWidget(btn_tike,item,2)
            self.ui.show_tasks.addWidget(lbl,item,3)
             
    def show_list_done(self):
        tasks=self.db.get_tasks_done()
        for item in range(len(tasks)):
            btn_delete=QPushButton()
            btn_delete.setText("❌")
            btn_delete.clicked.connect(partial(self.db.remove_from_database,tasks[item][0]))
            lbl=QLabel()
            lbl.setText(tasks[item][1])

            self.ui.show_done.addWidget(btn_delete,item,0)
            self.ui.show_done.addWidget(lbl,item,1)
 
    def check(self):
        self.show_list_tasks()
        self.show_list_done()
        self.show_list_tasks_important()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    main_window=MainWindow()
    main_window.show()
    app.exec()



