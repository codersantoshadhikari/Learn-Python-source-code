# ## Challenge
# # Store  you expenses from sunday to saturday and find total expenses 
# # and average expenses

# sunday = 500
# monday = 600
# tuesday = 700
# wednesday = 800
# thursday = 900
# friday = 1000
# saturday = 1100

# total = sunday + monday + tuesday + wednesday + thursday + friday + saturday
# print(total)

# Store expenses for each day
sunday = 500
monday = 600
tuesday = 700
wednesday = 800
thursday = 900
friday = 1000
saturday = 1100

# Calculate total expenses
total = sunday + monday + tuesday + wednesday + thursday + friday + saturday

# Calculate average expenses
average = total / 7

# Print the total and average expenses
print(f"Total expenses for the week: ${total}")
print(f"Average daily expense: ${average:.2f}")