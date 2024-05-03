from random import shuffle as sh

boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]
sh(boys)
sh(girls)
result=zip(boys,girls)
print(tuple(result))
