NRS_TO_USD = 0.009
NRS_TO_EURO = 0.0086
NRS_TO_JPY = 1.69

while True:
    nrs_amount = input("Enter amount in NRS (or type 'exit' to quit): ")
    if nrs_amount.lower() == 'exit':
        break
    try:
        nrs = float(nrs_amount)
        usd, euro, jpy = nrs * NRS_TO_USD, nrs * NRS_TO_EURO, nrs * NRS_TO_JPY
        print(f"{nrs} NRS is equivalent to USD ${usd:.2f}, Euro €{euro:.2f}, and Japanese ¥{jpy:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
