#Moein Moatali
"""    Hangman   """
import random
#بانک کلمات و انتخاب شانسی یک کلمه 
words_list = ["book","earth","tree","tierd","happy","computer","python","glass","pen","pillow","bed"]
word=random.choice( words_list )
#لیست حروف صحیح و غلط
true_char = []
false_char = []
#تعداد باخت
count_lose = 0

while count_lose < 6 :
    #گرفتن حدس کاربر و برسی تک کارکتر بودن آن
    guess=input("please enter your guess char: ").lower()
    if len(guess) > 1 : 
        print("your chars are large\nplease one char!")
        guess=input("please enter your guess char: ").lower()
    else:
        #نمایش کلمه و برسی درست و غلط بودن کارکتر
        if guess in word:
            count=word.count(guess)
            for i in range(count):
                true_char.append(guess)
            print("✅")
        else:
            false_char.append(guess)
            print("❌")
            count_lose += 1

        for item in word:
            if item in true_char:
                print(item , end=" ")
            else:
                print("_" , end=" ")
        
        if len(word) == len(true_char):
            print("\n❤️  --- you win ---❤️")
            break
    
    
#باخت کاربر
if count_lose == 6:
    print("\n----- Game over -----")
    
        



