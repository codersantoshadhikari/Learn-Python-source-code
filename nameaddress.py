	
#  Write a Python program to add the names of your 5 friends to a list and their corresponding addresses to another list. 
# Then, print the names and addresses in the format: "Name lives in Address."


# Define the lists of names and addresses
names = ['Manish Ji', 'Ram Ji', 'Hari sir', 'Bisal Ji', 'Sita Ji']
addresses = ['USA', 'Kathmandu', 'Pokhara', 'Bhaktapur', 'Lalitpur']


# Loop through the lists and print the names and addresses
for i in range(len(names)):
    print(f"{names[i]} lives in {addresses[i]}")