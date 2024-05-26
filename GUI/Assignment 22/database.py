import sqlite3
from PySide6.QtWidgets import *

class Database():
    def __init__(self):
        super().__init__()
        self.con=sqlite3.connect("ToDo_list.db")
        self.cursor=self.con.cursor()

    
    def add_to_database(self,title,priority,date,time,description):
        desc=description.text()
        ti=title.text()
        check=priority.isChecked()
        if check:
            x=1
        else:
            x=0
        da=date
        tim=time
        self.cursor.execute(f"INSERT INTO tasks(title,priority,date,time,done,description) VALUES('{ti}',{x},'{da}','{tim}',0,'{desc}')")
        self.con.commit()
        msg=QMessageBox()
        msg.setText("your task loaded ✅")
        msg.exec_()

    def remove_from_database(self,id):
        query=f"DELETE FROM tasks WHERE id={id};"
        self.cursor.execute(query)
        self.con.commit()
        msg=QMessageBox()
        msg.setText("your task deleted in database ✅")
        msg.exec_()

    def update_database(self,id):
        query=f"UPDATE tasks SET done = 1 WHERE id={id};"
        self.cursor.execute(query)
        self.con.commit()
        msg=QMessageBox()
        msg.setText("your task done ✅")
        msg.exec_()

    def get_tasks_important(self):
        query="SELECT * FROM tasks WHERE done=0 AND priority=1;"
        result=self.cursor.execute(query)
        tasks=result.fetchall()
        return tasks
    
    def get_tasks(self):
        query="SELECT * FROM tasks WHERE done=0 AND priority=0;"
        result=self.cursor.execute(query)
        tasks=result.fetchall()
        return tasks
    
    def get_tasks_done(self):
        query="SELECT * FROm tasks WHERE done=1;"
        result=self.cursor.execute(query)
        tasks=result.fetchall()
        return tasks
    
    def info(self,id):
        query=f"SELECT * FROM tasks WHERE id={id};"
        result=self.cursor.execute(query)
        task=result.fetchall()
        msg=QMessageBox()
        msg.setText(f"{task[0][-1]} \n {task[0][3]}")
        msg.exec_()
