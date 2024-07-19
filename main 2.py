from todo import Todo

all_todos = []

def display_todos():
    for todo in all_todos:
        print(todo.title, todo.description)


def add_todo(title, description):
    todo = Todo(title, description)
    all_todos.append(todo)
    display_todos()
