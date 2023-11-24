#Moein Moatali
 
"""   cheek traingle  """


#get sides
side_1=int(input("Enter the side1 size:"))
side_2=int(input("Enter the side2 size:"))
side_3=int(input("Enter the side3 size:"))

#cheek 
if (side_1 > (side_2 - side_3)) and (side_2 > (side_1 - side_3)) and (side_3 > (side_1 - side_2)):
    print("traingle is True")
else:
    print("traingle is False")