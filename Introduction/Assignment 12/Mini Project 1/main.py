from media import Media
from pyfiglet import figlet_format
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip


def prop():
    global name,director,IMDB,url,duration,casts
    name=input("What is media name? ")
    director=input("Who is director media? ")
    IMDB=input("How much is IMDB? ")
    url=input("write url: ")
    duration=input("How long is the movie? ")
    casts=input("What are the names of the actors in the movie? ")


class Option:

    @staticmethod
    def show_list():
        print(" 1--> add")
        print(" 2--> edit")
        print(" 3--> remove")
        print(" 4--> search")
        print(" 5--> search_minute")
        print(" 6--> exit")
    @staticmethod
    def add():
        print("Add a (Film - Series - Documentary - Clip) ?")
        select=input("Enter your choice: ")
        match select:
            case "Film":
                prop()
                country=input("Which country made this movie? ")
                result=Film(name,director,IMDB,url,duration,casts,country)
                MOVIES.append({"type":select,"name":result.name,"director":int(result.director),"IMDB":result.IMDB,"url":result.url,"duration":result.duration,"casts":result.casts})

            case "Series":
                prop()
                count=input("Enter count series: ")
                result=Series(name,director,IMDB,url,duration,casts,count)
                MOVIES.append({"type":select,"name":result.name,"director":int(result.director),"IMDB":result.IMDB,"url":result.url,"duration":result.duration,"casts":result.casts})

            case "Documentary":
                prop()
                country=input("Which country made this movie? ")
                count=input("Enter count series: ")
                result=Documentary(name,director,IMDB,url,duration,casts,count,country)
                MOVIES.append({"type":select,"name":result.name,"director":int(result.director),"IMDB":result.IMDB,"url":result.url,"duration":result.duration,"casts":result.casts})

            case "Clip":
                prop()
                country=input("Which country made this movie? ")
                result=Clip(name,director,IMDB,url,duration,casts,country)
                MOVIES.append({"type":select,"name":result.name,"director":int(result.director),"IMDB":result.IMDB,"url":result.url,"duration":result.duration,"casts":result.casts})
    @staticmethod
    def edit():
        type=input("What is the type of the movie?")
        film_name=input("What is the name of the movie? ")
        for item in MOVIES:
            if item["name"] == film_name and type== item["type"]:
                print("Please enter updated information:")
                prop()
                item['name']=name
                item['director']=director
                item["IMDB"]=IMDB
                item["url"]=url
                item['duration']=int(duration)
                item['casts']=casts
        else:
            print("There is not this movie")

    @staticmethod
    def remove():
        type=input("What is the type of the movie?")
        film_name=input("What is the name of the movie? ")
        for item in MOVIES:
            if item["name"] == film_name and type== item["type"]:
                MOVIES.remove(item)
                break
        else:
            print("There is not this movie")
    @staticmethod
    def search():
        type=input("What is the type of the movie?")
        film_name=input("What is the name of the movie? ")
        for item in MOVIES:
            if item["name"] == film_name and type== item["type"]:
                print("Your movie:")
                print(item)
                break
        else:
            print("There is not this movie")
        
        choice=input("Do you want download video?")
        if choice =="yes":
            Media.download()
        else:
            pass
    @staticmethod
    def search_minute():
        number_1=int(input("number 1: "))
        number_2=int(input("number 2: "))
        for item in MOVIES:
            if item["duration"] > number_1 and item["duration"] < number_2:
                print("Your movie:")
                print(item)
                
        else:
            print("There is not this movie")
        




MOVIES=[]
class Database:
    def __init__(self,path,type="r"):
        self.path=path
        self.type=type

    
    def read(self):
        f=open(self.path,self.type)
        movies=f.read().split("\n")
        for item in movies:
            item = item.split(",")
            MOVIES.append({"type":item[0],"name":item[1],"director":item[2],"IMDB":item[3],"url":item[4],"duration":int(item[5]),"casts":item[6]})
        else:
            print("*** Data loaded ***")
        f.close()

    def write(self):
        f=open(self.path,self.type)
        for item in MOVIES:
            f.write(item["type"]+","+item["name"]+","+item["director"]+","+item["IMDB"]+","+item["url"]+","+str(item["duration"])+","+item["casts"])
            f.write("\n")
        f.close()


print(figlet_format("Moein Player",font="slant"))
db=Database("Database.txt","r")
print("Loading...")
db.read()

while True:
    Option.show_list()
    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
            Option.add()
        
        case 2:
            Option.edit()

        case 3:
            Option.remove()

        case 4:
            Option.search()

        case 5:
            Option.search_minute()

        case 6:
            data=Database("Database.txt","w")
            data.write()
            print("Finish")
            exit(0)