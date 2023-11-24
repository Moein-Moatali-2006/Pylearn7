#Moein Moatali
#گرفتن اعداد
number_1= int(input("Enter your number : "))
number_2 = int(input("Enter your number : "))

if number_1 > number_2:
  number_1, number_2 = number_2, number_1

for i in range(1,number_1+1):
  if number_1 % i == 0 and number_2 % i == 0:
    GCD = i

print(f"GCD of {number_1} and {number_2} is : {GCD} " )