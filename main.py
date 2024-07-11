# # Assuming there's a class Product defined in product.py with attributes id, name, qty, and price
# from product import Product

# option_text = """
# What you want to do:
# 1. Add product
# 2. View all products
# 3. View product by ID
# """

# print(option_text)
# option = int(input("Enter your option: "))

# if option == 1:
#     # Open the file in append mode to add new products
#     with open("product.csv", "a") as f:
#         total_products = int(input("Enter total number of products: "))
#         for i in range(total_products):
#             product_id = input(f"Enter product {i+1} ID: ")
#             product_name = input(f"Enter product {i+1} name: ")
#             product_qty = input(f"Enter product {i+1} quantity: ")
#             product_price = input(f"Enter product {i+1} price: ")

#             # Create Product instance
#             product = Product(id=product_id, name=product_name, qty=product_qty, price=product_price)
            
#             # Write product details to file
#             f.write(f"{product.id},{product.name},{product.qty},{product.price}\n")

#         print("Products added successfully")

# elif option == 2:
#     # Read and display all products
#     try:
#         with open("product.csv", "r") as f:
#             print("Product List:")
#             print(f.read())
            
#     except FileNotFoundError:
#         print("No products found. Please add some products first.")

# elif option == 3:
#     # View product by ID
#     product_id = input("Enter product ID: ")
#     found = False
#     try:
#         with open("product.csv", "r") as f:
#             for line in f:
#                 id, name, qty, price = line.strip().split(',')
#                 if id == product_id:
#                     print(f"Product ID: {id}, Name: {name}, Quantity: {qty}, Price: {price}")
#                     found = True
#                     break
#         if not found:
#             print("Product not found.")
#     except FileNotFoundError:
#         print("No products found. Please add some products first.")

# else:
#     print("Invalid option. Please try again.")


#####	Develop a software application for a bank that includes functionalities to
#  add and view customer information. 
### Each customer should have an ID, name, phone number, and balance.
from product import Customer


def add_customer():
    with open("customers.csv", "a") as f:
        customer_id = input("Enter customer ID: ")
        customer_name = input("Enter customer name: ")
        customer_phone = input("Enter customer phone number: ")
        try:
            customer_balance = float(input("Enter customer balance: "))
        except ValueError:
            print("Invalid input. Please enter a valid number for balance.")
            return

        customer = Customer(id=customer_id, name=customer_name, phone=customer_phone, balance=customer_balance)
        f.write(f"{customer.id},{customer.name},{customer.phone},{customer.balance}\n")
        print("Customer added successfully")

def view_all_customers():
    try:
        with open("customers.csv", "r") as f:
            customers = f.readlines()
            if customers:
                print("Customer List:")
                for customer in customers:
                    print(customer.strip())
            else:
                print("No customers found. Please add some customers first.")
    except FileNotFoundError:
        print("No customers found. Please add some customers first.")

def view_customer_by_id():
    customer_id = input("Enter customer ID: ")
    found = False
    try:
        with open("customers.csv", "r") as f:
            for line in f:
                id, name, phone, balance = line.strip().split(',')
                if id == customer_id:
                    print(f"Customer ID: {id}, Name: {name}, Phone: {phone}, Balance: {balance}")
                    found = True
                    break
        if not found:
            print("Customer not found.")
    except FileNotFoundError:
        print("No customers found. Please add some customers first.")

def main():
    option_text = """
    What do you want to do:
    1. Add customer
    2. View all customers
    3. View customer by ID
    """

    print(option_text)
    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        return

    if option == 1:
        add_customer()
    elif option == 2:
        view_all_customers()
    elif option == 3:
        view_customer_by_id()
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
