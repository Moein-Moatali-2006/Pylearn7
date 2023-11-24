#Moein Moatali
User_list=input("enter your list: ---> 14#25#22 = [14,25,22] :  ")
list_1=User_list.split("#")
print(f"old_list: {list_1}")

list_2=set(list_1)
list_3=list(list_2)


print(f"new_list: {list_3}")

#1#2#3#4#4#4#2#2#9#12#21#4