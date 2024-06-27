atm_pin = '1234'

user_pin = ''
attempt = 5

while user_pin != atm_pin:
    if attempt <= 0:
        print("Your account has been blocked due to too many incorrect attempts.")
        break
    
    user_pin = input("Enter your pin: ")
    
    if user_pin != atm_pin:
        attempt -= 1
        if attempt > 0:
            print(f"Invalid pin. You have {attempt} attempts left")
else:
    print("Accepted ! . how much money do you want to withdraw") 
