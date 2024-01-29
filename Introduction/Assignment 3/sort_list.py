#Moein Moatali
#گرفتن لیست کاربر
my_list=[]
count=int(input("How many number is in your list? "))
for item in range(count):
    number=int(input("Enter your number for append list: "))
    my_list.append(number)


list_2 = my_list.copy()
list_2.sort()

#برسی به ترتیب بودن اعداد لیست
if list_2 == my_list :
    print(f"Your list is :{True}")
else:
    print(f"Your list is :{False}")


