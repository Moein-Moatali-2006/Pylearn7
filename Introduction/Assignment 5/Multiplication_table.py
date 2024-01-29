#Moein Moatali
"""     Multiplication_table   """

n=int(input("Enter your number: "))
m=int(input("Enter your number: "))

list1=[]
list2=[]


for item in range(1,n+1):
    list1.append(item)

for item in range(1,m+1):
    list2.append(item)

numbers=[]
for item in list2:
    for i in list1:
        numbers.append(int(item) * int(i))
        print(numbers[-1],"|",end="")
    print()

