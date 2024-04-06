import sys
import math
from sympy import coth
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def use_math(math_op):
    if math_op == "sin":
        number = eval(main_window.textbox.text())
        main_window.textbox.setText(str(math.sin(number)))
    elif math_op == "cos":
        number = eval(main_window.textbox.text())
        main_window.textbox.setText(str(math.cos(number)))
    elif math_op == "tan":
        number = eval(main_window.textbox.text())
        main_window.textbox.setText(str(math.tan(number)))
    elif math_op == "cot":
        number = eval(main_window.textbox.text())
        main_window.textbox.setText(str(coth(number)))
    elif math_op == "log":
        number = eval(main_window.textbox.text())
        main_window.textbox.setText(str(math.log(number)))
    elif math_op == "fac":
        number = eval(main_window.textbox.text())
        main_window.textbox.setText(str(math.factorial(number)))

def equal():
    try:
        second_number=float(main_window.textbox.text())
    except ValueError:
        main_window.textbox.setText("Error")
    
    result=0
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            main_window.textbox.setText("Zero Error")

    main_window.textbox.setText(str(result))

def operators(op):
    global first_number
    try:
        first_number = float(main_window.textbox.text())
    except ValueError:
        main_window.textbox.setText("Error")
        return
    
    main_window.textbox.setText("")
    global operator
    operator = op

def clear():
    main_window.textbox.setText("")

def number(add):
    old_number=main_window.textbox.text()
    new_number=old_number+add
    main_window.textbox.setText(new_number)


loader=QUiLoader()
app=QApplication(sys.argv)
main_window=loader.load("main.ui")


main_window.show()

#numbers
main_window.btn_1.clicked.connect(partial(number ,"1"))
main_window.btn_2.clicked.connect(partial(number ,"2"))
main_window.btn_3.clicked.connect(partial(number ,"3"))
main_window.btn_4.clicked.connect(partial(number ,"4"))
main_window.btn_5.clicked.connect(partial(number ,"5"))
main_window.btn_6.clicked.connect(partial(number ,"6"))
main_window.btn_7.clicked.connect(partial(number ,"7"))
main_window.btn_8.clicked.connect(partial(number ,"8"))
main_window.btn_9.clicked.connect(partial(number ,"9"))
main_window.btn_0.clicked.connect(partial(number ,"0"))
main_window.btn_dot.clicked.connect(partial(number ,"."))
#operators
main_window.btn_sum.clicked.connect(partial(operators , "+"))
main_window.btn_sub.clicked.connect(partial(operators , "-"))
main_window.btn_malt.clicked.connect(partial(operators , "*"))
main_window.btn_div.clicked.connect(partial(operators , "/"))
#equal
main_window.btn_equal.clicked.connect(partial(equal))
#clear
main_window.btn_clear.clicked.connect(partial(clear))
#math
main_window.btn_sin.clicked.connect(partial(use_math , "sin"))
main_window.btn_cos.clicked.connect(partial(use_math , "cos"))
main_window.btn_tan.clicked.connect(partial(use_math , "tan"))
main_window.btn_cot.clicked.connect(partial(use_math , "cot"))
main_window.btn_log.clicked.connect(partial(use_math , "log"))
main_window.btn_fac.clicked.connect(partial(use_math , "fac"))



app.exec()


