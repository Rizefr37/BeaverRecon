# Standard Library
from time import sleep
from random import choice
import sys
import os
# External Imports
try:
    from dns.resolver import query
    from emailrep import EmailRep
    import phonenumbers
    import bs4
except:
    print("Error: Missing Modules...")
    print("Attempting To Install...")
    sleep(2)
    os.system("pip3 install -r requirements.txt")
    print("\nDone Installing.")
    sleep(2)
    pass
# File Imports
from utils.colors import *
from utils.iputils import *
from utils.mainutils import *
from utils.banners import *
from utils.settings import *
from utils.phoneutils import *
from utils.update import *

## Version
VERSION = "0.8.1"

def cls():
    if sys.platform == 'win32':
        system("cls")
    else:
        system("clear")

def mainloop(themec):
    try:
        reload = False
        while True:
            if reload == True:
                break

            icons = ['ツ', '✦', '☣']
            icon = choice(icons)
            cls()
            print(banner(themec, VERSION))
            option = input(f"{reset}{bold}Option:{reset}{themec} ")

            if option.isnumeric():
                pass
            else:
                continue

            if option == "1":
                cls()
                print("Format: First Last Postal")
                name = input(f"{reset}{bold}Name:{reset}{themec} ").lstrip()
                try:
                    if name.split(" ")[2]:
                        pass
                except:
                    cls()
                    print("Please Enter A Full Name...")
                    sleep(2)
                    continue
                cls()
                print (f"{reset}{green}{icon}{reset}{blue} ThatsThem Lookup {green}{icon}{reset}")

                for x in thatsthem('name', name):
                    print(x)
                input(f"{reset}{bold}press enter to go back:{themec} ")
                continue

            elif option == "2":
                cls()
                print("Format: Street City State Postal")
                address = input(f"{reset}{bold}Address:{reset}{themec} ").lstrip()
                if address == "":
                    cls()
                    print("Please Enter A Proper Address...")
                    sleep(2)
                    continue
                cls()
                print (f"{reset}{green}{icon}{reset}{blue} ThatsThem Lookup {green}{icon}{reset}")

                for x in thatsthem('address', address):
                    print(x)
                input(f"{reset}{bold}press enter to go back:{themec} ")
                continue

            elif option == "3":
                target = []
                try:
                    cls()
                    ip = input(f"{reset}{bold}IP:{reset}{themec} ")
                    if validateinput('ip',ip) == True:
                        target.append(ip)
                        pass

                    else:
                        cls()
                        print (f"{orange}please enter a valid ipv4 address...")
                        sleep(2)
                        continue

                    while True:
                        cls()
                        for x in target:
                            currenttarget = x.lstrip().rstrip()
                        ipmenu(themec, currenttarget)
                        option = input(f"{reset}{bold}Option:{reset}{themec} ")

                        if option == "1":
                            cls()
                            print (f"{reset}{green}{icon}{reset}{blue} Geo Lookup {green}{icon}{reset}")
                            for line in iplookup(currenttarget):
                                print (line)
                            input(f"{reset}{bold}\npress enter to go back:{reset}{themec} ")
                            continue

                        elif option == "2":
                            cls()
                            print (f"{reset}{green}{icon}{reset}{blue} ThatsThem Lookup {green}{icon}{reset}")
                            for line in thatsthem('ip',currenttarget):
                                print(line)
                            input(f"{reset}{bold}press enter to go back:{reset}{themec} ")
                            continue

                        elif option == "3":
                            cls()
                            print (f"{reset}{green}{icon}{reset}{blue} Geo Lookup {green}{icon}{reset}")
                            for line in iplookup(currenttarget):
                                print (line)

                            print (f"\n{reset}{green}{icon}{reset}{blue} ThatsThem Lookup {green}{icon}{reset}")
                            for line in thatsthem('ip',currenttarget):
                                print(line)
                            input(f"{reset}{bold}press enter to go back:{reset}{themec} ")
                            continue

                        elif option == "4":
                            cls()
                            changetarget = input(f"{reset}{bold}Target:{reset}{themec} ")
                            if bool(isgoodipv4(changetarget)) == True:
                                target.clear()
                                target.append(changetarget)
                                continue

                            else: 
                                print("Invalid IP...")
                                sleep(1)
                                continue

                        elif option == "0":
                            break

                        else:
                            continue
                except Exception as e:
                    cls()
                    print (f"Error Has Occurred: {str(e)}")
                    sleep(2)
                    continue
            
            elif option == "4":
                target = []
                cls()
                username = input(f"{reset}{bold}Username:{reset}{themec} ")
                if validateinput('user', username) == False:
                    cls()
                    print("Please Enter A Username...")
                    sleep(2)
                    continue
                target.append(username)
                while True:
                    cls()
                    for x in target:
                        currenttarget = x.lstrip().rstrip()
                    usernamemenu(themec, currenttarget)
                    option = input(f"{reset}{bold}Option:{reset}{themec} ")

                    if option == "1":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} Scylla Lookup {green}{icon}{reset}")
                        for x in scylla("User", currenttarget):
                            print (x)
                        input(f"{reset}{bold}press enter to go back:{reset}{themec} ")
                        continue

                    elif option == "2":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} Username Checker {green}{icon}{reset}")
                        for x in usernamechecker(currenttarget): print(x)
                        input(f"\n{reset}{bold}press enter to go back:{reset}{themec} ")
                        continue
 
                    elif option == "3":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} Recovery Info {green}{icon}{reset}")
                        print (f"{reset}{themec}{reset}{blue}Instagram{reset}{themec}{reset}")
                        print(igpartialemail(currenttarget))
                        print (f"\n{reset}{themec}{reset}{blue}Twitter{reset}{themec}{reset}")
                        twitter(currenttarget)
                        input(f"\n{reset}{bold}press enter to go back:{reset}{themec} ")
                        continue

                    elif option == "4":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} Scylla Lookup {green}{icon}{reset}")
                        for x in scylla("User", currenttarget):
                            print (x)

                        print (f"{reset}{green}{icon}{reset}{blue} Username Checker {green}{icon}{reset}")
                        usernamechecker(currenttarget)

                        print (f"\n{reset}{green}{icon}{reset}{blue} Recovery Info {green}{icon}{reset}")

                        print (f"{reset}{themec}{reset}{blue}Instagram{reset}{themec}{reset}")
                        print(igpartialemail(currenttarget))

                        print (f"\n{reset}{themec}{reset}{blue}Twitter{reset}{themec}{reset}")
                        twitter(currenttarget)

                        input(f"\n{reset}{bold}press enter to go back:{reset}{themec} ")
                        continue

                    elif option == "5":
                        cls()
                        changetarget = input(f"{reset}{bold}Target:{reset}{themec} ")
                        if validateinput('user', username) == False:
                            print("Invalid Username...")
                            sleep(2)
                            continue
                        target.clear()
                        target.append(changetarget)
                        continue
                    elif option == "0":
                        break    
                    else:
                        continue

            elif option == "5":
                target = []
                cls()
                email = input(f"{reset}{bold}Email:{reset}{themec} ")
                if validateinput('email', email) == False:
                    cls()
                    print("Invalid Email...")
                    sleep(2)
                    continue
                else:
                    pass
                target.append(email)
                while True:
                    cls()
                    for x in target:
                        currenttarget = x.lstrip().rstrip()
                    emailmenu(themec, currenttarget)
                    option = input(f"{reset}{bold}Option:{reset}{themec} ")

                    if option == "1":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} Emailrep Lookup {green}{icon}{reset}")
                        for x in emailrep(currenttarget):
                            print(x)
                        input(f"\n{reset}{bold}press enter to go back: {themec}")
                        continue

                    elif option == "2":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} Scylla Lookup {green}{icon}{reset}")
                        for x in scylla("Email", currenttarget):
                            print (x)
                        input(f"{reset}{bold}press enter to go back: {themec}")
                        continue

                    elif option == "3":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} Pwndb2 Lookup {green}{icon}{reset}")
                        for x in pwndb2(currenttarget):
                            print (x)
                        input(f"{reset}{bold}press enter to go back: {themec}")
                        continue

                    elif option == "4":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} HIBP Lookup {green}{icon}{reset}")
                        for x in haveibeenpwned(currenttarget):
                            print(x)
                        input(f"{reset}{bold}\npress enter to go back:{reset}{themec} ")
                        continue

                    elif option == "5":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} ThatsThem Lookup {green}{icon}{reset}")
                        for x in thatsthem('email', currenttarget):
                            print(x)
                        input(f"{reset}{bold}press enter to go back:{reset}{themec} ")
                        continue

                    elif option == "6":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} Emailrep Lookup {green}{icon}{reset}")
                        for x in emailrep(currenttarget):
                            print(x)

                        print (f"\n{reset}{green}{icon}{reset}{blue} Scylla Lookup {green}{icon}{reset}")
                        for x in scylla("Email", currenttarget):
                            print (x)

                        print (f"{reset}{green}{icon}{reset}{blue} Pwndb2 Lookup {green}{icon}{reset}")
                        for x in pwndb2(currenttarget):
                            print (x)

                        print (f"{reset}{green}{icon}{reset}{blue} HIBP Lookup {green}{icon}{reset}")
                        for x in haveibeenpwned(currenttarget):
                            print(x)


                        print (f"\n{reset}{green}{icon}{reset}{blue} ThatsThem Lookup {green}{icon}{reset}")
                        for x in thatsthem('email', currenttarget):
                            print(x)
                        input(f"{reset}{bold}press enter to go back:{reset}{themec} ")
                        continue

                    elif option == "7":
                        cls()
                        changetarget = input(f"{reset}{bold}Target:{reset}{themec} ")
                        if validateinput('email', changetarget) == False:
                            cls()
                            print("Invalid Email...")
                            sleep(2)
                            continue
                        target.clear()
                        target.append(changetarget)
                        continue

                    elif option == "0":
                        break

                    else: 
                        continue
            
            elif option == "6":
                target = []
                cls()
                print("Format: 1231231234\nFYI: This Only Works on US Numbers")
                phone = input(f"{reset}{bold}Phone:{reset}{themec} ").lstrip()
                if validateinput('phone', phone) == False:
                    print("Invalid Phone Number...")
                    sleep(2)
                    continue
                else:
                    pass
                target.append(phone)
                while True:
                    cls()
                    for x in target:
                        currenttarget = x.lstrip().rstrip()
                    phonemenu(themec, currenttarget)
                    option = input(f"{reset}{bold}Option:{reset}{themec} ")

                    if option == "1":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} Thatsthem Lookup {green}{icon}{reset}")
                        for x in thatsthem('phone', currenttarget):
                            print(x)
                        input(f"{reset}{bold}press enter to go back:{themec} ")
                        continue

                    elif option == "2":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} Phone Scrape {green}{icon}{reset}")
                        for x in reversephone(themec,currenttarget):
                            print(x)
                        input(f"{reset}{bold}\npress enter to go back:{themec} ")
                        continue

                    elif option == "3":
                        cls()
                        print (f"{reset}{green}{icon}{reset}{blue} Thatsthem Lookup {green}{icon}{reset}")
                        for x in thatsthem('phone', currenttarget):
                            print(x)

                        print (f"{reset}{green}{icon}{reset}{blue} Phone Scrape {green}{icon}{reset}")
                        for x in reversephone(themec,currenttarget):
                            print(x)
                        input(f"{reset}{bold}\npress enter to go back:{themec} ")
                        continue                        

                    elif option == "4":
                        cls()
                        changetarget = input(f"{reset}{bold}Target:{reset}{themec} ")
                        if validateinput('phone', changetarget) == False:
                            print("Invalid Phone Number...")
                            sleep(2)
                            continue
                        target.clear()
                        target.append(changetarget)
                        continue

                    elif option == "0":
                        break    
                    else:
                        continue

            elif option == "7":
                cls()
                hash = input(f"{reset}{bold}Hash:{reset}{themec} ")
                if hash == "":
                    cls()
                    print("Please Enter A Hash...")
                    sleep(2)
                    continue
                cls()
                print (f"{reset}{green}{icon}{reset}{blue} Hash Decrypt(hashes.org) {green}{icon}{reset}")
                for x in hashcheck(hash):
                    print (x)
                input(f"{reset}{bold}\npress enter to go back:{themec} ")
                continue

            elif option == "8":
                cls()
                print (f"{reset}{green}{icon}{reset}{blue} Tool Info {green}{icon}{reset}")
                info(themec, VERSION)
                input(f"{bold}\npress enter to go back:{reset}{themec} ")
                continue
            
            elif option == "9":
                while True:
                    cls()
                    settingsmenu(themec)
                    option = input(f"{reset}{bold}Option:{reset}{themec} ")
                    if option == '1':
                        while True:
                            cls()
                            print(reset)
                            colormenu()
                            print("type 'back' to go back")
                            col = input("Color: ")
                            if col == "":
                                cls()
                                print("Please Pick A Color...")
                                sleep(2)
                                continue
                            elif col.lower() == "back":
                                break
                            else:
                                cls()
                                changecolor(col)
                                print(f"color changed to: {colortocode(col)}{col}")
                                reload = True
                                sleep(1)
                                break

                    elif option == "2":
                        while True:
                            cls()
                            print(f'{themec}1{reset} | {themec}Hashes.org : {themec}{getapikey("hasheskey")}{reset}')
                            print(f'{themec}2{reset} | {themec}Emailrep.io : {themec}{getapikey("emailrepkey")}{reset}')
                            print(f'{themec}0{reset} | {themec}Go Back{reset}')
                            option = input(f"{reset}{bold}Option:{reset}{themec} ")
                            if option == '1':
                                option = input(f"{reset}{bold}apikey:{reset}{themec} ")
                                chaneapikey("hasheskey", option)
                                cls()
                                print("Hashes.org Api Key Updated")
                                sleep(1.5)
                                reload = True
                                break
                            if option == '2':
                                option = input(f"{reset}{bold}apikey:{reset}{themec} ")
                                chaneapikey("emailrepkey", option)
                                cls()
                                print("Emailrep.io Api Key Updated")
                                sleep(1.5)
                                reload = True
                                break
                            elif option == '0':
                                break
                            else:
                                continue

                    elif option == "3":
                        print("Checking For Update...")
                        sleep(2)
                        check = checkversion(VERSION)
                        print(check)
                        if "Update" in check:
                            option = input("Would You Like To Update?(y/n): ")
                            if option.lower() == 'y':
                                print("Updating...")
                                sleep(2)
                                update()
                            else:
                                continue
                        sleep(2)

                    elif option == "4":
                        cls()
                        checkchangelog()
                        input(f"{reset}{bold}press enter to go back:{themec} ")
                        continue

                    elif option == "0":
                        break
                    else:
                        continue
            
            elif option == "0":
                print (f"{red}Exiting...{reset}")
                sys.exit()
    except KeyboardInterrupt:
        print (f"{red}\nCtrl-C Pressed Exiting...{reset}")
        sys.exit()

while True:
    themec = colortocode(getcolor())
    mainloop(themec)
    continue
