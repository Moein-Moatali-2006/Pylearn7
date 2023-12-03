#Moein Moatali
"""   Khayyam_Pascal  """
def Pascal(number):

    Triangle = []

    for i in range(number):
        row = [1] * (i + 1)

        for item in range(1, i):
            row[item] = Triangle[i - 1][item - 1] + Triangle[i - 1][item]

        Triangle.append(row)

    for row in Triangle:
        print(*row)

Pascal(int(input("Enter your number : ")))