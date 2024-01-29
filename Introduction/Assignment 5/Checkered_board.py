#Moein Moatali

"""   Checkered_board   """



n=int(input("Enter your number: "))
m=int(input("Enter your number: "))

for item in range(1,n+1):
    if item % 2 ==0:
        for i in range(1,m+1):
            if i % 2 ==0:
                print("#",end="")
            else:
                print("*",end="") 
        print()
    elif item % 2 !=0:
        for i in range(1,m+1):
            if i % 2 ==0:
                print("*",end="")
            else:
                print("#",end="")
        print()

