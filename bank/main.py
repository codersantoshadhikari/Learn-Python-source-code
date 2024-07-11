from customers import Customer

options_text = """
waht do you want to do:
1. Add customer
2. View all customers
3. View customer by ID
4. updated customer
5. delete customer
"""
option = int(input(options_text))

if option == 1:
    print("Add customer")
    c = Customer(id = "", name = "", phone = "", balance = "", CitizenShip = "")## bank oject
    c.id = input("Enter customer ID: ")
    c.name = input("Enter customer name: ")
    c.phone = input("Enter customer phone number: ")
    c.balance = input("Enter customer balance: ")
    c.CitizenShip = input("Enter customer CitizenShip: ")
    f = open("customers.csv", "a")
    f.write(f"{c.id},{c.name},{c.phone},{c.balance},{c.CitizenShip}\n")
    f.close()
    print(f"Customer {c.name} added successfully")

elif option == 2:
    print("View all customers")
    f = open("customers.csv", "r")
    print(f.read())
    f.close()

elif option == 3:
    print("View customer by ID")
    f = open("customers.csv", "r")
    id = input("Enter customer ID: ")
    print(f.read())
    f.close()

elif option == 4:
    print("updated customer")
    f = open("customers.csv", "r")
    id = input("Enter customer ID: ")
    print(f.read())
    f.close()
elif option == 5:
    print("delete customer")
    f = open("customers.csv", "r")
    id = input("Enter customer ID: ")
    print(f.read())
    f.close()
else:
    print("Invalid option. Please try again.")