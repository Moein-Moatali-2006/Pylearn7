import sqlite3
from termcolor2 import colored


con=sqlite3.connect("data_store.db")
db=con.cursor()


def show_menu():
    print("1---> show products")
    print("2---> add new product")
    print("3---> update the product")
    print("4 ---> remove the product")
    print("5 ---> exit")
    print("6 ---> show customers")

def add():
    name=input("Please enter a name for your new product : ")
    count=int(input("How many of this product do you have ? "))
    price=float(input("How much is this ? "))
    db.execute(f"INSERT INTO product(name,count,price) VALUES('{name}',{count},{price});")
    con.commit()
    print(" ✅ ")

def show_list():
    pro = db.execute("SELECT * FROM product").fetchall()
    print("****************************************")
    print(colored("YOUR PRODUCTS : ",color="green"))
    for p in pro:
        print(p)
    print("****************************************")
    
def update():
    id=int(input("What is product's id ? "))
    new_name=input("Please enter a new name for your new product : ")
    new_count=int(input("Enter new count :"))
    new_price=float(input("Enter new price: "))
    db.execute(f"UPDATE product SET name='{new_name}',count={new_count},price={new_price} WHERE id={id} ;")
    con.commit()
    print("✅")

def remove():
    id=int(input("What is product's id ? "))
    Condition = input("Do you sure of delete this product? (yes/no):")
    if Condition == "yes":
        db.execute(f"DELETE FROM product WHERE id={id}")
        con.commit()
        print("✅")

while True:
    show_menu()
    choice=int(input("Please enter your choice: "))

    if choice == 1 :
        show_list()
    elif choice == 2:
        add()
    elif choice == 3:
        update()
    elif choice == 4:
        remove()
    elif choice == 5:
        print("Thank you 🌹")
        exit(0)
   
        










