# Moein Moatli

""""   Store  """


PRODUCTS=[]

def read_from_database():
    f=open("database.txt","r")
    for line in f:
        result = line.split(",")
        my_dict={"code":result[0],"name":result[1],"price":int(result[2]),"count":int(result[3])}
        PRODUCTS.append(my_dict)

    f.close()


def write_to_database():
    ...
    


def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show list")
    print("6- buy")
    print("7- Exit")


def add():
    code=input("Enter code: ")
    name=input("Enter name: ")
    price=input("Enter price: ")
    count=input("Enter count: ")
    new_product={"code":code,"name":name,"price":price,"cont":count}
    PRODUCTS.append(new_product)


def edit():
    code=input("Enter code product for edit: ")
    for product in PRODUCTS:
        if product['code']==code:
            print(product["code"],"\t\t",product["name"],"\t\t",product["price"],"\t\t",product["count"])
            break
    else:
        print("not found")
    
    while True:
        print("1---> code ")
        print("2---> name ")
        print("3---> price ")
        print("4---> count ")
        print("5---> save and finish")
        user=input("enter code from list: ")
        if user=="1":
            new_code=input("new code: ")
            product["code"]=new_code
        elif user=="2":
            new_name=input("new name: ")
            product["name"]=new_name
        elif user=="3":
            new_price=input('new price: ')
            product['price']=new_price
        elif user=="4":
            new_count=input("new count:")
            product['count']=new_count
        elif user == "5":
            print("your data is Save")
            break



def remove():
    user_input=input("Enter your keyword: ")
    for product in PRODUCTS:
        if product["code"]==user_input or product["name"]==user_input:
            print(product["code"],"\t\t",product["name"],"\t\t",product["price"])
            PRODUCTS.remove(product)
            print("Delete your product")
            break
    else:
        print("not found ")


def search():
    user_input=input("Enter your keyword: ")
    for product in PRODUCTS:
        if product["code"]==user_input or product["name"]==user_input:
            print(product["code"],"\t\t",product["name"],"\t\t",product["price"])
            break
    else:
        print("not found ")


def show_list():
    print("code\t\t name\t\t price")
    for product in PRODUCTS:
        print(product["code"],"\t\t",product["name"],"\t\t",product["price"])


list_buy=[]
def buy():
    global list_buy,PRODUCTS
    user_input=input("Enter your code or name product: ")
    for product in PRODUCTS:
        if product["code"]==user_input or product["name"]==user_input:
            count=int(input("How many this product want you? "))
            if count <= product["count"]:   
                new_price=count * product['price']
                list_buy.append({"name":product['name'],"count":count,"price":new_price})
                product['count']-=count
                print("it's ok")
            else:
                print("I'm sorry.\n We have not this count product.")
            break
    else:
        print("not found ")




print("welcome to my store")
print("loading....")
read_from_database()
print("data loaded")


while True:
    show_menu()
    choice=int(input("Enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        result_price=0
        for item in list_buy:
            print(item)
            result_price+=item['price']
        
        print("result price= ",result_price)
        write_to_database()
        exit(0)
    else:
        print("adam bash")

