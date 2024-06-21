# import random

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# alphabets = upper = alphabet + alphabet_upper()
# all_combine_to_list = alphabets.split()

# print(all_combine_to_list)
# random1= random.choice(all_combine_to_list)
# random2= random.choice(all_combine_to_list)
# random3 = random.choice(all_combine_to_list)
# random4 = random.choice(all_combine_to_list)
# random5 = random.choice(all_combine_to_list)
# random5 = random.choice(all_combine_to_list)

# print(random1, random2, random3, random4, random5)
# print(random1 + random2 + random3)

import random
import string

def generate_password(length=12):
    characters = string.ascii_lowercase + string.digits + '@#$'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password_length = 12  # Change this to adjust the length of the password
password = generate_password(password_length)
print("Generated password:", password)
