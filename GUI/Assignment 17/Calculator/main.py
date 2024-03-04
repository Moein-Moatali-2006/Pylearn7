from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
# ----------------------------------------------------------------
numbers=[]

def number_0():
    global new_number
    numbers.append(0)
    new_number=""
    for item in numbers:
        new_number += str(item)
    my_window.textbox.setText(str(new_number))

def number_1():
    global new_number
    numbers.append(1)
    new_number=""
    for item in numbers:
        new_number += str(item)
    my_window.textbox.setText(str(new_number))

def number_2():
    global new_number
    numbers.append(2)
    new_number=""
    for item in numbers:
        new_number += str(item)
    my_window.textbox.setText(str(new_number))

def number_3():
    global new_number
    numbers.append(3)
    new_number=""
    for item in numbers:
        new_number += str(item)
    my_window.textbox.setText(str(new_number))

def number_4():
    global new_number
    numbers.append(4)
    new_number=""
    for item in numbers:
        new_number += str(item)
    my_window.textbox.setText(str(new_number))

def number_5():
    global new_number
    numbers.append(5)
    new_number=""
    for item in numbers:
        new_number += str(item)
    my_window.textbox.setText(str(new_number))

def number_6():
    global new_number
    numbers.append(6)
    new_number=""
    for item in numbers:
        new_number += str(item)
    my_window.textbox.setText(str(new_number))

def number_7():
    global new_number
    numbers.append(7)
    new_number=""
    for item in numbers:
        new_number += str(item)
    my_window.textbox.setText(str(new_number))

def number_8():
    global new_number
    numbers.append(8)
    new_number=""
    for item in numbers:
        new_number += str(item)
    my_window.textbox.setText(str(new_number))

def number_9():
    global new_number
    numbers.append(9)
    new_number=""
    for item in numbers:
        new_number += str(item)
    my_window.textbox.setText(str(new_number))

def dot():
    global new_number
    numbers.append(".")
    new_number=""
    for item in numbers:
        new_number += str(item)
    my_window.textbox.setText(str(new_number))


#********************************

def clear():
    numbers.clear()
    my_window.textbox.setText(str(0))




def plus():
    global number1,new_number,result
    number1=eval(new_number)
    my_window.textbox.setText(str(0))
    new_number=""
    numbers.clear()

    
    

def subtraction():
    global number1,new_number
    number1=eval(new_number)
    my_window.textbox.setText(str(0))
    new_number=""
    numbers.clear()

    
    

def division():
    global number1,new_number
    number1=eval(new_number)
    my_window.textbox.setText(str(0))
    new_number=""
    numbers.clear()
    
    
    

def multiplication():
    global number1,new_number
    number1=eval(new_number)
    my_window.textbox.setText(str(0))
    new_number=""
    numbers.clear()
    
    



def equal():
    #000000000000000000000000000000000000000000000000000
    number2=eval(new_number)
    
    my_window.textbox.setText(str(number1 + number2))

    my_window.textbox.setText(str(number1 / number2))

    my_window.textbox.setText(str(number1 * number2))

    my_window.textbox.setText(str(number1 - number2))
    
    pass
    #000000000000000000000000000000000000000000000000000



# ----------------------------------------------------------------
my_loader=QUiLoader()
my_app=QApplication([])
my_window=my_loader.load("ui_calculator.ui")
my_window.show()
# ----------------------------------------------------------------
my_window.btn_number_0.clicked.connect(number_0)
my_window.btn_number_1.clicked.connect(number_1)
my_window.btn_number_2.clicked.connect(number_2)
my_window.btn_number_3.clicked.connect(number_3)
my_window.btn_number_4.clicked.connect(number_4)
my_window.btn_number_5.clicked.connect(number_5)
my_window.btn_number_6.clicked.connect(number_6)
my_window.btn_number_7.clicked.connect(number_7)
my_window.btn_number_8.clicked.connect(number_8)
my_window.btn_number_9.clicked.connect(number_9)
my_window.btn_dot.clicked.connect(dot)
#*****************************************************************
my_window.btn_clear.clicked.connect(clear)
my_window.btn_plus.clicked.connect(plus)
my_window.btn_subtraction.clicked.connect(subtraction)
my_window.btn_division.clicked.connect(division)
my_window.btn_multiplication.clicked.connect(multiplication)
my_window.btn_equal.clicked.connect(equal)

# ----------------------------------------------------------------
my_app.exec()