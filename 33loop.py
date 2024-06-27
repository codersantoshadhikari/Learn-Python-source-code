
# #create multiplication table of 9
# for i in range(1,11):
#     print(i*9)
   

# for i in range(1,11):
#     # for j in range(1,11):
#     #     print(i*j)
#     print([i*j for j in range(1,11)])
#     print(f"{i} x {j} = {i*j}")
#     print("\n--------\n")


start = int(input("enter start : "))
end = int(input("enter end : "))

for i in range(start,end+1):
   for i in range(1,11):
      print(f"{i}*{i} = {i*i}")