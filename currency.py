### Create a program , that convert Nepali currency to USD , Euro ,Japnease 
## Enter Amount in NRS : 500 

NRS_TO_USD = 0.009
NRS_TO_EURO = 0.0086
NRS_TO_JPY = 1.69

nrs_amount = input("Enter amount in NRS : ")
nrs = float(nrs_amount)
usd, euro, jpy = nrs * NRS_TO_USD, nrs * NRS_TO_EURO, nrs * NRS_TO_JPY
print(f"{nrs} NRS is equivalent to USD ${usd:.2f}, Euro €{euro:.2f}, and Japanese ¥{jpy:.2f}")