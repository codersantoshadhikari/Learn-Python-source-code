#### Ask user to enter todo and print all todos

total_todo = input("Enter total number of todo : ")

todos = []
### Ask user to enter todos
for i in range(int(total_todo)):
    # todos.append(input("Enter todo : "))
    todo = input(f"Enter todo {i+1} : ")
    todos.append(todo)
### Display all results
for todo in todos:
    print(todo)