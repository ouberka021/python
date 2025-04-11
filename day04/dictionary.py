dict = {0:0}

print(dict)
dict[100]= "Apple"

print(dict)

print("--------------------------")
student1 = {}
print(type(student1))

student1["student_name"]="ali"
student1["student_name"]="Said"
student1["age"]=30
student1["gpa"]=3.0
student1["Full_time"]= True
print(student1)
#print(help(dict.pop))
student1.pop("age")

print(student1)
print(student1["gpa"])

print("--------------------------")
employee = {
    "employee_name": "Hala",
    "employee_id": 100,
    "employee_salary": 200000,
    "job_title": "Tester"
}
# to get the key
for each_key in employee.keys():
    print(each_key)

print("----------------------")
# to get the key
for each_key in employee.keys():
    print(f'{each_key} ==> {employee[each_key]}')

for each_key in employee.items():
    print(f'{each_key[0]} ==> {each_key[1]}')

print("--------------------------")
employee1 = {
    "employee_name": "Hal2",
    "employee_id": 1002,
    "employee_salary": 2000002,
    "job_title": "Tester2"
}
employee4 = {
    "employee_name": "jalal",
    "employee_id": 30,
    "employee_salary": 10000,
    "job_title": "Developer"
}

employee3 = [employee1, employee,employee4]
for each_dict in employee3:
    print("----------------------------")
    for each in each_dict.items():
        print(f"{each[0]} => {each[1]}")







