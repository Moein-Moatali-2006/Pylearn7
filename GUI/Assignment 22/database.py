import sqlite3


class Database:
    def __init__(self):
        super().__init__()
        self.con=sqlite3.connect("todo_list.db")
        self.cursor=self.con.cursor()

    def get_tasks(self):
        query="SELECT * FROM tasks"
        result=self.cursor.execute(query)
        tasks=result.fetchall()
        return tasks
    

    def add_new_tasks(self,new_title,new_description):
        try:
            query=f"INSERT INTO tasks(titel,description) VALUES('{new_title}','{new_description}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
        
    
    def remove_task(self):
        ...

    
    def task_done(self):
        query="Update ... SET ..."