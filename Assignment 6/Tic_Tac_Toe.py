#Moein Moatali
"""   TIC TAC TOE  """
import pyfiglet
import random
import termcolor2
import datetime

user_1=0
user_2=0

def show_board():
    for row in game_board:
        for cell in row:
            print(cell,end=" ")
        print()

def cheek_game():
    global user_1,user_2
    if game_board[0][0]==X and game_board[0][1]==X and game_board[0][2]==X:
        print("❤️  User_1 win  ❤️")
        user_1 +=1
        return "finish"
        

    if game_board[1][0]==X and game_board[1][1]==X and game_board[1][2]==X:
        print(" ❤️  User_1 win  ❤️")
        user_1 +=1
        return "finish"
        

    if game_board[2][0]==X and game_board[2][1]==X and game_board[2][2]==X:
        print("❤️  User_1 win  ❤️")
        user_1 +=1
        return "finish"


    if game_board[0][0]==O and game_board[0][1]==O and game_board[0][2]==O:
        print("❤️  User_2 win  ❤️")
        user_2 +=1
        return "finish"
        

    if game_board[1][0]==O and game_board[1][1]==O and game_board[1][2]==O:
        print("❤️  User_2 win  ❤️")
        user_2 +=1
        return "finish"
        

    if game_board[2][0]==O and game_board[2][1]==O and game_board[2][2]==O:
        print("❤️  User_2 win  ❤️")
        user_2 +=1
        return "finish"




    if game_board[0][0]==X and game_board[1][0]==X and game_board[2][0]==X:
        print("❤️  User_1 win  ❤️")
        user_1 +=1
        return "finish"
        

    if game_board[0][1]==X and game_board[1][1]==X and game_board[2][1]==X:
        print("❤️  User_1 win  ❤️")
        user_1 +=1
        return "finish"
        

    if game_board[0][2]==X and game_board[1][2]==X and game_board[2][2]==X:
        print("❤️  User_1 win  ❤️")
        user_1 +=1
        return "finish"


    if game_board[0][0]==O and game_board[1][0]==O and game_board[2][0]==O:
        print("❤️  User_2 win  ❤️")
        user_2 +=1
        return "finish"
        

    if game_board[0][1]==O and game_board[1][1]==O and game_board[2][1]==O:
        print("❤️  User_2 win  ❤️")
        user_2 +=1
        return "finish"
        

    if game_board[0][2]==O and game_board[1][2]==O and game_board[2][2]==O:
        print("❤️  User_2 win  ❤️")
        user_2 +=1
        return "finish"
    


    if game_board[0][0]==X and game_board[1][1]==X and game_board[2][2]==X:
        print("❤️  ser_1 win  ❤️")
        user_1 +=1
        return "finish"
        

    if game_board[0][2]==X and game_board[1][1]==X and game_board[2][0]==X:
        print("❤️  User_1 win  ❤️")
        user_1 +=1
        return "finish"

    
    if game_board[0][0]==X and game_board[1][1]==X and game_board[2][2]==X:
        print("❤️  User_2 win  ❤️")
        user_2 +=1
        return "finish"
        

    if game_board[0][2]==X and game_board[1][1]==X and game_board[2][0]==X:
        print("❤️  User_2 win  ❤️")
        user_2 +=1
        return "finish"

    my_list=[]
    for item in game_board:
        for i in item:
            if i =="_":
                my_list.append(False)
            else:
                my_list.append(True)
    
    if all(my_list):
        print(" ❤️ ❤️ ❤️ equal ❤️ ❤️ ❤️")
        return "finish"




X=termcolor2.colored("X",color="red")
O=termcolor2.colored("O",color="blue")
print(O)
print(pyfiglet.figlet_format("Tic Tac Toe",font="slant"))

player=input("Computer💻 or your freind🙋🏼? ").lower()
zaman_1=datetime.datetime.now()
game_board=[
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
]
show_board()

while True:
    while True:
        if player=="computer":
            print("User_1")
            while True:
                row=int(input("row: "))
                col=int(input("col: "))
                if 0<= row <=2 and 0<=row<=2:
                    if game_board[row][col]=="_":
                        game_board[row][col]=X
                        break
                    else:
                        print("jer nazan 😉")
                else:
                    print("chi masraf mikoni? ")
            
            show_board()
            cheek_game()
            if cheek_game() =="finish":
                break

            print(" user_2 ")
            while True:
                row=random.randint(0,2)
                col=random.randint(0,2)
                if game_board[row][col]=="_":
                    game_board[row][col]=O
                    break
                else:
                    continue
            
            show_board()
            cheek_game()
            if cheek_game()=="finish":
                break           
        else:
            print("user_1")
            while True:
                row=int(input("row: "))
                col=int(input("col: "))
                if 0<= row <=2 and 0<=row<=2:
                    if game_board[row][col]=="_":
                        game_board[row][col]=X
                        break
                    else:
                        print("jer nazan 😉")
                else:
                    print("chi masraf mikoni? ")

            show_board()
            cheek_game()
            if cheek_game() =="finish":
                break

            print("user_2")
            while True:
                row=int(input("row: "))
                col=int(input("col: "))
                if 0<= row <=2 and 0<=row<=2:
                    if game_board[row][col]=="_":
                        game_board[row][col]=O
                        break
                    else:
                        print("jer nazan 😉")
                else:
                    print("chi masraf mikoni? ")

            show_board()
            cheek_game()
            if cheek_game() =="finish":
                break

    if user_1 >0 :
        user_1-=1
    
    if user_2 > 0:
        user_2 -=1
    
    print("user_1: ",user_1)
    print("user_2: ",user_2)
    
    repat=input("do you want to continue? ")
    if repat=="no":
        break
    else:
        game_board=[
        ["_","_","_"],
        ["_","_","_"],
        ["_","_","_"]
        ]
    
zaman_2=datetime.datetime.now()
print("time:",zaman_2-zaman_1)


