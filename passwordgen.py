    ### create a function to that gemerate randam password
    ### Option : use pramater for for no of character in password


import random   
import string


length = int(input("Enter the length of password: "))
characters = string.ascii_letters + string.digits + '1234567890!@#$%^&*abcdefghijklmnopqrstuvwxyz()'

password = ''.join(random.choice(characters) for _ in range(length))

print("Generated password:", password)
