#Moein Moatali

import qrcode

name=input("What's your name? ")
number=input("What's your number? ")
res=name + " " + number

img=qrcode.make(res)
img.save("qrcode.png")


