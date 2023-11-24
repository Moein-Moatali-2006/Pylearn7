#Moein Moatali

"""   Guess Number   """



import random 

computer_number=random.randint(1,50)
for i in range(10):
    user_number=int(input("Enter your guess: "))

    if user_number == computer_number:
        print(" ***** You Woooon *****")
        print("count:",i)
        print("🌹 ❤️ 😍 🥰 🤩 😘")
        break
    elif user_number < computer_number:
        print("Go up 😉")
    elif user_number > computer_number:
        print("Go down 😉")

if i > 10 :
    print("I'm sorry")
    print("You are dumb")