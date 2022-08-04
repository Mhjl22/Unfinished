from random import randint
import time
import getpass

name_list = []
password_list = []
hmpglp = "1"
camlp = "1"
ttllp = "1"
for _ in range(1):
    value1 = randint (1, 7)
    value2 = randint (1, 7)
    value3 = randint (1, 7)
    value4 = randint (1, 7)
    value5 = randint (1, 7)
    value6 = randint (1, 7)
    value7 = randint (1, 7)
    value8 = randint (1, 7)
    value9 = randint (1, 7)
    value10 = randint (1, 7)
    value11 = randint (1, 7)
    value12 = randint (1, 7)
    value13 = randint (1, 7)
    value14 = randint (1, 7)
    value15 = randint (1, 7)
    value16 = randint (1, 7)
    value17 = randint (1, 7)
    value18 = randint (1, 7)
    value19 = randint (1, 7)
    value20 = randint (1, 7)
    value21 = randint (1, 7)
    value22 = randint (1, 7)
    value23 = randint (1, 7)
    value24 = randint (1, 7)
    value25 = randint (1, 7)
    value26 = randint (1, 7)
    value27 = randint (1, 7)
    value28 = randint (1, 7)

print("Hello, and welcome to firstembassy2.0")
#print("This app will allow you to see what you have on your calendar, ")

   
       
def home():
    while True:
        hmpg = input("where would you like to go? Calendar, News, Security Cameras, Settings, or Log Out? ")
        if hmpg.lower() == "calendar":
            #GET INPUT FROM THE CAST ON WHAT TO PUT ON EACH DAY
            day = input("what day would you like to view?")
        elif hmpg.lower() == "news":
            #GET INPUT FROM CAST ON WHAT KIND OF INFO
            #
            print("NEWS")
        elif hmpg.lower() == "security cameras":
            caminval = randint(0, 10)
            clrcde = input("Please enter clearance code: ")
            if clrcde == "075139855622093457122678440628" or clrcde == "05761": 
                print("please wait...")
                time.sleep(value5)
                print("code accepted")
                security_cameras()
            else: 
                print("invalid code, please wait while we alert authorities near your location")
                while caminval < 10:
                    print("please wait...")
                    time.sleep(5)
                    caminval = caminval + 1
                camlp == "invalid"
                print("authorities alerted")
                break
            
        elif hmpg.lower() == "settings":
            #GET INPUT FROM CAST ON WHAT SETTINGS
            print("SETTINGS")
        elif hmpg.lower() == "log out":
            print("logging out...")
            time.sleep(value28)
            break
        else:
            create_or_login()
    

def create_or_login():  
        if adduser.lower() == "log in":
            user_name = input("enter username: ")
            print("validating username...")
            time.sleep(value1)
            print("please wait...")
            time.sleep(value2)
            for i in name_list:
                if(i == user_name or "bypass"):
                    userName = name_list.index(user_name)
                    entrpwd = getpass.getpass("enter password: ")
                    print("validating password...")
                    time.sleep(value3)
                    print("please wait...")
                    time.sleep(value4)
                    if entrpwd == password_list[userName] or entrpwd == "05761":
                        print("Welcome " + user_name)
                        home()
                        #try a var loop
                       
                    
                    else:
                        print("invalid password")

        elif adduser.lower() == "create account":
            username = input("Pick a username: ")
            name_list.append(username)
            password = ("Pick a password: ")
            password_list.append(password)
            print("creating account...")
            time.sleep(value16)
            print("account created, return to the home page and sign in")
            
        elif adduser.lower() == "bypass":
            bypcde = input("enter bypass code: ")
            if bypcde == ("05761"):
                home()
               
                   
                    
        
                
        else:
            print("so you have chosen... death")
        


def security_cameras():
    while True:
        rmno = input("What room number would you like to surveil? ")
        if rmno == ("quit"):
            print("quitting...")
            time.sleep(value27)
        else:
            print("loading room number " + rmno + "...")
        if rmno == "666":
            while True:
                print("")
                print("X X X X X")
                time.sleep(value17)
                print("X X X X X")
                time.sleep(value18)
                print("X X X X X")
                time.sleep(value19)
                print("X X X X X")
                time.sleep(value20)
                print("X X X X X")
                print("")
        elif rmno == "quit":
            break    
        else:
            random_cams()
        

def random_cams():
    #FIX THIS
    camera_list = ["0", "0", "0", "0","X", "0", "0"]
    print("")
    time.sleep(value21)
    print(camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] )
    time.sleep(value22)
    print(camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] )
    time.sleep(value23)
    print(camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] )
    time.sleep(value24)
    print(camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] )
    time.sleep(value25)
    print(camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] + " " + camera_list[randint(0, 6)] )
    time.sleep(value26)
    print("")




while ttllp == "1":
    adduser = input("Would you like to create an account, log in, or quit? ")
    if adduser.lower() == "quit":
        ttllp = "2"
    else:
        create_or_login()