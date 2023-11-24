#Moein Moatali

"""    Average student   """


count=0
sum=0
while True:
    score=input("Enter score: ")
    if score == "exit":
        break
    else:
        score = float(score)
        count+=1
        sum+=score

print("Average: ",sum/count)