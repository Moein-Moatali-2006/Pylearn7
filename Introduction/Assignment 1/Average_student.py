#Moein Moatali
"""  Average student """

first_name=input("What is your first name? ")
last_name=input("What is your last name? ")

lesson1=eval(input("Tell me the grade of the lesson: "))
lesson2=eval(input("Tell me the grade of the lesson: "))
lesson3=eval(input("Tell me the grade of the lesson: "))


sum= lesson1 + lesson2 + lesson3
average = sum /3
print(f"{first_name} {last_name} average={average}")

if average >= 17 :
    print("Great")
elif average < 17 and average >= 12 :
    print("Normal")
elif average < 12 :
    print("Fail")
