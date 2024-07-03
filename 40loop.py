
# for i in range(1,11):
#     print(i*9)

    ### Write a progra that print 70 to 100 but not [77,78,81]

for i in range(70,101):
    if i == 77 or i == 78 or i == 81:
        continue
    print(i)