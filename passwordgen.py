    ### create a function to that gemerate randam password
    ### Option : use pramater for for no of character in password
   ### Option : use wish give me a password of 12 character


import random
import string

def generate_password(length=12):
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password = generate_password()
print("Generated password:", password)
