#imports
from random import seed
from random import randint
import time
#random
seed(1)

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

    
    
while True:
    #logging in
    userid = input("please enter your user id: ")
    print("logging " + userid + " in")
    time.sleep(value1)
    print("please wait...")
    time.sleep(value2)
    #PWD variables
    Arpwd = "Amell0157"
    Brpwd = ("Bill0310")
    Vrpwd = ("Vladmir0382")
    Krpwd = ("Karl1592")
    #INITIALrpwd = ("")
    # Amell's home page
    if userid == "AmellJ":
        Apwd = input("please enter password for AmellJ: ")
        print("validating...")
        time.sleep(value3)
        if Apwd == Arpwd:
            while True:
                Ahome = input("where would you like to go? Messaging, Calendar, Info? Or would you like to leave? ")
                #Amell's messages
                if Ahome == "messaging":
                    print("messages")
                #Amell's calendar
                elif Ahome == "calendar":
                    print("calendar")
                #Amell's data
                elif Ahome == "data":
                    Aspwd = input("enter password")
                    print("validating...")
                    time.sleep(value4)
                    if Aspwd == "starkwieeinAdler":
                        print("data")
                    else:
                        print("validation failed")
                elif Ahome == "info":
                    info = input("input request: ")
                    if info == "query section 1":
                        sect1 = input("1a, 1b, 1c, or 1d: ")
                        time.sleep(value5)
                        print("querying ...")
                        time.sleep(value6)
                    elif info == "query section 2":
                        sect2 = input("2a, 2b, 2c, or 2d: ")
                        time.sleep(value7)
                        print("querying ...")
                        time.sleep(value8)
                    elif info == "query section 3":
                        sect3 = input("3a, 3b, 3c, or 3d: ")
                        time.sleep(value9)
                        print("querying ...")
                        time.sleep(value10)
                    elif info == "query section 4":
                        sect4 = input("4a, 4b, 4c, or 4d: ")
                        time.sleep(value11)
                        print("querying ...")
                        time.sleep(value12)
                    elif info == "query section 5":
                        sect5 = input("5a, 5b, 5c, or 5d: ")
                        time.sleep(value13)
                        print("querying ...")
                        time.sleep(value14)
                    else:
                        print("")
                elif Ahome == "leave":
                    break
                    
                         
                        
                        
                else:
                    print("that was not an option")
        else:
            print("invalid password")
    #Bill's home page
    elif userid == "BillT":
        Bpwd = input("please enter password for BillT: ")
        if Bpwd == Brpwd:
            Bhome = input("where would you like to go? Messaging, Calendar, Info? Or would you like to leave? ")
    #Vladmir's home page
    elif userid == "VladmirP":
        Vpwd = input("please enter password for VladmirP: ")
        if Vpwd == Vrpwd:
            Vhome = input("where would you like to go? Messaging, Calendar, Info? Or would you like to leave? ")
    #xavier's home page
    #elif userid == "XAVIER'S CHARACTER":
        #INITIALpwd = input("please enter password for XAVIER'S CHARACTER: ")
       # if INITIALpwd == 
         #INITIALhome = input("where would you like to go? Messaging, Calendar, Info? Or would you like to leave? ")
    #Karl's home page
    elif userid == "KarlK":
        Kpwd = input("please enter password for KarlK: ")
        if Kpwd == Krpwd:
            Khome = input("where would you like to go? Messaging, Calendar, Info? Or would you like to leave? ")
    elif userid == "break":
        break
    


