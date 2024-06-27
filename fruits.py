# # Ask the user how many fruits they want to enter
num_fruits = int(input("Enter the number of fruits you want to list: "))

fruits = []

for i in range(num_fruits):
    fruit = input(f"Enter the name of fruit {i + 1}: ")
    fruits.append(fruit)

print("\nList of fruits you entered:")
for fruit in fruits:
    print(fruit)
