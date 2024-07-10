### OOP : object oriented programming in opp we use class and object to desgin a computer program
### class Blueprint to create object
### object is an instance of a class
### how to create a class


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


        ### how to create object
s1 = Student("santosh",age = 25)

def displayName(self):
    print(self.name)


    #### create class teacher with pramater name and salary , and display method
    ### Create 3 objects of class teacher and Display details

    class Teacher:
        def __init__(self,name,salary):
            self.name = name
            self.salary = salary

        def display(self):
            print(self.name)
            print(self.salary)


