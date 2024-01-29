# Moein Moatali

number = int(input("what's your number? "))

fac=False
sum=1

for item in range(1,number+1):
    sum=sum*item
    if sum == number:
        fac=True

print(fac)