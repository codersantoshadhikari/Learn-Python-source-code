
## Ask for user first name middle name and last name and print full name and check lenth
#  total name length

first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")

first_name_length = len(first_name)
middle_name_length = len(middle_name)
last_name_length = len(last_name)

# print(f"First name length is {first_name_length}")
# print(f"Middle name length is {middle_name_length}")
# print(f"Last name length is {last_name_length}")

total_name_length = first_name_length + middle_name_length + last_name_length
print(f"Total name length is {total_name_length}")

print(f"{first_name} {middle_name} {last_name}")

