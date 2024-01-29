import instaloader
import getpass

file = open("old_followers.txt", "r")
Old_Followers = []
for line in file:
    Old_Followers.append(line)
file.close()

Loader = instaloader.Instaloader ()

Username = input("Enter your username: ")
Password = getpass.getpass("Enter your password: ")

Loader.login(Username, Password)
print("---Login---")

Profile = instaloader.Profile.from_username(Loader.context, "rasool.vip")

New_followers=[]
for item in Profile.get_followees():
    New_followers.append(item)


for i in New_followers:
    if i not in Old_Followers:
        print(i)


file=open("followers.txt","w")
for follower in New_followers:
    file.write(follower+"\n")

file.close()