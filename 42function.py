## 3 parameter & return type

def find_cube(num):
    cube = num ** 3
    return cube

print(find_cube(2))



### 4 parameter & return type

def minvoter_age():
    return 18

hari_age = minvoter_age()
if hari_age >= 18:
    print("eligible for voting")
else:
    print("not eligible for voting")