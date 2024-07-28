import sys
import random
from functools import partial
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow
from sudoku import Sudoku


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_new_game.clicked.connect(partial(self.new_game))
        self.ui.btn_open_file.clicked.connect(partial(self.open_file))

        puzzle = Sudoku(3).difficulty(0.5)
        # print(puzzle.board)

        self.line_edits=[[None for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                if puzzle.board[i][j] != None:
                    new_cell.setText(str(puzzle.board[i][j]))
                    new_cell.setReadOnly(True)
                self.ui.grid_Layout.addWidget(new_cell,i,j)
                new_cell.textChanged.connect(partial(self.validation,i,j))
                self.line_edits[i][j]=new_cell

        self.new_game()


    def open_file(self):
        try:
            file_path = QFileDialog.getOpenFileName(self,"Open file.")[0]

            f=open(file_path,"r")
            big_text=f.read()
            rows=big_text.split("\n")
            puzzle_board=[[None for i in range(9)] for j in range(9)]
            for i in range(len(rows)):
                cells=rows[i].split(" ")
                for j in range(len(cells)):
                    puzzle_board[i][j]=int(cells[j])

            
            for i in range(9):
                for j in range(9):
                    self.line_edits[i][j].setReadOnly(False)
                    if puzzle_board[i][j] != 0:
                        self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                        self.line_edits[i][j].setReadOnly(True)
                    else:
                        self.line_edits[i][j].setText("")
        except:
            print("* * * * * * * * * *  File Error  * * * * * * * * * * ")

    def new_game(self):
        puzzle = Sudoku(3,seed=random.randint(1,1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setReadOnly(False)
                if puzzle.board[i][j] != None:
                    self.line_edits[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")

    def check(self):
        for i in range(0 , 9):      
            x = 0         
            num1 = self.line_edits[i][x].text()                 
            if self.line_edits[i][x].text() != None or self.line_edits[i][x].text() != "" or self.line_edits[i][x].text() != 'None' :
                for j in range(1,9) :
                    other_numbers_in_row = self.line_edits[i][j].text()
                    if other_numbers_in_row != None :
                        if num1 == other_numbers_in_row and num1 != None and num1 != "":
                            self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
                            self.line_edits[i][x].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")                            
                            return False
                        elif flag == 0  :
                            self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
                        elif flag == 1 :
                            self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
            
            x = 1
            for x in range(1,9) : 
                num1 = self.line_edits[i][x].text()                 
                if self.line_edits[i][x].text() != None or self.line_edits[i][x].text() != "" or self.line_edits[i][x].text() != 'None' :
                    for j in range(1,9) :
                        if x != j :
                            other_numbers_in_row = self.line_edits[i][j].text()
                            if other_numbers_in_row != None :
                                if num1 == other_numbers_in_row and num1 != None and num1 != "" and x < j :
                                    self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
                                    self.line_edits[i][x].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")                                   
                                    if x > j :
                                        self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")    
                                        self.line_edits[i][x].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")                                   
                                    return False
                                elif flag == 0 :
                                    self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")           
                                elif flag == 1 :
                                    self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
                                                     
        for j in range(0 , 9):      
            x = 0         
            num1 = self.line_edits[x][j].text()                 
            if self.line_edits[x][j].text() != None or self.line_edits[x][j].text() != "" or self.line_edits[x][j].text() != 'None' :
                for i in range(1,9) :
                    other_numbers_in_row = self.line_edits[i][j].text()
                    if other_numbers_in_row != None :
                        if num1 == other_numbers_in_row and num1 != None and num1 != "":
                            self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
                            self.line_edits[x][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")                        
                            return False
                        elif flag == 0  :
                                    self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")           
                        elif flag == 1 :
                                    self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
            
            x = 1
            for x in range(1,9) : 
                num1 = self.line_edits[x][j].text()                 
                if self.line_edits[x][j].text() != None or self.line_edits[x][j].text() != "" or self.line_edits[x][j].text() != 'None' :
                    for i in range(1,9) :
                        if x != i :
                            other_numbers_in_row = self.line_edits[i][j].text()
                            if other_numbers_in_row != None :
                                if num1 == other_numbers_in_row and num1 != None and num1 != "" and x < i :
                                    self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95));\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
                                    self.line_edits[x][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")                                   
                                    if x > j :
                                        self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")    
                                        self.line_edits[x][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")                                        
                                    return False
                                elif flag == 0  :
                                    self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")           
                                elif flag == 1 :
                                    self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")

        array=  []
        num1 = self.line_edits[i][j]
        x = 0 
        y = 3
        for i in range (x , y):  
            for j in range (x , y ) :     
                for i in range(3):
                    for j in range(3):
                        if num1 not in array :
                            array.append( self.line_edits[i][j].text() )
                        else :
                            self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")    
                x+= 3
                y+= 3
            x+=3
            y+=3
        

    def validation(self,i,j,text):
        if text not in ["1","2","3","4","5","6","7","8","9"]:
            self.line_edits[i][j].setText("")
        
        self.check()

 

if __name__ == "__main__":
    app=QApplication(sys.argv)

    window=MainWindow()
    window.show()

    app.exec()