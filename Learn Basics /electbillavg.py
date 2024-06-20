## Add your Electricity Bill From Jan dec In Dec in Dictonary and find total and average .

bills = {'Jan': 120, 'Feb': 130, 'Mar': 110, 'Apr': 115, 'May': 140, 'Jun': 135, 'Jul': 150, 'Aug': 145, 'Sep': 125, 'Oct': 130, 'Nov': 120, 'Dec': 150}

# Calculate total and average
total = sum(bills.values())
average = total / len(bills)

# Print the results
print(f"Total Electricity Bill for the year: ${total}")
print(f"Average Monthly Electricity Bill: ${average}")