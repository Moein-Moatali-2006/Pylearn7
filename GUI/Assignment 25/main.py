import sys
import datetime
import pytz
import sqlite3
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow
from PySide6.QtCore import QTimer


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #****
        # Timer for stopwatch
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stopwatch)
        
        # Variables to track time
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        
        # Connect buttons to their functions
        self.btn_stopwatch_start.clicked.connect(self.start_stopwatch)
        self.btn_stopwatch_stop.clicked.connect(self.stop_stopwatch)
        self.btn_stopwatch_reset.clicked.connect(self.reset_stopwatch)
        #****

        #*****
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_timer)

        # Variables for timer
        self.timer_seconds = 0
        self.timer_minutes = 0
        self.timer_hours = 0
        
        # Connect buttons
        self.btn_timer_start.clicked.connect(self.start_timer)
        self.btn_timer_stop.clicked.connect(self.stop_timer)
        self.btn_timer_reset.clicked.connect(self.reset_timer)
        #*****


        #*****
        # Timer for world clock
        self.worldclock_timer = QTimer()
        self.worldclock_timer.timeout.connect(self.update_worldclock)
        self.worldclock_timer.start(1000)  # Update every second
        #*****

        
        #*****
        # Connect to SQLite database
        self.conn = sqlite3.connect('Database.db')
        self.cursor = self.conn.cursor()

        # Load alarms from database
        self.load_alarms()

        # Timer for stopwatch
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stopwatch)
        
        # Variables to track time
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        
        # Connect buttons to their functions
        self.btn_stopwatch_start.clicked.connect(self.start_stopwatch)
        self.btn_stopwatch_stop.clicked.connect(self.stop_stopwatch)
        self.btn_stopwatch_reset.clicked.connect(self.reset_stopwatch)
        
        # Timer for countdown
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_timer)

        # Variables for timer
        self.timer_seconds = 0
        self.timer_minutes = 0
        self.timer_hours = 0
        
        # Connect buttons
        self.btn_timer_start.clicked.connect(self.start_timer)
        self.btn_timer_stop.clicked.connect(self.stop_timer)
        self.btn_timer_reset.clicked.connect(self.reset_timer)

        # Timer for world clock
        self.worldclock_timer = QTimer()
        self.worldclock_timer.timeout.connect(self.update_worldclock)
        self.worldclock_timer.start(1000)  # Update every second

        # Connect buttons for alarms
        self.btn_add_alarm.clicked.connect(self.add_alarm)
        #*****


    def start_stopwatch(self):
        self.timer.start(1000)  # Update every second
    
    def stop_stopwatch(self):
        self.timer.stop()

    def reset_stopwatch(self):
        self.timer.stop()
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.update_stopwatch_display()

    def update_stopwatch(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes >= 60:
            self.minutes = 0
            self.hours += 1
        self.update_stopwatch_display()

    def update_stopwatch_display(self):
        self.lbl_stopwatch_hour.setText(f"{self.hours:02d}")
        self.lbl_stopwatch_minute.setText(f"{self.minutes:02d}")
        self.lbl_stopwatch_second.setText(f"{self.seconds:02d}")

    #####
    def start_timer(self):
        try:
            self.timer_hours = int(self.Timer_hour.text())
            self.timer_minutes = int(self.Timer_minute.text())
            self.timer_seconds = int(self.Timer_second.text())
            self.countdown_timer.start(1000)  # Update every second
        except ValueError:
            pass  # Handle error for non-integer input

    def stop_timer(self):
        self.countdown_timer.stop()

    def reset_timer(self):
        self.countdown_timer.stop()
        self.Timer_hour.setText("00")
        self.Timer_minute.setText("00")
        self.Timer_second.setText("00")

    def update_timer(self):
        if self.timer_seconds == 0:
            if self.timer_minutes == 0:
                if self.timer_hours == 0:
                    self.countdown_timer.stop()
                else:
                    self.timer_hours -= 1
                    self.timer_minutes = 59
                    self.timer_seconds = 59
            else:
                self.timer_minutes -= 1
                self.timer_seconds = 59
        else:
            self.timer_seconds -= 1

        self.Timer_hour.setText(f"{self.timer_hours:02d}")
        self.Timer_minute.setText(f"{self.timer_minutes:02d}")
        self.Timer_second.setText(f"{self.timer_seconds:02d}")
    
    ###
    def update_worldclock(self):
        now_iran = datetime.datetime.now(pytz.timezone('Asia/Tehran'))
        now_usa = datetime.datetime.now(pytz.timezone('America/New_York'))
        now_germany = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        
        self.lbl_worldclock_iran.setText(now_iran.strftime("%H : %M : %S"))
        self.lbl_worldclock_usa.setText(now_usa.strftime("%H : %M : %S"))
        self.lbl_worldclock_germany.setText(now_germany.strftime("%H : %M : %S"))

    
    ###
    def load_alarms(self):
        # Clear the grid layout
        for i in reversed(range(self.show_alarms.count())):
            self.show_alarms.itemAt(i).widget().setParent(None)

        # Load alarms from database
        self.cursor.execute("SELECT name, hour, minute, second FROM clock")
        alarms = self.cursor.fetchall()

        for alarm in alarms:
            self.add_alarm_to_layout(alarm[0], alarm[1], alarm[2], alarm[3])

    def add_alarm_to_layout(self, name, hour, minute, second):
        # Create a widget for the alarm
        alarm_widget = QWidget()
        layout = QGridLayout()

        lbl_name = QLabel(f"Name: {name}")
        lbl_time = QLabel(f"Time: {hour:02}:{minute:02}:{second:02}")

        btn_edit = QPushButton("Edit")
        btn_delete = QPushButton("Delete")

        # Connect buttons
        btn_edit.clicked.connect(lambda: self.edit_alarm(name, hour, minute, second))
        btn_delete.clicked.connect(lambda: self.delete_alarm(name))

        layout.addWidget(lbl_name, 0, 0)
        layout.addWidget(lbl_time, 0, 1)
        layout.addWidget(btn_edit, 1, 0)
        layout.addWidget(btn_delete, 1, 1)

        alarm_widget.setLayout(layout)
        self.show_alarms.addWidget(alarm_widget)

    def add_alarm(self):
        name = self.lineEdit.text()
        hour = self.Timer_hour_3.text()
        minute = self.Timer_minute_3.text()
        second = self.Timer_second_3.text()

        # Insert into the database
        self.cursor.execute("INSERT INTO clock (name, hour, minute, second) VALUES (?, ?, ?, ?)",
                            (name, hour, minute, second))
        self.conn.commit()

        # Refresh the alarms layout
        self.load_alarms()

    def edit_alarm(self, name, hour, minute, second):
        # Code for editing an alarm
        # You can implement a dialog to edit the alarm details
        print(f"Edit alarm: {name}")

    def delete_alarm(self, name):
        # Delete from the database
        self.cursor.execute("DELETE FROM alarms WHERE name = ?", (name,))
        self.conn.commit()

        # Refresh the alarms layout
        self.load_alarms()

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
