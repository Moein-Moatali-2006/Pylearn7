#Moein Moatali
"""  Rock - Paper - Scissor game   """

import random

computer_score=0
user_score=0

while computer_score < 5 and user_score < 5:
    guess=random.randint(1,3)
    if guess == 1:
        computer="Rock"
    elif guess == 2:
        computer == "Paper"
    elif guess == 3:
        computer =="Scissor"


    
    user=input("Enter your choice from [Rock - Paper - scissor] : ")


    print(" 💻 :",computer)
    print(" 👷🏼‍♂️ :",user)


    if computer == "Rock" and user == "Paper":
        user_score += 1
    elif computer == "Rock" and user == "Scissor":
        computer_score += 1
    elif computer == "Paper" and user == "Rock":
        computer_score += 1
    elif computer == "Paper" and user == "Scissor":
        user_score += 1 
    elif computer == "Scissor" and user == "Rock":
        user_score += 1
    elif computer == "Scissor" and user == "Paper":
        computer_score +=1
    elif computer == user :
        print("brabar")

    print("computer:",computer_score)
    print("user: ",user_score)





