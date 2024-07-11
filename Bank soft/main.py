import csv

class Customer:
    def __init__(self, id="", name="", phone="", balance="", CitizenShip=""):
        self.id = id
        self.name = name
        self.phone = phone
        self.balance = balance
        self.CitizenShip = CitizenShip

def view_all_customers():
    try:
        with open("customers.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No customers found. The file does not exist.")

def view_customer_by_id(customer_id):
    try:
        with open("customers.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == customer_id:
                    print(row)
                    return
            print(f"No customer found with ID: {customer_id}")
    except FileNotFoundError:
        print("No customers found. The file does not exist.")

def update_customer(customer_id):
    customers = []
    found = False
    try:
        with open("customers.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == customer_id:
                    found = True
                    print(f"Current details: {row}")
                    name = input("Enter new customer name: ")
                    phone = input("Enter new customer phone number: ")
                    balance = input("Enter new customer balance: ")
                    CitizenShip = input("Enter new customer CitizenShip: ")
                    customers.append([customer_id, name, phone, balance, CitizenShip])
                else:
                    customers.append(row)

        if found:
            with open("customers.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(customers)
            print(f"Customer {customer_id} updated successfully.")
        else:
            print(f"No customer found with ID: {customer_id}")

    except FileNotFoundError:
        print("No customers found. The file does not exist.")

def delete_customer(customer_id):
    customers = []
    found = False
    try:
        with open("customers.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == customer_id:
                    found = True
                else:
                    customers.append(row)

        if found:
            with open("customers.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(customers)
            print(f"Customer {customer_id} deleted successfully.")
        else:
            print(f"No customer found with ID: {customer_id}")

    except FileNotFoundError:
        print("No customers found. The file does not exist.")

def main():
    options_text = """
    What do you want to do:
    1. Add customer
    2. View all customers
    3. View customer by ID
    4. Update customer
    5. Delete customer
    """
    option = int(input(options_text))

    if option == 1:
        print("Add customer")
        c = Customer()
        c.id = input("Enter customer ID: ")
        c.name = input("Enter customer name: ")
        c.phone = input("Enter customer phone number: ")
        c.balance = input("Enter customer balance: ")
        c.CitizenShip = input("Enter customer CitizenShip: ")
        with open("customers.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([c.id, c.name, c.phone, c.balance, c.CitizenShip])
        print(f"Customer {c.name} added successfully.")

    elif option == 2:
        print("View All customers")
        view_all_customers()

    elif option == 3:
        print("View customer by ID")
        customer_id = input("Enter customer ID: ")
        view_customer_by_id(customer_id)

    elif option == 4:
        print("Update customer")
        customer_id = input("Enter customer ID: ")
        update_customer(customer_id)

    elif option == 5:
        print("Delete customer")
        customer_id = input("Enter customer ID: ")
        delete_customer(customer_id)

    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
