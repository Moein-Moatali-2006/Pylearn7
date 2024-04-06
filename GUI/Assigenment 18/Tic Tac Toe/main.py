import sys
from functools import partial
from PySide6.QtWidgets import QApplication,QMessageBox
from PySide6.QtUiTools import QUiLoader

player_1_score = 0
player_2_score = 0

def check_x():
        global player_1_score
        msg_box=QMessageBox(text="player X wine! 🤩 😍 ❤️ 🌹 ")
        msg_box.show()
        player_1_score += 1
        msg_box.exec()

def check_O():
        global player_1_score
        msg_box=QMessageBox(text="player O wine! 🤩 😍 ❤️ 🌹 ")
        msg_box.show()
        player_2_score += 1
        msg_box.exec()

def check():
    global player_1_score
    global player_2_score
    if buttons[0][0].text()=="X" and buttons[0][1].text()=="X" and buttons[0][2].text()=="X":
        check_x()
        return
    elif buttons[1][0].text()=="X" and buttons[1][1].text()=="X" and buttons[1][2].text()=="X":
        check_x()
        return
    elif buttons[2][0].text()=="X" and buttons[2][1].text()=="X" and buttons[2][2].text()=="X":
        check_x()
        return
    elif buttons[0][0].text()=="X" and buttons[1][0].text()=="X" and buttons[2][0].text()=="X":
        check_x()
        return
    elif buttons[0][1].text()=="X" and buttons[1][1].text()=="X" and buttons[2][1].text()=="X":
        check_x()
        return
    elif buttons[0][2].text()=="X" and buttons[1][2].text()=="X" and buttons[2][2].text()=="X":
        check_x()
        return
    elif buttons[0][0].text()=="X" and buttons[1][1].text()=="X" and buttons[2][2].text()=="X":
        check_x()
        return
    elif buttons[0][2].text()=="X" and buttons[1][1].text()=="X" and buttons[2][0].text()=="X":
        check_x()
        return
    #
    if buttons[0][0].text()=="O" and buttons[0][1].text()=="O" and buttons[0][2].text()=="O":
        check_O()
        return
    elif buttons[1][0].text()=="O" and buttons[1][1].text()=="O" and buttons[1][2].text()=="O":
        check_O()
        return
    elif buttons[2][0].text()=="O" and buttons[2][1].text()=="O" and buttons[2][2].text()=="O":
        check_O()
        return
    elif buttons[0][0].text()=="O" and buttons[1][0].text()=="O" and buttons[2][0].text()=="O":
        check_O()
        return
    elif buttons[0][1].text()=="O" and buttons[1][1].text()=="O" and buttons[2][1].text()=="O":
        check_O()
        return
    elif buttons[0][2].text()=="O" and buttons[1][2].text()=="O" and buttons[2][2].text()=="O":
        check_O()
        return
    elif buttons[0][0].text()=="O" and buttons[1][1].text()=="O" and buttons[2][2].text()=="O":
        check_O()
        return
    elif buttons[0][2].text()=="O" and buttons[1][1].text()=="O" and buttons[2][0].text()=="O":
        check_O()
        return

    count=0
    for i in range(3):
        for j in range(3):
            if buttons[i][j].text() != "":
                count+=1

    if count == 9:
        msg_box=QMessageBox(text=" You are Equal 🌹 ")
        msg_box.show()
        msg_box.exec()

def about():
    msg_box =QMessageBox(text="This is the TIC TAC TOE game ❤️")
    msg_box.show()
    msg_box.exec()

def paly(row,col):
    global player
    global buttons
    if player == 1:
        buttons[row][col].setText("X")
        buttons[row][col].setStyleSheet("background-color:pink;color:red;")
        player=2
    elif player == 2:
        buttons[row][col].setText("O")
        buttons[row][col].setStyleSheet("background-color:lightblue;color:blue;")
        player=1

    check()
    #glo ... 
    main_window.lineEdit_X.setText(str(player_1_score))
    main_window.lineEdit_O.setText(str(player_2_score))
  
def new_game():
    for i in range(3):
        for x in range(3):
            buttons[i][x].setText("")
            buttons[i][x].setStyleSheet("background-color:white;")

loader=QUiLoader()
app=QApplication(sys.argv)
main_window=loader.load("main.ui")

main_window.show()
player=1

buttons=[[main_window.btn_1,main_window.btn_2,main_window.btn_3],
         [main_window.btn_4,main_window.btn_5,main_window.btn_6],
         [main_window.btn_7,main_window.btn_8,main_window.btn_9]]

for i in range(3):
    for x in range(3):
        buttons[i][x].clicked.connect(partial(paly,i,x))

main_window.btn_about.clicked.connect(partial(about))
main_window.btn_new_game.clicked.connect(partial(new_game))

app.exec()