# Assuming there's a class Product defined in product.py with attributes id, name, qty, and price
from product import Product

option_text = """
What you want to do:
1. Add product
2. View all products
3. View product by ID
"""

print(option_text)
option = int(input("Enter your option: "))

if option == 1:
    # Open the file in append mode to add new products
    with open("product.csv", "a") as f:
        total_products = int(input("Enter total number of products: "))
        for i in range(total_products):
            product_id = input(f"Enter product {i+1} ID: ")
            product_name = input(f"Enter product {i+1} name: ")
            product_qty = input(f"Enter product {i+1} quantity: ")
            product_price = input(f"Enter product {i+1} price: ")

            # Create Product instance
            product = Product(id=product_id, name=product_name, qty=product_qty, price=product_price)
            
            # Write product details to file
            f.write(f"{product.id},{product.name},{product.qty},{product.price}\n")

        print("Products added successfully")

elif option == 2:
    # Read and display all products
    try:
        with open("product.csv", "r") as f:
            print("Product List:")
            print(f.read())
            
    except FileNotFoundError:
        print("No products found. Please add some products first.")

elif option == 3:
    # View product by ID
    product_id = input("Enter product ID: ")
    found = False
    try:
        with open("product.csv", "r") as f:
            for line in f:
                id, name, qty, price = line.strip().split(',')
                if id == product_id:
                    print(f"Product ID: {id}, Name: {name}, Quantity: {qty}, Price: {price}")
                    found = True
                    break
        if not found:
            print("Product not found.")
    except FileNotFoundError:
        print("No products found. Please add some products first.")

else:
    print("Invalid option. Please try again.")