### Createing List

names = ['Santosh','Manish','Hari']
expenses = [1000,2000,3000]

# print(type(names))
# print(type(expenses[2]))

# for i in names:
#     print(i)

names.append('Rita')
names.append('Sita')

for i in names:
    print(i)


#### Find index by Value of First item

names = ['Santosh','Manish','Hari']
expenses = [1000,2000,3000]

names.append('Rita')
names.append('Sita')

print(names.index('Santosh'))