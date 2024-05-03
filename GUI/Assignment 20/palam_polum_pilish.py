import random
from termcolor2 import colored

play=["✋","🤚"]

computer_1_score=0
computer_2_score=0
user_score=0

print("🌹 Welcome to my game 🌹")

for item in range(5):
    while True:
        user=int(input("1-->✋    2-->🤚: "))
        if user== 1:
            user_choice="✋"
            break
        elif user==2:
            user_choice="🤚"
            break
        else:
            print("Please choice between 1 and 2")
    
    computer_1_choice=play[random.randint(0,1)]
    computer_2_choice=play[random.randint(0,1)]

    print(f"computer_1_choice--->{computer_1_choice}")
    print(f"computer_2_choice--->{computer_2_choice}")
    

    if (computer_1_choice == computer_2_choice) and (computer_1_choice != user_choice):
        user_score += 1
        print(colored("user win",color="green"))
    elif (computer_1_choice == user_choice) and (computer_1_choice != computer_2_choice):
        computer_2_score += 1
        print(colored("computer_2 win",color="green"))
    elif (computer_2_choice == user_choice) and (computer_2_choice != computer_1_choice):
        computer_1_score += 1
        print(colored("computer_1 win",color="green"))
    elif computer_1_choice == computer_2_choice == user_choice:
        print(colored("Equal",color="green"))

    print(colored("********************************",color="red"))


print(colored(f"computer_1 score --->{computer_1_score}"))
print(colored(f"computer_2 score --->{computer_2_score}"))
print(colored(f"user score --->{user_score}"))
