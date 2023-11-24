#Moein Moatali
#اضافه کردن کتابخانه رندوم به برنامه
import random
#گرفتن یک عدد برای اندازه لیست اعداد
number=int(input("please enter your number for make list number: "))

#بقیه شو بهت نمیگم 🤪
list_number=[]
for item in range(1,number+1):
    add=random.randint(1,100_000)
    if add not in list_number:
        list_number.append(add)
    else:
        add=random.randint(200_000,300_000)
        list_number.append(add)

print(list_number)