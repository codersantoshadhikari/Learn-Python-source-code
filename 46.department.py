

name = [
    # name , department
    ("santosh", "IT"),
    ("manish", "IT"),
    ("sujan", "MBA"),
    ("hari", "HR"),
    ("sari", "Micbiology"),
    ("bishwa", "software developer"),
    ("mina", "Micbiology"),
    ("rita", "HR"),
    ("sachin", "Micbiology"),
    ("gita", "HR"),

]

### Find all from Micbiology department
micbiology_name = [name for name in name if name[1] == "Micbiology"]

print(micbiology_name)
# for i in micbiology_name:
#     print(i[0])




# for i in name:
#     if i[1] == "IT":
#         print(i[0])



### Create 10 employee who works on different department
### Print all employee who are in IT Department

### Option: 
### Display all department along with their names.

name = [
    # name , department
    ("santosh", "IT"),
    ("manish", "IT"),
    ("sujan", "MBA"),
    ("hari", "HR"),
    ("sari", "Micbiology"),
    ("bishwa", "software developer"),
    ("mina", "Micbiology"),
    ("rita", "HR"),
    ("sachin", "Micbiology"),
    ("gita", "HR"),

]

for i in name:
    if i[1] == "IT":
        print(i[0])

 ### Create 10 employee who works on different department
### Print all employee who are in IT Department

### Option: 
### Display all department along with their names.

        # List of employees with their departments
employees = [
    ("santosh", "IT"),
    ("manish", "IT"),
    ("sujan", "MBA"),
    ("hari", "HR"),
    ("sari", "Microbiology"),
    ("bishwa", "Software Developer"),
    ("mina", "Microbiology"),
    ("rita", "HR"),
    ("sachin", "Microbiology"),
    ("gita", "HR")
]

# Print all employees who are in the IT department
print("Employees in the IT Department:")
for employee in employees:
    if employee[1] == "IT":
        print(employee[0])

print("\nAll Departments along with their Employees:")
# Display all departments along with their names
departments = {}
for employee in employees:
    name, department = employee
    if department not in departments:
        departments[department] = []
    departments[department].append(name)

for department, names in departments.items():
    print(f"{department}: {', '.join(names)}")
