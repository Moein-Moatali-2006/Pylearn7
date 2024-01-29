def generate_rug(n):
    if n == 1: return [[0]] 
    return [[n//2]*n] + [[n//2]+row+[n//2]
           for row in generate_rug(n-2)] + [[n//2]*n]

while 1:
    number=int(input('Enter a number:'))
    if number % 2 !=0:
        for item in generate_rug(number):
            print(item)
    else:
        print("Your number is false")
    
    if number == 'exit':
        break