import random
import re
from sys import platform
import keyboard

lower = "abcdefghijklmnñopqrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"
symbols = "!¡?¿=+-_@$#€&"
specialChar = '[!¡?¿=+-_/\@,.;:\'$#€\"&ç]'

Enter = "Press enter to"

string = lower + upper + numbers + symbols
Nfile = "passwords.txt"

search_pass = False
create_pass = False
overwrite_pass = False

def Main():
    print("Do you want to create a password:")
    look_or_create = input()
    if look_or_create.lower() == "yes":
        global create_pass
        create_pass = True
        Create()
    else:
        print("Do you want to search for a specific password: ")
        specific_or_all = input()
        if specific_or_all.lower() == "yes":
            global search_pass
            search_pass = True
            Create()
        else:
            with open(Nfile, "r") as rf1:
                data1 = rf1.read()
                print(data1)
                input("Press enter for exit: ")
                exit()
Main()

def Create():
    print("Enter the username: ")
    username = input()
    print("Enter the platform: ")
    platform = input()
    regex = re.compile("[specialChar]")
    if (regex.search(platform) == None):
        global search_string
        search_string = username + " : " + platform
        with open(Nfile, "r") as rf2:
            data2 = rf2.read()
            if search_string in data2:
                global lines
                lines = rf2.readlines()
                if create_pass == True:
                    print("Password allready exists, do you want to overwrite:")
                    overwrite = input()
                    if overwrite.lower() == "yes":
                        global overwrite_pass
                        overwrite_pass = True
                        rf2.close()
                        password()
                    else:
                        print("Want to see the password:")
                        see_password = input()
                        if see_password.lower() == "yes":
                            for line in lines:
                                if line.find(search_string):
                                    global line_number
                                    line_number = line.index(line)
                                    print("Line " + lines.index(line) + " :" + line)
                        else:
                            exit()
                elif search_pass == True:
                    for line in lines:
                        if line.find(search_string):
                            print("Line " + lines.index(line) + " :" + line)
            else:
                rf2.close()
                password()
    else:
        print("Platform contains special character, press enter to repeat:")
        if keyboard.read_key() == 'enter':
            input()
            Create()
Create()

def password():
    print("Introduce number of characters:")
    length = input()
    if length < 8:
        print("Number of characters too low, press enter to go back")
        if keyboard.read_key() == 'enter':
            input()
            password()
    elif length > 24:
        print("Number of characters too high, press enter to go back")
        if keyboard.read_key() == 'enter':
            input()
            password()
    else:    
        global password_char
        password_char = "".join(random.sample(string,length))
        print("Password created: " + password + " for " + platform)
        print("Do you want to save the password.")
        print("Yes or No")
        save_password = search_string + " : " + password_char
        ans = input()
        if ans.lower() == "yes":
            if overwrite_pass == True:
                with open(Nfile, "w") as wf:
                    lines[line_number - 1] = save_password + "\n"
                    for line in lines:
                        wf.write(line)
                        wf.close()
            else:
                with open(Nfile, "a") as af:
                    af.write(save_password)
                    af.close()
password()