todo_list = ['Learn python' , 'read a book' , 'do some coding''read a book' , 'do some coding']
todo_list.append('Finish my project')
todo_list.insert(1, 'eat lunch')
for i in todo_list:
    # todo_list.pop(1)
    print(todo_list.index(i), i)
