import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()/,'\|{-{}")
while True:
    try:
        while True:
            length = int(input("Enter password length: "))
            if(length > 0):
                passwrd = random.choices(characters, k = length)
                print("".join(passwrd))
                break
            else:
                print("Length should be greater than zero")
        break
    except ValueError as err:
        print("Enter integer value")
