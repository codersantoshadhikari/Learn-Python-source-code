### Create a program that calculate simple interest using GUI
### P* t * r / 100

def simple_interest():
    p = float(input("Enter the principal amount: "))
    t = float(input("Enter the time: "))
    r = float(input("Enter the rate: "))
### time is in years

    si = (p * t * r) / 100
    print("The simple interest is", si)

simple_interest()
