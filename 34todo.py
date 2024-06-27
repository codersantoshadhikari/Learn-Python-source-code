## create program that ask user to enter n no of todo and display it


todos = []
total_todo = input("Enter total number of todo : ")

for i in range(int(total_todo)):
    todos.append(input("Enter todo : "))

## Display all results 
for  todo in todos:
    print(todo)


    print("\n--------\n")
    print("All todos : ",todos)
    for todo in todos:
        print(todo)