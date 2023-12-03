#Moein Moatali

def Show_Diamond(number):
    for num in range(number):
        print(' ' * (number - num - 1), end='')
        print('*' * (2 * num + 1))

    for num in range(number - 2, -1, -1):
        print(' ' * (number - num - 1), end='')
        print('*' * (2 * num + 1))

number=int(input("Enter your number : "))
Show_Diamond(number)