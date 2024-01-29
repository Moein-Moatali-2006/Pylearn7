#Moein Moatali

"""   Calculator   """


#import library
import math 
import sympy

#Operators
operators="""
+:The sum of two numbers
-:Subtraction of two numbers
*:Multiplication of two numbers
/:Divide two numbers
sqrt:Calculat the sqrt of a number
sin:Calculate the sin of a number
cos:Calculate the cos of a number
tan:Calculate the tan of a number
cot:Calculate the cot of a number
factorial:Calculate the factorial of a number
"""

#print welcom
print("Wlocom to my calculator","\n",operators)


#get operator
operator=input("Please enter your operator:")

#cheek operator 
if operator in ["+" , "-" , "*" , "/"]:
    number_1=eval(input("Please enter your number 1: "))
    number_2=eval(input("please enter your number 2:"))
elif operator in ["sin" , "cos" , "tan" , "cot" , "sqrt" , "factoryal"]:
    number_1=eval(input("Please enter your number: "))
else:
    print(f"I'm sorry! {operator} is not supported")


#cheek operator and print result
if operator == "+" :
    print(f"result= ",number_1 + number_2)
elif operator == "-":
    print(f"result= ",number_1 - number_2)
elif operator == "*": 
    print(f"result= ",number_1 * number_2)
elif operator == "/":
    print(f"result= ",number_1 / number_2)
else:
    if operator == "sin":
        print(f"result= ",math.sin(number_1))
    elif operator == "cos":
        print(f"result= ",math.cos(number_1))
    elif operator == "tan":
        print(f"result= ",math.tan(number_1))
    elif operator == "cot":
        print(f"result= ",math.cot(number_1))
    elif operator == "sqrt":
        print(f"result= ",math.sqrt(number_1))
    elif operator == "factorial":
        print(f"result= ",math.factorial(number_1))