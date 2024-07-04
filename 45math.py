### create function that find square of number

# def square(number):
#     return number**2

# result = square(5)
# print(result)

import math
### square root finder

square_root = math.sqrt(25)

print(square_root)



number = 3.134568765
print(f"number is {number:.2f}")


n1 = math.ceil(10.1)
n2 = math.floor(10.2)

print (n1)
print (n2)

n3 = math.pow(2,3)

print (n3)

print (round(10.6))


### create function that round number 
## Enter number : 3.11
## Round number : 3


# number = float(input("Enter number : "))
# print(f"Round number : {round(number)}")

def round_number(number):
    return round(number)

number = float(input("Enter number : "))
print(f"Round number : {round_number(number)}")