#Moein Moatali
"""   BMI   """
Weight=float(input("Enter your weight in KG: "))
height=float(input("Enter your height in M: "))

result= Weight / (height ** 2) 

if result < 18.5:
    print("Under weight")
elif result >= 18.5 and result <=24.9:
    print("Normal weight")
elif result >= 25 and result <= 29.9:
    print("Over weight")
elif result >= 30 and result <=34.9:
    print("Obesty")
elif result >= 35 and result <= 39.9:
    print("Extreme obesty")