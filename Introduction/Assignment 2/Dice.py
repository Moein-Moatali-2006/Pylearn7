#Moein Moatali

"""  Dice  """
import random

while True :
    ready=input("yes or no :")
    if ready == "yes":
        number=random.randint(1,6)
        print("what's your number? ",number)
        while number == 6:
            print(" 🤩 🤩 🤩")
            number=random.randint(1,6)
            print("your gift:",number)
    else:
        break
            