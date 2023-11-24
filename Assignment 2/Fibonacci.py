#Moein Moatali

"""   Fibonacci   """


def fibonacci_list(number):
    if not isinstance(number, int) or number < 1:
        return "Invalid input"

    lst = []

    a = 1
    b = 1

    for i in range(number):
        lst.append(a)
        c = a + b
        a = b
        b = c

    return lst


result = fibonacci_list(int(input("Enter your number for Fibonacci : ")))


print(result)

