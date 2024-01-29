#Moein Moatali
#گرفتن یک عد  برای چاپ کارکتر ها از کاربر
number=int(input("Enter your number: "))
for item in range(1,number+1):
    if item % 2 == 0:
        print("#",end="")
    else:
        print("*",end="")