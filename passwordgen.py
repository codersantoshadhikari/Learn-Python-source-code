## Ceate a function to that generate randam password
### Option : use parameter for for no of character in password


import random   
import string


length = int(input("Enter the length of password: "))
characters = string.ascii_letters + string.digits + '1234567890!@#$%^&*abcdefghijklmnopqrstuvwxyz()'

password = ''.join(random.choice(characters) for _ in range(length))

print("Generated password:", password)
